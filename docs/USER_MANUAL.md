<div class="header-container">
  <img src="icon.png" width="200" height="200" style="border-radius: 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.15);" alt="Ableton AI Assistant Logo" />
  <h1>Ableton AI Assistant V1.0.0</h1>
  <h2>Official User Manual / Manual de Usuario Maestro</h2>
</div>

<p align="center">
  <img src="screenshot-UI.png" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.6);" alt="Ableton AI Assistant Console" />
</p>

<div class="page-break"></div>
### 🇪🇸 Español (ES)

## 🎯 La Visión (Introducción)

La mezcla de audio avanzada suele ser un cuello de botella analítico. El cerebro del productor entra en fatiga auditiva intentando resolver conflictos de fase milimétricos, perdiendo la perspectiva creativa global. Desarrollamos Ableton AI Assistant cuestionando el paradigma del DAW: ¿Por qué debemos mover knobs manualmente cuando una máquina tiene la precisión quirúrgica para calcular el enmascaramiento frecuencial? Esta herramienta es un revolucionario ingeniero cognitivo. Conectándose en tiempo real mediante el Protocolo de Contexto de Modelo (MCP) y una arquitectura TCP implacable, la IA de Claude 'escucha' el estado de tu consola y ejecuta decisiones de mastering hardcodeadas nativamente. Es el puente entre el código de bajo nivel de Ableton y la semántica natural de la IA.

> [!NOTE]
> Desarrollado por **produktes-code** y **Jesús Ferrer (CHUS BZN)** para establecer estándares profesionales en la ingeniería comercial.

---

## 📸 Interface / Ergonomics

![Desktop Interface](screenshot-UI.png)


---

## ⚙️ Masterclass de Parámetros (Funcionalidades)

- **Compresión Algorítmica Adaptativa (Glue Compressor)**: El asistente no lanza un preset ciego. Al instanciar el compresor, la IA establece dinámicamente un tiempo de Attack lento (para salvaguardar la pegada de los transitorios) y un Release ultra-rápido calculado sobre el BPM de la sesión. ¿El objetivo de ingeniería? Hacer que el compresor 'respire' con el ritmo del track, logrando densidad comercial sin estrangular el rango dinámico.
- **Despeje de Enmascaramiento y Fase (EQ Eight)**: Un problema clásico de producción amateur es el choque de graves. Nuestra lógica inyecta un recorte Side (S) estricto por debajo de 120Hz. Esta directiva técnica ancla la energía física del Kick y el Sub-bass puramente en Mono (Mid), erradicando las cancelaciones de fase al ser reproducido en clubs o sistemas de megafonía estéreo.
- **Framework LLM (Protocolo MCP)**: Aquí reside el corazón del genio. Ableton Assistant se erige como un servidor MCP que empodera al modelo Claude. La IA no adivina; 'lee' literalmente el payload JSON del estado de las pistas, razona matemáticamente el arreglo, y devuelve la orden de ejecución. Es programación neuro-lingüística aplicada a las frecuencias.
- **Telemetría de Red de Baja Latencia (TCP Core)**: Mover el knob de 'Gain' o 'Freq' desde fuera del DAW requiere un acceso implacable. Hemos programado el backend en Python utilizando sockets TCP crudos que atacan al Remote Script de Ableton. Esto garantiza que las modificaciones instruidas por voz o texto se reflejen en los dispositivos del DAW sin la latencia o inestabilidad de protocolos MIDI estándar.
- **Gestor de Control True Peak y LUFS**: La plataforma audita y despliega limitadores en el master con un techo duro (Ceiling) paramétrico y lookahead ajustado, asegurando matemáticamente la entrega a plataformas de streaming (Spotify, Apple Music) en los niveles de LUFS normativos.

---

## 🛡️ Arquitectura de Blindaje (Seguridad)

En el despliegue Retail y Enterprise, una caída de sistema no es un bug, es pérdida de capital. Hemos diseñado una coraza defensiva (Shielding) que emula las mejores prácticas de DevSecOps:

• **Ingeniería Anti-Flood (Rate limiting)**: Los algoritmos asíncronos estrangulan cualquier pico anómalo de peticiones mediante middlewares de limitación, evadiendo colapsos de Thread Pool.
• **Cristalografía Binaria (Magic Bytes)**: Validar un '.mp3' en el nombre es trivial para inyectar un payload malicioso. El sistema abre el encabezado del archivo y verifica la secuencia hexadecimal nativa para certificar la integridad del contenedor.
• **Sanidad de RAM (Limitador 2 GB)**: Los ataques OOM (Out Of Memory) destruyen servidores. Rechazamos implacablemente en el umbral de subida cualquier peso atípico.

---

### 🚀 Despliegue Técnico e Instalación CI/CD

Empleamos **CI/CD Automatizado vía GitHub Actions** para la aplicación de escritorio. Descarga la última versión compilada automáticamente para tu Sistema Operativo desde la sección **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.

#### 🧠 Instalación del Backend (Crucial)
Esta herramienta no es solo una interfaz; se conecta directamente al intérprete Python de Ableton Live y a Claude Desktop.
1. **Ableton Remote Script**: DEBES copiar la carpeta `remote-script/AntigravityCore` en tu directorio de MIDI Remote Scripts de Ableton Live.
2. **Servidor MCP**: DEBES configurar el archivo `claude_desktop_config.json` de Claude Desktop para que apunte al script `mcp-server/main.py`.

> [!CAUTION]
> **REQUISITO CRÍTICO:** Ableton Live **DEBE** estar abierto y en ejecución con el Remote Script activo ANTES de iniciar el Asistente IA o Claude Desktop. Si Ableton Live está cerrado, la conexión TCP fallará, causando que el asistente no funcione correctamente o se cierre de inmediato.

### 🍎 Usuarios de macOS (Gatekeeper)
Al no contar con un certificado de desarrollador de pago de Apple, Gatekeeper marcará el binario. El método legítimo de bypass local es hacer **Clic derecho sobre la app -> Abrir** (no hagas doble clic). No es un fallo, es el flujo estándar de software open-source de alto rendimiento.

### 🪟 Usuarios de Windows (SmartScreen)
Windows Defender puede mostrar un aviso azul de 'PC protegido' al ejecutar el instalador `.exe`. Haz clic en **'Más información'** y luego en **'Ejecutar de todas formas'**.

---

## 📚 Documentación y Manuales

Para una masterclass técnica exhaustiva, guías de resolución de problemas y detalles completos de la API, por favor descarga nuestro manual oficial:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](USER_MANUAL.pdf)**


---

## ⚖️ Manifiesto de Ingeniería, Créditos y Licencia

Este software es el resultado manifiesto de la profunda ingeniería concebida y articulada desde los laboratorios de produktes-code en unión indisociable con el Ingeniero Jesús Ferrer García (CHUS BZN).

Nos negamos a ofrecer cajas negras simplificadas. Entregamos consolas paramétricas absolutas. Licenciado bajo restricciones de propiedad intelectual y los más estrictos márgenes open source (CC BY-NC-SA 4.0). ESTÁNDAR CORPORATIVO - RETAIL READY. GRADO INGENIERÍA CERTIFICADO.

<div class="page-break"></div>

### 🇬🇧 English (EN)

## 🎯 The Vision (Introduction)

Advanced audio mixing is often an analytical bottleneck. The producer's brain enters ear fatigue trying to resolve millimeter phase conflicts, losing global creative perspective. We developed Ableton AI Assistant questioning the DAW paradigm: Why must we move knobs manually when a machine has the surgical precision to calculate frequency masking? This tool is a revolutionary cognitive engineer. Connecting in real time via the Model Context Protocol (MCP) and relentless TCP architecture, Claude's AI 'listens' to your console's state and natively executes hardcoded mastering decisions. It is the bridge between Ableton's low-level code and the natural semantics of AI.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.
> **DISCLAIMER: This is an unofficial community tool. It is not affiliated with, endorsed by, or in any way officially connected to Ableton AG.**

---

## 📸 Interface / Ergonomics

![Desktop Interface](screenshot-UI.png)


---

## ⚙️ Parameter Masterclass (Features)

- **Adaptive Algorithmic Compression (Glue Compressor)**: The assistant doesn't throw a blind preset. It dynamically sets a slow Attack (to safeguard transient punch) and an ultra-fast Release calculated on the session's BPM. The engineering goal? To make the compressor 'breathe' with the track's rhythm, achieving commercial density without strangling dynamic range.
- **Masking and Phase Clearing (EQ Eight)**: A classic amateur production issue is bass clashing. Our logic injects a strict Side (S) cut below 120Hz. This technical directive anchors the physical energy of the Kick and Sub-bass purely in Mono (Mid), eradicating phase cancellations in clubs.
- **LLM Framework (MCP Protocol)**: Here lies the heart of the genius. Ableton Assistant stands as an MCP server empowering the Claude model. The AI doesn't guess; it 'reads' the JSON payload of the tracks' states, mathematically reasons the fix, and returns the execution order.
- **Low-Latency Network Telemetry (TCP Core)**: Moving a 'Gain' or 'Freq' knob from outside the DAW requires relentless access. We programmed the Python backend using raw TCP sockets that attack the Ableton Remote Script. This ensures voice/text modifications reflect natively in milliseconds.
- **Anti-Clash DSP Engine (Real-Time Audio Analysis)**: New in V2, a separated background process reads the OS master audio loopback using Fast Fourier Transforms (FFT) at 44100Hz. It divides the spectrum into 8 key bands and calculates a heuristic Anti-Clash Score in real-time, streaming visualization data at 60fps via WebSockets.
- **MIDI Generator V2**: Advanced deterministic generation of genre-specific grooves (House, Techno, Trap, DnB) and constrained multi-mode melodies, natively wrapped in Ableton Undo steps for immediate Ctrl+Z reversibility.
- **True Peak and LUFS Control Manager**: The platform audits and deploys limiters on the master with a parametric hard ceiling and adjusted lookahead, mathematically ensuring delivery to streaming platforms at standard LUFS levels.

---

## 🛡️ Shielding Architecture (Security)

In Retail and Enterprise deployment, a system crash is not a bug; it is capital loss. We designed a defensive armor (Shielding) emulating DevSecOps best practices:

• **Anti-Flood Engineering (Rate limiting)**: Asynchronous algorithms strangle anomalous request spikes using limitation middlewares.
• **Binary Crystallography (Magic Bytes)**: The system opens the file header and verifies the native hexadecimal sequence to certify container integrity.
• **RAM Sanity (2 GB Limit)**: We relentlessly reject any atypical weight at the upload threshold to prevent Out Of Memory attacks.

---

## 🚀 Technical Deployment & CI/CD Installation

We employ **Automated CI/CD via GitHub Actions** for cross-platform desktop compilation (Windows, macOS, and Linux).

### 🛠️ Download Installers
Navigate to the **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** section of this repository to download binaries for your OS:
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg` / `Ableton.AI.Assistant-1.0.0-arm64.dmg`
- **Linux**: `ableton-ai-assistant_1.0.0_amd64.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

#### 🧠 Backend Installation (Crucial)
This tool is not just a UI; it connects directly to Ableton Live's Python interpreter and Claude Desktop.
1. **Ableton Remote Script**: You MUST copy the `remote-script/AntigravityCore` folder to your Ableton Live MIDI Remote Scripts directory.
2. **MCP Server**: You MUST configure your Claude Desktop `claude_desktop_config.json` to point to the `mcp-server/main.py` script. 

> [!CAUTION]
> **CRITICAL REQUIREMENT:** Ableton Live **MUST** be open and running with the Remote Script active BEFORE starting the AI Assistant or Claude Desktop. If Ableton Live is closed, the TCP connection will fail, causing the assistant to malfunction or crash immediately.

### 🍎 macOS Users (Gatekeeper)
Lacking a paid Apple developer certificate, Gatekeeper will quarantine the binary. As engineers, the legitimate local bypass is to **Right-click the app -> Open** (do not double-click). It is the standard flow of high-performance open-source software.

### 🪟 Windows Users (SmartScreen)
Windows Defender may show a blue 'Windows protected your PC' warning when running the `.exe` installer. Click **'More info'** and then **'Run anyway'**.

### 🐧 Linux Users (AppImage & Debian)
- **AppImage**: Grant execution permissions before launching:
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage` and run.
- **Debian Package (`.deb`)**: Install via terminal:
  `sudo dpkg -i ableton-ai-assistant_1.0.0_amd64.deb` or double-click to install via your distro software manager.

---

## 📚 Documentation & Manuals

For an exhaustive technical masterclass, troubleshooting guides, and full API details, please download our official manual:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](USER_MANUAL.pdf)**


---

## ⚖️ Engineering Manifesto, Credits & License

Software conceived and articulated from the produktes-code labs in inseparable union with Engineer Jesus Ferrer Garcia (CHUS BZN).

Licensed under proprietary restrictions and strictest open source margins (CC BY-NC-SA 4.0). CORPORATE STANDARD - RETAIL READY.



## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-21**.

<div class="page-break"></div>

### 🇩🇪 Deutsch (DE)

## 🎯 Die Vision (Einführung)

Das Mischen ist ein analytischer Engpass. Das Gehirn ermüdet bei der Lösung von Phasenkonflikten. Wir haben dieses Tool entwickelt, indem wir das DAW-Paradigma in Frage gestellt haben: Warum Knöpfe manuell bewegen, wenn eine Maschine Maskierungen berechnen kann? Diese KI agiert als kognitiver Ingenieur, der Abletons Status über MCP liest und native Mastering-Entscheidungen ausführt.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](screenshot-UI.png)


---

## ⚙️ Parameter Masterclass

- **Adaptive Kompression**: Stellt dynamisch langsamen Attack (für Transienten) und schnellen Release (basierend auf BPM) ein, um den Kompressor mit dem Rhythmus atmen zu lassen.
- **Phasenauflösung (EQ Eight)**: Ein strenger Side (S) Cut unter 120 Hz verankert Kick und Sub-Bass im Mono, um Phasenauslöschungen in Clubs zu vermeiden.
- **MCP-Protokoll**: Die KI liest den JSON-Payload des Spurstatus, argumentiert mathematisch und führt Aktionen präzise aus.
- **TCP-Kern**: Rohe TCP-Sockets greifen auf das Ableton Remote Script zu, um Modifikationen ohne MIDI-Latenz widerzuspiegeln.
- **Anti-Clash DSP Engine (Echtzeit-Audioanalyse)**: Neu in V2, ein separater Hintergrundprozess liest das OS-Master-Audio-Loopback mittels Fast Fourier Transforms (FFT) bei 44100Hz. Es unterteilt das Spektrum in 8 Schlüsselbänder und berechnet in Echtzeit einen heuristischen Anti-Clash Score. Visualisierungsdaten werden mit 60fps über WebSockets gestreamt.
- **MIDI Generator V2**: Fortschrittliche deterministische Generierung von genrespezifischen Grooves (House, Techno, Trap, DnB) und beschränkten Multi-Mode-Melodien, nativ eingebettet in Ableton Undo-Schritte für sofortige Ctrl+Z Reversibilität.
- **True Peak / LUFS Manager**: Setzt Limiter auf dem Master, um eine mathematisch perfekte Bereitstellung für Streaming-Plattformen zu gewährleisten.

---

## 🛡️ Abschirmarchitektur

Systemabstürze sind Kapitalverlust. Shielding:

• Anti-Flood: Middlewares blockieren Spitzen.
• Magic Bytes: Hexadezimale Überprüfung der Header-Integrität.
• RAM-Sanity (2 GB Limit): Schutz vor OOM-Attacken.

---

## 🚀 Technische Bereitstellung & CI/CD Installation

Wir verwenden **Automatisierte CI/CD über GitHub Actions** für die Desktop-Anwendung. Laden Sie den neuesten Build für Ihr Betriebssystem im Bereich **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** herunter.

#### 🧠 Backend-Installation (Entscheidend)
Dies ist nicht nur eine UI; es verbindet sich direkt mit dem Python-Interpreter von Ableton Live und Claude Desktop.
1. **Ableton Remote Script**: Sie MÜSSEN den Ordner `remote-script/AntigravityCore` in Ihr Ableton Live MIDI Remote Scripts-Verzeichnis kopieren.
2. **MCP Server**: Sie MÜSSEN Ihre `claude_desktop_config.json` so konfigurieren, dass sie auf das Skript `mcp-server/main.py` verweist.

### 🍎 macOS-Benutzer (Gatekeeper)
Da ein kostenpflichtiges Apple-Entwicklerzertifikat fehlt, wird Gatekeeper die Binärdatei unter Quarantäne stellen. Die legitime lokale Umgehung ist **Rechtsklick auf die App -> Öffnen** (nicht doppelklicken).

### 🪟 Windows-Benutzer (SmartScreen)
Windows Defender zeigt möglicherweise einen blauen Warnbildschirm beim Ausführen des `.exe`-Installationsprogramms an. Klicken Sie auf **'Weitere Informationen'** und dann auf **'Trotzdem ausführen'**.

## 📚 Dokumentation & Handbücher

Laden Sie unser offizielles Handbuch herunter:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](USER_MANUAL.pdf)**


---

## ⚖️ Engineering Manifesto & Credits

Entwickelt von produktes-code und Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

<div class="page-break"></div>

### 🇷🇺 Русский (RU)

## 🎯 Видение

Сведение - это аналитическое узкое место. Мы разработали этот инструмент, ставя под сомнение парадигму DAW: зачем крутить ручки вручную, когда машина может рассчитать маскирование? Этот ИИ действует как когнитивный инженер, читая состояние Ableton через MCP и выполняя решения по мастерингу.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](screenshot-UI.png)


---

## ⚙️ Мастер-класс параметров

- **Адаптивная компрессия**: Устанавливает медленную атаку и быстрый релиз (на основе BPM), чтобы компрессор дышал в ритме трека.
- **Фазовое разрешение (EQ Eight)**: Срез Side (S) ниже 120 Гц фиксирует бас в Mono, чтобы избежать фазовых отмен.
- **Протокол MCP**: ИИ читает состояние дорожек через JSON и выполняет математические решения.
- **Ядро TCP**: Сырые сокеты TCP управляют Ableton без задержки MIDI.
- **Движок DSP Anti-Clash (Анализ звука в реальном времени)**: Новинка V2, отдельный фоновый процесс читает OS master audio loopback с использованием быстрого преобразования Фурье (FFT) на 44100 Гц. Он разделяет спектр на 8 ключевых полос и вычисляет эвристический Anti-Clash Score в реальном времени, передавая данные визуализации при 60fps через WebSockets.
- **MIDI Generator V2**: Усовершенствованная детерминированная генерация жанровых грувов (House, Techno, Trap, DnB) и ограниченных многорежимных мелодий, нативно обернутая в шаги Undo Ableton для мгновенной обратимости с помощью Ctrl+Z.
- **Менеджер True Peak / LUFS**: Устанавливает лимитеры для идеальной доставки на стриминговые платформы.

---

## 🛡️ Архитектура экранирования

Экранирование:

• Anti-Flood: Блокировка всплесков запросов.
• Magic Bytes: Гексадецимальная проверка файлов.
• 2 GB Limit: Защита оперативной памяти.

---

## 🚀 Техническое развертывание и установка CI/CD

Мы используем **Автоматизированный CI/CD через GitHub Actions** для настольного приложения. Скачайте последнюю сборку для вашей ОС из раздела **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.

#### 🧠 Установка Backend (Критически важно)
Это не просто UI; он напрямую подключается к интерпретатору Python Ableton Live и Claude Desktop.
1. **Ableton Remote Script**: ВЫ ДОЛЖНЫ скопировать папку `remote-script/AntigravityCore` в вашу директорию MIDI Remote Scripts в Ableton Live.
2. **MCP Server**: ВЫ ДОЛЖНЫ настроить `claude_desktop_config.json` в Claude Desktop на скрипт `mcp-server/main.py`.

### 🍎 Пользователи macOS (Gatekeeper)
Из-за отсутствия платного сертификата разработчика Apple, Gatekeeper поместит бинарный файл в карантин. Законный локальный обход: **Правый клик по приложению -> Открыть** (не двойной клик).

### 🪟 Пользователи Windows (SmartScreen)
Windows Defender может показать синий экран. Нажмите **'Подробнее'**, а затем **'Выполнить в любом случае'**.

## 📚 Документация и руководства

Загрузите наше официальное руководство:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](USER_MANUAL.pdf)**


---

## ⚖️ Инженерный манифест

Разработано produktes-code и Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

<div class="page-break"></div>

### 🇯🇵 日本語 (JA)

## 🎯 ビジョン（はじめに）

ミキシングは分析のボトルネックです。DAWのパラダイムに疑問を投げかけることで、このツールを開発しました。機械がマスキングを計算できるのに、なぜノブを手動で動かす必要があるのでしょうか。このAIは、MCPを介してAbletonのステータスを読み取り、マスタリングの決定を実行する認知エンジニアとして機能します。

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](screenshot-UI.png)


---

## ⚙️ パラメーターマスタークラス（機能）

- **アダプティブコンプレッション**：スローアタックとファストリリース（BPMに基づく）を動的に設定し、コンプレッサーをトラックの一定のペースで呼吸させます。
- **位相分解能 (EQ Eight)**：120Hz未満のSide (S) カットにより、ベースがMonoに固定され、位相の打ち消し合いが回避されます。
- **MCPプロトコル**：AIはJSONを介してトラックのステータスを読み取り、数学的な決定を実行します。
- **TCPコア**：生のTCPソケットがMIDIレイテンシなしでAbletonを制御します。
- **Anti-Clash DSPエンジン (リアルタイムオーディオ分析)**: V2の新機能。分離されたバックグラウンドプロセスが、44100Hzで高速フーリエ変換（FFT）を使用してOSのマスターオーディオループバックを読み取ります。スペクトルを8つの主要な帯域に分割し、リアルタイムでヒューリスティックなAnti-Clashスコアを計算し、WebSocketsを介して60fpsで視覚化データをストリーミングします。
- **MIDIジェネレーター V2**: ジャンル固有のグルーヴ（House、Techno、Trap、DnB）と制限されたマルチモードメロディーの高度な決定論的生成。即時のCtrl+Z可逆性のためにAbletonの元に戻すステップにネイティブにラップされています。
- **True Peak / LUFSマネージャー**：ストリーミングプラットフォームへの完璧な配信のためにリミッターを設定します。

---

## 🛡️ シールドアーキテクチャ（セキュリティ）

防御装甲：

• アンチフラッド：リクエストのスパイクを制限します。
• マジックバイト：16進ヘッダーの検証。
• RAM制限（2 GB）：OOM攻撃を防ぎます。

---

## 🚀 技術展開（インストール） とCI/CDインストール

デスクトップアプリケーションには、**GitHub Actionsを介した自動CI/CD**を採用しています。**[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** セクションから最新のビルドをダウンロードします。

#### 🧠 バックエンドのインストール (重要)
これは単なるUIではありません。Ableton LiveのPythonインタープリターとClaude Desktopに直接接続します。
1. **Ableton Remote Script**：`remote-script/AntigravityCore` フォルダーをAbleton LiveのMIDI Remote Scriptsディレクトリにコピーする必要があります。
2. **MCP Server**：Claude Desktopの `claude_desktop_config.json` を設定して、`mcp-server/main.py` スクリプトを指すようにする必要があります。

### 🍎 macOSユーザー（Gatekeeper）
正当なローカルバイパス方法は、**アプリを右クリック -> 開く**ことです。

### 🪟 Windowsユーザー（SmartScreen）
**「詳細情報」**をクリックし、**「実行」**をクリックします。

## 📚 ドキュメントとマニュアル

公式マニュアルをダウンロードしてください：

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](USER_MANUAL.pdf)**


---

## ⚖️ エンジニアリングマニフェスト、クレジット、ライセンス

produktes-codeとJesus Ferrer（CHUS BZN）によって開発されました。 CC BY-NC-SA 4.0。 企業標準。

<div class="page-break"></div>

### 🇺🇦 Українська (UK)

## 🎯 Бачення

Зведення - це аналітичне вузьке місце. Ми розробили цей інструмент, ставлячи під сумнів парадигму DAW: навіщо крутити ручки вручну, коли машина може розрахувати маскування? Цей штучний інтелект діє як когнітивний інженер, читаючи стан Ableton через MCP і виконуючи рішення з майстерингу.

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](screenshot-UI.png)


---

## ⚙️ Майстер-клас параметрів

- **Адаптивна компресія**: Встановлює повільну атаку та швидкий реліз (на основі BPM), щоб компресор дихав у ритмі треку.
- **Фазова роздільна здатність (EQ Eight)**: Зріз Side (S) нижче 120 Гц фіксує бас у Mono, щоб уникнути фазових скасувань.
- **Протокол MCP**: ШІ читає стан доріжок через JSON і виконує математичні рішення.
- **Ядро TCP**: Сирі сокети TCP керують Ableton без затримки MIDI.
- **Рушій DSP Anti-Clash (Аналіз звуку в реальному часі)**: Новинка V2, окремий фоновий процес читає OS master audio loopback за допомогою швидкого перетворення Фур'є (FFT) на 44100 Гц. Він розділяє спектр на 8 ключових смуг і обчислює евристичний Anti-Clash Score в реальному часі, передаючи дані візуалізації при 60fps через WebSockets.
- **MIDI Generator V2**: Вдосконалена детермінована генерація жанрових грувів (House, Techno, Trap, DnB) і обмежених багаторежимних мелодій, нативно обгорнута в кроки Undo Ableton для миттєвої оборотності за допомогою Ctrl+Z.
- **Менеджер True Peak / LUFS**: Встановлює лімітери для ідеальної доставки на стримінгові платформи.

---

## 🛡️ Архітектура екранування

Екранування:

• Anti-Flood: Блокування сплесків запитів.
• Magic Bytes: Гексадецимальна перевірка файлів.
• 2 GB Limit: Захист оперативної пам'яті.

---

## 🚀 Технічне розгортання та встановлення CI/CD

Ми використовуємо **Автоматизований CI/CD через GitHub Actions** для додатку. Завантажте останню збірку для вашої ОС із розділу **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)**.

#### 🧠 Встановлення Backend (Критично важливо)
Це не просто UI; він безпосередньо підключається до інтерпретатора Python Ableton Live і Claude Desktop.
1. **Ableton Remote Script**: ВИ ПОВИННІ скопіювати папку `remote-script/AntigravityCore` у вашу директорію MIDI Remote Scripts.
2. **MCP Server**: ВИ ПОВИННІ налаштувати `claude_desktop_config.json` у Claude Desktop на скрипт `mcp-server/main.py`.

### 🍎 Користувачі macOS (Gatekeeper)
Через відсутність платного сертифіката розробника Apple, Gatekeeper помістить бінарний файл у карантин. Законний локальний обхід: **Правий клік по додатку -> Відкрити**.

### 🪟 Користувачі Windows (SmartScreen)
Windows Defender може показати синій екран. Натисніть **'Докладніше'**, а потім **'Виконати в будь-якому випадку'**.

## 📚 Документація та посібники

Завантажте наш офіційний посібник:

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](USER_MANUAL.pdf)**


---

## ⚖️ Інженерний маніфест

Розроблено produktes-code та Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

<div class="page-break"></div>

### 🇨🇳 中文 (ZH)

## 🎯 愿景 (介绍)

混音是一个分析瓶颈。我们通过质疑 DAW 范式来开发此工具：当机器可以计算掩蔽时，为什么还要手动转动旋钮？此 AI 充当认知工程师，通过 MCP 读取 Ableton 的状态并执行母带处理决策。

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](screenshot-UI.png)


---

## ⚙️ 参数大师班 (功能)

- **自适应压缩**：动态设置慢速起音和快速释放（基于 BPM），让压缩器随着轨道节奏呼吸。
- **相位解析 (EQ Eight)**：120Hz 以下的 Side (S) 切割将低音固定在 Mono 中，以避免相位抵消。
- **MCP 协议**：AI 通过 JSON 读取轨道状态并执行数学决策。
- **TCP 核心**：原始 TCP 套接字无延迟地控制 Ableton。
- **Anti-Clash DSP 引擎 (实时音频分析)**：V2新功能，一个独立后台进程以44100Hz使用快速傅里叶变换（FFT）读取OS主音频环回。它将频谱分为8个关键频段，并实时计算启发式的Anti-Clash Score，通过WebSockets以60fps流式传输可视化数据。
- **MIDI 生成器 V2**：特定流派律动（House、Techno、Trap、DnB）和受限多模式旋律的高级确定性生成，原生封装在Ableton撤销步骤中，支持立即Ctrl+Z可逆性。
- **True Peak / LUFS 管理器**：设置限制器以完美交付给流媒体平台。

---

## 🛡️ 屏蔽架构 (安全)

防御装甲：

• 反洪泛：限制请求峰值。
• 魔法字节：十六进制标头验证。
• RAM 限制 (2 GB)：防止 OOM 攻击。

---

## 🚀 技术部署 (安装) 与 CI/CD 安装

我们为桌面应用程序采用 **基于 GitHub Actions 的自动化 CI/CD**。从 **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** 部分下载适用于您操作系统的最新自动化版本。

#### 🧠 后端安装 (关键)
该工具不仅是一个UI；它直接连接到 Ableton Live 的 Python 解释器和 Claude Desktop。
1. **Ableton Remote Script**：您必须将 `remote-script/AntigravityCore` 文件夹复制到您的 Ableton Live MIDI Remote Scripts 目录。
2. **MCP Server**：您必须配置 Claude Desktop 的 `claude_desktop_config.json`，使其指向 `mcp-server/main.py` 脚本。

### 🍎 macOS 用户 (Gatekeeper)
合法本地绕过方法是 **右键单击应用程序 -> 打开**。

### 🪟 Windows 用户 (SmartScreen)
点击 **“更多信息”**，然后点击 **“仍要运行”**。

## 📚 文档和手册

请下载我们的官方手册：

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](USER_MANUAL.pdf)**


---

## ⚖️ 工程宣言，鸣谢与许可

由 produktes-code 和 Jesus Ferrer (CHUS BZN) 开发。CC BY-NC-SA 4.0。企业标准。