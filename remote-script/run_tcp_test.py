import sys
from unittest.mock import MagicMock
sys.modules['ableton'] = MagicMock()
sys.modules['ableton.v3'] = MagicMock()
sys.modules['ableton.v3.control_surface'] = MagicMock()

import unittest
from AbletonAIAssistant.test_tcp_reconnect import TestTcpReconnect

if __name__ == '__main__':
    unittest.main()
