![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
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

🌐 **Leer en:** [🇬🇧 English](README.md) | **🇪🇸 Español** | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 La Visión (Introducción)

La génesis de Ableton AI Assistant surge de una frustración profunda en la industria de la producción musical: el cerebro del productor entra en fatiga auditiva intentando resolver conflictos de fase milimétricos, perdiendo la perspectiva creativa global. Desarrollamos este asistente cuestionando el paradigma del DAW: ¿Por qué debemos mover knobs manualmente cuando una máquina tiene la precisión quirúrgica para calcular el enmascaramiento frecuencial?

Ableton AI Assistant fue diseñado para ser el **Gemelo Digital de Audio** definitivo para productores e ingenieros. No es un simple script MIDI; es un cerebro curatorial que comprende la energía de la mezcla y blinda tu sesión. Conectándose en tiempo real mediante el Protocolo de Contexto de Modelo (MCP) y una arquitectura TCP implacable, la IA de Claude 'escucha' el estado de tu consola y ejecuta decisiones de mastering hardcodeadas nativamente. Hemos creado esta herramienta para devolverle el control a los ingenieros sobre su identidad sonora.

> [!NOTE]
> Desarrollado por **produktes-code** y **Jesús Ferrer (CHUS BZN)** para establecer estándares profesionales en la ingeniería comercial.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)

---

## ⚙️ Masterclass de Parámetros (Funcionalidades)

- **Compresión Algorítmica Adaptativa (Glue Compressor)**: El asistente no lanza un preset ciego. Al instanciar el compresor, la IA establece dinámicamente un tiempo de Attack lento (para salvaguardar la pegada de los transitorios) y un Release ultra-rápido calculado sobre el BPM de la sesión. 
- **Despeje de Enmascaramiento y Fase (EQ Eight)**: Un problema clásico de producción amateur es el choque de graves. Nuestra lógica inyecta un recorte Side (S) estricto por debajo de 120Hz. Esta directiva técnica ancla la energía física del Kick y el Sub-bass puramente en Mono (Mid), erradicando las cancelaciones de fase al ser reproducido en clubs o sistemas de megafonía estéreo.
- **Framework LLM (Protocolo MCP)**: Aquí reside el corazón del genio. Ableton Assistant se erige como un servidor MCP que empodera al modelo Claude. La IA no adivina; 'lee' literalmente el payload JSON del estado de las pistas, razona matemáticamente el arreglo, y devuelve la orden de ejecución. Es programación neuro-lingüística aplicada a las frecuencias.
- **Arquitectura Asíncrona**: No hay cuelgues (freezes). El hilo principal (Main Thread) renderiza la UI a 60fps inquebrantables mientras los workers del servidor MCP operan en el abismo del background consumiendo núcleos de CPU.

---

## 🛡️ Arquitectura de Blindaje (Seguridad)

En un entorno de despliegue profesional, un crash no es un bug, es pérdida de capital (tomas vocales irrepetibles). Hemos diseñado una coraza defensiva (Shielding) que emula las mejores prácticas de DevSecOps:

• **Ingeniería Anti-Flood (Rate limiting)**: Los algoritmos asíncronos estrangulan cualquier pico anómalo de peticiones TCP mediante middlewares de limitación, evadiendo colapsos de Thread Pool al arrastrar cursores masivamente.
• **Validación de Payloads JSON**: El Remote Script inspecciona cada trama entrante y descarta estructuras malformadas, impidiendo inyecciones maliciosas de código OS.
• **Sanidad de RAM (Limitador 2 GB)**: El sistema restringe la ingesta de respuestas anormalmente largas del modelo LLM para evitar ataques OOM (Out Of Memory) que destruirían los servidores y congelarían tu sesión.

---

## 🚀 Despliegue Técnico e Instalación CI/CD

Para garantizar estabilidad multiplataforma, ahora empleamos **CI/CD Automatizado vía GitHub Actions**. 
En lugar de empaquetar de forma local, nuestro código fuente se compila nativamente en entornos puros de Windows, macOS y Linux Ubuntu en la nube.

### 🛠️ Descargar Instaladores
Navega a la sección **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** de este repositorio para descargar los binarios de tu SO:
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg`
- **Linux**: `Ableton.AI.Assistant-1.0.0.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

### 🍎 Usuarios de macOS (Gatekeeper)
Al no contar con un certificado de desarrollador de pago de Apple, Gatekeeper marcará el binario. Como ingenieros, el método legítimo de bypass local es hacer **Clic derecho sobre la app -> Abrir** (no hagas doble clic). Es el flujo estándar de software open-source de alto rendimiento.

### 🪟 Usuarios de Windows (SmartScreen)
Windows Defender puede mostrar un aviso azul de 'PC protegido' al ejecutar el instalador `.exe`. Haz clic en **'Más información'** y luego en **'Ejecutar de todas formas'**.

### 🐧 Usuarios de Linux (AppImage & Debian)
- **AppImage**: Otorga permisos de ejecución antes de lanzar:
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage` y ejecútalo.
- **Paquete Debian (`.deb`)**: Instala vía terminal:
  `sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb` o haz doble clic para instalar a través de tu gestor de software local.

---

## 🔌 Flujo de Señal y Setup

Una plataforma verdaderamente profesional debe ofrecer transparencia total sobre sus flujos de datos. La arquitectura híbrida requiere un ruteo preciso.

• **Remote Script (Python en Ableton)**: Debes arrastrar la carpeta `AntigravityCore` a la ruta nativa de Remote Scripts de Ableton Live (ej. `MIDI Remote Scripts/`). Esto inyecta nuestro backend directamente en el motor de audio de Live.
• **Sockets TCP de Baja Latencia**: El script de Python abre el puerto `9001` de forma silente. La aplicación de escritorio de Electron se conecta a este puerto mediante IPC bidireccional.
• **Inyección de Tokens LLM (API Keys)**: El sistema cifra y maneja tu clave de Claude API (Anthropic) localmente. Las inferencias pesadas transitan hacia la nube, mientras que la ejecución DSP matemática se calcula en la CPU local.

---

## 📚 Documentación y Manuales

Para una masterclass técnica exhaustiva, guías de resolución de problemas y detalles completos de la API, descarga nuestro manual oficial:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## ⚖️ Manifiesto de Ingeniería, Créditos y Licencia

Este software es el resultado manifiesto de la profunda ingeniería concebida y articulada desde los laboratorios de produktes-code en unión indisociable con el Ingeniero Jesús Ferrer García (CHUS BZN).

Nos negamos a ofrecer cajas negras simplificadas. Entregamos consolas paramétricas absolutas. Licenciado bajo restricciones de propiedad intelectual y los más estrictos márgenes open source (CC BY-NC-SA 4.0). ESTÁNDAR CORPORATIVO - STUDIO READY. GRADO INGENIERÍA CERTIFICADO.

## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-27**.
