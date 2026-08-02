![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton AI Assistant Logo" />
</p>

<h1 align="center">Ableton AI Assistant V1.0.0</h1>

<p align="center">
  <b>Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant</b><br/>
  <i>Kognitiver KI-Mischingenieur & MCP-Echtzeit-Audioassistent</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="License" />
</p>

🌐 **Lesen Sie auf:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | **🇩🇪 Deutsch** | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 Die Vision (Einführung)

Fortgeschrittenes Audio-Mixing ist oft ein analytischer Engpass. Das Gehirn des Produzenten leidet unter Ermüdung, wenn es versucht, millimetergenaue Phasenkonflikte zu lösen, und verliert dabei die kreative Perspektive. Wir haben den Ableton AI Assistant entwickelt und das DAW-Paradigma in Frage gestellt: Warum müssen wir Knöpfe manuell bewegen, wenn eine Maschine die chirurgische Präzision hat, um Frequenzmaskierung zu berechnen? 

Dieses Werkzeug ist der ultimative **Digitale Audio-Zwilling**. Es ist kein einfaches MIDI-Skript; es ist ein kognitiver Ingenieur. In Echtzeit über das Model Context Protocol (MCP) und eine unerbittliche TCP-Architektur verbunden, 'hört' die Claude-KI den Status Ihrer Konsole und führt nativ festcodierte Mastering-Entscheidungen aus. Es ist die Brücke zwischen Abletons Low-Level-Code und der natürlichen Semantik der KI.

> [!NOTE]
> Entwickelt von **produktes-code** und **Jesús Ferrer (CHUS BZN)**, um professionelle Standards in der kommerziellen Tontechnik zu setzen.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)

---

## ⚙️ Parameter Masterclass (Features)

- **Adaptive algorithmische Kompression (Glue Compressor)**: Die KI legt dynamisch eine langsame Attack-Zeit und ein ultraschnelles Release basierend auf dem BPM fest.
- **Phasen- und Maskierungskorrektur (EQ Eight)**: Wir injizieren einen strikten Side (S)-Schnitt unter 120Hz. Dies verankert den Subbass in Mono und verhindert Phasenauslöschungen.
- **LLM Framework (MCP Protocol)**: Die KI rät nicht; sie 'liest' den JSON-Payload des Spurenzustands, analysiert mathematisch und gibt den Ausführungsbefehl zurück.
- **Asynchrone Architektur**: Keine Verzögerungen. Der Haupt-Thread rendert die UI konstant mit 60fps, während der KI-Server die Spuren im Hintergrund analysiert.

---

## 🛡️ Abschirmarchitektur (Sicherheit)

Wir haben eine Schutzrüstung (Shielding) nach DevSecOps Best Practices entworfen:

• **Anti-Flood Engineering (Rate limiting)**: Drosselung anomaler TCP-Anfragespitzen, um Zusammenbrüche des Thread-Pools zu vermeiden.
• **JSON Payload Validierung**: Überprüfung jedes eingehenden Frames, um böswilligen OS-Code zu blockieren.
• **RAM-Sanity (2 GB Limit)**: Beschränkung extrem langer Modellantworten zur Vermeidung von OOM-Angriffen.

---

## 🚀 Technische Bereitstellung & CI/CD Installation

Um eine plattformübergreifende Stabilität zu gewährleisten, verwenden wir jetzt **Automatisierte CI/CD über GitHub Actions**. 
Anstelle einer lokalen Paketierung wird unser Quellcode nativ auf Windows-, macOS- und Linux-Umgebungen in der Cloud kompiliert.

### 🛠️ Installationsprogramme herunterladen
Navigieren Sie zum Abschnitt **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** dieses Repositories, um die Binärdateien für Ihr Betriebssystem herunterzuladen:
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg`
- **Linux**: `Ableton.AI.Assistant-1.0.0.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

### 🍎 macOS-Benutzer (Gatekeeper)
Da kein kostenpflichtiges Apple-Entwicklerzertifikat vorliegt, wird Gatekeeper die Binärdatei isolieren. Als Ingenieure wissen wir, dass der legitime Weg zur Umgehung darin besteht, mit der **rechten Maustaste auf die App zu klicken -> Öffnen**.

### 🪟 Windows-Benutzer (SmartScreen)
Windows Defender zeigt beim Ausführen des `.exe`-Installationsprogramms möglicherweise eine blaue Warnung an. Klicken Sie auf **'Weitere Informationen'** und dann auf **'Trotzdem ausführen'**.

### 🐧 Linux-Benutzer (AppImage & Debian)
- **AppImage**: Erteilen Sie vor dem Start Ausführungsrechte:
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage` und ausführen.
- **Debian-Paket (`.deb`)**: Installation über das Terminal:
  `sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb` oder doppelklicken, um über Ihren Software-Manager zu installieren.

---

## 🔌 Signalfluss & Setup

Eine professionelle Plattform muss absolute Transparenz über ihre Datenflüsse bieten. Die hybride Architektur erfordert präzises Routing.

• **Remote Script (Python in Ableton)**: Sie müssen den Ordner `AntigravityCore` in den Pfad für Remote-Skripte von Ableton Live ziehen. Dies injiziert unser Backend direkt in die Audio-Engine.
• **Low-Latency TCP Sockets**: Das Python-Skript öffnet lautlos den Port `9001`. Die Electron-Desktop-Anwendung verbindet sich bidirektional über IPC mit diesem Port.
• **LLM Tokens (API Keys)**: Das System verschlüsselt und verarbeitet Ihren Claude API-Schlüssel lokal. Nur komplexe Schlussfolgerungen reisen in die Cloud, während das DSP lokal berechnet wird.

---

## 📚 Dokumentation und Manuals

Für fortgeschrittene Anweisungen und die Parameter-Masterclass laden Sie das offizielle Handbuch herunter:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## ⚖️ Engineering Manifesto, Credits & Lizenz

Konzipiert von produktes-code in unzertrennlicher Einheit mit Jesus Ferrer Garcia (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-27**.
