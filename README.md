<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton Antigravity Logo" />
</p>

<h1 align="center">Ableton Antigravity V1.0.0</h1>

<p align="center">
  <b>Asistente de Inteligencia Artificial Híbrido e Integración TCP para Ableton Live</b><br/>
  <i>Hybrid AI Assistant & TCP Integration for Ableton Live</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge" alt="Versión 1.0.0" />
  <img src="https://img.shields.io/badge/Status-Cine_Station_Pro-success?style=for-the-badge" alt="Estado" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="Licencia" />
</p>

<p align="center">
  <b>🌐 Multilingual & Multimodal Support / Soporte Multiidioma:</b><br/>
  🇪🇸 Spanish | 🇬🇧 English
</p>

---

## 🎯 Overview / Descripción del Proyecto

**Ableton Antigravity** es el asistente de producción musical definitivo. Transforma Ableton Live en un entorno reactivo impulsado por Inteligencia Artificial (Claude / OpenAI) mediante el protocolo **Model Context Protocol (MCP)**. Actúa como tu ingeniero de mezcla personal, corrigiendo enmascaramiento de frecuencias, añadiendo dispositivos nativos y procesando audio en tiempo real, todo ello sin romper el flujo de trabajo ni arrebatar el control creativo.

> [!NOTE]
> Desarrollado por **produktes-code** y **Antigravity IA** para establecer estándares profesionales en la producción musical asistida (Cine Station Pro Standard).

---

## 📸 Interfaz Reactiva (Dashboard)
*(Diseño UI/UX nativo adaptado a Ableton Live 12)*

![Antigravity Dashboard](docs/screenshot-UI.png)

---

## ⚙️ Características Principales

1. 🎛️ **Control Macro Inteligente (TCP)**: Deslizadores de Ganancia, Drive y bypass que inyectan comandos matemáticos (JSON) directamente al puerto 9001 de Ableton.
2. 🧠 **Motor LOM (Live Object Model)**: Script de Python `AntigravityCore` que audita pistas, volumen y dispositivos sin emular clicks de ratón (100% nativo).
3. 🎤 **Prompting Multimodal**: Escribe órdenes naturales ("*Inserta un EQ Eight en la pista de voces*") o arrastra archivos de audio para análisis espectral (Drag & Drop).
4. 🩺 **Escaneo de Salud de Sesión**: Terminal Log en tiempo real que alerta de picos de recorte y enmascaramiento de frecuencias.
5. 🛡️ **Feedback Visual Bidireccional**: Consola que muestra todos los paquetes TCP enviados desde el *Frontend* de Electron hacia el *Backend* en Python.

---

## 🏗️ Stack Tecnológico

*   **Frontend & Shell:** Electron (Node.js) + HTML5 + Vanilla CSS/Tailwind (Interfaz).
*   **Backend Ableton (DAW):** Python 2/3 (API Remote Scripts LOM).
*   **Comunicación:** Puente IPC (Inter-Process Communication) en Electron hacia un Socket TCP puro.
*   **Cerebro IA:** Model Context Protocol (MCP) para integración con Claude 3.5 Sonnet / OpenAI.

### 📁 Estructura de Carpetas

```text
ableton-ai-assistant/
├── electron-app/       # Frontend Multimodal (Reactividad, IPC, TCP Sender)
├── mcp-server/         # Cerebro IA (Herramientas, prompts The Mentor y Mix Engineer)
├── remote-script/      # AntigravityCore (El script Python que se instala en Ableton)
├── docs/               # Manuales PDF multilingües compilados
└── build/              # Iconografía e instaladores
```

---

## 🚀 Instalación y Configuración Rápida

### 1. Instalación del Script en Ableton
Debes inyectar el cerebro de Python dentro de Ableton Live para abrir el puerto 9001:
```bash
# Copia la carpeta "AntigravityCore" a tus Remote Scripts:
# macOS: /Applications/Ableton Live 12 Suite.app/Contents/App-Resources/MIDI Remote Scripts/
# Windows: C:\ProgramData\Ableton\Live 12 Suite\Resources\MIDI Remote Scripts\
```
Abre Ableton > Preferencias > Link/Tempo/MIDI > Selecciona **AntigravityCore** en una ranura de Superficie de Control.

### 2. Instalación de la Aplicación (Cliente)
Ejecuta el archivo `.dmg` (macOS) o `.exe` (Windows) que encontrarás en la sección de Descargas/Releases de este repositorio.

---

## 💻 Instaladores Nativos

El proyecto se compila y empaqueta en binarios ejecutables para las distintas plataformas usando `electron-builder`:
*   **macOS**: Instalador nativo disponible como archivo `.dmg`.
*   **Windows**: Instalador disponible como archivo `.exe`.

---

## 📚 Documentación Completa

Para acceder a la documentación técnica, manual de usuario y guía de conexión MCP:
👉 **[Descargar Manual Técnico Completo (PDF)](./docs/USER_MANUAL.pdf)**

---

## ⚖️ Créditos y Licencia

Este software es propietario y está protegido bajo derechos de autor. Reservados todos los derechos. Creado y mantenido por **produktes-code** y **Jesús Ferrer García (CHUS BZN)**. Se prohíbe cualquier copia, redistribución o modificación no autorizada de este software.

*© 2026 Ableton Antigravity — Todos los derechos reservados.*
