# Antigravity AI Assistant V2.0.1

[![CI](https://github.com/produktes-code/ableton-ai-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/produktes-code/ableton-ai-assistant/actions/workflows/ci.yml)
[![Build](https://github.com/produktes-code/ableton-ai-assistant/actions/workflows/build_v2.yml/badge.svg)](https://github.com/produktes-code/ableton-ai-assistant/actions/workflows/build_v2.yml)
[![Version](https://img.shields.io/badge/version-2.0.1-8a2be2)](https://github.com/produktes-code/ableton-ai-assistant/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Qué es Antigravity V2.0.1
Antigravity AI Assistant es un copiloto de producción musical de última generación para **Ableton Live**. Integra control de la API de Live (LOM), generación avanzada de clips MIDI y análisis espectral de audio en tiempo real con una interfaz gráfica oscura y translúcida basada en Glassmorphism.

## Novedades V2.0.1
- **Compatibilidad ESM y Node 18 LTS**: Solución al conflicto `ERR_REQUIRE_ESM` de blake2.js usando Node 18 LTS y electron-builder 25.x.
- **Robustez en Test Suite**: Solución a conflictos de puerto `Errno 98` mediante el uso de puertos efímeros dinámicos en tests de integración.
- **Seguridad en MCP SDK**: Dependencia `mcp` actualizada a `>=1.28.1` libre de vulnerabilidades.
- **Release Automatizado**: Empaquetado multiplataforma integrado con corrección del repositorio remoto en `package.json`.

## Instalación rápida
1. **Script MIDI**: Copia el directorio `remote-script/AntigravityCore` en tu carpeta de *MIDI Remote Scripts* de Ableton Live.
2. **Seleccionar Superficie**: Abre Ableton Live, ve a Preferencias > Link/Tempo/MIDI y selecciona **AntigravityCore**.
3. **Interfaz de Usuario**:
   ```bash
   cd electron-app
   npm install
   npm start
   ```

## Arquitectura del sistema
El sistema se compone de tres módulos desacoplados:
- **Ableton Script (Python 3)**: Servidor TCP multi-hilo integrado en Ableton Live que expone la API del Live Object Model de manera no bloqueante.
- **DSP Engine (Python 3 / Asyncio)**: Subproceso dedicado al análisis de frecuencia y detección de choques de mezcla en tiempo real.
- **Electron UI (HTML5 / Vanilla CSS / JS)**: Aplicación de escritorio moderna que interactúa con Ableton y visualiza los datos espectrales a 60fps por WebSockets.

## Comandos LOM disponibles
A través de `CommandRegistry`, el sistema ofrece 39+ comandos autodescubiertos estructurados en:
- `play`, `stop`, `set_bpm`, `get_bpm` (Transporte)
- `list_tracks`, `create_track`, `set_track_volume` (Pistas)
- `create_clip`, `add_notes`, `quantize_notes` (Clips/MIDI)
- `list_devices`, `set_device_parameter` (Dispositivos)

## Motor DSP Anti-Clash
Procesa el flujo de audio en tiempo real a través de una FFT de 2048 muestras a 44100Hz:
- Divide el espectro en **8 bandas espectrales**.
- Calcula dinámicamente un **Anti-Clash Score** para advertir sobre choques de frecuencia y enmascaramiento.
- Genera un vector de croma simplificado para identificar armónicos dominantes.

## Tests (python tests/run_all_tests.py)
Incluye una suite de validación completa (unitarios, integración y estrés):
```bash
python3 tests/run_all_tests.py
```
*Garantiza 8/8 suites exitosas y 0 fallos críticos antes de cada compilación.*

## Seguridad
- Token de autenticación único autogenerado en cada sesión.
- Límite de tráfico de mensajes (hasta 64KB por payload).
- Control de tasa de peticiones (Rate Limit de 100 req/s con bloqueo IP automático).
- Cola FIFO con capacidad para 256 comandos para evitar sobrecarga (Backpressure).

## Compatibilidad
- **Ableton Live**: Versiones 11 y 12 (Standard / Suite).
- **OS**: macOS (Intel/M1/M2/M3/M4), Windows 10/11 y Linux (Ubuntu/Debian).

## Changelog
- **v2.0.1**: Build Fix, actualización de dependencias, soporte para Node 18, y puertos efímeros en integración.
- **v2.0.0**: Migración a CommandRegistry, motor DSP Anti-Clash aislado, seguridad TCP e interfaz Glassmorphism.
