![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge)

![Ableton AI Assistant Logo](build/icon.png)

# Ableton AI Assistant V1.0.0

##### Когнітивний ШІ-інженер зі зведення та аудіопомічник реального часу / Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant

🌐 **Читати на:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | **🇺🇦 Українська** | [🇨🇳 中文](README_zh.md)

---

## 📖 Завантажити посібник користувача (PDF)
Для отримання розширених інструкцій завантажте офіційний посібник:
📥 **[Завантажити USER_MANUAL.pdf (V1.0.0)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## 🎯 1. Бачення (Вступ)

Просунуте зведення аудіо часто є аналітичним вузьким місцем. Ми розробили Ableton AI Assistant, щоб вирішити цю проблему. Навіщо крутить ручки вручну, якщо машина має хірургічну точність для розрахунку частотного маскування? Цей інструмент — когнітивний інженер. Підключаючись в реальному часі через протокол MCP і TCP, ШІ Claude «чує» стан вашої консолі та виконує рішення з мастерингу.

> [!NOTE]
> Розроблено **produktes-code** та **Jesús Ferrer (CHUS BZN)** для встановлення професійних стандартів.

## 🚀 2. Технічне розгортання (Встановлення)

Для забезпечення стабільності ми використовуємо **Automated CI/CD через GitHub Actions**.
Вихідний код компілюється в хмарі для Windows, macOS та Linux.

#### Як завантажити та встановити
1. Перейдіть до розділу **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.
2. Завантажте останню версію:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

### 🍎 Користувачі macOS (Gatekeeper)
**Правий клік по додатку -> Відкрити**.

### 🪟 Користувачі Windows (SmartScreen)
Натисніть **«Докладніше»**, потім **«Виконати в будь-якому випадку»**.

## 🔌 3. Маршрутизація сигналів

• **Remote Script (Python):** Перемістіть `AntigravityCore` у папку Remote Scripts в Ableton.
• **Low-Latency TCP:** Скрипт Python відкриває порт `9001`. Додаток Electron підключається до цього порту.
• **LLM Tokens:** Ваш ключ API Claude шифрується локально.

## 💻 4. Операційна філософія

Ергономіка для професіоналів. Принцип Dark-Mode.
• **Dashboard:** Панель діагностики стану проєкту.
• **Нативні контролери:** Слайдери прив'язані до TCP-порту.
• **Асинхронність:** 60fps UI без зависань.

## ⚙️ 5. Майстер-клас параметрів

- **Адаптивний компресор (Glue Compressor):** ШІ динамічно встановлює повільну атаку та надшвидкий реліз на основі BPM.
- **Видалення фазових конфліктів (EQ Eight):** Ми робимо зріз Side (S) нижче 120 Гц, залишаючи саб-бас у моно.
- **LLM Framework (MCP):** ШІ математично аналізує JSON-дані ваших треків.

## 🌍 6. Мультимодальна інтеграція

100% підтримка Unicode та Hot-Reloading на 7 мовах.

## 🛡️ 7. Архітектура безпеки (Shielding)

• **Anti-Flood (Rate limiting):** Алгоритми обмежують аномальні стрибки TCP-запитів.
• **JSON Payload Validation:** Видалення шкідливих структур.
• **RAM-Sanity (2 GB Limit):** Запобігання OOM-атакам.

## 📝 8. Журнал налагодження (FAQ)

П: **macOS Gatekeeper блокує додаток.**
В: Правий клік -> Відкрити.

П: **TCP Deadlock / Немає відповіді.**
В: Порт `9001` заблоковано, або скрипт не призначено.

## ⚖️ 9. Інженерний маніфест та Ліцензія

Створено produktes-code та Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.
