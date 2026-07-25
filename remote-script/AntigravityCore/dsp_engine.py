import sys
import time
import asyncio
import logging
from collections import deque
import json

try:
    import numpy as np
    import sounddevice as sd
    import websockets
except ImportError as e:
    print(f"Error importando dependencias DSP: {e}", file=sys.stderr)
    sys.exit(1)

# Configuración y Constantes
SAMPLE_RATE = 44100
N_FFT = 2048
BLOCK_SIZE = 2048
N_BANDS = 8
WS_PORT = 9002
UPDATE_INTERVAL = 0.050

BAND_EDGES = [20, 60, 250, 500, 2000, 4000, 8000, 16000, 20000]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - DSP - %(levelname)s - %(message)s')
logger = logging.getLogger('DSPEngine')

audio_buffer = deque(maxlen=N_FFT * 4)
clients = set()

def audio_callback(indata, frames, time_info, status):
    if status:
        logger.warning(f"Audio status: {status}")
    if indata.shape[1] > 1:
        mono = np.mean(indata, axis=1)
    else:
        mono = indata[:, 0]
    audio_buffer.extend(mono.tolist())

def _empty_response():
    return {
        "bands": [0.0] * N_BANDS,
        "lufs": -100.0,
        "peak_db": -100.0,
        "rms_db": -100.0,
        "chroma": [0.0] * 12,
        "spectral_centroid": 0.0,
        "anti_clash_score": 1.0,
        "timestamp": time.time()
    }

def analyze_spectrum(data):
    if len(data) < N_FFT:
        return _empty_response()
        
    window = np.hanning(N_FFT)
    chunk = np.array(data[-N_FFT:]) * window
    
    fft_result = np.fft.rfft(chunk)
    magnitudes = np.abs(fft_result) / N_FFT
    
    freqs = np.fft.rfftfreq(N_FFT, 1.0 / SAMPLE_RATE)
    
    bands = np.zeros(N_BANDS)
    for i in range(N_BANDS):
        low, high = BAND_EDGES[i], BAND_EDGES[i+1]
        idx = np.where((freqs >= low) & (freqs < high))[0]
        if len(idx) > 0:
            bands[i] = np.mean(magnitudes[idx])
            
    max_band = np.max(bands)
    if max_band > 0:
        bands = bands / max_band
        
    rms = np.sqrt(np.mean(chunk**2))
    rms_db = 20 * np.log10(rms + 1e-9)
    peak_db = 20 * np.log10(np.max(np.abs(chunk)) + 1e-9)
    lufs = rms_db - 0.691
    
    chroma = np.zeros(12)
    for i, f in enumerate(freqs):
        if f > 20:
            midi_note = 69 + 12 * np.log2(f / 440.0)
            pitch_class = int(round(midi_note)) % 12
            chroma[pitch_class] += magnitudes[i]
            
    max_chroma = np.max(chroma)
    if max_chroma > 0:
        chroma = chroma / max_chroma
        
    spectral_centroid = np.sum(freqs * magnitudes) / (np.sum(magnitudes) + 1e-9)
    
    sub_bass = bands[0]
    bass = bands[1]
    low_mid = bands[2]
    mid = bands[3]
    presence = bands[5]
    air = bands[6]
    
    low_clash = (sub_bass * bass) * 0.3
    mid_clash = (low_mid * mid) * 0.2
    clarity_bonus = (presence + air) * 0.15
    score = 1.0 - low_clash - mid_clash + clarity_bonus
    score = max(0.0, min(1.0, score))
    
    return {
        "bands": bands.tolist(),
        "lufs": float(lufs),
        "peak_db": float(peak_db),
        "rms_db": float(rms_db),
        "chroma": chroma.tolist(),
        "spectral_centroid": float(spectral_centroid),
        "anti_clash_score": float(score),
        "timestamp": time.time()
    }

async def ws_handler(websocket, path):
    clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        clients.remove(websocket)

async def broadcast_loop():
    while True:
        if clients:
            data = analyze_spectrum(list(audio_buffer))
            msg = json.dumps(data)
            to_remove = set()
            for ws in clients:
                try:
                    await ws.send(msg)
                except websockets.exceptions.ConnectionClosed:
                    to_remove.add(ws)
            for ws in to_remove:
                clients.remove(ws)
        await asyncio.sleep(UPDATE_INTERVAL)

async def main():
    logger.info("Iniciando DSPEngine...")
    try:
        stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            blocksize=BLOCK_SIZE,
            callback=audio_callback
        )
        stream.start()
    except Exception as e:
        logger.error(f"Error iniciando sounddevice: {e}")
        await asyncio.sleep(1)
    
    # Python <= 3.8 compat websockets setup
    start_server = websockets.serve(ws_handler, "127.0.0.1", WS_PORT)
    await start_server
    logger.info(f"WebSocket server escuchando en ws://127.0.0.1:{WS_PORT}")
    
    await broadcast_loop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("DSPEngine detenido.")
    except Exception as e:
        logger.error(f"Error fatal: {e}")
