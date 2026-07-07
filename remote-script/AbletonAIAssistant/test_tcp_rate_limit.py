import unittest
import socket
import time
import json
import threading

import sys
from unittest.mock import MagicMock

# Mocks para Ableton
sys.modules['ableton'] = MagicMock()
sys.modules['ableton.v3'] = MagicMock()
sys.modules['ableton.v3.control_surface'] = MagicMock()

from AbletonAIAssistant import AbletonAIAssistant

class TestTcpRateLimit(unittest.TestCase):
    def test_rate_limit_25_messages(self):
        assistant = AbletonAIAssistant()
        assistant.show_message = MagicMock()
        assistant.song = MagicMock()
        assistant.application = MagicMock()
        assistant.schedule_message = MagicMock()
        
        # Esperamos a que el server se levante (esta en daemon thread)
        time.sleep(0.5)
        
        responses = []
        errors = 0
        
        # Enviamos 25 mensajes rapido
        for i in range(25):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect(('127.0.0.1', 9001))
                s.sendall(json.dumps({"action": "ping"}).encode('utf-8'))
                
                # Intentamos leer respuesta
                try:
                    resp = s.recv(1024)
                    if b"Rate limit exceeded" in resp:
                        errors += 1
                except socket.timeout:
                    pass
                s.close()
            except Exception as e:
                print(f"Error connect {i}: {e}")
                
        # Deberiamos tener unos 5 errores
        print(f"Mensajes rate limited detectados (con respuesta del server): {errors}")
        
        self.assertTrue(errors >= 4, f"Esperábamos ~5 mensajes limitados, pero detectamos {errors}")
        
        assistant.disconnect()

if __name__ == '__main__':
    unittest.main()
