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

🌐 **Читати українською:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | **🇺🇦 Українська** | [🇨🇳 中文](README_zh.md)

---

## 🎯 Бачення

Зведення - це аналітичне вузьке місце. Ми розробили цей інструмент, ставлячи під сумнів парадигму DAW: навіщо крутити ручки вручну, коли машина може розрахувати маскування? Цей штучний інтелект діє як когнітивний інженер, читаючи стан Ableton через MCP і виконуючи рішення з майстерингу.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)


---

## ⚙️ Майстер-клас параметрів

- **Адаптивна компресія**: Встановлює повільну атаку та швидкий реліз (на основі BPM), щоб компресор дихав у ритмі треку.
- **Фазова роздільна здатність (EQ Eight)**: Зріз Side (S) нижче 120 Гц фіксує бас у Mono, щоб уникнути фазових скасувань.
- **Протокол MCP**: ШІ читає стан доріжок через JSON і виконує математичні рішення.
- **Ядро TCP**: Сирі сокети TCP керують Ableton без затримки MIDI.
- **Менеджер True Peak / LUFS**: Встановлює лімітери для ідеальної доставки на стримінгові платформи.

---

## 🛡️ Архітектура екранування

Екранування:

• Anti-Flood: Блокування сплесків запитів.
• Magic Bytes: Гексадецимальна перевірка файлів.
• 2 GB Limit: Захист оперативної пам'яті.

---

## 🚀 Технічне розгортання та встановлення CI/CD

Ми використовуємо **Автоматизований CI/CD через GitHub Actions** для додатку. Завантажте останню збірку для вашої ОС із розділу **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.

#### 🧠 Встановлення Backend (Критично важливо)
Це не просто UI; він безпосередньо підключається до інтерпретатора Python Ableton Live і Claude Desktop.
1. **Ableton Remote Script**: ВИ ПОВИННІ скопіювати папку `remote-script/AbletonAIAssistant` у вашу директорію MIDI Remote Scripts.
2. **MCP Server**: ВИ ПОВИННІ налаштувати `claude_desktop_config.json` у Claude Desktop на скрипт `mcp-server/main.py`.

### 🍎 Користувачі macOS (Gatekeeper)
Через відсутність платного сертифіката розробника Apple, Gatekeeper помістить бінарний файл у карантин. Законний локальний обхід: **Правий клік по додатку -> Відкрити**.

### 🪟 Користувачі Windows (SmartScreen)
Windows Defender може показати синій екран. Натисніть **'Докладніше'**, а потім **'Виконати в будь-якому випадку'**.

## 📚 Документація та посібники

Завантажте наш офіційний посібник:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](docs/USER_MANUAL.pdf)**


---

## ⚖️ Інженерний маніфест

Розроблено produktes-code та Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.


