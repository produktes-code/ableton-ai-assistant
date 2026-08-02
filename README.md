![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton AI Assistant Logo" />
</p>

<h1 align="center">Ableton AI Assistant V1.0.0</h1>

<p align="center">
  <b>Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant</b><br/>
  <i>Ingeniero de Mezcla Cognitivo IA y Asistente de Audio en Tiempo Real MCP</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="License" />
</p>

🌐 **Read this in:** **🇬🇧 English** | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 The Vision (Introduction)

The genesis of Ableton AI Assistant stems from a deep frustration in the music production industry: the producer's brain enters ear fatigue trying to resolve millimeter phase conflicts, losing global creative perspective. We developed this assistant by questioning the DAW paradigm: Why must we move knobs manually when a machine has the surgical precision to calculate frequency masking?

Ableton AI Assistant was designed to be the ultimate **Audio Digital Twin** for producers and engineers. It is not a simple MIDI script; it is a curatorial brain that understands the energy of the mix and shields your session. Connecting in real time via the Model Context Protocol (MCP) and relentless TCP architecture, Claude's AI 'listens' to your console's state and natively executes hardcoded mastering decisions. We created this tool to give engineers back control over their sonic identity.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)

---

## ⚙️ Parameter Masterclass (Features)

- **Adaptive Algorithmic Compression (Glue Compressor)**: The assistant does not throw a blind preset. Upon instantiating the compressor, the AI dynamically sets a slow Attack time (to safeguard transient punch) and an ultra-fast Release calculated on the session's BPM.
- **Masking and Phase Clearing (EQ Eight)**: A classic amateur production problem is bass clashing. Our logic injects a strict Side (S) cut below 120Hz. This technical directive anchors the physical energy of the Kick and Sub-bass purely in Mono (Mid), eradicating phase cancellations when played in clubs or stereo PA systems.
- **LLM Framework (MCP Protocol)**: Here lies the heart of the genius. Ableton Assistant stands as an MCP server that empowers the Claude model. The AI does not guess; it literally 'reads' the JSON payload of the tracks' state, mathematically reasons the arrangement, and returns the execution order. It is neuro-linguistic programming applied to frequencies.
- **Asynchronous Architecture**: No blockages or freezes. The Main Thread renders the UI at an unbreakable 60fps while background MCP server workers operate in the abyss consuming CPU cores.

---

## 🛡️ Shielding Architecture (Security)

In Retail and Enterprise deployment, a crash is not a bug; it is capital loss (unrepeatable vocal takes). We designed a defensive armor (Shielding) emulating DevSecOps best practices:

• **Anti-Flood Engineering (Rate limiting)**: Asynchronous algorithms strangle any anomalous TCP request spikes using limitation middlewares, evading Thread Pool collapses when dragging cursors massively.
• **JSON Payload Validation**: The Remote Script inspects each incoming frame and discards malformed structures, preventing malicious OS code injections.
• **RAM Sanity (2 GB Limit)**: We relentlessly reject any atypical weight at the LLM model response threshold to prevent Out Of Memory (OOM) attacks that would destroy servers and freeze your session.

---

## 🚀 Technical Deployment & CI/CD Installation

To guarantee cross-platform stability, we now employ **Automated CI/CD via GitHub Actions**. 
Instead of local packaging, our source code is natively compiled on pure Windows, macOS and Linux Ubuntu environments in the cloud.

### 🛠️ Download Installers
Navigate to the **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** section of this repository to download binaries for your OS:
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg`
- **Linux**: `Ableton.AI.Assistant-1.0.0.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

### 🍎 macOS Users (Gatekeeper)
Lacking a paid Apple developer certificate, Gatekeeper will quarantine the binary. As engineers, the legitimate local bypass is to **Right-click the app -> Open** (do not double click). It is the standard flow of high-performance open-source software.

### 🪟 Windows Users (SmartScreen)
Windows Defender may show a blue 'Windows protected your PC' warning when running the `.exe` installer. Click **'More info'** and then **'Run anyway'**.

### 🐧 Linux Users (AppImage & Debian)
- **AppImage**: Grant execution permissions before launching:
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage` and run.
- **Debian Package (`.deb`)**: Install via terminal:
  `sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb` or double-click to install via your distro software manager.

---

## 🔌 Signal Flow & Setup

A truly professional platform must offer total transparency over its data flows. The hybrid architecture requires precise routing.

• **Remote Script (Python in Ableton)**: You must drag the `AntigravityCore` folder into Ableton Live's native Remote Scripts path (e.g., `MIDI Remote Scripts/`). This injects our backend directly into Live's audio engine.
• **Low-Latency TCP Sockets**: The Python script silently opens port `9001`. The Electron desktop application connects to this port via bidirectional IPC.
• **LLM Tokens Injection (API Keys)**: The system encrypts and handles your Claude API key (Anthropic) locally. Heavy inferences travel through the socket to the cloud, while DSP execution is calculated locally.

---

## 📚 Documentation & Manuals

For an exhaustive technical masterclass, troubleshooting guides, and full API details, please download our official manual:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## ⚖️ Engineering Manifesto, Credits & License

Software conceived and articulated from the produktes-code labs in inseparable union with Engineer Jesús Ferrer García (CHUS BZN).

We refuse to offer simplified black boxes. We deliver absolute parametric consoles. Licensed under intellectual property restrictions and the strictest open source margins (CC BY-NC-SA 4.0). CORPORATE STANDARD - STUDIO READY. CERTIFIED ENGINEERING GRADE.

## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-27**.
