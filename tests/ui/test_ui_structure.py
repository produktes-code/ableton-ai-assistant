import pytest
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
ELECTRON = ROOT / "electron-app"

class TestHTMLStructure:

  def test_ids_requeridos_en_html(self):
    html = (ELECTRON / "index.html").read_text()
    ids_requeridos = [
      "tcp-dot", "tcp-label", "bpm-value", "key-value",
      "lufs-value", "clash-value", "spectrogram-canvas",
      "chroma-canvas", "clash-meter-fill", "chat-history",
      "chat-input", "send-btn", "btn-play", "btn-stop",
      "btn-record", "tracks-view", "terminal-output",
      "queue-count", "refresh-session", "freeze-btn"
    ]
    for id in ids_requeridos:
      assert f'id="{id}"' in html, f"Falta id: {id}"

  def test_csp_correcta(self):
    html = (ELECTRON / "index.html").read_text()
    assert "ws://127.0.0.1:9002" in html
    assert "Content-Security-Policy" in html

  def test_scripts_referenciados_existen(self):
    html = (ELECTRON / "index.html").read_text()
    scripts = ["js/tcp-client.js", "js/dsp-visualizer.js",
               "js/app.js", "js/session-sync.js"]
    for script in scripts:
      assert script in html, f"Script no referenciado: {script}"
      assert (ELECTRON / script).exists(), f"Archivo no existe: {script}"

  def test_suggestion_chips_presentes(self):
    html = (ELECTRON / "index.html").read_text()
    assert "suggestion-chip" in html
    assert "sendSuggestion" in html

class TestCSSStructure:

  def test_variables_css_requeridas(self):
    css = (ELECTRON / "styles/glassmorphism.css").read_text()
    vars_requeridas = [
      "--accent-primary", "--glass-bg", "--glass-blur",
      "--text-primary", "--font-mono", "--accent-green",
      "--accent-red", "--radius-lg"
    ]
    for var in vars_requeridas:
      assert var in css, f"Falta variable CSS: {var}"

  def test_animaciones_presentes(self):
    css = (ELECTRON / "styles/glassmorphism.css").read_text()
    animaciones = ["pulse-green", "fadeInUp", "record-pulse"]
    for anim in animaciones:
      assert anim in css, f"Falta animacion: {anim}"

  def test_clases_glass_presentes(self):
    css = (ELECTRON / "styles/glassmorphism.css").read_text()
    clases = [".glass-panel", ".glass-inset", ".dot.connected",
              ".btn-transport", ".suggestion-chip", ".log-line"]
    for clase in clases:
      assert clase in css, f"Falta clase CSS: {clase}"

class TestJSStructure:

  def test_tcp_client_completo(self):
    js = (ELECTRON / "js/tcp-client.js").read_text()
    assert "class TCPClient" in js
    assert "connect()" in js or "connect (" in js
    assert "send(" in js
    assert "_handleData" in js
    assert "window.tcpClient" in js

  def test_dsp_visualizer_completo(self):
    js = (ELECTRON / "js/dsp-visualizer.js").read_text()
    assert "class DSPVisualizer" in js
    assert "_drawBands" in js
    assert "_drawChroma" in js
    assert "_interpolate" in js
    assert "requestAnimationFrame" in js

  def test_app_funciones_globales(self):
    js = (ELECTRON / "js/app.js").read_text()
    funciones = ["addLog", "clearLog", "transport",
                 "sendChat", "syncSession", "addMessageToChat",
                 "tryDirectCommand", "init"]
    for fn in funciones:
      assert fn in js, f"Falta funcion: {fn}"

  def test_session_sync_existe(self):
    js = (ELECTRON / "js/session-sync.js").read_text()
    assert "renderTracks" in js
    assert "updateQueueCount" in js
