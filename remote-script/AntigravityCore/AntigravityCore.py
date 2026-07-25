from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import ControlSurface
import logging
from logging.handlers import RotatingFileHandler
import threading
import socket
import json
import time
import os

# Compatibilidad para queue
try:
    import queue
except ImportError:
    import Queue as queue

from . import config
from .security import SecurityGuard
from .command_registry import CommandRegistry
from .dsp_bridge import DSPBridge

class AntigravityCore(ControlSurface):
    def __init__(self, *a, **k):
        super(AntigravityCore, self).__init__(*a, **k)
        self._setup_logging()
        self.logger.info("Inicializando AntigravityCore V2.0.0 (Phase 2)")
        
        # Command Registry integration
        self.ctx = {"song": getattr(self, "song", lambda: None)(), "application": getattr(self, "application", lambda: None)()}
        self.registry = CommandRegistry(self.ctx)
        self.registry.auto_discover()
        
        # DSP Bridge integration
        self._dsp_bridge = DSPBridge(self.logger)
        self._dsp_bridge.start()
        
        self.security = SecurityGuard()
        self.command_queue = queue.Queue(maxsize=config.QUEUE_MAX_SIZE)
        self.shutdown_event = threading.Event()
        
        self._publish_token()
        self._setup_server()
        
        # Iniciar el tick de procesamiento principal
        self.schedule_message(1, self._process_command_queue_tick)

    def _setup_logging(self):
        self.logger = logging.getLogger("AntigravityCore")
        self.logger.setLevel(logging.INFO)
        # Evitar agregar handlers múltiples si se recarga
        if not self.logger.handlers:
            handler = RotatingFileHandler(
                config.LOG_FILE_PATH, maxBytes=1024*1024, backupCount=3
            )
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _publish_token(self):
        try:
            with open(config.TOKEN_FILE_PATH, 'w') as f:
                f.write(self.security.session_token)
            self.logger.info("Session token publicado.")
        except Exception as e:
            self.logger.error(f"Error publicando token: {e}")

    def _cleanup_token(self):
        if os.path.exists(config.TOKEN_FILE_PATH):
            try:
                os.remove(config.TOKEN_FILE_PATH)
            except Exception:
                pass

    def _setup_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('127.0.0.1', config.PORT))
        self.server_socket.listen(5)
        
        self.server_thread = threading.Thread(target=self._tcp_listen_loop)
        self.server_thread.daemon = True
        self.server_thread.start()
        self.logger.info(f"TCP Server escuchando en puerto {config.PORT}")

    def _tcp_listen_loop(self):
        """
        Hilo TCP: SOLO escucha, SOLO valida, SOLO encola.
        NUNCA accede al LOM.
        """
        while not self.shutdown_event.is_set():
            try:
                self.server_socket.settimeout(1.0)
                conn, addr = self.server_socket.accept()
                
                # Manejar conexión de manera bloqueante simple para asegurar orden 
                # y backpressure natural (podría ser thread-pool en el futuro).
                self._handle_connection(conn, addr)
                
            except socket.timeout:
                continue
            except Exception as e:
                if not self.shutdown_event.is_set():
                    self.logger.error(f"Error en socket accept: {e}")

    def _handle_connection(self, conn, addr):
        try:
            conn.settimeout(2.0)
            data = conn.recv(config.MAX_MESSAGE_SIZE + 1)
            if not data:
                conn.close()
                return
            
            ip = addr[0]
            validation = self.security.validate_payload(data, ip)
            
            if "error" in validation:
                self._send_response(conn, validation)
                conn.close()
                return
                
            payload = validation["payload"]
            action = payload.get("action")
            
            # Handshake directo desde Hilo TCP sin LOM
            if action == "discover":
                response = {
                    "status": "ok",
                    "version": config.VERSION,
                    "protocol": config.PROTOCOL_VERSION,
                    "token": self.security.session_token,
                    "port": config.PORT,
                    "dsp_port": config.DSP_PORT
                }
                self._send_response(conn, response)
                conn.close()
                return
            
            # Encolar para Hilo Principal Ableton
            queue_item = {
                "conn": conn,
                "payload": payload,
                "timestamp": time.time()
            }
            try:
                self.command_queue.put_nowait(queue_item)
            except queue.Full:
                self._send_response(conn, {"error": "queue_full"})
                conn.close()
                
        except socket.timeout:
            conn.close()
        except Exception as e:
            self.logger.error(f"Error handle_connection: {e}")
            conn.close()

    def _process_command_queue_tick(self):
        """
        Hilo Principal Ableton: Procesa cola (MAX 10/tick).
        """
        if self.shutdown_event.is_set():
            return
            
        processed = 0
        while processed < 10:
            try:
                item = self.command_queue.get_nowait()
                conn = item["conn"]
                payload = item["payload"]
                timestamp = item["timestamp"]
                
                # Timeout de 5000ms
                if (time.time() - timestamp) * 1000 > config.COMMAND_TIMEOUT_MS:
                    self._send_response(conn, {"error": "command_timeout"})
                    conn.close()
                    continue
                
                # Despachar (Fase 2 incluirá el Dispatcher real)
                response = self._dispatch_command(payload)
                self._send_response(conn, response)
                conn.close()
                
                processed += 1
            except queue.Empty:
                break
            except Exception as e:
                self.logger.error(f"Error procesando comando: {e}")
                
        # Re-schedule del tick
        self.schedule_message(1, self._process_command_queue_tick)

    def _dispatch_command(self, payload):
        try:
            result = self.registry.dispatch(payload)
            return {"status": "ok", "result": result}
        except ValueError as ve:
            return {"error": str(ve)}
        except Exception as e:
            self.logger.error(f"Error dispatching command: {e}")
            return {"error": "internal_error", "details": str(e)}

    def _send_response(self, conn, data):
        try:
            msg = json.dumps(data).encode('utf-8')
            conn.sendall(msg)
        except Exception as e:
            self.logger.error(f"Error enviando respuesta: {e}")

    def disconnect(self):
        self.logger.info("Iniciando shutdown limpio de AntigravityCore V2.0.0...")
        self.shutdown_event.set()
        
        if hasattr(self, '_dsp_bridge'):
            self._dsp_bridge.stop()
        
        try:
            self.server_socket.close()
        except Exception:
            pass
            
        if hasattr(self, 'server_thread') and self.server_thread.is_alive():
            self.server_thread.join(timeout=3)
            
        self._cleanup_token()
        self.logger.info("AntigravityCore V2.0.0 desconectado completamente.")
        super(AntigravityCore, self).disconnect()
