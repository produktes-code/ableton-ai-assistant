import sys
import os
import unittest
from unittest.mock import MagicMock
import numpy as np

# Mockear websockets y sounddevice antes de importar dsp_engine
sys.modules['sounddevice'] = MagicMock()
sys.modules['websockets'] = MagicMock()
sys.modules['websockets.exceptions'] = MagicMock()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "remote-script", "AntigravityCore")))

import dsp_engine
import dsp_bridge

class TestDSPEngine(unittest.TestCase):
    def test_empty_analysis_cuando_buffer_vacio(self):
        res = dsp_engine.analyze_spectrum([])
        self.assertIn("bands", res)
        self.assertIn("lufs", res)
        self.assertIn("chroma", res)
        self.assertEqual(len(res["bands"]), 8)
        self.assertEqual(len(res["chroma"]), 12)
        self.assertEqual(res["lufs"], -100.0)

    def test_analyze_spectrum_con_seno_puro(self):
        t = np.linspace(0, 1, 44100, endpoint=False)
        signal = np.sin(2 * np.pi * 440 * t)
        
        res = dsp_engine.analyze_spectrum(list(signal))
        bands = res["bands"]
        
        # 440Hz está en la banda 2 (250-500Hz). Debe tener energía.
        # Presencia es banda 5 (4000-8000). Debe tener mucha menos.
        self.assertLess(bands[5], bands[2])
        self.assertGreater(bands[2], 0.0)
        
    def test_anti_clash_score_rango(self):
        res1 = dsp_engine._empty_response()
        score1 = res1["anti_clash_score"]
        self.assertTrue(0.0 <= score1 <= 1.0)
        
        noise = np.random.normal(0, 0.5, 2048)
        res2 = dsp_engine.analyze_spectrum(list(noise))
        score2 = res2["anti_clash_score"]
        self.assertTrue(0.0 <= score2 <= 1.0)

    def test_chroma_normalizado(self):
        res = dsp_engine._empty_response()
        self.assertEqual(len(res["chroma"]), 12)
        
        t = np.linspace(0, 1, 44100, endpoint=False)
        signal = np.sin(2 * np.pi * 440 * t)
        res2 = dsp_engine.analyze_spectrum(list(signal))
        
        for c in res2["chroma"]:
            self.assertTrue(0.0 <= c <= 1.0)
            
        self.assertAlmostEqual(max(res2["chroma"]), 1.0)

    def test_dsp_bridge_no_crashea_sin_dependencias(self):
        logger = MagicMock()
        bridge = dsp_bridge.DSPBridge(logger)
        bridge._has_deps = False
        
        try:
            bridge.start()
            bridge.stop()
        except Exception as e:
            self.fail(f"DSPBridge threw exception: {e}")

if __name__ == '__main__':
    unittest.main()
