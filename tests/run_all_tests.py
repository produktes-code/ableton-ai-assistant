import subprocess
import sys
import json
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent

SUITES = [
    {
        "nombre": "Seguridad TCP",
        "path": "tests/unit/test_security.py",
        "critico": True
    },
    {
        "nombre": "Command Registry",
        "path": "tests/unit/test_command_registry.py",
        "critico": True
    },
    {
        "nombre": "DSP Engine",
        "path": "tests/unit/test_dsp_engine.py",
        "critico": True
    },
    {
        "nombre": "MIDI Generator",
        "path": "tests/unit/test_midi_generator.py",
        "critico": True
    },
    {
        "nombre": "Session Manager",
        "path": "tests/unit/test_session_manager.py",
        "critico": True
    },
    {
        "nombre": "UI Structure",
        "path": "tests/ui/test_ui_structure.py",
        "critico": True
    },
    {
        "nombre": "TCP Integration",
        "path": "tests/integration/test_tcp_integration.py",
        "critico": True
    },
    {
        "nombre": "Stress Suite",
        "path": "tests/stress/test_stress_suite.py",
        "critico": False
    },
]

def run_suite(suite):
    start = time.monotonic()
    result = subprocess.run(
        [sys.executable, "-m", "pytest",
         suite["path"], "-v", "--tb=short",
         f"--junit-xml=docs/test_{suite['path'].replace('/','-')}.xml"],
        capture_output=True,
        text=True,
        cwd=ROOT
    )
    elapsed = time.monotonic() - start
    passed = result.returncode == 0
    return {
        "nombre": suite["nombre"],
        "passed": passed,
        "tiempo": round(elapsed, 2),
        "critico": suite["critico"],
        "output": result.stdout[-500:] if not passed else ""
    }

print("=" * 65)
print("  ANTIGRAVITY V2.0.0 — SUITE MAESTRA DE TESTS")
print(f"  {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 65)

resultados = []
for suite in SUITES:
    path = ROOT / suite["path"]
    if not path.exists():
        print(f"  SKIP  {suite['nombre']} (archivo no encontrado en {path})")
        continue
    print(f"  RUN   {suite['nombre']}...")
    r = run_suite(suite)
    resultados.append(r)
    estado = "PASS" if r["passed"] else "FAIL"
    print(f"  {estado}  {suite['nombre']} ({r['tiempo']}s)")
    if not r["passed"] and r["critico"]:
        print(f"        ERROR CRITICO:")
        print(f"        {r['output']}")

pasados = sum(1 for r in resultados if r["passed"])
fallados = sum(1 for r in resultados if not r["passed"])
criticos_fallados = sum(1 for r in resultados
                        if not r["passed"] and r["critico"])

print()
print("=" * 65)
print(f"  RESULTADO: {pasados}/{len(resultados)} suites pasadas")
print(f"  Criticos fallados: {criticos_fallados}")
print()
if criticos_fallados == 0:
    print("  SISTEMA LISTO PARA RELEASE V2.0.0")
else:
    print("  CORREGIR FALLOS CRITICOS ANTES DEL RELEASE")
print("=" * 65)

report = {
    "timestamp": time.time(),
    "version": "2.0.0",
    "total_suites": len(resultados),
    "passed": pasados,
    "failed": fallados,
    "criticos_fallados": criticos_fallados,
    "resultados": resultados
}

import json as j
Path(ROOT / "docs").mkdir(exist_ok=True)
with open(ROOT / "docs/master_test_report.json", "w") as f:
    j.dump(report, f, indent=2)

print(f"  Reporte guardado: docs/master_test_report.json")

sys.exit(0 if criticos_fallados == 0 else 1)
