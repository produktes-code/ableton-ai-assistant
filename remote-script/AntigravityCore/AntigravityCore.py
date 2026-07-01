from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import ControlSurface
import logging
import threading
import socket
import json
from .midi_generator import MidiGenerator
from .session_manager import SessionManager

# Configurar logging básico para depuración dentro de Live
logger = logging.getLogger(__name__)

class AntigravityCore(ControlSurface):
    """
    Núcleo del asistente Antigravity para Ableton Live.
    Actúa como un puente entre la API de Live (LOM) y el servidor MCP.
    """
    
    def __init__(self, *a, **k):
        super(AntigravityCore, self).__init__(*a, **k)
        self.show_message("Antigravity Core Inicializado")
        logger.info("AntigravityCore se ha cargado correctamente.")
        self.midi_gen = MidiGenerator(self.song())
        self.session_man = SessionManager(self.song(), self.application())
        self._setup_server()

    def _setup_server(self):
        """
        Inicializa un servidor TCP simple en un hilo separado para 
        comunicarse con el servidor MCP externo sin bloquear Live.
        """
        self.host = '127.0.0.1'
        self.port = 9001
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        
        self.running = True
        self.server_thread = threading.Thread(target=self._server_loop)
        self.server_thread.daemon = True
        self.server_thread.start()
        logger.info(f"Antigravity TCP Server escuchando en {self.host}:{self.port}")

    def _server_loop(self):
        while self.running:
            try:
                self.server_socket.settimeout(1.0)
                conn, addr = self.server_socket.accept()
                with conn:
                    data = conn.recv(4096)
                    if data:
                        self._handle_command(data.decode('utf-8'))
            except socket.timeout:
                continue
            except Exception as e:
                if self.running:
                    logger.error(f"Error en socket: {e}")

    def _handle_command(self, raw_data):
        """
        Maneja los comandos entrantes del MCP.
        Encola las llamadas al LOM en el hilo principal usando schedule_message.
        """
        try:
            command = json.loads(raw_data)
            logger.info(f"Comando recibido: {command}")
            action = command.get('action')
            payload = command.get('payload', {})
            
            if action == 'ping':
                self.schedule_message(1, lambda: self.show_message("Antigravity: PING recibido"))
            elif action == 'read_midi':
                track_idx = payload.get('track_index', 0)
                clip_idx = payload.get('clip_index', 0)
                # Ejecutar en el main thread para evitar crash del LOM
                self.schedule_message(1, lambda: self._execute_read_midi(track_idx, clip_idx))
            elif action == 'inject_midi':
                track_idx = payload.get('track_index', 0)
                clip_idx = payload.get('clip_index', 0)
                notes = payload.get('notes', [])
                self.schedule_message(1, lambda: self._execute_inject_midi(track_idx, clip_idx, notes))
            elif action == 'add_device':
                track_idx = payload.get('track_index', 0)
                device_name = payload.get('device_name', '')
                self.schedule_message(1, lambda: self._execute_add_device(track_idx, device_name))
            elif action == 'set_parameter':
                track_idx = payload.get('track_index', 0)
                device_idx = payload.get('device_index', 0)
                param_name = payload.get('param_name', '')
                val = payload.get('value', 0.0)
                self.schedule_message(1, lambda: self._execute_set_param(track_idx, device_idx, param_name, val))
                
        except json.JSONDecodeError:
            logger.error("JSON inválido recibido")

    def _execute_read_midi(self, track_idx, clip_idx):
        result = self.midi_gen.read_midi_clip(track_idx, clip_idx)
        logger.info(f"Lectura MIDI resultado: {result}")

    def _execute_inject_midi(self, track_idx, clip_idx, notes):
        result = self.midi_gen.inject_midi_notes(track_idx, clip_idx, notes)
        logger.info(f"Inyección MIDI resultado: {result}")
        if result['status'] == 'success':
            self.show_message("Antigravity: Notas MIDI inyectadas")

    def _execute_add_device(self, track_idx, device_name):
        result = self.session_man.add_native_device(track_idx, device_name)
        logger.info(f"Add device resultado: {result}")
        if result['status'] == 'success':
            self.show_message(f"Antigravity: {device_name} añadido")

    def _execute_set_param(self, track_idx, device_idx, param_name, val):
        result = self.session_man.set_device_parameter(track_idx, device_idx, param_name, val)
        logger.info(f"Set parameter resultado: {result}")


    def disconnect(self):
        """
        Llamado cuando el script se descarga.
        """
        self.running = False
        try:
            if hasattr(self, 'server_socket'):
                self.server_socket.close()
        except Exception:
            pass
        self.show_message("Antigravity Core Desconectado")
        logger.info("AntigravityCore desconectado.")
        super(AntigravityCore, self).disconnect()

