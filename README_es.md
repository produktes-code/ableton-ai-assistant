<div align="center">
  <img src="https://raw.githubusercontent.com/produktes-code/ableton-ai-assistant/main/build/icon.png" width="128" alt="Logo" />
  <h1>Ableton AI Assistant</h1>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-blue?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Version-1.0.0-orange?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge" alt="Status" />
</p>

🌐 **Multilingual & Multimodal Support / Soporte Multiidioma:**
🇪🇸 Spanish | 🇬🇧 English | 🇩🇪 Deutsch | 🇺🇦 Ukrainian | 🇷🇺 Russian | 🇨🇳 Chinese | 🇯🇵 Japanese

---

## 🎯 Descripción del Proyecto
Ableton AI Assistant es el asistente de producción musical definitivo. Transforma Ableton Live en un entorno reactivo impulsado por Inteligencia Artificial (Claude / OpenAI) mediante el protocolo **Model Context Protocol (MCP)**. Actúa como tu ingeniero de mezcla personal, corrigiendo enmascaramiento de frecuencias, añadiendo dispositivos nativos y procesando audio en tiempo real, todo ello sin romper el flujo de trabajo ni arrebatar el control creativo.

## ✨ Características Principales
- **Arquitectura TCP directa**: Baja latencia y comunicación instantánea con Ableton Live.
- **Soporte Multimodal**: Interfaz y procesamiento de comandos en 7 idiomas.
- **Seguridad y Blindaje**: 
  - **Rate limiting** para evitar saturación del servidor.
  - Validación de **Magic Bytes** y tipos MIME para archivos de audio.
  - Límite estricto de **2 GB** por archivo para procesamiento.
- **Instaladores Nativos**: Binarios optimizados para macOS (.dmg) y Windows (.exe).

## 💻 Instalación y Requisitos
El proceso de instalación ha sido diseñado para ser completamente *Plug & Play*:
1. Dirígete a la sección de [Releases](https://github.com/produktes-code/ableton-ai-assistant/releases/latest) y descarga el instalador correspondiente a tu sistema operativo (macOS o Windows).
2. Ejecuta el instalador y sigue las instrucciones en pantalla.
3. Abre Ableton Live, dirígete a `Preferences > Link/Tempo/MIDI` y selecciona el *Remote Script* del asistente.
4. *(Opcional)* Configura tu archivo `.env` para añadir claves de API personalizadas si utilizas modelos en la nube.

## 🚀 Guía de Uso Rápido
Una vez instalado y conectado:
1. Abre la interfaz del asistente junto a tu sesión de Ableton Live.
2. Escribe o dicta un comando en la terminal del asistente (por ejemplo: *"Añade un EQ Eight en la pista 1 y recorta los graves a 100Hz"*).
3. La IA procesará la solicitud a través del protocolo TCP y ejecutará los cambios automáticamente.

## 🛠️ Stack Tecnológico
Este proyecto ha sido desarrollado utilizando tecnologías de vanguardia para asegurar el máximo rendimiento:
- **Frontend**: Electron y Vanilla JS para una interfaz de escritorio ligera y reactiva.
- **Backend/Core**: Python (integración nativa y procesamiento de bajo nivel).
- **Integración DAW**: Ableton Live API y scripts remotos (MIDI/OSC).
- **Inteligencia Artificial**: Integración nativa con Claude AI (Anthropic) y soporte para LLMs locales.

## 📄 Licencia
Este proyecto está distribuido bajo la licencia **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**. Puedes compartir y adaptar el material, siempre y cuando des el crédito apropiado y no lo utilices con fines comerciales.

## 📚 Documentación y Manuales
Para una explicación técnica exhaustiva, guías de resolución de problemas, y detalles completos de la API, por favor descarga y consulta nuestro manual oficial:
📥 **[Descargar Manual de Usuario en PDF (Todos los idiomas)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

## 👥 Créditos
Diseñado, desarrollado y mantenido por **produktes-code** y **Chus BZN**.


⚠️ Aviso para usuarios de macOS: Al abrir la aplicación por primera vez, macOS puede mostrar un aviso de seguridad. Solución: haz clic derecho sobre la aplicación y selecciona "Abrir", luego haz clic en "Abrir" en el diálogo. Si ya fue bloqueada, ve a Preferencias del Sistema > Privacidad y Seguridad y haz clic en "Abrir de todos modos".

