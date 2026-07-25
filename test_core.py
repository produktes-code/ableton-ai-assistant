import sys
import os
import json
import socket
import time
import threading
from unittest.mock import MagicMock

# Mockear el módulo ableton.v3
sys.modules['ableton'] = MagicMock()
sys.modules['ableton.v3'] = MagicMock()
mock_cs = MagicMock()
sys.modules['ableton.v3.control_surface'] = mock_cs

class MockControlSurface:
    def __init__(self, *a, **k):
        pass
    def schedule_message(self, delay, callback):
        # Simplistic mock for schedule_message
        # delay is in ticks, but we just use seconds
        t = threading.Timer(delay * 0.1, callback)
        t.daemon = True
        t.start()
    def disconnect(self):
        pass

mock_cs.ControlSurface = MockControlSurface

# Agregar el directorio actual al path para importar módulos locales
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "remote-script")))

from AntigravityCore.AntigravityCore import AntigravityCore
from AntigravityCore import config

def test_core_handshake():
    print("--- INICIANDO TEST CORE HANDSHAKE (FASE 1) ---")
    core = AntigravityCore()
    time.sleep(0.5) # Wait for server to start
    
    try:
        # Test TCP connection and handshake
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect(('127.0.0.1', config.PORT))
        
        req = json.dumps({"action": "discover", "protocol": 2}).encode('utf-8')
        s.sendall(req)
        
        data = s.recv(4096)
        res = json.loads(data.decode('utf-8'))
        
        assert res.get("status") == "ok", f"Handshake failed: {res}"
        assert res.get("version") == config.VERSION, "Version mismatch"
        assert res.get("token") == core.security.session_token, "Token mismatch"
        print("✅ Handshake exitoso (discover)")
        
        # Test ping (needs token)
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect(('127.0.0.1', config.PORT))
        req2 = json.dumps({"action": "ping", "protocol": 2, "token": core.security.session_token}).encode('utf-8')
        s2.sendall(req2)
        
        # This will be processed by the tick
        data2 = s2.recv(4096)
        res2 = json.loads(data2.decode('utf-8'))
        assert res2.get("status") == "ok", f"Ping failed: {res2}"
        print("✅ Ping exitoso (queue_tick processing works)")
        
    finally:
        core.disconnect()
    
    print("--- TEST CORE COMPLETADO ---")

if __name__ == "__main__":
    test_core_handshake()
