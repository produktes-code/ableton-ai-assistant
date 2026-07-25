import socket
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AntigravityMCP")

mcp = FastMCP("Antigravity")

ABLETON_HOST = '127.0.0.1'
ABLETON_PORT = 9001

def send_to_ableton(action: str, payload: dict = None) -> dict:
    """Envía un comando al servidor TCP de Antigravity en Ableton Live."""
    if payload is None:
        payload = {}
    
    command = {"action": action, "payload": payload}
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2.0)
            s.connect((ABLETON_HOST, ABLETON_PORT))
            s.sendall(json.dumps(command).encode('utf-8'))
            return {"status": "success", "message": f"Comando '{action}' enviado a Ableton."}
    except Exception as e:
        logger.error(f"Error conectando a Ableton: {e}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def test_connection() -> str:
    """Envía un ping a Ableton Live para probar la conexión."""
    result = send_to_ableton("ping")
    if result["status"] == "success":
        return "Conexión con Ableton Live exitosa."
    else:
        return f"Fallo al conectar con Ableton Live: {result['message']}"

@mcp.tool()
def read_midi_clip(track_index: int, clip_index: int) -> str:
    """
    Lee las notas de un clip MIDI existente para usar como contexto musical.
    track_index: Índice de la pista (0-indexed).
    clip_index: Índice del slot del clip (0-indexed).
    """
    payload = {"track_index": track_index, "clip_index": clip_index}
    # En un sistema real asíncrono, esperaríamos la respuesta del socket TCP.
    # Por ahora enviamos el trigger.
    result = send_to_ableton("read_midi", payload)
    return f"Comando de lectura MIDI enviado: {result['message']}"

@mcp.tool()
def inject_midi_notes(track_index: int, clip_index: int, notes_json_string: str) -> str:
    """
    Inyecta nuevas notas de forma no destructiva en un clip.
    notes_json_string: Array de objetos JSON stringificado. Cada objeto debe tener:
      pitch (int), time (float), duration (float), velocity (int), probability (float 0.0-1.0).
    """
    try:
        notes = json.loads(notes_json_string)
        payload = {"track_index": track_index, "clip_index": clip_index, "notes": notes}
        result = send_to_ableton("inject_midi", payload)
        return f"Comando de inyección MIDI enviado: {result['message']}"
    except json.JSONDecodeError:
        return "Error: El formato de notes_json_string es inválido."

@mcp.tool()
def add_native_device(track_index: int, device_name: str) -> str:
    """
    Inserta un dispositivo nativo en una pista buscando en el navegador.
    track_index: Índice de la pista (0-indexed).
    device_name: Nombre parcial o ruta del dispositivo (ej. "Audio Effects/EQ Eight").
    """
    payload = {"track_index": track_index, "device_name": device_name}
    result = send_to_ableton("add_device", payload)
    return f"Comando de inyección de dispositivo enviado: {result['message']}"

@mcp.tool()
def set_device_parameter(track_index: int, device_index: int, param_name: str, value: float) -> str:
    """
    Ajusta el valor de un parámetro específico de un dispositivo.
    track_index: Índice de la pista (0-indexed).
    device_index: Índice del dispositivo en la cadena (0-indexed).
    param_name: Nombre exacto del parámetro (ej. "Gain", "Freq", "Q").
    value: Valor numérico a asignar.
    """
    payload = {
        "track_index": track_index,
        "device_index": device_index,
        "param_name": param_name,
        "value": value
    }
    result = send_to_ableton("set_parameter", payload)
    return f"Comando de ajuste de parámetro enviado: {result['message']}"

if __name__ == "__main__":
    logger.info("Iniciando servidor MCP de Antigravity...")
    # FastMCP se encarga de manejar el transporte stdio por defecto
    mcp.run()
