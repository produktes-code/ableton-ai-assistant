import unittest
from unittest.mock import MagicMock
import socket
import time
import threading
import sys

# Mocks para LOM (Ableton Live API)
sys.modules["ableton"] = MagicMock()
sys.modules["ableton.v3"] = MagicMock()
sys.modules["ableton.v3.control_surface"] = MagicMock()

# Ahora podemos importar
from AbletonAIAssistant import AbletonAIAssistant  # noqa: E402


class TestTcpReconnect(unittest.TestCase):
    def test_reconnect_on_busy_port(self):
        import os

        # Obtener un puerto libre
        s_temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_temp.bind(("127.0.0.1", 0))
        port = s_temp.getsockname()[1]
        s_temp.close()

        os.environ["ABLETON_TCP_PORT"] = str(port)

        blocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        blocker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        blocker.bind(("127.0.0.1", port))
        blocker.listen(1)

        # Mocks para metodos base de ControlSurface
        assistant = AbletonAIAssistant()
        assistant.show_message = MagicMock()
        assistant.song = MagicMock()
        assistant.application = MagicMock()

        def release_port():
            time.sleep(2)
            blocker.close()

        t = threading.Thread(target=release_port)
        t.start()

        time.sleep(6)

        self.assertTrue(hasattr(assistant, "server_socket"))
        self.assertNotEqual(assistant.server_socket.fileno(), -1)

        assistant.disconnect()
        t.join()


if __name__ == "__main__":
    unittest.main()
