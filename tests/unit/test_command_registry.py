import sys
import os
import unittest
from unittest.mock import MagicMock

# Mockear el módulo ableton.v3
sys.modules['ableton'] = MagicMock()
sys.modules['ableton.v3'] = MagicMock()
sys.modules['ableton.v3.control_surface'] = MagicMock()

# Configurar path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "remote-script")))

from AntigravityCore.command_registry import CommandRegistry

class TestCommandRegistry(unittest.TestCase):
    def setUp(self):
        self.ctx = {"song": None, "application": None}
        self.registry = CommandRegistry(self.ctx)
        self.registry.auto_discover()

    def test_auto_discovery_and_count(self):
        # We registered ping + 15 transport + 12 tracks + 11 clips = 39 commands
        count = self.registry.get_command_count()
        self.assertGreater(count, 30, f"Command count should be > 30, got {count}")

    def test_list_commands(self):
        cmds = self.registry.list_commands()
        self.assertIn("ping", cmds)
        self.assertIn("transport_play", cmds)
        self.assertIn("description", cmds["ping"])

    def test_invalid_action(self):
        with self.assertRaises(ValueError) as context:
            self.registry.dispatch({"action": "non_existent_action"})
        self.assertIn("no existe", str(context.exception))
        self.assertIn("Comandos disponibles incluyen", str(context.exception))

    def test_param_validation_unexpected(self):
        with self.assertRaises(ValueError) as context:
            self.registry.dispatch({"action": "ping", "params": {"unexpected": 123}})
        self.assertIn("Parámetro inesperado", str(context.exception))

    def test_param_validation_type_int(self):
        with self.assertRaises(ValueError) as context:
            # set_key expects int for root_note
            self.registry.dispatch({"action": "set_key", "params": {"root_note": "not_an_int"}})
        self.assertIn("debe ser int", str(context.exception))

    def test_missing_action(self):
        with self.assertRaises(ValueError) as context:
            self.registry.dispatch({"params": {}})
        self.assertIn("Falta 'action'", str(context.exception))

if __name__ == '__main__':
    unittest.main()
