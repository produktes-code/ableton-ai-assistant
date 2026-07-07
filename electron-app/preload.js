const { contextBridge, ipcRenderer } = require('electron');
const fs = require('fs');
const path = require('path');

// Exponer de forma segura la API al proceso de renderizado (Frontend)
contextBridge.exposeInMainWorld('assistantAPI', {
    // Enviar comandos de texto (Prompt del usuario)
    sendCommand: (command) => ipcRenderer.send('send-command', command),
    
    // Enviar acciones directas de la UI (Sliders, Botones, Menús)
    sendAction: (actionObj) => ipcRenderer.send('send-action', actionObj),
    
    // Recibir respuestas
    onResponse: (callback) => ipcRenderer.on('command-response', (_event, value) => callback(value)),
    
    // Función Multimodal: Enviar ruta de archivo de audio soltado
    sendAudioReference: (filePath) => ipcRenderer.send('send-audio-reference', filePath),

    // Health Check
    healthCheck: () => ipcRenderer.send('health-check'),
    onHealthStatus: (callback) => ipcRenderer.on('health-status', (_event, status) => callback(status)),

    // Obtener traducciones sincrónicamente para evitar errores de fetch locales (CORS / file://)
    getTranslation: (lang) => {
        try {
            const filePath = path.join(__dirname, 'locales', `${lang}.json`);
            return JSON.parse(fs.readFileSync(filePath, 'utf8'));
        } catch(e) {
            console.error(`Error leyendo idioma ${lang}:`, e);
            return null;
        }
    }
});
