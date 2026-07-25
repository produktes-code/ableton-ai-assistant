# Antigravity AI Assistant V2.0.1
## Manual de Usuario Completo
**Autor:** Produktes-code (Chus BZN)
**Versión:** 2.0.1 — Cine Station Pro Standard
**Fecha:** 2025

---

## 1. Introducción

Antigravity AI Assistant es un sistema de control inteligente para Ableton Live 11 y 12 que integra inteligencia artificial directamente en tu flujo de producción musical. Actúa como un nexo en tiempo real entre la API de Ableton y modelos de lenguaje de vanguardia, permitiéndote interactuar con tu sesión musical mediante lenguaje natural.

### ¿Qué puedes hacer con Antigravity?
- **Controlar Ableton Live con lenguaje natural**: Puedes pedirle al asistente que agregue pistas, ajuste volúmenes, silencie canales o arme pistas para grabación simplemente escribiéndolo o hablándole.
- **Generar patrones MIDI automáticamente**: Genera grooves de batería estructurados (como ritmos de House, Techno, Trap, y DnB) o crea líneas melódicas completas adaptadas automáticamente a la escala y tonalidad de tu sesión.
- **Analizar tu mezcla con el Motor DSP Anti-Clash**: Monitorea el espectro de audio de tu mezcla en tiempo real agrupado en 8 bandas clave para detectar enmascaramiento y problemas de colisión de frecuencias.
- **Búsqueda inteligente de muestras**: Busca y clasifica tus samples locales utilizando modelos de IA que reconocen el timbre y carácter de tus sonidos.
- **Conversión avanzada de Audio a MIDI**: Integra la biblioteca BasicPitch para convertir clips de audio monofónicos o polifónicos a notas MIDI legibles con alta precisión.

---

## 2. Instalación

### macOS (ARM + Intel)
1. Descarga el instalador oficial de la sección de releases: `antigravity-app-2.0.1-arm64.dmg`.
2. Haz doble clic en el archivo descargado y arrastra la aplicación `Antigravity AI Assistant` a tu carpeta `/Applications`.
3. Copia el directorio completo de `remote-script/AntigravityCore/` a la carpeta de Remote Scripts de tu Ableton Live:
   - En macOS: `/Users/TU_USUARIO/Library/Preferences/Ableton/Live x.x.x/User Library/Remote Scripts/` o haciendo clic derecho sobre la aplicación de Ableton > Mostrar contenido del paquete > `Contents/App-Resources/MIDI Remote Scripts/`.
4. Abre Ableton Live. Ve a `Preferences > Link/MIDI`, y en la lista de superficies de control selecciona **AntigravityCore**.

### Windows x64
1. Descarga el ejecutable de instalación: `antigravity-app-Setup-2.0.1.exe`.
2. Haz doble clic en el instalador para iniciar el proceso. Si aparece la advertencia de SmartScreen de Windows, haz clic en **Más información** y luego en **Ejecutar de todas formas**.
3. Copia el directorio completo de `remote-script/AntigravityCore/` a tu carpeta de scripts MIDI de Ableton Live:
   - En Windows: `C:\Users\TU_USUARIO\Documents\Ableton\User Library\Remote Scripts\` o en el directorio de instalación de Live bajo `Resources\MIDI Remote Scripts\`.
4. En las opciones de Live (`Opciones > Preferencias > Link/MIDI`), selecciona **AntigravityCore** como superficie de control.

### Linux AppImage
1. Descarga el paquete ejecutable de Linux: `Antigravity-AI-Assistant-2.0.1.AppImage`.
2. Haz clic derecho sobre el archivo, ve a Propiedades > Permisos y marca la casilla **Permitir ejecutar el archivo como un programa**, o ejecuta en tu terminal:
   ```bash
   chmod +x Antigravity-AI-Assistant-2.0.1.AppImage
   ```
3. Ejecuta la aplicación haciendo doble clic o a través de la consola.
4. Sigue los mismos pasos para copiar la carpeta `remote-script/AntigravityCore/` al directorio de Remote Scripts de tu instalación de Ableton Live en Linux.

### Configuración inicial
1. Abre tu DAW Ableton Live asegurándote de que el Remote Script de AntigravityCore esté configurado correctamente.
2. Inicia la aplicación Antigravity en tu ordenador.
3. El indicador (dot) TCP de estado de conexión se pondrá en verde automáticamente una vez que la interfaz detecte a Ableton.
4. Los parámetros dinámicos de BPM, KEY (Tonalidad) y los valores de LUFS/espectro aparecerán de inmediato en la barra superior.

---

## 3. Arquitectura del Sistema

El asistente está diseñado con un modelo de tres capas desacopladas y de alto rendimiento que previene que los procesos pesados de IA y renderizado visual impacten en el motor de audio en tiempo real de Ableton Live:

```
Ableton Live 11/12
     |
AntigravityCore.py (Remote Script)
     |-- TCP Server 127.0.0.1:9001
     |-- CommandRegistry (39+ comandos LOM)
     |-- MidiGenerator V2
     |-- SessionManager V2
     |-- DSPBridge
          |
          dsp_engine.py (proceso separado)
               |-- Captura audio (sounddevice)
               |-- FFT 8 bandas frecuenciales
               |-- Anti-Clash Score
               |-- WebSocket ws://localhost:9002

App Electron (UI)
     |-- TCP Client (auto-discovery)
     |-- DSP Visualizer (60fps interpolado)
     |-- Chat IA multimodal
     |-- Session Sync en tiempo real
```

### Componente 1: Remote Script (AntigravityCore)
Escrito en Python y cargado directamente por el framework de Ableton Live. Expone un servidor de sockets TCP local que escucha comandos de control del DAW. Este módulo está diseñado para ejecutarse en hilos cooperativos seguros que no bloquean la UI ni el audio de Ableton.

### Componente 2: DSP Engine
Un proceso de sistema independiente que corre de manera paralela. Captura la salida de audio de Ableton mediante interfaces loopback o hardware, realiza transformadas de Fourier rápidas (FFT), analiza el espectro y envía los descriptores espectrales a través de un servidor WebSocket a la aplicación Electron.

### Componente 3: App Electron (Interfaz de Usuario)
Una UI interactiva construida con tecnologías web (HTML5/Vanilla CSS/JS) que utiliza técnicas de Glassmorphism para integrarse visualmente con la estética moderna de Ableton Live 12. Se conecta al script de Ableton para enviar comandos y lee el WebSocket de audio para pintar el analizador espectral a 60 FPS estables.

### Protocolo TCP v2
- **Seguridad local**: Enlace (binding) exclusivo a la dirección de bucle local `127.0.0.1`.
- **Token por sesión**: Cada arranque de Ableton genera un token de seguridad criptográfico único de 32 bytes necesario para conectarse.
- **Tasa de transferencia regulada**: Límite estricto de 100 peticiones por segundo por cliente para evitar ataques de denegación de servicio internos.
- **Cola FIFO**: Gestión de órdenes secuenciales con capacidad para 256 comandos y descarte seguro por sobrepresión (backpressure).
- **Métricas detalladas**: Todas las respuestas devuelven la latencia de procesamiento exacta en milisegundos (`latency_ms`).

---

## 4. Comandos LOM Disponibles

### Transporte

| Comando | Descripción | Parámetros |
|---------|-------------|------------|
| `ping` | Test básico de conectividad de red | ninguno |
| `transport_play` | Inicia la reproducción en la línea de tiempo | ninguno |
| `transport_stop` | Detiene la reproducción y detiene la grabación | ninguno |
| `transport_record` | Activa o desactiva la grabación general | `enabled: bool` |
| `set_bpm` | Modifica el tempo del set (rango 20 - 999) | `bpm: float` |
| `get_bpm` | Retorna el tempo actual del set de Ableton | ninguno |
| `get_position` | Retorna la posición de reproducción en beats | ninguno |
| `set_position` | Mueve el cabezal a la posición dada en beats | `beats: float` |
| `set_loop` | Configura el bucle de reproducción | `enabled: bool`, `start: float`, `end: float` |
| `get_key` | Retorna la tonalidad global (disponible en Live 12) | ninguno |
| `set_key` | Define la tonalidad global de la sesión | `root_note: int (0-11)` |
| `stop_all_clips` | Detiene inmediatamente la reproducción de todos los clips | ninguno |

### Pistas

| Comando | Descripción | Parámetros |
|---------|-------------|------------|
| `get_all_tracks` | Obtiene un listado completo con los nombres e índices de pista | ninguno |
| `get_track_info` | Obtiene información detallada de una pista específica | `track_index: int` |
| `set_track_mute` | Activa o desactiva el estado de silenciado de una pista | `track_index: int`, `muted: bool` |
| `set_track_solo` | Activa o desactiva el modo solo en una pista | `track_index: int`, `soloed: bool` |
| `set_track_volume` | Ajusta el control de ganancia de volumen (rango 0.0 a 1.0) | `track_index: int`, `volume: float` |
| `set_track_pan` | Ajusta el panorama estereofónico (rango -1.0 a 1.0) | `track_index: int`, `pan: float` |
| `set_track_name` | Modifica el nombre de la pista | `track_index: int`, `name: str` |

### Clips

| Comando | Descripción | Parámetros |
|---------|-------------|------------|
| `create_midi_clip` | Genera un clip MIDI vacío en la pista y slot especificados | `track_index: int`, `slot_index: int`, `length_bars: float` |
| `fire_clip` | Lanza o reproduce un clip en la sesión | `track_index: int`, `slot_index: int` |
| `stop_clip` | Detiene la reproducción del clip indicado | `track_index: int`, `slot_index: int` |
| `delete_clip` | Elimina permanentemente el clip de la rejilla | `track_index: int`, `slot_index: int` |
| `get_session_state` | Retorna una captura JSON con el estado de toda la rejilla de sesión | ninguno |
| `fire_scene` | Lanza la escena correspondiente | `scene_index: int` |

### Dispositivos

| Comando | Descripción | Parámetros |
|---------|-------------|------------|
| `get_devices` | Lista los efectos e instrumentos de una pista | `track_index: int` |
| `set_device_parameter` | Modifica el valor de un parámetro del dispositivo | `track_index: int`, `device_index: int`, `param_index: int`, `value: float` |
| `add_device` | Inserta un dispositivo en la pista indicada | `track_index: int`, `device_name: str` |

---

## 5. Motor DSP Anti-Clash

El motor Anti-Clash procesa la señal de audio de salida máster del DAW en tiempo real. Divide el rango audible humano en 8 bandas clave y analiza la densidad de frecuencia para calcular el factor de interferencia y masking en la mezcla.

### Bandas Frecuenciales Analizadas

| # | Nombre | Rango de Frecuencias | Uso Musical Principal |
|---|--------|---------------------|-----------------------|
| 1 | **SUB** | 20 Hz - 60 Hz | Frecuencias subgraves, bombos pesados, sintetizadores sub |
| 2 | **BASS** | 60 Hz - 250 Hz | Cuerpo del bajo, pegada del bombo, frecuencias graves |
| 3 | **LO-MID** | 250 Hz - 500 Hz | Frecuencias medias-bajas, cuerpo de guitarras y sintetizadores |
| 4 | **MID** | 500 Hz - 2.000 Hz | Rango medio principal, voces, instrumentos solistas |
| 5 | **HI-MID** | 2.000 Hz - 4.000 Hz | Claridad, inteligibilidad vocal, ataque de redoblantes |
| 6 | **PRES** | 4.000 Hz - 8.000 Hz | Sibilancia vocal, brillo de platillos y efectos |
| 7 | **AIR** | 8.000 Hz - 16.000 Hz | Sensación de espacio, aire y definición en altas frecuencias |
| 8 | **ULTRA** | 16.000 Hz - 20.000 Hz | Frecuencias ultra-altas, brillo extremo y armónicos |

### Interpretación del Anti-Clash Score
El motor evalúa las relaciones frecuenciales y genera un porcentaje consolidado de claridad:
- **90% - 100%** 🟢 **Excelente**: Mezcla limpia, amplio rango dinámico y nula superposición destructiva.
- **70% - 90%** 🟡 **Aceptable**: Mezcla correcta. Puede haber leve acumulación de frecuencias graves.
- **50% - 70%** 🟠 **Precaución**: Enmascaramiento o conflicto severo. Se sugiere aplicar filtros ecualizadores de corte.
- **Menos de 50%** 🔴 **Crítico**: Colisión de frecuencias destructiva. Pérdida de inteligibilidad y dinámica.

---

## 6. Generación MIDI

El motor MIDI integrado permite automatizar la creación de clips musicales complejos con un solo comando.

### Estilos de Groove Disponibles

- **House (120-128 BPM)**: Ritmo clásico "four-on-the-floor" con bombo en negras, palmadas o redoblantes en los tiempos 2 y 4, e hihats en las corcheas intermedias.
- **Techno (128-140 BPM)**: Enfoque minimalista e hipnótico, hihats continuos en semicorcheas y síncopas de percusión.
- **Trap (140-150 BPM)**: Subdivisiones rápidas de hihats en tresillos de fusa, cajas espaciadas y síncopas de ritmo urbano.
- **DnB (170-180 BPM)**: Estructura sincopada clásica "snare-kick" veloz con acentos fantasmas de platillos.

### Modos de Escala Soportados
Los comandos de melodía permiten restringir las notas a tonalidades y modos específicos para mantener la consonancia harmónica:
- Modos clásicos: `major`, `minor`, `dorian`, `phrygian`, `lydian`, `mixolydian`, `pentatonic`, `blues`.

### Algoritmo de Humanización
Cuando se activa el parámetro `humanize=True`, el generador introduce variaciones realistas controladas:
- **Desviación de tiempo (Jitter)**: Mueve aleatoriamente el inicio de cada nota en un margen de ±20 milisegundos.
- **Desviación de dinámica (Velocity)**: Modifica aleatoriamente la velocidad MIDI de cada pulsación en ±8 unidades para simular la presión variante de los dedos de un músico.

### Undo Histórico
Para prevenir pérdidas accidentales de datos o partituras previas, todas las escrituras MIDI están envueltas en bloques transaccionales del DAW:
- Mediante llamadas a `begin_undo_step()` y `end_undo_step()`.
- Cualquier patrón generado puede deshacerse de forma nativa en Ableton Live presionando **Cmd+Z** en macOS o **Ctrl+Z** en Windows.

---

## 7. Seguridad

El sistema implementa medidas estrictas de aislamiento para garantizar la seguridad del ordenador en redes locales:
- **Binding de loopback**: El servidor TCP y WebSocket solo aceptan peticiones provenientes del host local (`127.0.0.1`), rechazando interfaces externas.
- **Autenticación criptográfica**: Un token temporal autogenerado de 32 bytes protege el canal contra escrituras desde scripts maliciosos del sistema.
- **Control de velocidad (Rate Limiting)**: Un límite estricto de 100 peticiones por segundo bloquea inmediatamente al cliente emisor por 5 segundos si se abusa del canal.
- **Control de búfer (Backpressure)**: El script almacena comandos en una cola FIFO limitada a 256 peticiones. Si la cola se satura, las peticiones excesivas se descartan para prevenir desbordamientos de memoria del proceso de Ableton.
- **Filtro de tamaño de mensaje**: Máximo de 64 KB por petición de socket para evitar exploits basados en el desbordamiento de búfer.

---

## 8. Solución de Problemas

### El indicador TCP en la interfaz gráfica no cambia a verde
1. Asegúrate de que Ableton Live esté abierto y reproduciendo o editando.
2. Confirma que la carpeta `AntigravityCore` se encuentra exactamente dentro del directorio de scripts MIDI de Ableton.
3. Abre las preferencias de Ableton Live > pestaña Link/MIDI y verifica que **AntigravityCore** esté seleccionado como Superficie de Control activa.
4. Si la app sigue sin conectar, cierra Ableton Live y vuelve a abrirlo para reiniciar el servidor de red.

### ¿Cómo ver los archivos de registro (logs) de depuración?
Puedes monitorear el comportamiento del Remote Script en tiempo real en la terminal ejecutando:
- En macOS / Linux:
  ```bash
  tail -f /tmp/antigravity_core.log
  ```
- En Windows (PowerShell):
  ```powershell
  Get-Content -Path "$env:TEMP\antigravity_core.log" -Wait
  ```

### Error de "Puerto 9001 ya en uso" (Address already in use)
Si el puerto 9001 está ocupado por una sesión colgada, puedes liberarlo ejecutando:
- En macOS / Linux:
  ```bash
  lsof -i :9001
  kill -9 [PID_OBTENIDO]
  ```
- En Windows (Cmd como administrador):
  ```cmd
  netstat -ano | findstr :9001
  taskkill /PID [PID_OBTENIDO] /F
  ```

### El visualizador de espectro (DSP) no muestra datos o no se mueve
1. Confirma que tienes instalados los módulos de dependencias del analizador:
   ```bash
   pip install numpy sounddevice websockets
   ```
2. Asegúrate de que el script independiente `dsp_engine.py` se está ejecutando correctamente en segundo plano y que tu DAW está reproduciendo audio en el bus de salida máster.

### Reinstalación limpia del sistema
1. Cierra Ableton Live y la aplicación de Antigravity.
2. Elimina por completo la carpeta `AntigravityCore` del directorio de Remote Scripts.
3. Vuelve a copiar una versión limpia desde la carpeta de distribución.
4. Reinicia Ableton Live y carga un nuevo set vacío.

---

*Antigravity AI Assistant V2.0.1*
*Produktes-code (Chus BZN) — 2025*
*github.com/produktes-code/ableton-ai-assistant*
