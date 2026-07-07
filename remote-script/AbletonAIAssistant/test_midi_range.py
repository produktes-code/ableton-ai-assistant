import unittest
from unittest.mock import MagicMock
import sys

# Mocks para Ableton
sys.modules['ableton'] = MagicMock()
sys.modules['ableton.v3'] = MagicMock()
sys.modules['ableton.v3.control_surface'] = MagicMock()

# Mock de Live
class MockMidiNoteSpec:
    def __init__(self, start_time, duration, pitch, velocity, mute, probability):
        self.pitch = pitch
        self.velocity = velocity
        
mock_live = MagicMock()
mock_live.Clip.MidiNoteSpecification = MockMidiNoteSpec
sys.modules['Live'] = mock_live

from AbletonAIAssistant.midi_generator import MidiGenerator

class TestMidiRange(unittest.TestCase):
    def test_pitch_clamp(self):
        # Mock de song y clip
        mock_song = MagicMock()
        mock_track = MagicMock()
        mock_clip_slot = MagicMock()
        mock_clip = MagicMock()
        
        mock_clip.is_midi_clip = True
        mock_clip_slot.has_clip = True
        mock_clip_slot.clip = mock_clip
        
        mock_track.clip_slots = [mock_clip_slot]
        mock_song.tracks = [mock_track]
        
        gen = MidiGenerator(mock_song)
        
        # Inyectar notas invalidas (pitch > 127 y pitch < 0)
        invalid_notes = [
            {"pitch": 150, "velocity": 130},
            {"pitch": -10, "velocity": -5}
        ]
        
        result = gen.inject_midi_notes(0, 0, invalid_notes)
        self.assertEqual(result["status"], "success")
        
        # Verificar que se anadieron las notas clampeadas
        mock_clip.add_new_notes.assert_called_once()
        args, kwargs = mock_clip.add_new_notes.call_args
        
        notes_tuple = args[0]
        self.assertEqual(len(notes_tuple), 2)
        
        # Primer nota clampeada (150 -> 127)
        self.assertEqual(notes_tuple[0].pitch, 127)
        self.assertEqual(notes_tuple[0].velocity, 127)
        
        # Segunda nota clampeada (-10 -> 0)
        self.assertEqual(notes_tuple[1].pitch, 0)
        self.assertEqual(notes_tuple[1].velocity, 1)

if __name__ == '__main__':
    unittest.main()
