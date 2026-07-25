import sys
import os
import unittest
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "remote-script", "AntigravityCore")))
from session_manager import SessionManager

class TestSessionManager(unittest.TestCase):
    def setUp(self):
        self.param = MagicMock()
        self.param.name = "Cutoff"
        self.param.value = 0.5
        self.param.min = 0.0
        self.param.max = 1.0
        
        self.device = MagicMock()
        self.device.parameters = [self.param]
        
        self.track = MagicMock()
        self.track.devices = [self.device]
        
        self.song = MagicMock()
        self.song.tracks = [self.track]
        
        self.ctx = {"song": self.song, "application": MagicMock()}

    def test_get_device_params_estructura(self):
        params = SessionManager.get_device_params(0, 0, self.ctx)
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0]["name"], "Cutoff")
        self.assertEqual(params[0]["value"], 0.5)
        self.assertEqual(params[0]["min"], 0.0)
        self.assertEqual(params[0]["max"], 1.0)

    def test_set_param_respeta_limites(self):
        SessionManager.set_device_param(0, 0, 0, 1.5, self.ctx)
        self.assertEqual(self.param.value, 1.0)
        
        SessionManager.set_device_param(0, 0, 0, -0.5, self.ctx)
        self.assertEqual(self.param.value, 0.0)
        
        SessionManager.set_device_param(0, 0, 0, 0.5, self.ctx)
        self.assertEqual(self.param.value, 0.5)

    def test_load_device_retorna_bool(self):
        efx = MagicMock()
        efx.name = "Auto Filter"
        self.ctx["application"].browser.audio_effects = [efx]
        self.ctx["application"].browser.instruments = []
        
        res1 = SessionManager.load_device(0, "Auto Filter", self.ctx)
        self.assertTrue(res1)
        
        res2 = SessionManager.load_device(0, "NonExistent", self.ctx)
        self.assertFalse(res2)

if __name__ == "__main__":
    unittest.main()
