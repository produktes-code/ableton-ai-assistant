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

🌐 **Lesen Sie dies auf:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | **🇩🇪 Deutsch** | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 Die Vision (Einführung)

Das Mischen ist ein analytischer Engpass. Das Gehirn ermüdet bei der Lösung von Phasenkonflikten. Wir haben dieses Tool entwickelt, indem wir das DAW-Paradigma in Frage gestellt haben: Warum Knöpfe manuell bewegen, wenn eine Maschine Maskierungen berechnen kann? Diese KI agiert als kognitiver Ingenieur, der Abletons Status über MCP liest und native Mastering-Entscheidungen ausführt.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)


---

## ⚙️ Parameter Masterclass

- **Adaptive Kompression**: Stellt dynamisch langsamen Attack (für Transienten) und schnellen Release (basierend auf BPM) ein, um den Kompressor mit dem Rhythmus atmen zu lassen.
- **Phasenauflösung (EQ Eight)**: Ein strenger Side (S) Cut unter 120 Hz verankert Kick und Sub-Bass im Mono, um Phasenauslöschungen in Clubs zu vermeiden.
- **MCP-Protokoll**: Die KI liest den JSON-Payload des Spurstatus, argumentiert mathematisch und führt Aktionen präzise aus.
- **TCP-Kern**: Rohe TCP-Sockets greifen auf das Ableton Remote Script zu, um Modifikationen ohne MIDI-Latenz widerzuspiegeln.
- **True Peak / LUFS Manager**: Setzt Limiter auf dem Master, um eine mathematisch perfekte Bereitstellung für Streaming-Plattformen zu gewährleisten.

---

## 🛡️ Abschirmarchitektur

Systemabstürze sind Kapitalverlust. Shielding:

• Anti-Flood: Middlewares blockieren Spitzen.
• Magic Bytes: Hexadezimale Überprüfung der Header-Integrität.
• RAM-Sanity (2 GB Limit): Schutz vor OOM-Attacken.

---

## 🚀 Technische Bereitstellung

Zeit für Abhängigkeiten ist in der Produktion verschwendet. 'Zero-Friction'-Architektur kompilliert DSP und Python direkt.

### 🍎 macOS-Benutzer (Gatekeeper)
Gatekeeper wird die Binärdatei unter Quarantäne stellen (fehlendes Bezahlzertifikat). Ingenieurslösung: **Rechtsklick -> Öffnen** (nicht doppelklicken).

### 🪟 Windows-Benutzer (SmartScreen)
Windows Defender zeigt möglicherweise einen blauen Warnbildschirm beim `.exe` an. Klicken Sie auf **'Weitere Informationen'** und dann auf **'Trotzdem ausführen'**.

---

## 📚 Dokumentation & Handbücher

Laden Sie unser offizielles Handbuch herunter:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](docs/USER_MANUAL.pdf)**


---

## ⚖️ Engineering Manifesto & Credits

Entwickelt von produktes-code und Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.


