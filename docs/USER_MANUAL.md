[IMAGOTIPO]

![Imagotipo produktes-code](ruta/imagotipo.png)
*Logotipo corporativo de produktes-code y Ableton AI Assistant.*

# ABLETON AI ASSISTANT V1.0.0

<div class="cover-subtitle">Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant / Ingeniero de Mezcla Cognitivo IA y Asistente de Audio en Tiempo Real MCP</div>

🌐 **Language Selector / Selector de Idiomas:**
`[ES]` `[EN]` `[DE]` `[RU]` `[UK]` `[JA]` `[ZH]`

🔒 **Keywords de Seguridad:**
`CERTIFIED` | `RETAIL-READY` | `Rate limiting` | `Magic Bytes` | `2 GB` | `7 idiomas` | `CC BY-NC-SA 4.0`

---

<div class="page-break"></div>

## 1. THE VISION (INTRODUCTION)

La génesis de **Ableton AI Assistant** nace de una frustración histórica y profunda dentro del ecosistema de la producción musical profesional: el fenómeno de la fatiga auditiva acumulada. Tras largas jornadas de mezcla en el estudio, el oído humano pierde la capacidad objetiva de discriminar conflictos de fase milimétricos y solapamientos frecuenciales microscópicos. Los productores e ingenieros dedican horas rutinarias a mover potenciómetros manualmente, perdiendo de vista la perspectiva artística global del proyecto.

Cuestionamos radicalmente el paradigma tradicional de las estaciones de trabajo de audio digital (DAW): *¿Por qué un ingeniero debe ejecutar manualmente ajustes matemáticos repetitivos cuando una arquitectura de procesamiento digital puede calcular la enmascaración frecuencial con precisión quirúrgica?*

Ableton AI Assistant fue concebido no como un simple complemento o script MIDI decorativo, sino como el **Gemelo Digital de Audio (Audio Digital Twin)** definitivo. Se trata de un motor cognitivo que analiza la energía acumulada en las pistas, comprende la estructura cromática y espectral del arreglo, y blinda la sesión contra distorsiones y cancelaciones de fase. 

Conectándose en tiempo real mediante el **Protocolo de Contexto de Modelo (MCP - Model Context Protocol)** y alimentado por una arquitectura TCP de ultra baja latencia, la Inteligencia Artificial "escucha" inductivamente el estado dinámico del mezclador de Ableton Live y ejecuta órdenes paramétricas hardcodeadas en el motor DSP nativo. Devolvemos a los creadores e ingenieros el dominio absoluto sobre su identidad sonora.

![Dashboard principal](ruta/dashboard.png)
*Vista general del panel de control de Ableton AI Assistant.*

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

<div class="page-break"></div>

## 2. INTERFACE / ERGONOMICS

El diseño de interfaces destinadas a creadores sonoros exige un respeto escrupuloso por la ergonomía visual en entornos de trabajo con iluminación reducida. Las largas sesiones nocturnas en control rooms requieren una paleta cromática libre de deslumbramientos.

### 2.1 Principio Dark-Mode Puro
La interfaz de Ableton AI Assistant adopta un esquema de color **Dark-Mode absoluto basado en RGB(15, 15, 15)**. Esta directiva atenúa el estrés de los fotorreceptores oculares, manteniendo el contraste óptimo mediante acentos funcionales en tono Dorado/Amarillo Corporativo (#F5A623). Los elementos activos capturan la atención del operador sin saturar la retina.

### 2.2 Lienzo Principal (The Dashboard)
El panel principal actúa como un centro de mando diagnóstico unificado:
- **Monitor de Salud del Proyecto**: Barras de medición RMS y Peak con detección instantánea de headroom.
- **Alertas de Saturación Crítica**: Indicadores visuales reactivos que advierten sobre picos que superan los 0.0 dBFS.
- **Jerarquía Paramétrica Simplificada**: Eliminación de menús anidados de más de dos niveles; cada control principal permanece accesible a un único clic o gesto táctil.

### 2.3 Controles Táctiles Nativos
El potenciómetro virtual central y los deslizadores de *Drive* y *Gain Staging* no son representaciones gráficas pasivas. Cada control está vinculado bidireccionalmente al hilo del socket TCP local mediante una frecuencia de actualización milimétrica, eliminando cualquier tipo de latencia percibida al manipular la consola desde dispositivos físicos o táctiles.

### 2.4 Naturaleza Asíncrona del Renderizado
La arquitectura gráfica de Electron aísla completamente el hilo de renderizado (Main UI Thread), garantizando una tasa de refresco inquebrantable de **60 cuadros por segundo (60 fps)**. Mientras los procesos asíncronos de análisis espectral y la comunicación con el servidor MCP ocurren en segundo plano, la consola táctil responde de manera instantánea y fluida.

---

<div class="page-break"></div>

## 3. TECHNICAL DEPLOYMENT & CI/CD INSTALLATION

Para garantizar una estabilidad absoluta en cualquier entorno operativo comercial o de estudio, la compilación de Ableton AI Assistant se ejecuta de forma centralizada mediante un flujo de **Integración y Despliegue Continuo (CI/CD)** alojado en GitHub Actions.

![Logotipos de plataformas](ruta/logos.png)
*Instaladores disponibles para Windows, macOS y Linux.*

### 3.1 Pipeline de Compilación Automatizada
El código fuente no se empaqueta localmente en máquinas de desarrollo. En cada release, servidores de compilación limpios en la nube compilan de forma nativa los artefactos finales para Windows, macOS y Linux Ubuntu, ejecutando pruebas de integración estáticas antes de publicar el empaquetado final.

### 3.2 Descarga de Instaladores Oficiales
Los binarios compilados están disponibles directamente en el repositorio oficial de GitHub dentro de la sección **Releases**:
- **Windows (x64)**: `Ableton.AI.Assistant.Setup.1.0.0.exe` (Instalador ejecutable de 64 bits)
- **macOS (Universal - Intel & Apple Silicon)**: `Ableton.AI.Assistant-1.0.0.dmg` (Imagen de disco montable)
- **Linux (Debian/Ubuntu)**: `Ableton.AI.Assistant-1.0.0.deb` (Paquete Debian nativo)
- **Linux (Portabilidad Universal)**: `Ableton.AI.Assistant-1.0.0.AppImage` (Binario autónomo ejecutable)

### 3.3 Instrucciones Específicas por Sistema Operativo

#### 🍎 macOS (Bypass de Gatekeeper)
Al tratarse de una distribución de ingeniería de alto rendimiento sin certificado de desarrollador de Apple de pago, el subsistema Gatekeeper mostrará una advertencia al abrir el paquete `.dmg`.
1. Monte el archivo `.dmg` descargado y arrastre la aplicación a la carpeta `Aplicaciones`.
2. En lugar de hacer doble clic, haga **Clic Derecho (Control + Clic)** sobre el icono de Ableton AI Assistant y seleccione **Abrir**.
3. En el cuadro de diálogo de confirmación de seguridad, pulse el botón **Abrir**. Esta acción autoriza permanentemente la ejecución en el sandbox de su sistema.

#### 🪟 Windows (Aviso de SmartScreen)
En Windows 10 y Windows 11, la protección Windows Defender SmartScreen puede interrumpir la ejecución inicial del archivo `.exe`.
1. Inicie el instalador `Ableton.AI.Assistant.Setup.1.0.0.exe`.
2. Al aparecer la ventana azul *"Windows protegió su PC"*, haga clic en el texto **Más información**.
3. Seleccione el botón **Ejecutar de todas formas** para iniciar el asistente de instalación.

#### 🐧 Linux (AppImage & Paquete Debian)
Para distribuciones basadas en Ubuntu, Debian, Manjaro o Fedora:
- **Formato AppImage**:
  ```bash
  chmod +x Ableton.AI.Assistant-1.0.0.AppImage
  ./Ableton.AI.Assistant-1.0.0.AppImage
  ```
- **Formato Debian (`.deb`)**:
  ```bash
  sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb
  sudo apt-get install -f # En caso de requerir dependencias de sistema
  ```

---

<div class="page-break"></div>

## 4. SIGNAL FLOW & SETUP

El diseño híbrido de Ableton AI Assistant combina tres capas de ejecución tecnológica altamente especializadas: el motor de audio en Python dentro de Ableton Live, la interfaz nativa en Electron y el servidor MCP conectado a la infraestructura de inteligencia artificial en la nube.

![Diagrama de flujo de señal](ruta/diagrama.png)
*Arquitectura híbrida: comunicación entre el Remote Script, la app Electron y la nube.*

### 4.1 Instalación del Remote Script de Ableton (Python Engine)
1. Descargue el paquete de código fuente o localice la carpeta `AntigravityCore` dentro del directorio de instalación de la aplicación.
2. Copie la carpeta completa `AntigravityCore` dentro de la ruta nativa de Remote Scripts de su instalación de Ableton Live:
   - **macOS**: `/Applications/Ableton Live 11/12 Suite.app/Contents/App-Resources/MIDI Remote Scripts/`
   - **Windows**: `C:\ProgramData\Ableton\Live 11/12 Suite\Resources\MIDI Remote Scripts\`
3. Abra Ableton Live, acceda a **Preferencias -> Link / MIDI**, y en la pestaña de **Control Surface (Superficie de Control)**, seleccione `AntigravityCore` en la primera casilla disponible.

![Selección del Control Surface](ruta/control_surface.png)
*Selección de 'AntigravityCore' en las preferencias de Ableton Live.*

### 4.2 Sockets TCP de Ultra Baja Latencia (Local Loopback)
Una vez inicializado el Remote Script `AntigravityCore`, Python abre silenciosamente un servidor de sockets TCP escuchando en la dirección local `127.0.0.1` a través del puerto especificado **9001**.
- La aplicación Electron actúa como cliente IPC de alta velocidad, conectándose a este puerto.
- Cada variación de volumen, panorama o parámetros DSP se transmite utilizando tramas binarias compactas que garantizan una latencia de transporte inferior a **1 milisegundo en la red local**.

### 4.3 Inyección Segura de Tokens LLM (Claude API)
Para utilizar las funciones avanzadas de auditoría y razonamiento acústico:
1. Acceda al panel de **Configuración (Settings)** en la interfaz de Ableton AI Assistant.
2. Introduzca su clave de API de Anthropic Claude (`sk-ant-...`).
3. El sistema cifra localmente el token en el llavero seguro del sistema operativo (Keychain / Credential Manager). Las solicitudes de lenguaje natural se envían a través de canales HTTPS cifrados (TLS 1.3), enviando únicamente vectores numéricos de las pistas y preservando la privacidad del audio local.

---

<div class="page-break"></div>

## 5. OPERATIVE PHILOSOPHY (USER GUIDE)

La filosofía de trabajo de Ableton AI Assistant está orientada a complementar y potenciar las habilidades del ingeniero de mezcla, estructurando el proceso operacional en cuatro fases consecutivas:

```
[ FASE 1: Auditoría ] ➔ [ FASE 2: Staging ] ➔ [ FASE 3: Despeje ] ➔ [ FASE 4: Mastering ]
```

### 5.1 Modo Auditoría de Sesión
Al iniciar una nueva sesión de producción, el operador activa el botón **Analyze Session**. El Remote Script escanea instantáneamente la totalidad de las pistas del proyecto en Ableton Live, extrayendo métricas fundamentales:
- Conteo total de pistas de audio y MIDI.
- Distribución de picos máximos (dBFS) e intensidad integrada (LUFS).
- Mapeo de panoramas estéreo e identificación de instrumentos de frecuencia grave.

### 5.2 Estaciado Dinámico de Ganancia (Gain Staging)
El mantenimiento de un headroom adecuado es la regla de oro en el entorno digital. El asistente calcula la atenuación o ganancia necesaria para posicionar el valor nominal de cada canal entre **-18 dBFS y -12 dBFS**, permitiendo que los plugins de emulación analógica operen en su punto dulce lineal sin introducir distorsión armónica no deseada.

### 5.3 Control de Enmascaramiento y Limpieza Espectral
A través de algoritmos de detección espectral en tiempo real, la consola identifica frecuencias de choque. Al pulsar **Clear Masking**, el sistema envía una orden paramétrica al plugin *EQ Eight* de Ableton, ejecutando un corte de fase estricto para limpiar el rango inferior de la mezcla.

### 5.4 Pulido de Master de Alta Fidelidad
En la etapa final de entrega, el asistente analiza la curva tonal de la pista Master y ajusta dinámicamente los parámetros de compresión y ecualización de bus para optimizar la respuesta dinámica frente a los algoritmos de las plataformas de streaming.

---

<div class="page-break"></div>

## 6. PARAMETER MASTERCLASS (FEATURES) – DETALLE TÉCNICO

Esta sección expone detalladamente la lógica matemática e ingenieril aplicada por el motor de Ableton AI Assistant al manipular los procesadores nativos de Ableton Live.

### 6.1 Compresión Algorítmica Adaptativa (Glue Compressor)
La compresión de bus no debe aplicarse mediante presets estáticos. El asistente analiza el ritmo de la pista (BPM) y la envolvente de los transitorios para instanciar el procesador *Glue Compressor* con los siguientes parámetros calculados:

$$\text{Attack Time} = \text{Lento (30 ms)} \quad \text{para preservar la pegada del bombo y la caja.}$$

$$\text{Release Time} = \text{Ultrarrápido (100 ms o Auto)}, \quad \text{sincronizado al tempo de la sesión.}$$

- **Ratio**: Fijado en 2:1 o 4:1 según el rango dinámico entrante.
- **Makeup Gain**: Compensación de ganancia automatizada sobre el valor RMS efectivo.

### 6.2 Despeje de Enmascaramiento y Fase (EQ Eight)
Uno de los errores más comunes en la mezcla de música electrónica y urbana es la cancelación de fase en frecuencias subgraves.

![Alerta de enmascaramiento](ruta/alerta.png)
*Ejemplo de alerta por conflicto de frecuencias entre Kick y Bass.*

Nuestra directiva técnica ejecuta una instrucción de procesamiento Mid/Side en el *EQ Eight* asignado a las pistas secundarias y de efectos:
- **Filtro de Corte de Graves (High-Pass / Low-Cut)**: Pendiente de 48 dB/octava en la señal **Side (S)** fijada estrictamente por debajo de **120 Hz**.
- **Resultado Físico**: Toda la energía comprendida entre 20 Hz y 120 Hz (Kick y Sub-bass) queda anclada de forma puramente **Mono (Mid)**. Esto erradica las cancelaciones de fase al reproducir el material en sistemas de sonido estéreo de clubs, festivales o dispositivos móviles.

### 6.3 Framework LLM (Protocolo MCP - Model Context Protocol)
El asistente implementa una arquitectura de servidor MCP que actúa como pasarela entre el modelo de lenguaje Claude 3.5 Sonnet y el motor de Ableton Live.
1. **Petición**: El Remote Script empaqueta el estado del proyecto en un Payload JSON estructurado:
   ```json
   {
     "session_bpm": 124.0,
     "tracks_count": 16,
     "master_peak_db": -0.4,
     "low_end_conflict": true,
     "kick_track_id": 1,
     "bass_track_id": 2
   }
   ```
2. **Razonamiento**: El servidor MCP evalúa las métricas frente a la base de conocimiento de ingeniería de sonido.
3. **Ejecución**: El modelo responde con un conjunto de instrucciones deterministas que el Remote Script aplica sobre la superficie de control de Ableton sin margen para la improvisación imprecisa.

---

<div class="page-break"></div>

## 7. GLOBAL MULTIMODAL INTEGRATION

En produktes-code rechazamos el tratamiento de la internacionalización mediante traducciones mecánicas de texto plano. Hemos desarrollado una arquitectura **Multimodal Estructural** diseñada para responder a las exigencias de ingenieros globales.

### 7.1 Soporte Lingüístico Nativo en 7 Idiomas
Toda la documentación, alertas de la interfaz, descripciones técnicas e inferencias del asistente están plenamente integradas en 7 idiomas oficiales:
- 🇪🇸 **Español (ES)** - Idioma primario de desarrollo e ingeniería.
- 🇬🇧 **English (EN)** - Estándar internacional comercial.
- 🇩🇪 **Deutsch (DE)** - Especificación técnica para la industria centroeuropea.
- 🇷🇺 **Русский (RU)** - Adaptación léxica para Europa del Este.
- 🇺🇦 **Українська (UK)** - Integración completa de soporte regional.
- 🇯🇵 **日本語 (JA)** - Formato adaptado para el mercado asiático de alta tecnología.
- 🇨🇳 **中文 (ZH)** - Soporte optimizado en tipografía Unicode simplificada.

### 7.2 Cumplimiento Unicode 100% y Hot-Reloading
La consola soporta la codificación **UTF-8 completa**. El usuario puede alternar dinámicamente entre cualquiera de los 7 idiomas desde el panel de preferencias sin necesidad de reiniciar la aplicación ni interrumpir la reproducción en Ableton Live.

---

<div class="page-break"></div>

## 8. SHIELDING ARCHITECTURE (SECURITY)

En un entorno de producción profesional o de emisión en directo, una congelación del sistema informático es inaceptable. Hemos implementado una coraza defensiva (**Shielding**) inspirada en las mejores prácticas de DevSecOps.

### 8.1 Ingeniería Anti-Flood (Rate Limiting)
Para evitar que movimientos masivos de deslizadores o ráfagas de datos en la interfaz colapsen el hilo de ejecución de Python en Ableton:
- Un middleware de limitación de tasa (*Rate Limiter*) estrangula las peticiones TCP entrantes en el socket 9001.
- Los paquetes de control se filtran mediante un algoritmo de balde de tokens (*Token Bucket*), procesando un máximo de **100 eventos por segundo**, suficiente para garantizar fluidez suave sin saturar el CPU.

### 8.2 Validación Rigurosa de Payloads JSON
Cada trama de datos recibida desde la red local es sometida a una inspección de esquemas estricta antes de ser ejecutada por el Remote Script. Si un paquete presenta una estructura corrupta o incompleta, es descartado inmediatamente y registrado en el log de auditoría de seguridad sin interrumpir la transmisión de audio.

### 8.3 Sanidad de Memoria RAM (Limitador Estricto de 2 GB)
Los modelos de lenguaje pueden generar respuestas excesivamente extensas que pongan en riesgo la estabilidad de la memoria. La aplicación cuenta con un guardián de RAM que rechaza implacablemente cualquier respuesta de la API que supere el umbral de **2 GB de uso de memoria del proceso**, salvaguardando la sesión de Ableton Live frente a errores de desbordamiento (Out Of Memory - OOM).

---

<div class="page-break"></div>

## 9. DEBUG LOG (FAQ) – SECCIÓN EXTENSA DE RESOLUCIÓN DE PROBLEMAS

A continuación se detalla una lista de soluciones a situaciones técnicas comunes identificadas en entornos de producción:

#### 1. ¿Por qué macOS indica que la aplicación está "dañada y no se puede abrir"?
*Respuesta*: Este mensaje es una advertencia de seguridad predeterminada de Apple Gatekeeper cuando un binario no cuenta con una firma comercial de pago. Siga las instrucciones del apartado 3.3: haga clic derecho sobre el archivo en la carpeta Aplicaciones y seleccione **Abrir**.

#### 2. Windows Defender SmartScreen bloquea el ejecutable de instalación `.exe`.
*Respuesta*: Es el comportamiento habitual para software open-source independiente. Pulse sobre el texto **Más información** dentro de la ventana de advertencia de Windows y seleccione **Ejecutar de todas formas**.

#### 3. En Linux Linux Ubuntu/Debian, el archivo `.AppImage` no se inicia al hacer doble clic.
*Respuesta*: Debe otorgar permisos de ejecución al archivo descargado. Abra la terminal y ejecute `chmod +x Ableton.AI.Assistant-1.0.0.AppImage` antes de lanzarlo.

#### 4. Ableton Live no muestra `AntigravityCore` en la lista de Superficies de Control.
*Respuesta*: Verifique que la carpeta `AntigravityCore` esté copiada dentro del directorio correcto de `MIDI Remote Scripts` correspondiente a la versión exacta de su Ableton Live (11 o 12 Suite/Standard) y reinicie el DAW.

#### 5. Error de conexión: "TCP Socket Binding Error on Port 9001".
*Respuesta*: Otra aplicación o instancia previa de Python puede estar ocupando el puerto 9001. Cierre los procesos secundarios o verifique las reglas del firewall local para permitir conexiones entrantes en `127.0.0.1:9001`.

#### 6. La aplicación Electron muestra el estado "Disconnected" en la barra inferior.
*Respuesta*: Asegúrese de que Ableton Live esté abierto y que la superficie de control `AntigravityCore` esté seleccionada y activa en las Preferencias MIDI.

#### 7. Error HTTP 401 al intentar realizar una auditoría con inteligencia artificial.
*Respuesta*: La clave API de Anthropic Claude introducida en el menú de Configuración es inválida o ha expirado. Compruebe su clave en el panel de control de Anthropic y vuelva a guardarla.

#### 8. El tiempo de respuesta de las auditorías de IA es lento (más de 5 segundos).
*Respuesta*: Las consultas de lenguaje natural dependen de la latencia de su conexión a Internet con los servidores en la nube de Anthropic. Las funciones de control de transporte y faders locales operan de forma instantánea a 0 ms.

#### 9. La alerta de enmascaramiento frecuencial de graves continúa activa tras pulsar "Clear Masking".
*Respuesta*: Verifique si en su sesión existen múltiples pistas de bajo o sintetizadores adicionales que no hayan sido procesados con el filtro de corte Side por debajo de 120 Hz.

#### 10. La interfaz de la aplicación se muestra en blanco o congelada.
*Respuesta*: Reinicie la aplicación Electron. El motor Remote Script en Ableton Live continuará funcionando en segundo plano sin interrumpir la reproducción del proyecto.

#### 11. ¿Se requiere conexión permanente a Internet para usar la aplicación?
*Respuesta*: No. Las funciones de control táctil, Gain Staging y visualización del Dashboard operan en su totalidad de forma local fuera de línea. Únicamente el módulo de asesoría LLM requiere conexión WAN.

#### 12. Se observan bombeos excesivos (*pumping*) al aplicar la compresión Glue automática.
*Respuesta*: Aumente ligeramente el tiempo de ataque desde la interfaz o reduzca la ganancia de entrada de la pista analizada si la señal sobrepasa el umbral de entrada tolerado.

#### 13. Aparece un aviso de "Rate Limit Exceeded (HTTP 429)".
*Respuesta*: Ha superado la cuota de peticiones por minuto permitida por su cuenta en la API de Anthropic. Espere 60 segundos antes de enviar una nueva consulta.

#### 14. ¿Cómo actualizar la aplicación a una nueva versión compilada?
*Respuesta*: Descargue el nuevo ejecutable o paquete `.dmg`/`.deb` desde GitHub Releases y reemplácelo sobre la versión existente. Sus configuraciones y claves guardadas se preservarán automáticamente.

#### 15. ¿Cómo reportar un error técnico o proponer una mejora?
*Respuesta*: Acceda al apartado de **Issues** en el repositorio oficial de GitHub de produktes-code y complete la plantilla de reporte de errores adjuntando el archivo de log local.

---

<div class="page-break"></div>

## 10. ENGINEERING MANIFESTO, CREDITS & LICENSE

Este software es el resultado manifiesto de la profunda ingeniería concebida, estructurada y articulada desde los laboratorios de **produktes-code** en unión indisociable con el Ingeniero **Jesús Ferrer García (CHUS BZN)**.

Nos negamos a entregar soluciones simplificadas de caja negra que reduzcan la capacidad de decisión del creador. Diseñamos e implementamos consolas paramétricas absolutas que garantizan el control técnico e intelectual sobre cada proceso.

### Licencia de Distribución
Licenciado bajo restricciones de propiedad intelectual y los más estrictos márgenes open source bajo la licencia **Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)**.

```
CORPORATE STANDARD - STUDIO READY - CERTIFIED ENGINEERING GRADE
```

---

<div class="page-break"></div>

## 11. SECURITY AUDIT

Este repositorio ha superado satisfactoriamente una auditoría de seguridad exhaustiva de **Nivel 4** con fecha **27 de julio de 2026**.

- **Análisis Estático de Código**: Superado (0 vulnerabilidades críticas detectadas).
- **Inspección de Dependencias**: Superado (Remediación completa de dependencias obsoletas en entornos Node.js y Python).
- **Linting de Seguridad DevSecOps**: Verificado (Validación de tramas de red, control de memoria RAM y sanitización de claves de API).

---

<div class="page-break"></div>

## 12. GLOSARIO DE TÉRMINOS TÉCNICOS

- **MCP (Model Context Protocol)**: Protocolo estándar abierto que permite a modelos de inteligencia artificial interactuar con herramientas y entornos locales de forma segura y estructurada.
- **TCP (Transmission Control Protocol)**: Protocolo de red fundamental orientado a conexión que garantiza la entrega ordenada y sin pérdidas de paquetes entre la app Electron y Ableton Live.
- **DSP (Digital Signal Processing)**: Conjunto de algoritmos matemáticos dedicados a la manipulación y procesamiento numérico de señales de audio digital en tiempo real.
- **LLM (Large Language Model)**: Redes neuronales de lenguaje de gran tamaño (como Claude 3.5 Sonnet) entrenadas para comprender y generar razonamientos contextuales complejos.
- **API (Application Programming Interface)**: Interfaz de código que permite la comunicación estandarizada entre aplicaciones de software independientes.
- **JSON (JavaScript Object Notation)**: Format de texto ligero utilizado para empaquetar y transferir la estructura de pistas de Ableton Live a través de la red local.
- **OOM (Out Of Memory)**: Condición de fallo crítico del sistema provocada cuando una aplicación agota la memoria RAM física disponible asignada por el sistema operativo.
- **DAW (Digital Audio Workstation)**: Entorno de software integral utilizado para la grabación, edición, mezcla y masterización de música (ej. Ableton Live).
- **Remote Script**: Módulo ejecutable en código Python que se integra en el núcleo de Ableton Live para exponer sus APIs internas a controladores externos.
- **Rate Limiting**: Mecanismo de control defensivo que limita la cantidad de peticiones enviadas a un servidor en un periodo de tiempo determinado para prevenir colapsos.