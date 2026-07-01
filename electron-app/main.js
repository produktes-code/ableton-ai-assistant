const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const net = require('net');

// Lógica de conexión con Ableton (TCP)
const ABLETON_HOST = '127.0.0.1';
const ABLETON_PORT = 9001;
let tcpClient = null;

function connectToAbleton() {
    tcpClient = new net.Socket();
    tcpClient.connect(ABLETON_PORT, ABLETON_HOST, () => {
        console.log('Conectado al Remote Script de Ableton (Puerto 9001).');
    });

    tcpClient.on('data', (data) => {
        console.log('Datos recibidos de Ableton:', data.toString());
    });

    tcpClient.on('error', (err) => {
        console.error('Error TCP con Ableton:', err.message);
    });
}

// Configuración segura de Electron
function createWindow() {
    const win = new BrowserWindow({
        width: 400,
        height: 700,
        titleBarStyle: 'hiddenInset',
        backgroundColor: '#16130b', // Surface color de Stitch
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js')
        }
    });

    win.loadFile('index.html');
}

app.whenReady().then(() => {
    createWindow();
    // Iniciar conexión con Ableton en background
    connectToAbleton();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

// --- IPC Listeners (API Letal Multimodal) ---

ipcMain.on('send-command', (event, commandText) => {
    console.log(`[Prompt Usuario] Recibido texto: ${commandText}`);
    // En un entorno real de producción, esto iría al LLM (Claude) para generar JSON.
    // Por ahora lo enviamos como acción de chat al servidor para no romper el socket.
    if (tcpClient && !tcpClient.destroyed) {
        try {
            tcpClient.write(JSON.stringify({ action: "chat", payload: { text: commandText } }) + "\n");
        } catch(e) {}
    }
});

// Novedad Fase 13: Acciones Estructuradas Directas
ipcMain.on('send-action', (event, actionObj) => {
    console.log(`[Acción UI] Ejecutando:`, actionObj);
    if (tcpClient && !tcpClient.destroyed) {
        try {
            // Se envía el JSON puro tal cual lo requiere el módulo The Mix Engineer en Python
            tcpClient.write(JSON.stringify(actionObj) + "\n");
        } catch(e) {
            console.error("Error enviando acción TCP:", e);
        }
    }
});

ipcMain.on('send-audio-reference', (event, filePath) => {
    console.log(`[Multimodal] Referencia de audio soltada: ${filePath}`);
    // Aquí el servidor MCP/Librosa analizaría el archivo (Timbre/EQ Match)
    event.reply('command-response', `Audio ${path.basename(filePath)} cargado para análisis.`);
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
