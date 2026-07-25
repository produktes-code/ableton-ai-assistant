from pathlib import Path
STRANGE = Path("/Volumes/Strange/repositorios/ableton-ai-assistant")
FASE5 = [
    "electron-app/index.html",
    "electron-app/styles/glassmorphism.css",
    "electron-app/js/tcp-client.js",
    "electron-app/js/dsp-visualizer.js",
    "electron-app/js/app.js",
    "electron-app/js/session-sync.js",
    "tests/ui/__init__.py",
    "tests/ui/test_ui_structure.py",
]
print("VERIFICACION STRANGE FASE 5")
print("=" * 50)
todos_ok = True
for f in FASE5:
    ruta = STRANGE / f
    if ruta.exists():
        lines = len(ruta.read_text(errors='replace').splitlines())
        print(f"  OK    {f} ({lines} lineas)")
    else:
        print(f"  FALTA {f}")
        todos_ok = False
print()
print("STRANGE FASE 5: OK" if todos_ok else "STRANGE FASE 5: INCOMPLETA")
print("=" * 50)
