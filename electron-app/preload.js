const { contextBridge, ipcRenderer } = require('electron');

// Exponer de forma segura la API al proceso de renderizado (Frontend)
contextBridge.exposeInMainWorld('antigravityAPI', {
    // Enviar comandos de texto (Prompt del usuario)
    sendCommand: (command) => ipcRenderer.send('send-command', command),
    
    // Enviar acciones directas de la UI (Sliders, Botones, Menús)
    sendAction: (actionObj) => ipcRenderer.send('send-action', actionObj),
    
    // Recibir respuestas
    onResponse: (callback) => ipcRenderer.on('command-response', (_event, value) => callback(value)),
    
    // Función Multimodal: Enviar ruta de archivo de audio soltado
    sendAudioReference: (filePath) => ipcRenderer.send('send-audio-reference', filePath)
});
