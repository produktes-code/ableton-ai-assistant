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

## 🎯 1. The Vision (Introduction)

Advanced audio mixing is often an analytical bottleneck. The producer's brain enters ear fatigue trying to resolve millimeter phase conflicts, losing global creative perspective. We developed Ableton AI Assistant questioning the DAW paradigm: Why must we move knobs manually when a machine has the surgical precision to calculate frequency masking? This tool is a revolutionary cognitive engineer. Connecting in real time via the Model Context Protocol (MCP) and relentless TCP architecture, Claude's AI 'listens' to your console's state and natively executes hardcoded mastering decisions. It is the bridge between Ableton's low-level code and the natural semantics of AI.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

## 🚀 2. Technical Deployment (Installation) & CI/CD Installation

To guarantee cross-platform stability, we now employ **Automated CI/CD via GitHub Actions**. 
Instead of local packaging, our source code is natively compiled on pure Windows and macOS environments in the cloud.

#### How to Download and Install
1. Navigate to the **Releases** section of this repository.
2. Download the latest automated build for your Operating System:
   - `antigravity-app.Setup.1.0.0.exe` (Windows)
   - `antigravity-app-1.0.0.dmg` (macOS)

### 🍎 macOS Users (Gatekeeper)
Lacking a paid Apple developer certificate, Gatekeeper will quarantine the binary. As engineers, the legitimate local bypass is to **Right-click the app -> Open** (do not double click). This is not a bug; it is the standard flow for high-performance open-source software.

### 🪟 Windows Users (SmartScreen)
Windows Defender may show a blue 'Windows protected your PC' warning when running the `.exe` installer. Click **'More info'** and then **'Run anyway'**.

## 🔌 3. Signal Flow & Setup

A truly professional platform must offer total transparency over its data flows. The hybrid architecture of Ableton AI Assistant requires precise routing.

• **Remote Script (Python in Ableton):** You must drag the `AntigravityCore` folder into Ableton Live's native Remote Scripts path (e.g., `MIDI Remote Scripts/`). This injects our backend directly into Live's audio engine.
• **Low-Latency TCP Sockets:** The Python script silently opens port `9001`. The Electron desktop application (Frontend) connects to this port via bidirectional IPC. This design evades the latency limitations typical of standard MIDI protocols.
• **LLM Tokens Injection (API Keys):** The system encrypts and handles your Claude API key (Anthropic) locally. Heavy natural language processing inferences travel through the socket to the cloud, while the mathematical DSP execution is calculated on the local CPU.

## 💻 4. Operative Philosophy (User Guide)

Designing interfaces for producers demands respecting their visual ergonomics during long studio sessions. Ableton's Dark-Mode principle has been traced and optimized.

• **Main Canvas (The Dashboard):** A diagnostic panel that instantly exposes the "Project Health" through progress bars and critical saturation alerts.
• **Native Tactile Controls:** The central Knob and the Drive/Gain sliders are not visual mockups. They are reactive controls bound millisecond by millisecond to the TCP port. Sliding them in the app alters your mix in Ableton with zero delay.
• **Asynchronous Nature:** No freezes. The main thread renders the UI and chat at a constant 60fps while the IA's MCP server analyzes the JSON tree nodes of your tracks in the abyss of the background.

## ⚙️ 5. Parameter Masterclass (Features)

- **Adaptive Algorithmic Compression (Glue Compressor):** The assistant does not throw a blind preset. Upon instantiating the compressor, the AI dynamically sets a slow Attack time (to safeguard transient punch) and an ultra-fast Release calculated on the session's BPM.
- **Masking and Phase Clearing (EQ Eight):** A classic amateur production problem is bass clashing. Our logic injects a strict Side (S) cut below 120Hz. This technical directive anchors the physical energy of the Kick and Sub-bass purely in Mono (Mid), eradicating phase cancellations when played in clubs or stereo PA systems.
- **LLM Framework (MCP Protocol):** Here lies the heart of the genius. Ableton Assistant stands as an MCP server that empowers the Claude model. The AI does not guess; it literally 'reads' the JSON payload of the tracks' state, mathematically reasons the arrangement, and returns the execution order. It is neuro-linguistic programming applied to frequencies.

## 🌍 6. Global Multimodal Integration

Treating internationalization through simple flat translation JSONs is an insult to the global professional. We encoded a Structural Multimodal paradigm. This implies 100% Unicode support and Hot-Reloading of complete lexical layers in 7 languages (ES, EN, DE, UK, RU, ZH, JA). Because engineering precision and respect for the producer do not understand language barriers.

## 🛡️ 7. Shielding Architecture (Security)

In a professional studio environment, a crash can mean the loss of an unrepeatable vocal take. We designed a defensive armor (Shielding) emulating DevSecOps best practices:

• **Anti-Flood Engineering (Rate limiting):** Algorithms strangle any anomalous TCP request spikes using limitation middlewares, evading Thread Pool collapses when dragging MIDI cursors massively.
• **JSON Payload Validation:** The Remote Script inspects each incoming frame and discards malformed structures, preventing malicious OS code injections.
• **Binary Crystallography & RAM (2 GB Limit):** The system restricts the ingestion of abnormally long responses from the LLM model to prevent Out Of Memory (OOM) attacks that would freeze your Ableton session.

## 📝 8. Debug Log (FAQ)

Q: **macOS Gatekeeper reports the application is 'damaged' or cannot be opened.**
A: This is a strict temporary Apple security flag. As an engineer, you know you must approve the binary using 'Right-click -> Open'. We confirm the absolute integrity of the local compilation.

Q: **TCP Deadlock / No response from Ableton Live.**
A: Two probable engineering causes: A) Local port `9001` is blocked by a restrictive OS firewall. B) You have not assigned the `AntigravityCore` script in the Link/MIDI tab of Ableton Live's Preferences.

Q: **Latency discrepancies in Chat (API / LLM).**
A: Sliders manipulation (Gain/Drive) occurs through the local socket (0ms). Only complex chat inferences (model reasoning) travel to Anthropic's servers. Check your WAN routing if the chat takes more than 3 seconds to respond.

## ⚖️ 9. Engineering Manifesto, Credits & License

This software is the manifest result of profound engineering conceived and articulated from the produktes-code labs in inseparable union with Engineer Jesús Ferrer García (CHUS BZN).

We refuse to offer simplified black boxes. We deliver absolute parametric consoles. Licensed under intellectual property restrictions and the strictest open source margins (CC BY-NC-SA 4.0). CORPORATE STANDARD - STUDIO READY. CERTIFIED ENGINEERING GRADE.
