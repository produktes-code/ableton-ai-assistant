import sys
import os
import unittest
from unittest.mock import MagicMock
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "remote-script", "AntigravityCore")))
from midi_generator import MidiGenerator

class TestMidiGenerator(unittest.TestCase):
    def test_validate_note_rango_completo(self):
        MidiGenerator.validate_note(0, 64, 0, 1)
        MidiGenerator.validate_note(60, 64, 0, 1)
        MidiGenerator.validate_note(127, 64, 0, 1)
        MidiGenerator.validate_note(60, 1, 0, 1)
        MidiGenerator.validate_note(60, 127, 0, 1)
        
        with self.assertRaises(ValueError): MidiGenerator.validate_note(-1, 64, 0, 1)
        with self.assertRaises(ValueError): MidiGenerator.validate_note(128, 64, 0, 1)
        with self.assertRaises(ValueError): MidiGenerator.validate_note(60, 0, 0, 1)
        with self.assertRaises(ValueError): MidiGenerator.validate_note(60, 64, -1, 1)
        with self.assertRaises(ValueError): MidiGenerator.validate_note(60, 64, 0, -1)

    def test_house_groove_estructura(self):
        notes = MidiGenerator.generate_groove("house", 1, 124.0)
        self.assertGreater(len(notes), 0)
        has_kick_0 = any(n["pitch"] == 36 and n["start"] == 0.0 for n in notes)
        self.assertTrue(has_kick_0)
        for n in notes:
            self.assertTrue(0 <= n["pitch"] <= 127)
            self.assertTrue(1 <= n["velocity"] <= 127)

    def test_techno_hihat_densidad(self):
        notes = MidiGenerator.generate_groove("techno", 1, 130.0)
        hihats = [n for n in notes if n["pitch"] in (42, 46)]
        self.assertGreaterEqual(len(hihats), 16)

    def test_humanizacion_jitter(self):
        random.seed(42)
        n1 = MidiGenerator.generate_groove("house", 1, 120.0, humanize=True)
        random.seed(99)
        n2 = MidiGenerator.generate_groove("house", 1, 120.0, humanize=True)
        self.assertNotEqual(n1[0]["start"], n2[0]["start"])

    def test_groove_invalido_error(self):
        with self.assertRaises(ValueError):
            MidiGenerator.generate_groove("invalido", 1, 120.0)

    def test_melody_en_escala(self):
        notes = MidiGenerator.generate_melody(60, "minor", 1, 0.8)
        for n in notes:
            self.assertTrue(0 <= n["pitch"] <= 127)
            self.assertTrue(1 <= n["velocity"] <= 127)

    def test_undo_step_garantizado(self):
        song = MagicMock()
        clip = MagicMock()
        clip.song = song
        clip.canonical_parent = song
        clip.add_new_notes.side_effect = Exception("Fallo forzado")
        
        try:
            MidiGenerator.inject_notes(clip, [{"pitch":60, "velocity":100, "start":0, "duration":1}])
        except Exception:
            pass
            
        song.begin_undo_step.assert_called_once()
        song.end_undo_step.assert_called_once()

    def test_quantize_grid_025(self):
        notes = [{"start": 0.33}]
        quant = MidiGenerator.quantize_notes(notes, 0.25)
        self.assertEqual(quant[0]["start"], 0.25)

    def test_transpose_clampa_rango(self):
        notes = [{"pitch": 120}, {"pitch": 5}]
        trans = MidiGenerator.transpose_notes(notes, 20)
        self.assertEqual(trans[0]["pitch"], 127)
        trans2 = MidiGenerator.transpose_notes(notes, -30)
        self.assertEqual(trans2[1]["pitch"], 0)

if __name__ == "__main__":
    unittest.main()
