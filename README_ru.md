![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton AI Assistant Logo" />
</p>

<h1 align="center">Ableton AI Assistant V1.0.0</h1>

<p align="center">
  <b>Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant</b><br/>
  <i>Когнитивный ИИ-инженер по сведению и аудиопомощник реального времени</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="License" />
</p>

🌐 **Читать на:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | **🇷🇺 Русский** | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 Видение (Введение)

Продвинутое сведение аудио часто является аналитическим узким местом. Мы разработали Ableton AI Assistant, чтобы решить эту проблему. Зачем крутить ручки вручную, если машина обладает хирургической точностью для расчета частотной маскировки? Этот инструмент — когнитивный инженер. Подключаясь в реальном времени через протокол MCP и TCP, ИИ Claude «слышит» состояние вашей консоли и выполняет решения по мастерингу.

> [!NOTE]
> Разработано **produktes-code** и **Jesús Ferrer (CHUS BZN)** для установления профессиональных стандартов.

---

## 📸 Интерфейс (Ergonomics)

![Desktop Interface](docs/screenshot-UI.png)

---

## ⚙️ Мастер-класс параметров (Функции)

- **Адаптивный компрессор (Glue Compressor)**: ИИ динамически устанавливает медленную атаку и сверхбыстрый релиз на основе BPM.
- **Удаление фазовых конфликтов (EQ Eight)**: Мы делаем срез Side (S) ниже 120 Гц, оставляя саб-бас в моно.
- **LLM Framework (MCP)**: ИИ математически анализирует JSON-данные ваших треков и возвращает порядок выполнения.
- **Асинхронность**: 60fps UI без зависаний, пока сервер ИИ работает в фоновом режиме.

---

## 🛡️ Архитектура безопасности

• **Anti-Flood (Rate limiting)**: Алгоритмы ограничивают аномальные скачки TCP-запросов.
• **JSON Payload Validation**: Удаление вредоносных структур и OS-инъекций.
• **RAM-Sanity (2 GB Limit)**: Предотвращение OOM-атак путем блокировки тяжелых ответов модели.

---

## 🚀 Техническое развертывание и установка CI/CD

Для обеспечения стабильности мы используем **Automated CI/CD через GitHub Actions**.
Исходный код компилируется в облаке для Windows, macOS и Linux.

### 🛠️ Скачать установщики
Перейдите в раздел **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**, чтобы скачать бинарные файлы для вашей ОС:
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg`
- **Linux**: `Ableton.AI.Assistant-1.0.0.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

### 🍎 Пользователи macOS (Gatekeeper)
**Правый клик по приложению -> Открыть**.

### 🪟 Пользователи Windows (SmartScreen)
Нажмите **«Подробнее»**, затем **«Выполнить в любом случае»**.

### 🐧 Пользователи Linux (AppImage & Debian)
- **AppImage**: Дайте права на выполнение:
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage` и запустите.
- **Debian Package (`.deb`)**: Установка через терминал:
  `sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb`

---

## 🔌 Маршрутизация сигналов и настройка

• **Remote Script (Python в Ableton)**: Переместите `AntigravityCore` в папку Remote Scripts.
• **Low-Latency TCP Sockets**: Скрипт Python открывает порт `9001`. Приложение Electron подключается к этому порту по IPC.
• **LLM Tokens (API Keys)**: Ваш ключ API Claude шифруется локально. Тяжелые запросы идут в облако, DSP вычисляется локально.

---

## 📚 Документация и руководства

Для получения расширенных инструкций загрузите официальное руководство:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## ⚖️ Инженерный манифест и Лицензия

Создано produktes-code и Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-27**.
