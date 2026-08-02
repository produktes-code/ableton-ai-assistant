![Ableton AI Assistant Logo](../build/icon.png)

# Ableton AI Assistant - Manual de Usuario / User Manual

*Official Documentation & Technical Guide*

---

![Ableton AI Assistant UI](../docs/screenshot-UI.png)

### Keywords de Seguridad

`CERTIFIED`, `RETAIL-READY`, `Rate limiting`, `Magic Bytes`, `2 GB`, `7 idiomas`, `CC BY-NC-SA 4.0`



### ![ES](https://flagcdn.com/h24/es.png) Español (ES)

#### 🎯 1. La Visión (Introducción)

La génesis de Ableton AI Assistant surge de una frustración profunda en la industria de la producción musical: el cerebro del productor entra en fatiga auditiva intentando resolver conflictos de fase milimétricos, perdiendo la perspectiva creativa global. Desarrollamos este asistente cuestionando el paradigma del DAW: ¿Por qué debemos mover knobs manualmente cuando una máquina tiene la precisión quirúrgica para calcular el enmascaramiento frecuencial?

Ableton AI Assistant fue diseñado para ser el **Gemelo Digital de Audio** definitivo para productores e ingenieros. No es un simple script MIDI; es un cerebro curatorial que comprende la energía de la mezcla y blinda tu sesión. Conectándose en tiempo real mediante el Protocolo de Contexto de Modelo (MCP) y una arquitectura TCP implacable, la IA de Claude 'escucha' el estado de tu consola y ejecuta decisiones de mastering hardcodeadas nativamente. Hemos creado esta herramienta para devolverle el control a los ingenieros sobre su identidad sonora.

> [!NOTE]
> Desarrollado por **produktes-code** y **Jesús Ferrer (CHUS BZN)** para establecer estándares profesionales en la ingeniería comercial.

#### 🚀 2. Despliegue Técnico (Instalación) e Instalación CI/CD

Para garantizar estabilidad multiplataforma, ahora empleamos **CI/CD Automatizado vía GitHub Actions**. 
En lugar de empaquetar de forma local, nuestro código fuente se compila nativamente en entornos puros de Windows, macOS y Linux Ubuntu en la nube.

###### Cómo Descargar e Instalar
1. Navega a la sección **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** de este repositorio.
2. Descarga la última versión compilada automáticamente para tu Sistema Operativo:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu/Debian)

##### 🍎 Usuarios de macOS (Gatekeeper)
Al no contar con un certificado de desarrollador de pago de Apple, Gatekeeper marcará el binario. Como ingenieros, el método legítimo de bypass local es hacer **Clic derecho sobre la app -> Abrir** (no hagas doble clic).

##### 🪟 Usuarios de Windows (SmartScreen)
Windows Defender puede mostrar un aviso azul de 'PC protegido' al ejecutar el instalador `.exe`. Haz clic en **'Más información'** y luego en **'Ejecutar de todas formas'**.

#### 🔌 3. Flujo de Señal y Setup

Una plataforma verdaderamente profesional debe ofrecer transparencia total sobre sus flujos de datos. La arquitectura híbrida de Ableton AI Assistant requiere un ruteo preciso.

• **Remote Script (Python en Ableton):** Debes arrastrar la carpeta `AntigravityCore` a la ruta nativa de Remote Scripts de Ableton Live (ej. `MIDI Remote Scripts/`). Esto inyecta nuestro backend directamente en el motor de audio de Live.
• **Sockets TCP de Baja Latencia:** El script de Python abre el puerto `9001` de forma silente. La aplicación de escritorio de Electron (Frontend) se conecta a este puerto mediante IPC bidireccional. Este diseño evade las limitaciones de latencia típicas del protocolo MIDI estándar.
• **Inyección de Tokens LLM (API Keys):** El sistema cifra y maneja tu clave de Claude API (Anthropic) localmente. Las inferencias pesadas de procesamiento de lenguaje natural viajan por el socket hacia la nube, mientras que la ejecución matemática DSP se calcula en el CPU local.

#### 💻 4. Filosofía Operativa (Guía de Uso)

Diseñar interfaces para creadores exige respetar su ergonomía visual durante largas jornadas nocturnas. El principio de Dark-Mode de Ableton (RGB: 15, 15, 15) maximiza la legibilidad del contraste y concentra la visión donde importa.

• **Lienzo Principal (El Dashboard):** Un panel de diagnóstico que expone instantáneamente la "Salud del Proyecto" mediante barras de progreso y alertas críticas de saturación. Sin menús ocultos de 4 niveles de profundidad.
• **Controles Táctiles Nativos:** El Knob central y los sliders de Drive/Gain no son maquetas visuales. Son controles reactivos unidos milisegundo a milisegundo al puerto TCP. Deslizarlos en la app altera tu mezcla en Ableton sin delay.
• **La Naturaleza Asíncrona:** No hay cuelgues (freezes). El hilo principal (Main Thread) renderiza la UI a 60fps inquebrantables mientras los workers del servidor MCP operan en el abismo del background consumiendo núcleos de CPU.

#### ⚙️ 5. Masterclass de Parámetros (Funcionalidades)

- **Compresión Algorítmica Adaptativa (Glue Compressor):** El asistente no lanza un preset ciego. Al instanciar el compresor, la IA establece dinámicamente un tiempo de Attack lento (para salvaguardar la pegada de los transitorios) y un Release ultra-rápido calculado sobre el BPM de la sesión. 
- **Despeje de Enmascaramiento y Fase (EQ Eight):** Un problema clásico de producción amateur es el choque de graves. Nuestra lógica inyecta un recorte Side (S) estricto por debajo de 120Hz. Esta directiva técnica ancla la energía física del Kick y el Sub-bass puramente en Mono (Mid), erradicando las cancelaciones de fase al ser reproducido en clubs o sistemas de megafonía estéreo.
- **Framework LLM (Protocolo MCP):** Aquí reside el corazón del genio. Ableton Assistant se erige como un servidor MCP que empodera al modelo Claude. La IA no adivina; 'lee' literalmente el payload JSON del estado de las pistas, razona matemáticamente el arreglo, y devuelve la orden de ejecución. Es programación neuro-lingüística aplicada a las frecuencias.

#### 🌍 6. Integración Multimodal Global

Tratar la internacionalización mediante simples JSON de traducción plana es un insulto al profesional global. Hemos codificado un paradigma Multimodal Estructural. Esto implica soporte Unicode del 100% y recarga en caliente (Hot-Reloading) de las capas léxicas completas en los 7 idiomas (ES, EN, DE, UK, RU, ZH, JA). Porque la precisión de la ingeniería y el respeto al operador no entienden de barreras idiomáticas.

#### 🛡️ 7. Arquitectura de Blindaje (Seguridad)

En un entorno de despliegue profesional, un crash no es un bug, es pérdida de capital (tomas vocales irrepetibles). Hemos diseñado una coraza defensiva (Shielding) que emula las mejores prácticas de DevSecOps:

• **Ingeniería Anti-Flood (Rate limiting):** Los algoritmos asíncronos estrangulan cualquier pico anómalo de peticiones TCP mediante middlewares de limitación, evadiendo colapsos de Thread Pool al arrastrar cursores masivamente.
• **Validación de Payloads JSON:** El Remote Script inspecciona cada trama entrante y descarta estructuras malformadas, impidiendo inyecciones maliciosas de código OS.
• **Sanidad de RAM (Limitador 2 GB):** El sistema restringe la ingesta de respuestas anormalmente largas del modelo LLM para evitar ataques OOM (Out Of Memory) que destruirían los servidores y congelarían tu sesión.

#### 📝 8. Debug Log (FAQ)

P: **macOS Gatekeeper informa que la aplicación está 'dañada' o no puede abrirse.**
R: Este es un flag de seguridad estricto temporal de Apple. Como ingeniero, sabes que debes aprobar el binario usando 'Clic derecho -> Abrir'. Confirmamos la absoluta integridad de la compilación local.

P: **Interbloqueo infinito de TCP / No hay respuesta de Ableton.**
R: Dos causas de ingeniería probables: A) El puerto local `9001` está bloqueado por el firewall de tu OS. B) No has asignado el script `AntigravityCore` en la pestaña Link/MIDI de las Preferencias de Ableton Live.

P: **Discrepancias de latencia en la conexión de red (API / LLM).**
R: La manipulación de los faders transcurre por el socket local (0ms). Únicamente las inferencias LLM masivas transitan por el socket WAN. Revisa tu router si los pings son altos en la charla.

#### ⚖️ 9. Manifiesto de Ingeniería, Créditos y Licencia

Este software es el resultado manifiesto de la profunda ingeniería concebida y articulada desde los laboratorios de produktes-code en unión indisociable con el Ingeniero Jesús Ferrer García (CHUS BZN).

Nos negamos a ofrecer cajas negras simplificadas. Entregamos consolas paramétricas absolutas. Licenciado bajo restricciones de propiedad intelectual y los más estrictos márgenes open source (CC BY-NC-SA 4.0). ESTÁNDAR CORPORATIVO - STUDIO READY. GRADO INGENIERÍA CERTIFICADO.

---



### ![EN](https://flagcdn.com/h24/gb.png) English (EN)

#### 🎯 1. The Vision (Introduction)

The genesis of Ableton AI Assistant stems from a deep frustration in the music production industry: the producer's brain enters ear fatigue trying to resolve millimeter phase conflicts, losing global creative perspective. We developed this assistant by questioning the DAW paradigm: Why must we move knobs manually when a machine has the surgical precision to calculate frequency masking?

Ableton AI Assistant was designed to be the ultimate **Audio Digital Twin** for producers and engineers. It is not a simple MIDI script; it is a curatorial brain that understands the energy of the mix and shields your session. Connecting in real time via the Model Context Protocol (MCP) and relentless TCP architecture, Claude's AI 'listens' to your console's state and natively executes hardcoded mastering decisions. We created this tool to give engineers back control over their sonic identity.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

#### 🚀 2. Technical Deployment (Installation) & CI/CD Installation

To guarantee cross-platform stability, we now employ **Automated CI/CD via GitHub Actions**. 
Instead of local packaging, our source code is natively compiled on pure Windows, macOS and Linux Ubuntu environments in the cloud.

###### How to Download and Install
1. Navigate to the **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** section of this repository.
2. Download the latest automated build for your Operating System:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu/Debian)

##### 🍎 macOS Users (Gatekeeper)
Lacking a paid Apple developer certificate, Gatekeeper will quarantine the binary. As engineers, the legitimate local bypass is to **Right-click the app -> Open** (do not double click).

##### 🪟 Windows Users (SmartScreen)
Windows Defender may show a blue 'Windows protected your PC' warning when running the `.exe` installer. Click **'More info'** and then **'Run anyway'**.

#### 🔌 3. Signal Flow & Setup

A truly professional platform must offer total transparency over its data flows. The hybrid architecture of Ableton AI Assistant requires precise routing.

• **Remote Script (Python in Ableton):** You must drag the `AntigravityCore` folder into Ableton Live's native Remote Scripts path (e.g., `MIDI Remote Scripts/`). This injects our backend directly into Live's audio engine.
• **Low-Latency TCP Sockets:** The Python script silently opens port `9001`. The Electron desktop application (Frontend) connects to this port via bidirectional IPC. This design evades the latency limitations typical of standard MIDI protocols.
• **LLM Tokens Injection (API Keys):** The system encrypts and handles your Claude API key (Anthropic) locally. Heavy natural language processing inferences travel through the socket to the cloud, while the mathematical DSP execution is calculated on the local CPU.

#### 💻 4. Operative Philosophy (User Guide)

Designing interfaces for creators demands respecting their visual ergonomics during long night shifts. Ableton's Dark-Mode principle (RGB: 15, 15, 15) maximizes contrast readability and focuses vision where it matters.

• **Main Canvas (The Dashboard):** A diagnostic panel that instantly exposes the "Project Health" through progress bars and critical saturation alerts. No 4-level deep hidden menus.
• **Native Tactile Controls:** The central Knob and the Drive/Gain sliders are not visual mockups. They are reactive controls bound millisecond by millisecond to the TCP port. Sliding them in the app alters your mix in Ableton with zero delay.
• **Asynchronous Nature:** No blockages or freezes. The Main Thread renders the UI at an unbreakable 60fps while background MCP server workers operate in the abyss consuming CPU cores.

#### ⚙️ 5. Parameter Masterclass (Features)

- **Adaptive Algorithmic Compression (Glue Compressor):** The assistant does not throw a blind preset. Upon instantiating the compressor, the AI dynamically sets a slow Attack time (to safeguard transient punch) and an ultra-fast Release calculated on the session's BPM.
- **Masking and Phase Clearing (EQ Eight):** A classic amateur production problem is bass clashing. Our logic injects a strict Side (S) cut below 120Hz. This technical directive anchors the physical energy of the Kick and Sub-bass purely in Mono (Mid), eradicating phase cancellations when played in clubs or stereo PA systems.
- **LLM Framework (MCP Protocol):** Here lies the heart of the genius. Ableton Assistant stands as an MCP server that empowers the Claude model. The AI does not guess; it literally 'reads' the JSON payload of the tracks' state, mathematically reasons the arrangement, and returns the execution order. It is neuro-linguistic programming applied to frequencies.

#### 🌍 6. Global Multimodal Integration

Treating internationalization through simple flat translation JSONs is an insult to the global professional. We encoded a Structural Multimodal paradigm. This implies 100% Unicode support and Hot-Reloading of complete lexical layers in 7 languages (ES, EN, DE, UK, RU, ZH, JA). Because engineering precision and respect for the operator do not understand language barriers.

#### 🛡️ 7. Shielding Architecture (Security)

In a professional deployment environment, a crash is not a bug; it is capital loss (unrepeatable vocal takes). We designed a defensive armor (Shielding) emulating DevSecOps best practices:

• **Anti-Flood Engineering (Rate limiting):** Asynchronous algorithms strangle any anomalous TCP request spikes using limitation middlewares, evading Thread Pool collapses when dragging cursors massively.
• **JSON Payload Validation:** The Remote Script inspects each incoming frame and discards malformed structures, preventing malicious OS code injections.
• **RAM Sanity (2 GB Limit):** We relentlessly reject any atypical weight at the LLM model response threshold to prevent Out Of Memory (OOM) attacks that would destroy servers and freeze your session.

#### 📝 8. Debug Log (FAQ)

Q: **macOS Gatekeeper reports the application is 'damaged' or cannot be opened.**
A: This is a strict temporary Apple security flag. As an engineer, you know you must approve the binary using 'Right-click -> Open'. We confirm the absolute integrity of the local compilation.

Q: **Infinite TCP Deadlock / No response from Ableton.**
A: Two probable engineering causes: A) Local port `9001` is blocked by your OS firewall. B) You have not assigned the `AntigravityCore` script in the Link/MIDI tab of Ableton Live's Preferences.

Q: **Latency discrepancies in Chat (API / LLM).**
A: Sliders manipulation occurs through the local socket (0ms). Only massive LLM inferences travel through the WAN socket. Check your router if pings are high in the chat.

#### ⚖️ 9. Engineering Manifesto, Credits & License

This software is the manifest result of profound engineering conceived and articulated from the produktes-code labs in inseparable union with Engineer Jesús Ferrer García (CHUS BZN).

We refuse to offer simplified black boxes. We deliver absolute parametric consoles. Licensed under intellectual property restrictions and the strictest open source margins (CC BY-NC-SA 4.0). CORPORATE STANDARD - STUDIO READY. CERTIFIED ENGINEERING GRADE.

---



### ![DE](https://flagcdn.com/h24/de.png) Deutsch (DE)

#### 🎯 1. Die Vision (Einführung)

Fortgeschrittenes Audio-Mixing ist oft ein analytischer Engpass. Das Gehirn des Produzenten leidet unter Ermüdung, wenn es versucht, millimetergenaue Phasenkonflikte zu lösen, und verliert dabei die kreative Perspektive. Wir haben den Ableton AI Assistant entwickelt und das DAW-Paradigma in Frage gestellt: Warum müssen wir Knöpfe manuell bewegen, wenn eine Maschine die chirurgische Präzision hat, um Frequenzmaskierung zu berechnen? 

Dieses Werkzeug ist der ultimative **Digitale Audio-Zwilling**. Es ist kein einfaches MIDI-Skript; es ist ein kognitiver Ingenieur. In Echtzeit über das Model Context Protocol (MCP) und eine unerbittliche TCP-Architektur verbunden, 'hört' die Claude-KI den Status Ihrer Konsole und führt nativ festcodierte Mastering-Entscheidungen aus. Es ist die Brücke zwischen Abletons Low-Level-Code und der natürlichen Semantik der KI.

> [!NOTE]
> Entwickelt von **produktes-code** und **Jesús Ferrer (CHUS BZN)**, um professionelle Standards in der kommerziellen Tontechnik zu setzen.

#### 🚀 2. Technische Bereitstellung & CI/CD Installation

Um eine plattformübergreifende Stabilität zu gewährleisten, verwenden wir jetzt **Automatisierte CI/CD über GitHub Actions**. 
Anstelle einer lokalen Paketierung wird unser Quellcode nativ auf Windows-, macOS- und Linux-Umgebungen in der Cloud kompiliert.

###### Herunterladen und Installieren
1. Navigieren Sie zum Abschnitt **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** dieses Repositories.
2. Laden Sie den neuesten automatisierten Build für Ihr Betriebssystem herunter:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

##### 🍎 macOS-Benutzer (Gatekeeper)
Da kein kostenpflichtiges Apple-Entwicklerzertifikat vorliegt, wird Gatekeeper die Binärdatei isolieren. Als Ingenieure wissen wir, dass der legitime Weg zur Umgehung darin besteht, mit der **rechten Maustaste auf die App zu klicken -> Öffnen**.

##### 🪟 Windows-Benutzer (SmartScreen)
Windows Defender zeigt beim Ausführen des `.exe`-Installationsprogramms möglicherweise eine blaue Warnung an. Klicken Sie auf **'Weitere Informationen'** und dann auf **'Trotzdem ausführen'**.

#### 🔌 3. Signalfluss & Setup

Eine professionelle Plattform muss absolute Transparenz über ihre Datenflüsse bieten. Die hybride Architektur des Ableton AI Assistant erfordert präzises Routing.

• **Remote Script (Python in Ableton):** Sie müssen den Ordner `AntigravityCore` in den Pfad für Remote-Skripte von Ableton Live ziehen. Dies injiziert unser Backend direkt in die Audio-Engine.
• **Low-Latency TCP Sockets:** Das Python-Skript öffnet lautlos den Port `9001`. Die Electron-Desktop-Anwendung verbindet sich bidirektional über IPC mit diesem Port.
• **LLM Tokens (API Keys):** Das System verschlüsselt und verarbeitet Ihren Claude API-Schlüssel lokal. Nur komplexe Schlussfolgerungen reisen in die Cloud, während das DSP lokal berechnet wird.

#### 💻 4. Operative Philosophie

Die Gestaltung von Schnittstellen erfordert den Respekt vor der visuellen Ergonomie. Abletons Dark-Mode-Prinzip wurde nachgezeichnet.

• **Hauptleinwand (Dashboard):** Ein Diagnosefeld, das den "Projektzustand" sofort aufdeckt.
• **Native Taktyle Steuerung:** Der zentrale Knob und die Schieberegler sind keine Mockups. Sie sind reaktive Regler, die millisekundengenau an den TCP-Port gebunden sind.
• **Asynchron:** Keine Verzögerungen. Der Haupt-Thread rendert die UI konstant mit 60fps, während der KI-Server die Spuren im Hintergrund analysiert.

#### ⚙️ 5. Parameter Masterclass

- **Adaptive algorithmische Kompression (Glue Compressor):** Die KI legt dynamisch eine langsame Attack-Zeit und ein ultraschnelles Release basierend auf dem BPM fest.
- **Phasen- und Maskierungskorrektur (EQ Eight):** Wir injizieren einen strikten Side (S)-Schnitt unter 120Hz. Dies verankert den Subbass in Mono und verhindert Phasenauslöschungen.
- **LLM Framework (MCP):** Die KI rät nicht; sie 'liest' den JSON-Payload des Spurenzustands, analysiert mathematisch und gibt den Ausführungsbefehl zurück.

#### 🌍 6. Globale Multimodale Integration

Wir haben ein strukturelles multimodales Paradigma codiert. Dies bedeutet 100% Unicode-Unterstützung und Hot-Reloading in 7 Sprachen (ES, EN, DE, UK, RU, ZH, JA).

#### 🛡️ 7. Abschirmarchitektur (Sicherheit)

Wir haben eine Schutzrüstung (Shielding) nach DevSecOps Best Practices entworfen:

• **Anti-Flood (Rate limiting):** Drosselung anomaler TCP-Anfragespitzen, um Zusammenbrüche des Thread-Pools zu vermeiden.
• **JSON Payload Validierung:** Überprüfung jedes eingehenden Frames, um böswilligen OS-Code zu blockieren.
• **RAM-Sanity (2 GB Limit):** Beschränkung extrem langer Modellantworten zur Vermeidung von OOM-Angriffen.

#### 📝 8. Debug-Protokoll (FAQ)

Q: **macOS Gatekeeper blockiert die App.**
A: Rechtsklick -> Öffnen. Wir bestätigen die Integrität.

Q: **TCP Deadlock / Keine Antwort von Ableton Live.**
A: A) Lokaler Port `9001` blockiert. B) Das `AntigravityCore`-Skript wurde in Ableton nicht zugewiesen.

#### ⚖️ 9. Engineering Manifesto, Credits & Lizenz

Konzipiert von produktes-code in unzertrennlicher Einheit mit Jesus Ferrer Garcia (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

---



### ![RU](https://flagcdn.com/h24/ru.png) Русский (RU)

#### 🎯 1. Видение (Введение)

Продвинутое сведение аудио часто является аналитическим узким местом. Мы разработали Ableton AI Assistant, чтобы решить эту проблему. Зачем крутить ручки вручную, если машина обладает хирургической точностью для расчета частотной маскировки? Этот инструмент — когнитивный инженер. Подключаясь в реальном времени через протокол MCP и TCP, ИИ Claude «слышит» состояние вашей консоли и выполняет решения по мастерингу.

> [!NOTE]
> Разработано **produktes-code** и **Jesús Ferrer (CHUS BZN)** для установления профессиональных стандартов.

#### 🚀 2. Техническое развертывание (Установка)

Для обеспечения стабильности мы используем **Automated CI/CD через GitHub Actions**.
Исходный код компилируется в облаке для Windows, macOS и Linux.

###### Как скачать и установить
1. Перейдите в раздел **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.
2. Скачайте последнюю версию:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

##### 🍎 Пользователи macOS (Gatekeeper)
**Правый клик по приложению -> Открыть**.

##### 🪟 Пользователи Windows (SmartScreen)
Нажмите **«Подробнее»**, затем **«Выполнить в любом случае»**.

#### 🔌 3. Маршрутизация сигналов

• **Remote Script (Python):** Переместите `AntigravityCore` в папку Remote Scripts в Ableton.
• **Low-Latency TCP:** Скрипт Python открывает порт `9001`. Приложение Electron подключается к этому порту по IPC.
• **LLM Tokens:** Ваш ключ API Claude шифруется локально.

#### 💻 4. Операционная философия

Эргономика для профессионалов. Принцип Dark-Mode.
• **Dashboard:** Панель диагностики состояния проекта.
• **Нативные контроллеры:** Слайдеры миллисекунда в миллисекунду привязаны к TCP-порту.
• **Асинхронность:** 60fps UI без зависань.

#### ⚙️ 5. Мастер-класс параметров

- **Адаптивный компрессор (Glue Compressor):** ИИ динамически устанавливает медленную атаку и сверхбыстрый релиз на основе BPM.
- **Удаление фазовых конфликтов (EQ Eight):** Мы делаем срез Side (S) ниже 120 Гц, оставляя саб-бас в моно.
- **LLM Framework (MCP):** ИИ математически анализирует JSON-данные ваших треков и возвращает порядок выполнения.

#### 🌍 6. Мультимодальная интеграция

100% поддержка Unicode и Hot-Reloading на 7 языках.

#### 🛡️ 7. Архитектура безопасности

• **Anti-Flood (Rate limiting):** Алгоритмы ограничивают аномальные скачки TCP-запросов.
• **JSON Payload Validation:** Удаление вредоносных структур.
• **RAM-Sanity (2 GB Limit):** Предотвращение OOM-атак.

#### 📝 8. Журнал отладки (FAQ)

В: **macOS Gatekeeper блокирует приложение.**
О: Правый клик -> Открыть.

В: **TCP Deadlock / Нет ответа.**
О: Порт `9001` заблокирован, или скрипт не назначен в настройках Ableton.

#### ⚖️ 9. Инженерный манифест и Лицензия

Создано produktes-code и Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

---



### ![JA](https://flagcdn.com/h24/jp.png) 日本語 (JA)

#### 🎯 1. ビジョン (概要)

高度なオーディオミキシングは、しばしば分析のボトルネックになります。機械が周波数マスキングを計算するための外科的な精度を持っているのに、なぜ手動でノブを動かさなければならないのでしょうか？このツールは革新的な認知エンジニアです。Model Context Protocol (MCP) とTCPアーキテクチャを通じてリアルタイムで接続し、Claude AIはコンソールの状態を「聴き」、マスタリングの決定を実行します。

> [!NOTE]
> **produktes-code** と **Jesús Ferrer (CHUS BZN)** によって開発されました。

#### 🚀 2. 技術的なデプロイ (インストール)

クロスプラットフォームの安定性を保証するため、**GitHub Actionsを介した自動CI/CD**を採用しています。
ソースコードは、クラウド内のWindows、macOS、Linux環境向けにコンパイルされています。

###### ダウンロードとインストール
1. このリポジトリの **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** セクションに移動します。
2. オペレーティングシステム用の最新ビルドをダウンロードします：
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

##### 🍎 macOSユーザー (Gatekeeper)
有料のApple開発者証明書がないため、Gatekeeperはバイナリをブロックします。正当なバイパス方法は、**アプリを右クリックして「開く」**を選択することです。

##### 🪟 Windowsユーザー (SmartScreen)
Windows Defenderが青い警告画面を表示する場合があります。**「詳細情報」**をクリックし、**「実行」**をクリックします。

#### 🔌 3. 信号フローとセットアップ

• **Remote Script (Python):** `AntigravityCore` フォルダをAbleton LiveのRemote Scriptsパスにドラッグする必要があります。
• **低遅延TCPソケット:** Pythonスクリプトはサイレントにポート `9001` を開きます。ElectronデスクトップアプリケーションはIPCを介してこのポートに接続します。
• **LLMトークン:** Claude APIキーはローカルで暗号化されます。

#### 💻 4. 操作哲学 (ユーザーガイド)

プロデューサー向けのインターフェース設計。ダークモードの原則。
• **メインキャンバス (Dashboard):** プロジェクトの「健康状態」を即座に表示します。
• **ネイティブな触覚コントロール:** スライダーはTCPポートにミリ秒単位でバインドされています。
• **非同期性:** メインスレッドはUIを60fpsでレンダリングします。

#### ⚙️ 5. パラメーターのマスタークラス (機能)

- **適応型アルゴリズム圧縮 (Glue Compressor):** AIは、セッションのBPMに基づいて、遅いアタック時間と超高速なリリースを動的に設定します。
- **マスキングと位相のクリア (EQ Eight):** 120Hz未満のSide (S)カットを注入し、サブベースをモノラルに固定します。
- **LLMフレームワーク (MCP):** AIはトラック状態のJSONデータを数学的に推論し、実行順序を返します。

#### 🌍 6. グローバルマルチモーダル統合

7言語（ES、EN、DE、UK、RU、ZH、JA）の100% Unicodeサポートとホットリロード。

#### 🛡️ 7. シールドアーキテクチャ (セキュリティ)

• **アンチフラッド (レート制限):** 異常なTCP要求スパイクを制限します。
• **JSONペイロードの検証:** 悪意のあるOSコードの挿入を防ぎます。
• **RAM制限 (2 GB Limit):** OOM攻撃を防ぎます。

#### 📝 8. デバッグログ (FAQ)

Q: **macOS Gatekeeperがアプリをブロックする。**
A: 右クリック -> 開く。

Q: **TCPデッドロック / Ableton Liveからの応答がない。**
A: A) ローカルポート `9001` がファイアウォールでブロックされている。B) `AntigravityCore` スクリプトが割り当てられていない。

#### ⚖️ 9. エンジニアリング宣言とライセンス

produktes-codeとJesus Ferrer (CHUS BZN) によって開発されました。CC BY-NC-SA 4.0。CORPORATE STANDARD。

---



### ![UK](https://flagcdn.com/h24/ua.png) Українська (UK)

#### 🎯 1. Бачення (Вступ)

Просунуте зведення аудіо часто є аналітичним вузьким місцем. Ми розробили Ableton AI Assistant, щоб вирішити цю проблему. Навіщо крутить ручки вручну, якщо машина має хірургічну точність для розрахунку частотного маскування? Цей інструмент — когнітивний інженер. Підключаючись в реальному часі через протокол MCP і TCP, ШІ Claude «чує» стан вашої консолі та виконує рішення з мастерингу.

> [!NOTE]
> Розроблено **produktes-code** та **Jesús Ferrer (CHUS BZN)** для встановлення професійних стандартів.

#### 🚀 2. Технічне розгортання (Встановлення)

Для забезпечення стабільності ми використовуємо **Automated CI/CD через GitHub Actions**.
Вихідний код компілюється в хмарі для Windows, macOS та Linux.

###### Як завантажити та встановити
1. Перейдіть до розділу **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.
2. Завантажте останню версію:
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

##### 🍎 Користувачі macOS (Gatekeeper)
**Правий клік по додатку -> Відкрити**.

##### 🪟 Користувачі Windows (SmartScreen)
Натисніть **«Докладніше»**, потім **«Виконати в будь-якому випадку»**.

#### 🔌 3. Маршрутизація сигналів

• **Remote Script (Python):** Перемістіть `AntigravityCore` у папку Remote Scripts в Ableton.
• **Low-Latency TCP:** Скрипт Python відкриває порт `9001`. Додаток Electron підключається до цього порту.
• **LLM Tokens:** Ваш ключ API Claude шифрується локально.

#### 💻 4. Операційна філософія

Ергономіка для професіоналів. Принцип Dark-Mode.
• **Dashboard:** Панель діагностики стану проєкту.
• **Нативні контролери:** Слайдери прив'язані до TCP-порту.
• **Асинхронність:** 60fps UI без зависань.

#### ⚙️ 5. Майстер-клас параметрів

- **Адаптивний компресор (Glue Compressor):** ШІ динамічно встановлює повільну атаку та надшвидкий реліз на основі BPM.
- **Видалення фазових конфліктів (EQ Eight):** Ми робимо зріз Side (S) нижче 120 Гц, залишаючи саб-бас у моно.
- **LLM Framework (MCP):** ШІ математично аналізує JSON-дані ваших треків.

#### 🌍 6. Мультимодальна інтеграція

100% підтримка Unicode та Hot-Reloading на 7 мовах.

#### 🛡️ 7. Архітектура безпеки (Shielding)

• **Anti-Flood (Rate limiting):** Алгоритми обмежують аномальні стрибки TCP-запитів.
• **JSON Payload Validation:** Видалення шкідливих структур.
• **RAM-Sanity (2 GB Limit):** Запобігання OOM-атакам.

#### 📝 8. Журнал налагодження (FAQ)

П: **macOS Gatekeeper блокує додаток.**
В: Правий клік -> Відкрити.

П: **TCP Deadlock / Немає відповіді.**
В: Порт `9001` заблоковано, або скрипт не призначено.

#### ⚖️ 9. Інженерний маніфест та Ліцензія

Створено produktes-code та Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

---



### ![ZH](https://flagcdn.com/h24/cn.png) 中文 (ZH)

#### 🎯 1. 愿景 (简介)

高级音频混音通常是一个分析瓶颈。我们开发了 Ableton AI Assistant，并对 DAW 范式提出了质疑：当机器具有计算频率掩蔽的外科手术般的精度时，为什么我们必须手动移动旋钮？这个工具是一个革命性的认知工程师。通过模型上下文协议 (MCP) 和 TCP 架构进行实时连接，Claude AI 可以“监听”控制台的状态并执行母带处理决策。

> [!NOTE]
> 由 **produktes-code** 和 **Jesús Ferrer (CHUS BZN)** 开发。

#### 🚀 2. 技术部署 (安装)

为了保证跨平台稳定性，我们使用 **通过 GitHub Actions 进行自动化 CI/CD**。
源代码在云中为 Windows、macOS 和 Linux 环境编译。

###### 下载和安装
1. 导航到此存储库的 **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** 部分。
2. 下载适用于您操作系统的最新版本：
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

##### 🍎 macOS 用户 (Gatekeeper)
**右键单击该应用程序 -> 打开**。

##### 🪟 Windows 用户 (SmartScreen)
单击 **“更多信息”**，然后单击 **“仍要运行”**。

#### 🔌 3. 信号流与设置

• **Remote Script (Python):** 将 `AntigravityCore` 文件夹拖到 Ableton Live 的 Remote Scripts 路径中。
• **低延迟 TCP 套接字:** Python 脚本打开端口 `9001`。Electron 桌面应用程序通过 IPC 连接到此端口。
• **LLM 令牌:** 您的 Claude API 密钥在本地加密。

#### 💻 4. 操作理念

制作人的界面设计。暗模式原则。
• **主画布 (Dashboard):** 诊断面板。
• **原生触觉控制:** 滑块毫秒级绑定到 TCP 端口。
• **异步:** 60fps UI，没有冻结。

#### ⚙️ 5. 参数大师班 (功能)

- **自适应算法压缩 (Glue Compressor):** AI 根据 BPM 动态设置慢速起音和超快速释放。
- **相位与掩蔽清除 (EQ Eight):** 注入低于 120Hz 的 Side (S) 削减。
- **LLM 框架 (MCP):** AI 从数学上推理轨道状态的 JSON 数据并返回执行顺序。

#### 🌍 6. 全球多模态集成

100% Unicode 支持和 7 种语言的热重载。

#### 🛡️ 7. 屏蔽架构 (安全性)

• **防洪 (速率限制):** 限制异常 TCP 请求。
• **JSON 负载验证:** 防止恶意操作系统代码注入。
• **RAM 限制 (2 GB Limit):** 防止 OOM 攻击。

#### 📝 8. 调试日志 (FAQ)

Q: **macOS Gatekeeper 阻止该应用程序。**
A: 右键单击 -> 打开。

Q: **TCP 死锁 / 无响应。**
A: A) 本地端口 `9001` 被防火墙阻止。B) 未分配 `AntigravityCore` 脚本。

#### ⚖️ 9. 工程宣言与许可证

由 produktes-code 和 Jesus Ferrer (CHUS BZN) 创建。CC BY-NC-SA 4.0。CORPORATE STANDARD。