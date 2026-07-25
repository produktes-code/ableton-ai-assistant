import os
from pathlib import Path

STRANGE = Path("/Volumes/Strange/repositorios/ableton-ai-assistant")

FASE4 = [
    "remote-script/AntigravityCore/midi_generator.py",
    "remote-script/AntigravityCore/session_manager.py",
    "tests/unit/test_midi_generator.py",
    "tests/unit/test_session_manager.py",
]

print("=" * 60)
print("VERIFICACION STRANGE — FASE 4")
print("=" * 60)

todos_ok = True
for archivo in FASE4:
    ruta = STRANGE / archivo
    if ruta.exists():
        lines = len(ruta.read_text(errors='replace').splitlines())
        size = ruta.stat().st_size
        print(f"  OK    {archivo}")
        print(f"        {lines} lineas | {size} bytes")
    else:
        print(f"  FALTA {archivo}")
        todos_ok = False

print()
if todos_ok:
    print("STRANGE FASE 4: COMPLETA")
else:
    print("STRANGE FASE 4: INCOMPLETA — Revisar rsync")
print("=" * 60)
