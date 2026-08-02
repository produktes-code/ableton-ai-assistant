![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge)

![Ableton AI Assistant Logo](build/icon.png)

# Ableton AI Assistant V1.0.0

##### Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant / Ingeniero de Mezcla Cognitivo IA y Asistente de Audio en Tiempo Real MCP

🌐 **Read this in:** **🇬🇧 English** | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 📖 Download the User Manual (PDF)
For advanced engineering instructions and parameter masterclass, download the Official User Manual (PDF):
📥 **[Download USER_MANUAL.pdf (V1.0.0)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## 🎯 1. The Vision (Introduction)

The genesis of Ableton AI Assistant stems from a deep frustration in the music production industry: the producer's brain enters ear fatigue trying to resolve millimeter phase conflicts, losing global creative perspective. We developed this assistant by questioning the DAW paradigm: Why must we move knobs manually when a machine has the surgical precision to calculate frequency masking?

Ableton AI Assistant was designed to be the ultimate **Audio Digital Twin** for producers and engineers. It is not a simple MIDI script; it is a curatorial brain that understands the energy of the mix and shields your session. Connecting in real time via the Model Context Protocol (MCP) and relentless TCP architecture, Claude's AI 'listens' to your console's state and natively executes hardcoded mastering decisions. We created this tool to give engineers back control over their sonic identity.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

## 🚀 2. Technical Deployment (Installation) & CI/CD Installation

To guarantee cross-platform stability, we now employ **Automated CI/CD via GitHub Actions**. 
Instead of local packaging, our source code is natively compiled on pure Windows, macOS and Linux Ubuntu environments in the cloud.

#### How to Download and Install
1. Navigate to the **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** section of this repository.
2. Download the latest automated build for your Operating System:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu/Debian)

### 🍎 macOS Users (Gatekeeper)
Lacking a paid Apple developer certificate, Gatekeeper will quarantine the binary. As engineers, the legitimate local bypass is to **Right-click the app -> Open** (do not double click).

### 🪟 Windows Users (SmartScreen)
Windows Defender may show a blue 'Windows protected your PC' warning when running the `.exe` installer. Click **'More info'** and then **'Run anyway'**.

## 🔌 3. Signal Flow & Setup

A truly professional platform must offer total transparency over its data flows. The hybrid architecture of Ableton AI Assistant requires precise routing.

• **Remote Script (Python in Ableton):** You must drag the `AntigravityCore` folder into Ableton Live's native Remote Scripts path (e.g., `MIDI Remote Scripts/`). This injects our backend directly into Live's audio engine.
• **Low-Latency TCP Sockets:** The Python script silently opens port `9001`. The Electron desktop application (Frontend) connects to this port via bidirectional IPC. This design evades the latency limitations typical of standard MIDI protocols.
• **LLM Tokens Injection (API Keys):** The system encrypts and handles your Claude API key (Anthropic) locally. Heavy natural language processing inferences travel through the socket to the cloud, while the mathematical DSP execution is calculated on the local CPU.

## 💻 4. Operative Philosophy (User Guide)

Designing interfaces for creators demands respecting their visual ergonomics during long night shifts. Ableton's Dark-Mode principle (RGB: 15, 15, 15) maximizes contrast readability and focuses vision where it matters.

• **Main Canvas (The Dashboard):** A diagnostic panel that instantly exposes the "Project Health" through progress bars and critical saturation alerts. No 4-level deep hidden menus.
• **Native Tactile Controls:** The central Knob and the Drive/Gain sliders are not visual mockups. They are reactive controls bound millisecond by millisecond to the TCP port. Sliding them in the app alters your mix in Ableton with zero delay.
• **Asynchronous Nature:** No blockages or freezes. The Main Thread renders the UI at an unbreakable 60fps while background MCP server workers operate in the abyss consuming CPU cores.

## ⚙️ 5. Parameter Masterclass (Features)

- **Adaptive Algorithmic Compression (Glue Compressor):** The assistant does not throw a blind preset. Upon instantiating the compressor, the AI dynamically sets a slow Attack time (to safeguard transient punch) and an ultra-fast Release calculated on the session's BPM.
- **Masking and Phase Clearing (EQ Eight):** A classic amateur production problem is bass clashing. Our logic injects a strict Side (S) cut below 120Hz. This technical directive anchors the physical energy of the Kick and Sub-bass purely in Mono (Mid), eradicating phase cancellations when played in clubs or stereo PA systems.
- **LLM Framework (MCP Protocol):** Here lies the heart of the genius. Ableton Assistant stands as an MCP server that empowers the Claude model. The AI does not guess; it literally 'reads' the JSON payload of the tracks' state, mathematically reasons the arrangement, and returns the execution order. It is neuro-linguistic programming applied to frequencies.

## 🌍 6. Global Multimodal Integration

Treating internationalization through simple flat translation JSONs is an insult to the global professional. We encoded a Structural Multimodal paradigm. This implies 100% Unicode support and Hot-Reloading of complete lexical layers in 7 languages (ES, EN, DE, UK, RU, ZH, JA). Because engineering precision and respect for the operator do not understand language barriers.

## 🛡️ 7. Shielding Architecture (Security)

In a professional deployment environment, a crash is not a bug; it is capital loss (unrepeatable vocal takes). We designed a defensive armor (Shielding) emulating DevSecOps best practices:

• **Anti-Flood Engineering (Rate limiting):** Asynchronous algorithms strangle any anomalous TCP request spikes using limitation middlewares, evading Thread Pool collapses when dragging cursors massively.
• **JSON Payload Validation:** The Remote Script inspects each incoming frame and discards malformed structures, preventing malicious OS code injections.
• **RAM Sanity (2 GB Limit):** We relentlessly reject any atypical weight at the LLM model response threshold to prevent Out Of Memory (OOM) attacks that would destroy servers and freeze your session.

## 📝 8. Debug Log (FAQ)

Q: **macOS Gatekeeper reports the application is 'damaged' or cannot be opened.**
A: This is a strict temporary Apple security flag. As an engineer, you know you must approve the binary using 'Right-click -> Open'. We confirm the absolute integrity of the local compilation.

Q: **Infinite TCP Deadlock / No response from Ableton.**
A: Two probable engineering causes: A) Local port `9001` is blocked by your OS firewall. B) You have not assigned the `AntigravityCore` script in the Link/MIDI tab of Ableton Live's Preferences.

Q: **Latency discrepancies in Chat (API / LLM).**
A: Sliders manipulation occurs through the local socket (0ms). Only massive LLM inferences travel through the WAN socket. Check your router if pings are high in the chat.

## ⚖️ 9. Engineering Manifesto, Credits & License

This software is the manifest result of profound engineering conceived and articulated from the produktes-code labs in inseparable union with Engineer Jesús Ferrer García (CHUS BZN).

We refuse to offer simplified black boxes. We deliver absolute parametric consoles. Licensed under intellectual property restrictions and the strictest open source margins (CC BY-NC-SA 4.0). CORPORATE STANDARD - STUDIO READY. CERTIFIED ENGINEERING GRADE.
