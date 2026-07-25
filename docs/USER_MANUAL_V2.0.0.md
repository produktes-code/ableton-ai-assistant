# Antigravity V2.0.0 - Manual de Usuario Oficial

## Introducción
Bienvenido a Antigravity V2.0.0, la herramienta de Inteligencia Artificial más avanzada para Ableton Live. Esta versión representa un rediseño completo del sistema de comunicación, la interfaz visual y el procesamiento digital de señales (DSP). El asistente actúa como un puente directo entre tu entorno de producción y modelos de lenguaje avanzados, permitiendo el control LOM, análisis de audio e interactividad total.

## Instalación
Para instalar y configurar el sistema:
1. Asegúrate de tener instalado Ableton Live 11 o 12.
2. Copia la carpeta `remote-script/AntigravityCore` en la ruta de MIDI Remote Scripts de tu sistema Ableton.
3. En las preferencias de Ableton, selecciona `AntigravityCore` como superficie de control.
4. Entra en la carpeta `electron-app`, ejecuta `npm install` para instalar las dependencias y luego inicia la interfaz gráfica con `npm start`.

## Arquitectura
La arquitectura de Antigravity V2.0.0 está dividida en tres componentes aislados y especializados para garantizar estabilidad y rendimiento crítico:
1. **Ableton Remote Script**: Implementado en Python sobre la API oficial de Ableton Live (LOM). Ejecuta un servidor TCP en un hilo seguro utilizando mecanismos de control que previenen cualquier congelamiento de la aplicación musical.
2. **DSP Engine**: Un subproceso Python independiente que analiza la salida de audio del sistema mediante WebSocket para proveer visualización espectral e indicadores de choque frecuencial en tiempo real.
3. **Electron UI**: La interfaz de usuario construida con estética Glassmorphism, que se conecta al script TCP y al WebSocket del DSP para presentar los visualizadores a 60fps y el chat interactivo.

## Comandos LOM
El sistema cuenta con un robusto registro de comandos (`CommandRegistry`) auto-descubierto que incluye 39+ comandos organizados en los siguientes dominios:
- **Transport**: Comandos para iniciar (`play`), detener (`stop`), y cambiar el BPM del set.
- **Tracks**: Comandos para listar pistas (`list_tracks`), añadir nuevas pistas de audio/MIDI y alterar sus propiedades (solo, mute, volumen).
- **Clips**: Comandos para crear, manipular y secuenciar clips de notas musicales.
- **Devices**: Comandos para listar dispositivos instalados y mapear sus parámetros en tiempo real.
- **Mixer**: Ajustes finos de envíos, retorno y mezcla maestro.

## Motor DSP Anti-Clash
El motor DSP Anti-Clash se ejecuta en un proceso aislado y analiza el espectro de audio mediante una FFT en tiempo real segmentada en 8 bandas espectrales críticas:
- Bandas de sub-graves, graves, medios-bajos, medios, medios-altos, presencia, brillo y aire.
- Genera un **Anti-Clash Score** heurístico de 0 a 100 indicando la claridad de la mezcla.
- Realiza un análisis HPCP (Harmonic Pitch Class Profile) simplificado para detectar tonalidades dominantes.
- Los datos se envían a través de un WebSocket a la interfaz de usuario con una tasa de muestreo interna de 20fps interpolada a 60fps.

## Generación MIDI
El generador MIDI V2 permite la creación instantánea de contenido musical de alta calidad:
- **Grooves predefinidos**: Generación automática de patrones rítmicos para géneros como House, Techno, Trap y DnB.
- **Escalas musicales**: Creación de melodías y acordes adaptados en 8 escalas clásicas (Mayor, Menor Natural, Menor Armónica, Pentatónica, Dórica, etc.).
- **Humanización probabilística**: Introduce pequeños retardos (jitter) y variaciones de velocidad (velocity) para simular una interpretación humana natural.
- **Undo Histórico**: Sistema de paso atrás para revertir los cambios MIDI fácilmente usando comandos locales.

## Seguridad
El blindaje de seguridad de la conexión de red TCP incluye:
- **Token de Sesión Único**: Generado de forma dinámica al arrancar para evitar accesos no autorizados.
- **Rate Limiter**: Límite estricto de 100 peticiones por segundo, con bloqueo automático del cliente infractor.
- **Validación de Mensajes**: Rechazo automático de mensajes que superen los 64KB de tamaño para evitar ataques de denegación de servicio.
- **Backpressure FIFO**: Cola de procesamiento estructurada de hasta 256 comandos antes del descarte seguro.

## Solución de problemas
Si encuentras algún inconveniente con el sistema, consulta las siguientes soluciones comunes:
- **Error de puerto ocupado**: Verifica que no haya otra instancia del servidor TCP corriendo en el puerto 19001 o del websocket en el 9002.
- **Retardo en visualización**: Asegúrate de que el proceso DSP Engine no esté consumiendo más del 15% de CPU. Si es así, aumenta el tamaño del búfer de audio en la configuración.
- **Problemas de conexión**: Comprueba que el script MIDI esté seleccionado en Ableton y que el token de sesión sea el correcto.
