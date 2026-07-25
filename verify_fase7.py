from pathlib import Path
STRANGE = Path("/Volumes/Strange/repositorios/ableton-ai-assistant")
FASE7 = [
    ".github/workflows/build_v2.yml",
    "docs/USER_MANUAL_V2.0.0.md",
    "tests/release/test_release_readiness.py",
]
print("VERIFICACION STRANGE FASE 7")
print("=" * 50)
todos_ok = True
for f in FASE7:
    ruta = STRANGE / f
    if ruta.exists():
        lines = len(ruta.read_text(errors='replace').splitlines())
        print(f"  OK    {f} ({lines} lineas)")
    else:
        print(f"  FALTA {f}")
        todos_ok = False
print()
print("STRANGE FASE 7: OK" if todos_ok else "INCOMPLETA")
print("=" * 50)
