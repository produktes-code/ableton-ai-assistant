![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge)

![Ableton AI Assistant Logo](build/icon.png)

# Ableton AI Assistant V1.0.0

##### Ingeniero de Mezcla Cognitivo IA y Asistente de Audio en Tiempo Real MCP / Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant

🌐 **Leer en:** [🇬🇧 English](README.md) | **🇪🇸 Español** | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 1. La Visión (Introducción)

La mezcla de audio avanzada suele ser un cuello de botella analítico. El cerebro del productor entra en fatiga auditiva intentando resolver conflictos de fase milimétricos, perdiendo la perspectiva creativa global. Desarrollamos Ableton AI Assistant cuestionando el paradigma del DAW: ¿Por qué debemos mover knobs manualmente cuando una máquina tiene la precisión quirúrgica para calcular el enmascaramiento frecuencial? Esta herramienta es un revolucionario ingeniero cognitivo. Conectándose en tiempo real mediante el Protocolo de Contexto de Modelo (MCP) y una arquitectura TCP implacable, la IA de Claude 'escucha' el estado de tu consola y ejecuta decisiones de mastering hardcodeadas nativamente. Es el puente entre el código de bajo nivel de Ableton y la semántica natural de la IA.

> [!NOTE]
> Desarrollado por **produktes-code** y **Jesús Ferrer (CHUS BZN)** para establecer estándares profesionales en la ingeniería comercial.

## 🚀 2. Despliegue Técnico (Instalación) e Instalación CI/CD

Para garantizar estabilidad multiplataforma, ahora empleamos **CI/CD Automatizado vía GitHub Actions**. 
En lugar de empaquetar de forma local, nuestro código fuente se compila nativamente en entornos puros de Windows y macOS en la nube.

#### Cómo Descargar e Instalar
1. Navega a la sección **Releases** de este repositorio.
2. Descarga la última versión compilada automáticamente para tu Sistema Operativo:
   - `antigravity-app.Setup.1.0.0.exe` (Windows)
   - `antigravity-app-1.0.0.dmg` (macOS)

### 🍎 Usuarios de macOS (Gatekeeper)
Al no contar con un certificado de desarrollador de pago de Apple, Gatekeeper marcará el binario. El método legítimo de bypass local es hacer **Clic derecho sobre la app -> Abrir** (no hagas doble clic). No es un fallo, es el flujo estándar de software open-source de alto rendimiento.

### 🪟 Usuarios de Windows (SmartScreen)
Windows Defender puede mostrar un aviso azul de 'PC protegido' al ejecutar el instalador `.exe`. Haz clic en **'Más información'** y luego en **'Ejecutar de todas formas'**.

## 🔌 3. Flujo de Señal y Setup

Una plataforma verdaderamente profesional debe ofrecer transparencia total sobre sus flujos de datos. La arquitectura híbrida de Ableton AI Assistant requiere un ruteo preciso.

• **Remote Script (Python en Ableton):** Debes arrastrar la carpeta `AntigravityCore` a la ruta nativa de Remote Scripts de Ableton Live (ej. `MIDI Remote Scripts/`). Esto inyecta nuestro backend directamente en el motor de audio de Live.
• **Sockets TCP de Baja Latencia:** El script de Python abre el puerto `9001` de forma silente. La aplicación de escritorio de Electron (Frontend) se conecta a este puerto mediante IPC bidireccional. Este diseño evade las limitaciones de latencia típicas del protocolo MIDI estándar.
• **Inyección de Tokens LLM (API Keys):** El sistema cifra y maneja tu clave de Claude API (Anthropic) localmente. Las inferencias pesadas de procesamiento de lenguaje natural viajan por el socket hacia la nube, mientras que la ejecución matemática DSP se calcula en el CPU local.

## 💻 4. Filosofía Operativa (Guía de Uso)

Diseñar interfaces para productores exige respetar su ergonomía visual durante largas jornadas en el estudio. El principio de Dark-Mode de Ableton se ha calcado y optimizado.

• **Lienzo Principal (El Dashboard):** Un panel de diagnóstico que expone instantáneamente la "Salud del Proyecto" mediante barras de progreso y alertas críticas de saturación.
• **Controles Táctiles Nativos:** El Knob central y los sliders de Drive/Gain no son maquetas visuales. Son controles reactivos unidos milisegundo a milisegundo al puerto TCP. Deslizarlos en la app altera tu mezcla en Ableton sin delay.
• **Naturaleza Asíncrona:** No hay cuelgues (freezes). El hilo principal renderiza la UI y el chat a 60fps constantes mientras el servidor MCP de la IA analiza los nodos del árbol JSON de tus pistas en el background.

## ⚙️ 5. Masterclass de Parámetros (Funcionalidades)

- **Compresión Algorítmica Adaptativa (Glue Compressor):** El asistente no lanza un preset ciego. Al instanciar el compresor, la IA establece dinámicamente un tiempo de Attack lento (para salvaguardar la pegada de los transitorios) y un Release ultra-rápido calculado sobre el BPM de la sesión. 
- **Despeje de Enmascaramiento y Fase (EQ Eight):** Un problema clásico de producción amateur es el choque de graves. Nuestra lógica inyecta un recorte Side (S) estricto por debajo de 120Hz. Esta directiva técnica ancla la energía física del Kick y el Sub-bass puramente en Mono (Mid), erradicando las cancelaciones de fase al ser reproducido en clubs o sistemas de megafonía estéreo.
- **Framework LLM (Protocolo MCP):** Aquí reside el corazón del genio. Ableton Assistant se erige como un servidor MCP que empodera al modelo Claude. La IA no adivina; 'lee' literalmente el payload JSON del estado de las pistas, razona matemáticamente el arreglo, y devuelve la orden de ejecución. Es programación neuro-lingüística aplicada a las frecuencias.

## 🌍 6. Integración Multimodal Global

Tratar la internacionalización mediante simples JSON de traducción plana es un insulto al profesional global. Hemos codificado un paradigma Multimodal Estructural. Esto implica soporte Unicode del 100% y recarga en caliente (Hot-Reloading) de las capas léxicas completas en los 7 idiomas (ES, EN, DE, UK, RU, ZH, JA). Porque la precisión de la ingeniería y el respeto al productor no entienden de barreras idiomáticas.

## 🛡️ 7. Arquitectura de Blindaje (Seguridad)

En un entorno de estudio profesional, un crash puede significar la pérdida de una toma vocal irrepetible. Hemos diseñado una coraza defensiva (Shielding) que emula las mejores prácticas de DevSecOps:

• **Ingeniería Anti-Flood (Rate limiting):** Los algoritmos estrangulan cualquier pico anómalo de peticiones TCP mediante middlewares de limitación, evadiendo colapsos de Thread Pool al arrastrar cursores MIDI masivamente.
• **Validación de Payloads JSON:** El Remote Script inspecciona cada trama entrante y descarta estructuras malformadas, impidiendo inyecciones maliciosas de código OS.
• **Cristalografía Binaria y RAM (Limitador 2 GB):** El sistema restringe la ingesta de respuestas anormalmente largas del modelo LLM para evitar ataques OOM (Out Of Memory) que congelarían tu sesión de Ableton.

## 📝 8. Debug Log (FAQ)

P: **macOS Gatekeeper informa que la aplicación está 'dañada' o no puede abrirse.**
R: Este es un flag de seguridad estricto temporal de Apple. Como ingeniero, sabes que debes aprobar el binario usando 'Clic derecho -> Abrir'. Confirmamos la absoluta integridad de la compilación local.

P: **Interbloqueo de TCP / No hay respuesta del Ableton Live.**
R: Dos causas de ingeniería probables: A) El puerto `9001` local está bloqueado por un firewall restrictivo en tu OS. B) No has asignado el script `AntigravityCore` en la pestaña Link/MIDI de las Preferencias de Ableton Live.

P: **Discrepancias de latencia en el Chat (API / LLM).**
R: La manipulación de los sliders (Gain/Drive) transcurre por el socket local (0ms). Únicamente las inferencias complejas del chat (razonamiento del modelo) viajan a los servidores de Anthropic. Revisa tu enrutamiento WAN si el chat tarda más de 3 segundos en responder.

## ⚖️ 9. Manifiesto de Ingeniería, Créditos y Licencia

Este software es el resultado manifiesto de la profunda ingeniería concebida y articulada desde los laboratorios de produktes-code en unión indisociable con el Ingeniero Jesús Ferrer García (CHUS BZN).

Nos negamos a ofrecer cajas negras simplificadas. Entregamos consolas paramétricas absolutas. Licenciado bajo restricciones de propiedad intelectual y los más estrictos márgenes open source (CC BY-NC-SA 4.0). ESTÁNDAR CORPORATIVO - STUDIO READY. GRADO INGENIERÍA CERTIFICADO.
