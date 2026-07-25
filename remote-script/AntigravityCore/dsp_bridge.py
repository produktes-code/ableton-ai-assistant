import os
import sys
import time
import subprocess
import threading
from pathlib import Path

class DSPBridge:
    def __init__(self, logger):
        self._logger = logger
        self._process = None
        self._monitor_thread = None
        self._restart_count = 0
        self._max_restarts = 3
        self._should_run = False
        self._dsp_script = Path(__file__).parent / "dsp_engine.py"
        self._has_deps = self._check_deps()

    def _check_deps(self):
        try:
            import numpy
            import sounddevice
            import websockets
            return True
        except ImportError:
            return False

    def start(self):
        if not self._has_deps:
            self._logger.warning("Dependencias DSP no encontradas (numpy, sounddevice, websockets). DSP desactivado.")
            return

        if not self._dsp_script.exists():
            self._logger.error(f"Script DSP no encontrado: {self._dsp_script}")
            return
            
        self._should_run = True
        self._spawn_process()
        
        self._monitor_thread = threading.Thread(target=self._monitor_process)
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def _spawn_process(self):
        if self._process and self._process.poll() is None:
            return
            
        env = os.environ.copy()
        env["ANTIGRAVITY_DSP"] = "1"
        
        try:
            self._process = subprocess.Popen(
                [sys.executable, str(self._dsp_script)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
                close_fds=True
            )
            self._logger.info(f"DSP Engine lanzado (PID: {self._process.pid})")
        except Exception as e:
            self._logger.error(f"Error lanzando DSP Engine: {e}")

    def _monitor_process(self):
        while self._should_run:
            if self._process:
                ret = self._process.poll()
                if ret is not None:
                    stderr = ""
                    try:
                        stderr = self._process.stderr.read().decode('utf-8')
                    except Exception:
                        pass
                        
                    self._logger.error(f"DSP Engine falló (Exit {ret}): {stderr}")
                    
                    if self._restart_count < self._max_restarts:
                        self._restart_count += 1
                        self._logger.info(f"Reiniciando DSP Engine ({self._restart_count}/{self._max_restarts})...")
                        time.sleep(2)
                        self._spawn_process()
                    else:
                        self._logger.error("Máximo de reinicios superado para DSP Engine.")
                        self._should_run = False
                        break
            time.sleep(5)

    def stop(self):
        self._should_run = False
        if self._process and self._process.poll() is None:
            self._logger.info("Deteniendo DSP Engine...")
            self._process.terminate()
            try:
                self._process.wait(timeout=3)
                self._logger.info("DSP Engine detenido limpiamente.")
            except subprocess.TimeoutExpired:
                self._logger.warning("DSP Engine no terminó, forzando kill...")
                self._process.kill()
