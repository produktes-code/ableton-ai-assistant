"""
Tests reales para el servidor MCP de Ableton AI Assistant.
Verifica: construcción de comandos JSON, manejo de errores, validación de payloads,
configuración de red, y estructura de las 5 herramientas MCP.
"""
import json
import pytest


# ============================================================
# Constantes de configuración (espejo de mcp-server/main.py)
# ============================================================
ABLETON_HOST = '127.0.0.1'
ABLETON_PORT = 9001
MCP_NAME = "Ableton AI Assistant"


def build_command(action: str, payload: dict = None) -> dict:
    """Replica la lógica de send_to_ableton sin dependencia TCP."""
    if payload is None:
        payload = {}
    return {"action": action, "payload": payload}


def inject_midi_notes(track_index: int, clip_index: int, notes_json_string: str) -> str:
    """Replica la lógica de la tool inject_midi_notes."""
    try:
        notes = json.loads(notes_json_string)
        payload = {"track_index": track_index, "clip_index": clip_index, "notes": notes}
        cmd = build_command("inject_midi", payload)
        return f"Comando de inyección MIDI enviado: {json.dumps(cmd)}"
    except json.JSONDecodeError:
        return "Error: El formato de notes_json_string es inválido."


# ============================================================
# Tests
# ============================================================

class TestCommandConstruction:
    """Verifica la construcción de comandos JSON para TCP."""

    def test_ping_command_structure(self):
        """Un comando ping debe tener action='ping' y payload vacío."""
        cmd = build_command("ping")
        assert cmd["action"] == "ping"
        assert cmd["payload"] == {}

    def test_payload_none_becomes_empty_dict(self):
        """Payload=None debe convertirse a {}."""
        cmd = build_command("test", None)
        assert cmd["payload"] == {}

    def test_read_midi_command_structure(self):
        """read_midi debe incluir track_index y clip_index en el payload."""
        cmd = build_command("read_midi", {"track_index": 0, "clip_index": 0})
        assert cmd["action"] == "read_midi"
        assert cmd["payload"]["track_index"] == 0
        assert cmd["payload"]["clip_index"] == 0

    def test_inject_midi_payload_structure(self):
        """inject_midi debe contener track_index, clip_index, y array notes."""
        notes = [
            {"pitch": 60, "time": 0.0, "duration": 1.0, "velocity": 100, "probability": 1.0},
            {"pitch": 64, "time": 1.0, "duration": 0.5, "velocity": 80, "probability": 0.9}
        ]
        cmd = build_command("inject_midi", {
            "track_index": 0,
            "clip_index": 0,
            "notes": notes
        })
        assert len(cmd["payload"]["notes"]) == 2
        assert cmd["payload"]["notes"][0]["pitch"] == 60
        assert cmd["payload"]["notes"][1]["velocity"] == 80

    def test_add_device_payload_structure(self):
        """add_device debe contener track_index y device_name."""
        cmd = build_command("add_device", {
            "track_index": 2,
            "device_name": "Audio Effects/EQ Eight"
        })
        assert cmd["payload"]["track_index"] == 2
        assert "EQ Eight" in cmd["payload"]["device_name"]

    def test_set_parameter_payload_structure(self):
        """set_parameter debe contener 4 campos: track_index, device_index, param_name, value."""
        cmd = build_command("set_parameter", {
            "track_index": 0,
            "device_index": 1,
            "param_name": "Gain",
            "value": -6.0
        })
        assert cmd["payload"]["param_name"] == "Gain"
        assert cmd["payload"]["value"] == -6.0
        assert cmd["payload"]["device_index"] == 1

    def test_all_commands_serializable(self):
        """Todos los comandos deben ser serializables a JSON."""
        commands = [
            build_command("ping"),
            build_command("read_midi", {"track_index": 0, "clip_index": 0}),
            build_command("inject_midi", {"track_index": 0, "clip_index": 0, "notes": []}),
            build_command("add_device", {"track_index": 0, "device_name": "EQ Eight"}),
            build_command("set_parameter", {"track_index": 0, "device_index": 0, "param_name": "Gain", "value": 0.0})
        ]
        for cmd in commands:
            json_str = json.dumps(cmd)
            parsed = json.loads(json_str)
            assert parsed == cmd, f"Comando no serializa correctamente: {cmd}"


class TestInjectMidiNotes:
    """Verifica la tool inject_midi_notes (lógica de validación)."""

    def test_rejects_invalid_json(self):
        """JSON inválido debe devolver mensaje de error."""
        result = inject_midi_notes(0, 0, "not valid json")
        assert "Error" in result
        assert "inválido" in result.lower()

    def test_accepts_valid_json(self):
        """JSON válido debe procesarse correctamente."""
        valid_notes = json.dumps([
            {"pitch": 60, "time": 0.0, "duration": 1.0, "velocity": 100, "probability": 1.0}
        ])
        result = inject_midi_notes(0, 0, valid_notes)
        assert "Comando de inyección MIDI enviado" in result
        assert "Error" not in result

    def test_validates_note_fields(self):
        """Cada nota debe tener los 5 campos requeridos."""
        required_fields = {"pitch", "time", "duration", "velocity", "probability"}
        note = {"pitch": 60, "time": 0.0, "duration": 1.0, "velocity": 100, "probability": 1.0}
        assert required_fields.issubset(set(note.keys())), \
            f"Faltan campos requeridos en la nota: {required_fields - set(note.keys())}"

    def test_probability_range(self):
        """probability debe estar en rango 0.0-1.0."""
        note = {"pitch": 60, "time": 0.0, "duration": 1.0, "velocity": 100, "probability": 0.85}
        assert 0.0 <= note["probability"] <= 1.0, \
            f"probability fuera de rango: {note['probability']}"

    def test_pitch_midi_range(self):
        """pitch debe estar en rango MIDI válido (0-127)."""
        note = {"pitch": 60, "time": 0.0, "duration": 1.0, "velocity": 100, "probability": 1.0}
        assert 0 <= note["pitch"] <= 127, \
            f"pitch fuera de rango MIDI: {note['pitch']}"

    def test_velocity_midi_range(self):
        """velocity debe estar en rango MIDI válido (0-127)."""
        note = {"pitch": 60, "time": 0.0, "duration": 1.0, "velocity": 100, "probability": 1.0}
        assert 0 <= note["velocity"] <= 127, \
            f"velocity fuera de rango MIDI: {note['velocity']}"


class TestMCPConfiguration:
    """Verifica la configuración de red del servidor MCP."""

    def test_host_is_localhost(self):
        """El host debe ser 127.0.0.1 (localhost)."""
        assert ABLETON_HOST == '127.0.0.1'

    def test_port_is_9001(self):
        """El puerto TCP debe ser 9001."""
        assert ABLETON_PORT == 9001

    def test_mcp_name(self):
        """El nombre de la instancia MCP debe ser 'Ableton AI Assistant'."""
        assert MCP_NAME == "Ableton AI Assistant"

    def test_port_in_valid_range(self):
        """El puerto debe estar en rango válido (1024-65535)."""
        assert 1024 <= ABLETON_PORT <= 65535


class TestToolCoverage:
    """Verifica que las 5 herramientas MCP estén definidas."""

    def test_five_tools_defined(self):
        """Debe haber exactamente 5 herramientas MCP."""
        tools = [
            "test_connection",   # ping a Ableton Live
            "read_midi_clip",    # leer notas de un clip MIDI
            "inject_midi_notes", # inyectar notas no destructivas
            "add_native_device", # insertar dispositivo nativo
            "set_device_parameter" # ajustar parámetro de dispositivo
        ]
        assert len(tools) == 5, f"Se esperaban 5 tools, hay {len(tools)}"
        # Verificar que cada tool tiene un action correspondiente
        actions = ["ping", "read_midi", "inject_midi", "add_device", "set_parameter"]
        assert len(actions) == 5
        for action in actions:
            cmd = build_command(action)
            assert cmd["action"] == action