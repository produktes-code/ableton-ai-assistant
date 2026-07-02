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

🌐 **Читать на:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | **🇷🇺 Русский** | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 Видение

Сведение - это аналитическое узкое место. Мы разработали этот инструмент, ставя под сомнение парадигму DAW: зачем крутить ручки вручную, когда машина может рассчитать маскирование? Этот ИИ действует как когнитивный инженер, читая состояние Ableton через MCP и выполняя решения по мастерингу.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)


---

## ⚙️ Мастер-класс параметров

- **Адаптивная компрессия**: Устанавливает медленную атаку и быстрый релиз (на основе BPM), чтобы компрессор дышал в ритме трека.
- **Фазовое разрешение (EQ Eight)**: Срез Side (S) ниже 120 Гц фиксирует бас в Mono, чтобы избежать фазовых отмен.
- **Протокол MCP**: ИИ читает состояние дорожек через JSON и выполняет математические решения.
- **Ядро TCP**: Сырые сокеты TCP управляют Ableton без задержки MIDI.
- **Менеджер True Peak / LUFS**: Устанавливает лимитеры для идеальной доставки на стриминговые платформы.

---

## 🛡️ Архитектура экранирования

Экранирование:

• Anti-Flood: Блокировка всплесков запросов.
• Magic Bytes: Гексадецимальная проверка файлов.
• 2 GB Limit: Защита оперативной памяти.

---

## 🚀 Техническое развертывание

Архитектура 'Zero-Friction':

• macOS: Gatekeeper заблокирует файл. Решение: 'Правый клик -> Открыть'.
• Windows: Автоматическая конфигурация PATH.

---

## 📚 Документация и руководства

Загрузите наше официальное руководство:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](docs/USER_MANUAL.pdf)**


---

## ⚖️ Инженерный манифест

Разработано produktes-code и Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.



⚠️ macOS Users Notice: When opening the application for the first time, macOS may show a security warning. Solution: right-click on the application and select "Open", then click "Open" in the dialog. If it was already blocked, go to System Preferences > Privacy & Security and click "Open Anyway".