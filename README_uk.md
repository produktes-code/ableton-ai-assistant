![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton AI Assistant Logo" />
</p>

<h1 align="center">Ableton AI Assistant V1.0.0</h1>

<p align="center">
  <b>Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant</b><br/>
  <i>Когнітивний ШІ-інженер зі зведення та аудіопомічник реального часу</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="License" />
</p>

🌐 **Читати на:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | **🇺🇦 Українська** | [🇨🇳 中文](README_zh.md)

---

## 🎯 Бачення (Вступ)

Просунуте зведення аудіо часто є аналітичним вузьким місцем. Ми розробили Ableton AI Assistant, щоб вирішити цю проблему. Навіщо крутить ручки вручну, якщо машина має хірургічну точність для розрахунку частотного маскування? Цей інструмент — когнітивний інженер. Підключаючись в реальному часі через протокол MCP і TCP, ШІ Claude «чує» стан вашої консолі та виконує рішення з мастерингу.

> [!NOTE]
> Розроблено **produktes-code** та **Jesús Ferrer (CHUS BZN)** для встановлення професійних стандартів.

---

## 📸 Інтерфейс (Ergonomics)

![Desktop Interface](docs/screenshot-UI.png)

---

## ⚙️ Майстер-клас параметрів (Функції)

- **Адаптивний компресор (Glue Compressor)**: ШІ динамічно встановлює повільну атаку та надшвидкий реліз на основі BPM.
- **Видалення фазових конфліктів (EQ Eight)**: Ми робимо зріз Side (S) нижче 120 Гц, залишаючи саб-бас у моно.
- **LLM Framework (MCP)**: ШІ математично аналізує JSON-дані ваших треків.
- **Асинхронність**: 60fps UI без зависань.

---

## 🛡️ Архітектура безпеки (Shielding)

• **Anti-Flood (Rate limiting)**: Алгоритми обмежують аномальні стрибки TCP-запитів.
• **JSON Payload Validation**: Видалення шкідливих структур.
• **RAM-Sanity (2 GB Limit)**: Запобігання OOM-атакам.

---

## 🚀 Технічне розгортання та встановлення CI/CD

Для забезпечення стабільності ми використовуємо **Automated CI/CD через GitHub Actions**.
Вихідний код компілюється в хмарі для Windows, macOS та Linux.

### 🛠️ Завантажити інсталятори
Перейдіть до розділу **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**:
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg`
- **Linux**: `Ableton.AI.Assistant-1.0.0.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

### 🍎 Користувачі macOS (Gatekeeper)
**Правий клік по додатку -> Відкрити**.

### 🪟 Користувачі Windows (SmartScreen)
Натисніть **«Докладніше»**, потім **«Виконати в будь-якому випадку»**.

### 🐧 Користувачі Linux (AppImage & Debian)
- **AppImage**: Надайте права на виконання:
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage`
- **Debian Package (`.deb`)**: Встановлення через термінал:
  `sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb`

---

## 🔌 Маршрутизація сигналів

• **Remote Script (Python)**: Перемістіть `AntigravityCore` у папку Remote Scripts.
• **Low-Latency TCP**: Скрипт Python відкриває порт `9001`.
• **LLM Tokens**: Ваш ключ API Claude шифрується локально.

---

## 📚 Документація

Для отримання розширених інструкцій завантажте офіційний посібник:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## ⚖️ Інженерний маніфест

Створено produktes-code та Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-27**.
