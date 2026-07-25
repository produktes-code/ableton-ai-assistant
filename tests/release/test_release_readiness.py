import pytest
import os
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent

def test_workflow_github_actions():
    wf = ROOT / ".github" / "workflows" / "build_v2.yml"
    assert wf.exists(), "No existe workflow build_v2.yml"
    assert "pytest" in wf.read_text(), "Workflow no incluye pytest"

def test_package_json_version():
    pkg = ROOT / "electron-app" / "package.json"
    assert pkg.exists(), "No existe package.json"
    data = json.loads(pkg.read_text())
    assert data.get("version") == "2.0.0", "Version en package.json no es 2.0.0"

def test_manual_pdf_md_existe():
    man = ROOT / "docs" / "USER_MANUAL_V2.0.0.md"
    assert man.exists(), "No existe el manual de usuario"

def test_readme_actualizado():
    readme = ROOT / "README.md"
    assert readme.exists(), "No existe README.md"
    content = readme.read_text().upper()
    assert "V2.0.0" in content, "README no menciona V2.0.0"

def test_master_report_verde():
    report_file = ROOT / "docs" / "master_test_report.json"
    assert report_file.exists(), "No existe master_test_report.json"
    report = json.loads(report_file.read_text())
    assert report["criticos_fallados"] == 0, "Hay pruebas criticas fallidas en el master report"
    assert report["passed"] >= 8, "No se pasaron suficientes suites maestras"

def test_estructura_completa_repo():
    required = [
        "electron-app/index.html",
        "electron-app/js/app.js",
        "remote-script/AntigravityCore/AntigravityCore.py",
        "remote-script/AntigravityCore/dsp_engine.py",
        "tests/run_all_tests.py"
    ]
    for req in required:
        assert (ROOT / req).exists(), f"Falta el archivo critico: {req}"
