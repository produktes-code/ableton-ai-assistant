import os
from pathlib import Path

STRANGE = Path("/Volumes/Strange/repositorios/ableton-ai-assistant")

print("=" * 60)
print("VERIFICACION DISCO STRANGE — FASE 3")
print("=" * 60)

ARCHIVOS_REQUERIDOS = [
    "remote-script/AntigravityCore/config.py",
    "remote-script/AntigravityCore/security.py",
    "remote-script/AntigravityCore/AntigravityCore.py",
    "remote-script/AntigravityCore/command_registry.py",
    "remote-script/AntigravityCore/dsp_engine.py",
    "remote-script/AntigravityCore/dsp_bridge.py",
    "remote-script/AntigravityCore/commands/__init__.py",
    "remote-script/AntigravityCore/commands/transport.py",
    "remote-script/AntigravityCore/commands/tracks.py",
    "remote-script/AntigravityCore/commands/clips.py",
    "remote-script/AntigravityCore/commands/devices.py",
    "remote-script/AntigravityCore/commands/mixer.py",
    "remote-script/AntigravityCore/commands/locators.py",
    "remote-script/AntigravityCore/commands/arrangement.py",
    "remote-script/AntigravityCore/commands/session.py",
    "remote-script/AntigravityCore/commands/midi.py",
    "tests/unit/test_security.py",
    "tests/unit/test_command_registry.py",
    "tests/unit/test_dsp_engine.py",
]

if not STRANGE.exists():
    print("AVISO: Disco Strange no detectado en /Volumes/Strange")
    print("Intentando ruta alternativa...")
    ALTERNATIVAS = [
        Path("/Volumes/Strange/repositorios/ableton-ai-assistant"),
        Path("/Volumes/STRANGE/repositorios/ableton-ai-assistant"),
        Path(os.path.expanduser("~/Desktop/Strange/repositorios/ableton-ai-assistant")),
    ]
    for alt in ALTERNATIVAS:
        if alt.exists():
            STRANGE = alt
            print(f"Encontrado en: {STRANGE}")
            break
    else:
        print("Strange no encontrado. Ejecutar sincronizacion:")
        print()
        print("rsync -av --progress \\")
        print("  /Users/jesusferrer/.gemini/antigravity-ide/scratch/ableton-ai-assistant/ \\")
        print("  /Volumes/Strange/repositorios/ableton-ai-assistant/")
        print()
        print("Luego volver a ejecutar este script.")
        exit(1)

todos_ok = True
print(f"Disco Strange montado en: {STRANGE}")
print()

for archivo in ARCHIVOS_REQUERIDOS:
    ruta = STRANGE / archivo
    if ruta.exists():
        try:
            contenido = ruta.read_text(errors='replace')
            lines = len(contenido.splitlines())
            size = ruta.stat().st_size
            print(f"  OK    {archivo}")
            print(f"        {lines} lineas | {size} bytes")
        except Exception as e:
            print(f"  ERROR {archivo}: {e}")
            todos_ok = False
    else:
        print(f"  FALTA {archivo}")
        todos_ok = False

print()
print("=" * 60)
if todos_ok:
    print("STRANGE: VERIFICACION COMPLETA")
    print("Todos los archivos presentes y legibles")
else:
    print("STRANGE: FALTAN ARCHIVOS")
    print("Sincronizar con:")
    print("rsync -av --progress \\")
    print("  /Users/jesusferrer/.gemini/antigravity-ide/scratch/ableton-ai-assistant/ \\")
    print("  /Volumes/Strange/repositorios/ableton-ai-assistant/")
print("=" * 60)
