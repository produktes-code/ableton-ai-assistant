![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge)

![Ableton AI Assistant Logo](build/icon.png)

# Ableton AI Assistant V1.0.0

##### Kognitiver KI-Mischingenieur & MCP-Echtzeit-Audioassistent / Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant

🌐 **Lesen Sie auf:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | **🇩🇪 Deutsch** | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 📖 Laden Sie das Benutzerhandbuch herunter (PDF)
Für fortgeschrittene Anweisungen und die Parameter-Masterclass laden Sie das offizielle Handbuch herunter:
📥 **[USER_MANUAL.pdf (V1.0.0) herunterladen](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## 🎯 1. Die Vision (Einführung)

Fortgeschrittenes Audio-Mixing ist oft ein analytischer Engpass. Das Gehirn des Produzenten leidet unter Ermüdung, wenn es versucht, millimetergenaue Phasenkonflikte zu lösen, und verliert dabei die kreative Perspektive. Wir haben den Ableton AI Assistant entwickelt und das DAW-Paradigma in Frage gestellt: Warum müssen wir Knöpfe manuell bewegen, wenn eine Maschine die chirurgische Präzision hat, um Frequenzmaskierung zu berechnen? 

Dieses Werkzeug ist der ultimative **Digitale Audio-Zwilling**. Es ist kein einfaches MIDI-Skript; es ist ein kognitiver Ingenieur. In Echtzeit über das Model Context Protocol (MCP) und eine unerbittliche TCP-Architektur verbunden, 'hört' die Claude-KI den Status Ihrer Konsole und führt nativ festcodierte Mastering-Entscheidungen aus. Es ist die Brücke zwischen Abletons Low-Level-Code und der natürlichen Semantik der KI.

> [!NOTE]
> Entwickelt von **produktes-code** und **Jesús Ferrer (CHUS BZN)**, um professionelle Standards in der kommerziellen Tontechnik zu setzen.

## 🚀 2. Technische Bereitstellung & CI/CD Installation

Um eine plattformübergreifende Stabilität zu gewährleisten, verwenden wir jetzt **Automatisierte CI/CD über GitHub Actions**. 
Anstelle einer lokalen Paketierung wird unser Quellcode nativ auf Windows-, macOS- und Linux-Umgebungen in der Cloud kompiliert.

#### Herunterladen und Installieren
1. Navigieren Sie zum Abschnitt **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** dieses Repositories.
2. Laden Sie den neuesten automatisierten Build für Ihr Betriebssystem herunter:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

### 🍎 macOS-Benutzer (Gatekeeper)
Da kein kostenpflichtiges Apple-Entwicklerzertifikat vorliegt, wird Gatekeeper die Binärdatei isolieren. Als Ingenieure wissen wir, dass der legitime Weg zur Umgehung darin besteht, mit der **rechten Maustaste auf die App zu klicken -> Öffnen**.

### 🪟 Windows-Benutzer (SmartScreen)
Windows Defender zeigt beim Ausführen des `.exe`-Installationsprogramms möglicherweise eine blaue Warnung an. Klicken Sie auf **'Weitere Informationen'** und dann auf **'Trotzdem ausführen'**.

## 🔌 3. Signalfluss & Setup

Eine professionelle Plattform muss absolute Transparenz über ihre Datenflüsse bieten. Die hybride Architektur des Ableton AI Assistant erfordert präzises Routing.

• **Remote Script (Python in Ableton):** Sie müssen den Ordner `AntigravityCore` in den Pfad für Remote-Skripte von Ableton Live ziehen. Dies injiziert unser Backend direkt in die Audio-Engine.
• **Low-Latency TCP Sockets:** Das Python-Skript öffnet lautlos den Port `9001`. Die Electron-Desktop-Anwendung verbindet sich bidirektional über IPC mit diesem Port.
• **LLM Tokens (API Keys):** Das System verschlüsselt und verarbeitet Ihren Claude API-Schlüssel lokal. Nur komplexe Schlussfolgerungen reisen in die Cloud, während das DSP lokal berechnet wird.

## 💻 4. Operative Philosophie

Die Gestaltung von Schnittstellen erfordert den Respekt vor der visuellen Ergonomie. Abletons Dark-Mode-Prinzip wurde nachgezeichnet.

• **Hauptleinwand (Dashboard):** Ein Diagnosefeld, das den "Projektzustand" sofort aufdeckt.
• **Native Taktyle Steuerung:** Der zentrale Knob und die Schieberegler sind keine Mockups. Sie sind reaktive Regler, die millisekundengenau an den TCP-Port gebunden sind.
• **Asynchron:** Keine Verzögerungen. Der Haupt-Thread rendert die UI konstant mit 60fps, während der KI-Server die Spuren im Hintergrund analysiert.

## ⚙️ 5. Parameter Masterclass

- **Adaptive algorithmische Kompression (Glue Compressor):** Die KI legt dynamisch eine langsame Attack-Zeit und ein ultraschnelles Release basierend auf dem BPM fest.
- **Phasen- und Maskierungskorrektur (EQ Eight):** Wir injizieren einen strikten Side (S)-Schnitt unter 120Hz. Dies verankert den Subbass in Mono und verhindert Phasenauslöschungen.
- **LLM Framework (MCP):** Die KI rät nicht; sie 'liest' den JSON-Payload des Spurenzustands, analysiert mathematisch und gibt den Ausführungsbefehl zurück.

## 🌍 6. Globale Multimodale Integration

Wir haben ein strukturelles multimodales Paradigma codiert. Dies bedeutet 100% Unicode-Unterstützung und Hot-Reloading in 7 Sprachen (ES, EN, DE, UK, RU, ZH, JA).

## 🛡️ 7. Abschirmarchitektur (Sicherheit)

Wir haben eine Schutzrüstung (Shielding) nach DevSecOps Best Practices entworfen:

• **Anti-Flood (Rate limiting):** Drosselung anomaler TCP-Anfragespitzen, um Zusammenbrüche des Thread-Pools zu vermeiden.
• **JSON Payload Validierung:** Überprüfung jedes eingehenden Frames, um böswilligen OS-Code zu blockieren.
• **RAM-Sanity (2 GB Limit):** Beschränkung extrem langer Modellantworten zur Vermeidung von OOM-Angriffen.

## 📝 8. Debug-Protokoll (FAQ)

Q: **macOS Gatekeeper blockiert die App.**
A: Rechtsklick -> Öffnen. Wir bestätigen die Integrität.

Q: **TCP Deadlock / Keine Antwort von Ableton Live.**
A: A) Lokaler Port `9001` blockiert. B) Das `AntigravityCore`-Skript wurde in Ableton nicht zugewiesen.

## ⚖️ 9. Engineering Manifesto, Credits & Lizenz

Konzipiert von produktes-code in unzertrennlicher Einheit mit Jesus Ferrer Garcia (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.
