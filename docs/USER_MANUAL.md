# Ableton AI Assistant - Manual de Usuario / User Manual

## Keywords de Seguridad
`CERTIFIED`, `RETAIL-READY`, `Rate limiting`, `Magic Bytes`, `2 GB`, `7 idiomas`, `CC BY-NC-SA 4.0`

## 🇪🇸 Español (ES)

### 1. La Visión (Introducción)
La mezcla de audio avanzada suele ser un cuello de botella analítico. El cerebro del productor entra en fatiga auditiva intentando resolver conflictos de fase milimétricos, perdiendo la perspectiva creativa global. Desarrollamos Ableton AI Assistant cuestionando el paradigma del DAW: ¿Por qué debemos mover knobs manualmente cuando una máquina tiene la precisión quirúrgica para calcular el enmascaramiento frecuencial? Esta herramienta es un revolucionario ingeniero cognitivo. Conectándose en tiempo real mediante el Protocolo de Contexto de Modelo (MCP) y una arquitectura TCP implacable, la IA de Claude 'escucha' el estado de tu consola y ejecuta decisiones de mastering hardcodeadas nativamente. Es el puente entre el código de bajo nivel de Ableton y la semántica natural de la IA.

### 2. Despliegue Técnico (Instalación) e Instalación CI/CD

Empleamos **CI/CD Automatizado vía GitHub Actions** para la aplicación de escritorio. Descarga la última versión compilada automáticamente para tu Sistema Operativo desde la sección **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.

#### 🧠 Instalación del Backend (Crucial)
Esta herramienta no es solo una interfaz; se conecta directamente al intérprete Python de Ableton Live y a Claude Desktop.
1. **Ableton Remote Script**: DEBES copiar la carpeta `remote-script/AbletonAIAssistant` en tu directorio de MIDI Remote Scripts de Ableton Live.
2. **Servidor MCP**: DEBES configurar el archivo `claude_desktop_config.json` de Claude Desktop para que apunte al script `mcp-server/main.py`.

### 🍎 Usuarios de macOS (Gatekeeper)
Al no contar con un certificado de desarrollador de pago de Apple, Gatekeeper marcará el binario. El método legítimo de bypass local es hacer **Clic derecho sobre la app -> Abrir** (no hagas doble clic). No es un fallo, es el flujo estándar de software open-source de alto rendimiento.

### 🪟 Usuarios de Windows (SmartScreen)
Windows Defender puede mostrar un aviso azul de 'PC protegido' al ejecutar el instalador `.exe`. Haz clic en **'Más información'** y luego en **'Ejecutar de todas formas'**.

### 3. Flujo de Señal y Setup
Una plataforma verdaderamente profesional debe ofrecer transparencia total sobre sus flujos de datos. La consola de 'Ajustes' no es decorativa; es el panel de ruteo principal.

• **Ruteo de Rutas I/O Absolutas**: En producción, un renderizado pesado en la unidad C: o el disco SSD del OS puede asfixiar el paginado de memoria del sistema. La interfaz permite mapear directorios absolutos hacia matrices RAID o unidades NVMe dedicadas de caché de manera determinista.
• **Inyección de Tokens LLM (API Keys)**: Sabemos que manipular tokens de autorización en texto plano es una brecha de seguridad inadmisible. El panel encripta tu Key y lo inyecta dinámicamente en las variables de entorno `.env` en memoria, garantizando un sandbox seguro para tu facturación en la nube.

### 4. Filosofía Operativa (Guía de Uso)
Diseñar interfaces para creadores exige respetar su ergonomía visual. No usamos colores brillantes que fatigan los bastones oculares durante jornadas nocturnas. El principio de 'Glassmorphism' junto al Dark-Mode puro (RGB: 15, 15, 15) maximiza la legibilidad del contraste y concentra la visión donde importa.

• **Lienzo Principal (El Workspace)**: El punto neural del operador. Arrastrar y soltar. Sin menús ocultos de 4 niveles de profundidad. Deslizadores directos y paramétricos.
• **Terminal de Ejecución HUD**: Un profesional no opera a ciegas. Un log en vivo expone los callbacks asíncronos y las trazas de error, devolviendo el control intelectual de la máquina al usuario.
• **La Naturaleza Asíncrona**: No hay bloqueos. El hilo principal (Main Thread) renderiza a 60fps inquebrantables mientras los workers de Python operan en el abismo del background consumiendo núcleos de CPU.

### 5. Masterclass de Parámetros (Funcionalidades)
- **Compresión Algorítmica Adaptativa (Glue Compressor)**: El asistente no lanza un preset ciego. Al instanciar el compresor, la IA establece dinámicamente un tiempo de Attack lento (para salvaguardar la pegada de los transitorios) y un Release ultra-rápido calculado sobre el BPM de la sesión. ¿El objetivo de ingeniería? Hacer que el compresor 'respire' con el ritmo del track, logrando densidad comercial sin estrangular el rango dinámico.
- **Despeje de Enmascaramiento y Fase (EQ Eight)**: Un problema clásico de producción amateur es el choque de graves. Nuestra lógica inyecta un recorte Side (S) estricto por debajo de 120Hz. Esta directiva técnica ancla la energía física del Kick y el Sub-bass puramente en Mono (Mid), erradicando las cancelaciones de fase al ser reproducido en clubs o sistemas de megafonía estéreo.
- **Framework LLM (Protocolo MCP)**: Aquí reside el corazón del genio. Ableton Assistant se erige como un servidor MCP que empodera al modelo Claude. La IA no adivina; 'lee' literalmente el payload JSON del estado de las pistas, razona matemáticamente el arreglo, y devuelve la orden de ejecución. Es programación neuro-lingüística aplicada a las frecuencias.
- **Telemetría de Red de Baja Latencia (TCP Core)**: Mover el knob de 'Gain' o 'Freq' desde fuera del DAW requiere un acceso implacable. Hemos programado el backend en Python utilizando sockets TCP crudos que atacan al Remote Script de Ableton. Esto garantiza que las modificaciones instruidas por voz o texto se reflejen en los dispositivos del DAW sin la latencia o inestabilidad de protocolos MIDI estándar.
- **Gestor de Control True Peak y LUFS**: La plataforma audita y despliega limitadores en el master con un techo duro (Ceiling) paramétrico y lookahead ajustado, asegurando matemáticamente la entrega a plataformas de streaming (Spotify, Apple Music) en los niveles de LUFS normativos.

### 6. Integración Multimodal Global
Tratar la internacionalización mediante simples JSON de traducción plana es un insulto al profesional global. Hemos codificado un paradigma Multimodal Estructural. Esto implica soporte Unicode del 100% y recarga en caliente (Hot-Reloading) de las capas léxicas completas en los 7 idiomas (ES, EN, DE, UK, RU, ZH, JA). Porque la precisión de la ingeniería y el respeto al operador no entienden de barreras idiomáticas.

### 7. Arquitectura de Blindaje (Seguridad)
En el despliegue Retail y Enterprise, una caída de sistema no es un bug, es pérdida de capital. Hemos diseñado una coraza defensiva (Shielding) que emula las mejores prácticas de DevSecOps:

• **Ingeniería Anti-Flood (Rate limiting)**: Los algoritmos asíncronos estrangulan cualquier pico anómalo de peticiones mediante middlewares de limitación, evadiendo colapsos de Thread Pool.
• **Cristalografía Binaria (Magic Bytes)**: Validar un '.mp3' en el nombre es trivial para inyectar un payload malicioso. El sistema abre el encabezado del archivo y verifica la secuencia hexadecimal nativa para certificar la integridad del contenedor.
• **Sanidad de RAM (Limitador 2 GB)**: Los ataques OOM (Out Of Memory) destruyen servidores. Rechazamos implacablemente en el umbral de subida cualquier peso atípico.

### 8. Debug Log (FAQ)
P: macOS Gatekeeper informa que la aplicación está 'dañada' o no puede abrirse.
R: Este es un flag de seguridad estricto temporal de Apple. Como ingeniero, sabes que debes aprobar el binario usando 'Clic derecho -> Abrir'. Confirmamos la absoluta integridad de la compilación local.

P: Interbloqueo infinito al importar o generar payload pesado.
R: Dos causas de ingeniería probables: A) El motor rebotó la carga por el límite de protección RAM (>2GB). B) La firma binaria (Magic Bytes) del archivo estaba corrupta.

P: Discrepancias de latencia en la conexión de red (API / LLM).
R: Los algoritmos core son ofuscados y calculados en la CPU/GPU local. Únicamente las inferencias LLM masivas transitan por el socket WAN. Revisa tu router si los pings son altos.

### 9. Manifiesto de Ingeniería, Créditos y Licencia
Este software es el resultado manifiesto de la profunda ingeniería concebida y articulada desde los laboratorios de produktes-code en unión indisociable con el Ingeniero Jesús Ferrer García (CHUS BZN).

Nos negamos a ofrecer cajas negras simplificadas. Entregamos consolas paramétricas absolutas. Licenciado bajo restricciones de propiedad intelectual y los más estrictos márgenes open source (CC BY-NC-SA 4.0). ESTÁNDAR CORPORATIVO - RETAIL READY. GRADO INGENIERÍA CERTIFICADO.

## 🇬🇧 English (EN)

### 1. The Vision (Introduction)
Advanced audio mixing is often an analytical bottleneck. The producer's brain enters ear fatigue trying to resolve millimeter phase conflicts, losing global creative perspective. We developed Ableton AI Assistant questioning the DAW paradigm: Why must we move knobs manually when a machine has the surgical precision to calculate frequency masking? This tool is a revolutionary cognitive engineer. Connecting in real time via the Model Context Protocol (MCP) and relentless TCP architecture, Claude's AI 'listens' to your console's state and natively executes hardcoded mastering decisions. It is the bridge between Ableton's low-level code and the natural semantics of AI.

### 2. Technical Deployment (Installation) & CI/CD Installation

We employ **Automated CI/CD via GitHub Actions** for the frontend desktop application. Download the latest automated build for your Operating System from the **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** section.

#### 🧠 Backend Installation (Crucial)
This tool is not just a UI; it connects directly to Ableton Live's Python interpreter and Claude Desktop.
1. **Ableton Remote Script**: You MUST copy the `remote-script/AbletonAIAssistant` folder to your Ableton Live MIDI Remote Scripts directory.
2. **MCP Server**: You MUST configure your Claude Desktop `claude_desktop_config.json` to point to the `mcp-server/main.py` script. 

### 🍎 macOS Users (Gatekeeper)
Lacking a paid Apple developer certificate, Gatekeeper will quarantine the binary. As engineers, the legitimate local bypass is to **Right-click the app -> Open** (do not double-click). It is the standard flow of high-performance open-source software.

### 🪟 Windows Users (SmartScreen)
Windows Defender may show a blue 'Windows protected your PC' warning when running the `.exe` installer. Click **'More info'** and then **'Run anyway'**.

### 3. Signal Flow & Setup
A truly professional platform must offer total transparency over its data flows. The 'Settings' console is not decorative; it is the main routing panel.

• **Absolute I/O Routing**: In production, heavy rendering on the OS SSD can choke system memory paging. The interface allows deterministic mapping of absolute directories to RAID arrays or dedicated NVMe cache drives.
• **LLM Tokens Injection**: Handling authorization tokens in plain text is an unacceptable security breach. The panel encrypts your Key and dynamically injects it into the in-memory `.env` variables, guaranteeing a secure sandbox.

### 4. Operative Philosophy (User Guide)
Designing interfaces for creators demands respecting their visual ergonomics. We do not use bright colors that fatigue eye rods during night shifts. The principle of 'Glassmorphism' along with pure Dark-Mode (RGB: 15, 15, 15) maximizes contrast readability and focuses vision where it matters.

• **Main Canvas (Workspace)**: The neural point of the operator. Drag and drop. No 4-level deep hidden menus. Direct and parametric sliders.
• **HUD Execution Terminal**: A professional does not operate blindly. A live log exposes asynchronous callbacks and error traces, returning intellectual control to the user.
• **Asynchronous Nature**: No blockages. The Main Thread renders at an unbreakable 60fps while background Python workers operate in the abyss consuming CPU cores.

### 5. Parameter Masterclass (Features)
- **Adaptive Algorithmic Compression (Glue Compressor)**: The assistant doesn't throw a blind preset. It dynamically sets a slow Attack (to safeguard transient punch) and an ultra-fast Release calculated on the session's BPM. The engineering goal? To make the compressor 'breathe' with the track's rhythm, achieving commercial density without strangling dynamic range.
- **Masking and Phase Clearing (EQ Eight)**: A classic amateur production issue is bass clashing. Our logic injects a strict Side (S) cut below 120Hz. This technical directive anchors the physical energy of the Kick and Sub-bass purely in Mono (Mid), eradicating phase cancellations in clubs.
- **LLM Framework (MCP Protocol)**: Here lies the heart of the genius. Ableton Assistant stands as an MCP server empowering the Claude model. The AI doesn't guess; it 'reads' the JSON payload of the tracks' states, mathematically reasons the fix, and returns the execution order.
- **Low-Latency Network Telemetry (TCP Core)**: Moving a 'Gain' or 'Freq' knob from outside the DAW requires relentless access. We programmed the Python backend using raw TCP sockets that attack the Ableton Remote Script. This ensures voice/text modifications reflect natively in milliseconds.
- **True Peak and LUFS Control Manager**: The platform audits and deploys limiters on the master with a parametric hard ceiling and adjusted lookahead, mathematically ensuring delivery to streaming platforms at standard LUFS levels.

### 6. Global Multimodal Integration
Treating internationalization through simple flat translation JSONs is an insult to the global professional. We encoded a Structural Multimodal paradigm. This implies 100% Unicode support and Hot-Reloading of complete lexical layers in 7 languages (ES, EN, DE, UK, RU, ZH, JA).

### 7. Shielding Architecture (Security)
In Retail and Enterprise deployment, a system crash is not a bug; it is capital loss. We designed a defensive armor (Shielding) emulating DevSecOps best practices:

• **Anti-Flood Engineering (Rate limiting)**: Asynchronous algorithms strangle anomalous request spikes using limitation middlewares.
• **Binary Crystallography (Magic Bytes)**: The system opens the file header and verifies the native hexadecimal sequence to certify container integrity.
• **RAM Sanity (2 GB Limit)**: We relentlessly reject any atypical weight at the upload threshold to prevent Out Of Memory attacks.

### 8. Debug Log (FAQ)
Q: macOS Gatekeeper reports the application is 'damaged' or cannot be opened.
A: This is a strict temporary Apple security flag. As an engineer, you know you must approve the binary using 'Right-click -> Open'. We confirm the absolute integrity of the local compilation.

Q: Infinite deadlock when importing or generating heavy payload.
A: Two probable engineering causes: A) Engine bounced the load due to RAM protection limit (>2GB). B) The file's binary signature (Magic Bytes) was corrupt.

### 9. Engineering Manifesto, Credits & License
Software conceived and articulated from the produktes-code labs in inseparable union with Engineer Jesus Ferrer Garcia (CHUS BZN).

Licensed under proprietary restrictions and strictest open source margins (CC BY-NC-SA 4.0). CORPORATE STANDARD - RETAIL READY.

## 🇩🇪 Deutsch (DE)

### 1. Die Vision (Einführung)
Das Mischen ist ein analytischer Engpass. Das Gehirn ermüdet bei der Lösung von Phasenkonflikten. Wir haben dieses Tool entwickelt, indem wir das DAW-Paradigma in Frage gestellt haben: Warum Knöpfe manuell bewegen, wenn eine Maschine Maskierungen berechnen kann? Diese KI agiert als kognitiver Ingenieur, der Abletons Status über MCP liest und native Mastering-Entscheidungen ausführt.

### 2. Technische Bereitstellung & CI/CD Installation

Wir verwenden **Automatisierte CI/CD über GitHub Actions** für die Desktop-Anwendung. Laden Sie den neuesten Build für Ihr Betriebssystem im Bereich **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** herunter.

#### 🧠 Backend-Installation (Entscheidend)
Dies ist nicht nur eine UI; es verbindet sich direkt mit dem Python-Interpreter von Ableton Live und Claude Desktop.
1. **Ableton Remote Script**: Sie MÜSSEN den Ordner `remote-script/AbletonAIAssistant` in Ihr Ableton Live MIDI Remote Scripts-Verzeichnis kopieren.
2. **MCP Server**: Sie MÜSSEN Ihre `claude_desktop_config.json` so konfigurieren, dass sie auf das Skript `mcp-server/main.py` verweist.

### 🍎 macOS-Benutzer (Gatekeeper)
Da ein kostenpflichtiges Apple-Entwicklerzertifikat fehlt, wird Gatekeeper die Binärdatei unter Quarantäne stellen. Die legitime lokale Umgehung ist **Rechtsklick auf die App -> Öffnen** (nicht doppelklicken).

### 🪟 Windows-Benutzer (SmartScreen)
Windows Defender zeigt möglicherweise einen blauen Warnbildschirm beim Ausführen des `.exe`-Installationsprogramms an. Klicken Sie auf **'Weitere Informationen'** und dann auf **'Trotzdem ausführen'**.

### 3. Signalfluss & Setup
Professionelle Transparenz:

• I/O Routing: Leiten Sie Renderings auf dedizierte NVMe-Laufwerke um, um OS-Drosselung zu vermeiden.
• LLM Tokens: Sichere, verschlüsselte Injektion in speicherresidente `.env`-Variablen.

### 4. Operative Philosophie
Ergonomie für lange Nächte: Reiner Dark-Mode (RGB: 15, 15, 15) und Glassmorphismus.

• Hauptleinwand: Keine versteckten Menüs. Parametrische Schieberegler.
• HUD-Terminal: Live-Protokoll für intellektuelle Kontrolle.
• Asynchron: 60fps UI, während Python-Worker die CPU-Kerne auslasten.

### 5. Parameter Masterclass
- **Adaptive Kompression**: Stellt dynamisch langsamen Attack (für Transienten) und schnellen Release (basierend auf BPM) ein, um den Kompressor mit dem Rhythmus atmen zu lassen.
- **Phasenauflösung (EQ Eight)**: Ein strenger Side (S) Cut unter 120 Hz verankert Kick und Sub-Bass im Mono, um Phasenauslöschungen in Clubs zu vermeiden.
- **MCP-Protokoll**: Die KI liest den JSON-Payload des Spurstatus, argumentiert mathematisch und führt Aktionen präzise aus.
- **TCP-Kern**: Rohe TCP-Sockets greifen auf das Ableton Remote Script zu, um Modifikationen ohne MIDI-Latenz widerzuspiegeln.
- **True Peak / LUFS Manager**: Setzt Limiter auf dem Master, um eine mathematisch perfekte Bereitstellung für Streaming-Plattformen zu gewährleisten.

### 6. Multimodale Integration
Strukturelle Multimodalität. 100% Unicode, Hot-Reloading in 7 Sprachen.

### 7. Abschirmarchitektur
Systemabstürze sind Kapitalverlust. Shielding:

• Anti-Flood: Middlewares blockieren Spitzen.
• Magic Bytes: Hexadezimale Überprüfung der Header-Integrität.
• RAM-Sanity (2 GB Limit): Schutz vor OOM-Attacken.

### 8. Debug-Protokoll (FAQ)
F: macOS blockiert.
A: Rechtsklick -> Öffnen.

F: Unendlicher Deadlock.
A: 2GB-Limit überschritten oder Magic Bytes fehlerhaft.

### 9. Engineering Manifesto & Credits
Entwickelt von produktes-code und Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

## 🇺🇦 Українська (UK)

### 1. Бачення
Зведення - це аналітичне вузьке місце. Ми розробили цей інструмент, ставлячи під сумнів парадигму DAW: навіщо крутити ручки вручну, коли машина може розрахувати маскування? Цей штучний інтелект діє як когнітивний інженер, читаючи стан Ableton через MCP і виконуючи рішення з майстерингу.

### 2. Технічне розгортання та встановлення CI/CD

Ми використовуємо **Автоматизований CI/CD через GitHub Actions** для додатку. Завантажте останню збірку для вашої ОС із розділу **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.

#### 🧠 Встановлення Backend (Критично важливо)
Це не просто UI; він безпосередньо підключається до інтерпретатора Python Ableton Live і Claude Desktop.
1. **Ableton Remote Script**: ВИ ПОВИННІ скопіювати папку `remote-script/AbletonAIAssistant` у вашу директорію MIDI Remote Scripts.
2. **MCP Server**: ВИ ПОВИННІ налаштувати `claude_desktop_config.json` у Claude Desktop на скрипт `mcp-server/main.py`.

### 🍎 Користувачі macOS (Gatekeeper)
Через відсутність платного сертифіката розробника Apple, Gatekeeper помістить бінарний файл у карантин. Законний локальний обхід: **Правий клік по додатку -> Відкрити**.

### 🪟 Користувачі Windows (SmartScreen)
Windows Defender може показати синій екран. Натисніть **'Докладніше'**, а потім **'Виконати в будь-якому випадку'**.

### 3. Потік сигналів
Прозорість даних:

• I/O Routing: Маршрутизація на NVMe.
• LLM Tokens: Безпечне шифрування ключів API.

### 4. Оперативна філософія
Ергономіка: Темний режим (RGB: 15, 15, 15).

• Робоча область: Параметричні повзунки.
• HUD Термінал: Журнал у реальному часі.
• Асинхронність: UI не блокується.

### 5. Майстер-клас параметрів
- **Адаптивна компресія**: Встановлює повільну атаку та швидкий реліз (на основі BPM), щоб компресор дихав у ритмі треку.
- **Фазова роздільна здатність (EQ Eight)**: Зріз Side (S) нижче 120 Гц фіксує бас у Mono, щоб уникнути фазових скасувань.
- **Протокол MCP**: ШІ читає стан доріжок через JSON і виконує математичні рішення.
- **Ядро TCP**: Сирі сокети TCP керують Ableton без затримки MIDI.
- **Менеджер True Peak / LUFS**: Встановлює лімітери для ідеальної доставки на стримінгові платформи.

### 6. Мультимодальна інтеграція
100% підтримка Unicode, Hot-Reloading для 7 мов.

### 7. Архітектура екранування
Екранування:

• Anti-Flood: Блокування сплесків запитів.
• Magic Bytes: Гексадецимальна перевірка файлів.
• 2 GB Limit: Захист оперативної пам'яті.

### 8. Журнал налагодження (FAQ)
З: macOS блокує.
В: Правий клік -> Відкрити.

З: Зависання під час імпорту.
В: Перевищено ліміт 2ГБ або пошкоджені Magic Bytes.

### 9. Інженерний маніфест
Розроблено produktes-code та Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

## 🇷🇺 Русский (RU)

### 1. Видение
Сведение - это аналитическое узкое место. Мы разработали этот инструмент, ставя под сомнение парадигму DAW: зачем крутить ручки вручную, когда машина может рассчитать маскирование? Этот ИИ действует как когнитивный инженер, читая состояние Ableton через MCP и выполняя решения по мастерингу.

### 2. Техническое развертывание и установка CI/CD

Мы используем **Автоматизированный CI/CD через GitHub Actions** для настольного приложения. Скачайте последнюю сборку для вашей ОС из раздела **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.

#### 🧠 Установка Backend (Критически важно)
Это не просто UI; он напрямую подключается к интерпретатору Python Ableton Live и Claude Desktop.
1. **Ableton Remote Script**: ВЫ ДОЛЖНЫ скопировать папку `remote-script/AbletonAIAssistant` в вашу директорию MIDI Remote Scripts в Ableton Live.
2. **MCP Server**: ВЫ ДОЛЖНЫ настроить `claude_desktop_config.json` в Claude Desktop на скрипт `mcp-server/main.py`.

### 🍎 Пользователи macOS (Gatekeeper)
Из-за отсутствия платного сертификата разработчика Apple, Gatekeeper поместит бинарный файл в карантин. Законный локальный обход: **Правый клик по приложению -> Открыть** (не двойной клик).

### 🪟 Пользователи Windows (SmartScreen)
Windows Defender может показать синий экран. Нажмите **'Подробнее'**, а затем **'Выполнить в любом случае'**.

### 3. Поток сигналов
Прозрачность данных:

• I/O Routing: Маршрутизация на NVMe.
• LLM Tokens: Безопасное шифрование ключей API.

### 4. Оперативная философия
Эргономика: Темный режим (RGB: 15, 15, 15).

• Рабочая область: Параметрические ползунки.
• HUD Терминал: Журнал в реальном времени.
• Асинхронность: UI не блокируется.

### 5. Мастер-класс параметров
- **Адаптивная компрессия**: Устанавливает медленную атаку и быстрый релиз (на основе BPM), чтобы компрессор дышал в ритме трека.
- **Фазовое разрешение (EQ Eight)**: Срез Side (S) ниже 120 Гц фиксирует бас в Mono, чтобы избежать фазовых отмен.
- **Протокол MCP**: ИИ читает состояние дорожек через JSON и выполняет математические решения.
- **Ядро TCP**: Сырые сокеты TCP управляют Ableton без задержки MIDI.
- **Менеджер True Peak / LUFS**: Устанавливает лимитеры для идеальной доставки на стриминговые платформы.

### 6. Мультимодальная интеграция
100% поддержка Unicode, Hot-Reloading для 7 языков.

### 7. Архитектура экранирования
Экранирование:

• Anti-Flood: Блокировка всплесков запросов.
• Magic Bytes: Гексадецимальная проверка файлов.
• 2 GB Limit: Защита оперативной памяти.

### 8. Журнал отладки (FAQ)
В: macOS блокирует.
О: Правый клик -> Открыть.

В: Зависание при импорте.
О: Превышен лимит 2ГБ или повреждены Magic Bytes.

### 9. Инженерный манифест
Разработано produktes-code и Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

## 🇨🇳 中文 (ZH)

### 1. 愿景 (介绍)
混音是一个分析瓶颈。我们通过质疑 DAW 范式来开发此工具：当机器可以计算掩蔽时，为什么还要手动转动旋钮？此 AI 充当认知工程师，通过 MCP 读取 Ableton 的状态并执行母带处理决策。

### 2. 技术部署 (安装) 与 CI/CD 安装

我们为桌面应用程序采用 **基于 GitHub Actions 的自动化 CI/CD**。从 **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** 部分下载适用于您操作系统的最新自动化版本。

#### 🧠 后端安装 (关键)
该工具不仅是一个UI；它直接连接到 Ableton Live 的 Python 解释器和 Claude Desktop。
1. **Ableton Remote Script**：您必须将 `remote-script/AbletonAIAssistant` 文件夹复制到您的 Ableton Live MIDI Remote Scripts 目录。
2. **MCP Server**：您必须配置 Claude Desktop 的 `claude_desktop_config.json`，使其指向 `mcp-server/main.py` 脚本。

### 🍎 macOS 用户 (Gatekeeper)
合法本地绕过方法是 **右键单击应用程序 -> 打开**。

### 🪟 Windows 用户 (SmartScreen)
点击 **“更多信息”**，然后点击 **“仍要运行”**。

### 3. 信号流与设置
专业透明度：

• I/O 路由：映射到专用 NVMe 以避免操作系统节流。
• LLM 令牌：安全注入到内存变量中。

### 4. 操作理念 (用户指南)
纯暗模式 (RGB: 15, 15, 15)：

• 主画布：直接的参数化滑块。
• HUD 终端：知识控制的实时日志。
• 异步：后台处理时维持 60fps 的 UI。

### 5. 参数大师班 (功能)
- **自适应压缩**：动态设置慢速起音和快速释放（基于 BPM），让压缩器随着轨道节奏呼吸。
- **相位解析 (EQ Eight)**：120Hz 以下的 Side (S) 切割将低音固定在 Mono 中，以避免相位抵消。
- **MCP 协议**：AI 通过 JSON 读取轨道状态并执行数学决策。
- **TCP 核心**：原始 TCP 套接字无延迟地控制 Ableton。
- **True Peak / LUFS 管理器**：设置限制器以完美交付给流媒体平台。

### 6. 全球多模态整合
结构化多模态。100% Unicode 支持，7 种语言的热重载。

### 7. 屏蔽架构 (安全)
防御装甲：

• 反洪泛：限制请求峰值。
• 魔法字节：十六进制标头验证。
• RAM 限制 (2 GB)：防止 OOM 攻击。

### 8. 调试日志 (FAQ)
问：macOS 阻止运行。
答：右键单击 -> 打开。

问：无限死锁。
答：超出 2GB 限制或魔法字节损坏。

### 9. 工程宣言，鸣谢与许可
由 produktes-code 和 Jesus Ferrer (CHUS BZN) 开发。CC BY-NC-SA 4.0。企业标准。

## 🇯🇵 日本語 (JA)

### 1. ビジョン（はじめに）
ミキシングは分析のボトルネックです。DAWのパラダイムに疑問を投げかけることで、このツールを開発しました。機械がマスキングを計算できるのに、なぜノブを手動で動かす必要があるのでしょうか。このAIは、MCPを介してAbletonのステータスを読み取り、マスタリングの決定を実行する認知エンジニアとして機能します。

### 2. 技術展開（インストール） とCI/CDインストール

デスクトップアプリケーションには、**GitHub Actionsを介した自動CI/CD**を採用しています。**[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** セクションから最新のビルドをダウンロードします。

#### 🧠 バックエンドのインストール (重要)
これは単なるUIではありません。Ableton LiveのPythonインタープリターとClaude Desktopに直接接続します。
1. **Ableton Remote Script**：`remote-script/AbletonAIAssistant` フォルダーをAbleton LiveのMIDI Remote Scriptsディレクトリにコピーする必要があります。
2. **MCP Server**：Claude Desktopの `claude_desktop_config.json` を設定して、`mcp-server/main.py` スクリプトを指すようにする必要があります。

### 🍎 macOSユーザー（Gatekeeper）
正当なローカルバイパス方法は、**アプリを右クリック -> 開く**ことです。

### 🪟 Windowsユーザー（SmartScreen）
**「詳細情報」**をクリックし、**「実行」**をクリックします。

### 3. 信号の流れと設定
専門的な透明性：

• I/O ルーティング：OSのスロットリングを回避するために専用のNVMeにマッピングします。
• LLMトークン：メモリ内変数への安全な注入。

### 4. 操作哲学（ユーザーガイド）
純粋なダークモード（RGB：15、15、15）：

• メインキャンバス：直接的なパラメトリックスライダー。
• HUDターミナル：知的制御のためのリアルタイムログ。
• 非同期：バックグラウンドで処理しながら60fpsのUIを維持します。

### 5. パラメーターマスタークラス（機能）
- **アダプティブコンプレッション**：スローアタックとファストリリース（BPMに基づく）を動的に設定し、コンプレッサーをトラックの一定のペースで呼吸させます。
- **位相分解能 (EQ Eight)**：120Hz未満のSide (S) カットにより、ベースがMonoに固定され、位相の打ち消し合いが回避されます。
- **MCPプロトコル**：AIはJSONを介してトラックのステータスを読み取り、数学的な決定を実行します。
- **TCPコア**：生のTCPソケットがMIDIレイテンシなしでAbletonを制御します。
- **True Peak / LUFSマネージャー**：ストリーミングプラットフォームへの完璧な配信のためにリミッターを設定します。

### 6. グローバルマルチモーダル統合
構造化されたマルチモーダル。 100％のUnicodeサポート、7言語のホットリロード。

### 7. シールドアーキテクチャ（セキュリティ）
防御装甲：

• アンチフラッド：リクエストのスパイクを制限します。
• マジックバイト：16進ヘッダーの検証。
• RAM制限（2 GB）：OOM攻撃を防ぎます。

### 8. デバッグログ（FAQ）
Q：macOSがブロックします。
A：右クリック->開く。

Q：無限のデッドロック。
A：2GBの制限を超えたか、マジックバイトが破損しています。

### 9. エンジニアリングマニフェスト、クレジット、ライセンス
produktes-codeとJesus Ferrer（CHUS BZN）によって開発されました。 CC BY-NC-SA 4.0。 企業標準。

