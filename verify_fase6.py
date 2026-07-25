from pathlib import Path
STRANGE = Path("/Volumes/Strange/repositorios/ableton-ai-assistant")
FASE6 = [
    "tests/integration/__init__.py",
    "tests/integration/test_tcp_integration.py",
    "tests/stress/__init__.py",
    "tests/stress/test_stress_suite.py",
    "tests/run_all_tests.py",
    "docs/master_test_report.json",
]
print("VERIFICACION STRANGE FASE 6")
print("=" * 50)
todos_ok = True
for f in FASE6:
    ruta = STRANGE / f
    if ruta.exists():
        lines = len(ruta.read_text(errors='replace').splitlines())
        print(f"  OK    {f} ({lines} lineas)")
    else:
        print(f"  FALTA {f}")
        todos_ok = False
print()
print("STRANGE FASE 6: OK" if todos_ok else "INCOMPLETA")
print("=" * 50)
