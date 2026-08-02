![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge)

![Ableton AI Assistant Logo](build/icon.png)

# Ableton AI Assistant V1.0.0

##### Когнитивный ИИ-инженер по сведению и аудиопомощник реального времени / Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant

🌐 **Читать на:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | **🇷🇺 Русский** | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 📖 Скачать руководство пользователя (PDF)
Для получения расширенных инструкций загрузите официальное руководство:
📥 **[Скачать USER_MANUAL.pdf (V1.0.0)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## 🎯 1. Видение (Введение)

Продвинутое сведение аудио часто является аналитическим узким местом. Мы разработали Ableton AI Assistant, чтобы решить эту проблему. Зачем крутить ручки вручную, если машина обладает хирургической точностью для расчета частотной маскировки? Этот инструмент — когнитивный инженер. Подключаясь в реальном времени через протокол MCP и TCP, ИИ Claude «слышит» состояние вашей консоли и выполняет решения по мастерингу.

> [!NOTE]
> Разработано **produktes-code** и **Jesús Ferrer (CHUS BZN)** для установления профессиональных стандартов.

## 🚀 2. Техническое развертывание (Установка)

Для обеспечения стабильности мы используем **Automated CI/CD через GitHub Actions**.
Исходный код компилируется в облаке для Windows, macOS и Linux.

#### Как скачать и установить
1. Перейдите в раздел **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.
2. Скачайте последнюю версию:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

### 🍎 Пользователи macOS (Gatekeeper)
**Правый клик по приложению -> Открыть**.

### 🪟 Пользователи Windows (SmartScreen)
Нажмите **«Подробнее»**, затем **«Выполнить в любом случае»**.

## 🔌 3. Маршрутизация сигналов

• **Remote Script (Python):** Переместите `AntigravityCore` в папку Remote Scripts в Ableton.
• **Low-Latency TCP:** Скрипт Python открывает порт `9001`. Приложение Electron подключается к этому порту по IPC.
• **LLM Tokens:** Ваш ключ API Claude шифруется локально.

## 💻 4. Операционная философия

Эргономика для профессионалов. Принцип Dark-Mode.
• **Dashboard:** Панель диагностики состояния проекта.
• **Нативные контроллеры:** Слайдеры миллисекунда в миллисекунду привязаны к TCP-порту.
• **Асинхронность:** 60fps UI без зависань.

## ⚙️ 5. Мастер-класс параметров

- **Адаптивный компрессор (Glue Compressor):** ИИ динамически устанавливает медленную атаку и сверхбыстрый релиз на основе BPM.
- **Удаление фазовых конфликтов (EQ Eight):** Мы делаем срез Side (S) ниже 120 Гц, оставляя саб-бас в моно.
- **LLM Framework (MCP):** ИИ математически анализирует JSON-данные ваших треков и возвращает порядок выполнения.

## 🌍 6. Мультимодальная интеграция

100% поддержка Unicode и Hot-Reloading на 7 языках.

## 🛡️ 7. Архитектура безопасности

• **Anti-Flood (Rate limiting):** Алгоритмы ограничивают аномальные скачки TCP-запросов.
• **JSON Payload Validation:** Удаление вредоносных структур.
• **RAM-Sanity (2 GB Limit):** Предотвращение OOM-атак.

## 📝 8. Журнал отладки (FAQ)

В: **macOS Gatekeeper блокирует приложение.**
О: Правый клик -> Открыть.

В: **TCP Deadlock / Нет ответа.**
О: Порт `9001` заблокирован, или скрипт не назначен в настройках Ableton.

## ⚖️ 9. Инженерный манифест и Лицензия

Создано produktes-code и Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.
