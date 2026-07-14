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

Advanced audio mixing is often an analytical bottleneck. The producer's brain enters ear fatigue trying to resolve millimeter phase conflicts, losing global creative perspective. We developed Ableton AI Assistant questioning the DAW paradigm: Why must we move knobs manually when a machine has the surgical precision to calculate frequency masking? This tool is a revolutionary cognitive engineer. Connecting in real time via the Model Context Protocol (MCP) and relentless TCP architecture, Claude's AI 'listens' to your console's state and natively executes hardcoded mastering decisions. It is the bridge between Ableton's low-level code and the natural semantics of AI.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.
> **DISCLAIMER: This is an unofficial community tool. It is not affiliated with, endorsed by, or in any way officially connected to Ableton AG.**

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)


---

## ⚙️ Parameter Masterclass (Features)

- **Adaptive Algorithmic Compression (Glue Compressor)**: The assistant doesn't throw a blind preset. It dynamically sets a slow Attack (to safeguard transient punch) and an ultra-fast Release calculated on the session's BPM. The engineering goal? To make the compressor 'breathe' with the track's rhythm, achieving commercial density without strangling dynamic range.
- **Masking and Phase Clearing (EQ Eight)**: A classic amateur production issue is bass clashing. Our logic injects a strict Side (S) cut below 120Hz. This technical directive anchors the physical energy of the Kick and Sub-bass purely in Mono (Mid), eradicating phase cancellations in clubs.
- **LLM Framework (MCP Protocol)**: Here lies the heart of the genius. Ableton Assistant stands as an MCP server empowering the Claude model. The AI doesn't guess; it 'reads' the JSON payload of the tracks' states, mathematically reasons the fix, and returns the execution order.
- **Low-Latency Network Telemetry (TCP Core)**: Moving a 'Gain' or 'Freq' knob from outside the DAW requires relentless access. We programmed the Python backend using raw TCP sockets that attack the Ableton Remote Script. This ensures voice/text modifications reflect natively in milliseconds.
- **True Peak and LUFS Control Manager**: The platform audits and deploys limiters on the master with a parametric hard ceiling and adjusted lookahead, mathematically ensuring delivery to streaming platforms at standard LUFS levels.

---

## 🛡️ Shielding Architecture (Security)

In Retail and Enterprise deployment, a system crash is not a bug; it is capital loss. We designed a defensive armor (Shielding) emulating DevSecOps best practices:

• **Anti-Flood Engineering (Rate limiting)**: Asynchronous algorithms strangle anomalous request spikes using limitation middlewares.
• **Binary Crystallography (Magic Bytes)**: The system opens the file header and verifies the native hexadecimal sequence to certify container integrity.
• **RAM Sanity (2 GB Limit)**: We relentlessly reject any atypical weight at the upload threshold to prevent Out Of Memory attacks.

---

### 🚀 Technical Deployment & CI/CD Installation

We employ **Automated CI/CD via GitHub Actions** for the frontend desktop application. Download the latest automated build for your Operating System from the **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** section.

#### 🧠 Backend Installation (Crucial)
This tool is not just a UI; it connects directly to Ableton Live's Python interpreter and Claude Desktop.
1. **Ableton Remote Script**: You MUST copy the `remote-script/AbletonAIAssistant` folder to your Ableton Live MIDI Remote Scripts directory.
2. **MCP Server**: You MUST configure your Claude Desktop `claude_desktop_config.json` to point to the `mcp-server/main.py` script. 

> [!CAUTION]
> **CRITICAL REQUIREMENT:** Ableton Live **MUST** be open and running with the Remote Script active BEFORE starting the AI Assistant or Claude Desktop. If Ableton Live is closed, the TCP connection will fail, causing the assistant to malfunction or crash immediately.

### 🍎 macOS Users (Gatekeeper)
Lacking a paid Apple developer certificate, Gatekeeper will quarantine the binary. As engineers, the legitimate local bypass is to **Right-click the app -> Open** (do not double-click). It is the standard flow of high-performance open-source software.

### 🪟 Windows Users (SmartScreen)
Windows Defender may show a blue 'Windows protected your PC' warning when running the `.exe` installer. Click **'More info'** and then **'Run anyway'**.

---

## 📚 Documentation & Manuals

For an exhaustive technical masterclass, troubleshooting guides, and full API details, please download our official manual:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](docs/USER_MANUAL.pdf)**


---

## ⚖️ Engineering Manifesto, Credits & License

Software conceived and articulated from the produktes-code labs in inseparable union with Engineer Jesus Ferrer Garcia (CHUS BZN).

Licensed under proprietary restrictions and strictest open source margins (CC BY-NC-SA 4.0). CORPORATE STANDARD - RETAIL READY.


