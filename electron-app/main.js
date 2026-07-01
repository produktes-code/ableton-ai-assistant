const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const net = require('net');
const fs = require('fs');
const logger = require('./logger');
const tcpLimiter = require('./rateLimiter');

// Lógica de conexión con Ableton (TCP)
const ABLETON_HOST = '127.0.0.1';
const ABLETON_PORT = 9001;
let tcpClient = null;

function connectToAbleton() {
    tcpClient = new net.Socket();
    tcpClient.connect(ABLETON_PORT, ABLETON_HOST, () => {
        logger.info('Conectado al Remote Script de Ableton (Puerto 9001).');
    });

    tcpClient.on('data', (data) => {
        logger.info('Datos recibidos de Ableton:', data.toString());
    });

    tcpClient.on('error', (err) => {
        logger.error('Error TCP con Ableton:', err.message);
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
    logger.info(`[Prompt Usuario] Recibido texto: ${commandText}`);
    if (tcpClient && !tcpClient.destroyed) {
        if (!tcpLimiter.checkLimit()) {
            logger.warn('Rate limit excedido en TCP command');
            return;
        }
        try {
            tcpClient.write(JSON.stringify({ action: "chat", payload: { text: commandText } }) + "\n");
        } catch(e) {
            logger.error("Error enviando command TCP:", e.message);
        }
    }
});

ipcMain.on('send-action', (event, actionObj) => {
    logger.info(`[Acción UI] Ejecutando:`, actionObj);
    if (tcpClient && !tcpClient.destroyed) {
        if (!tcpLimiter.checkLimit()) {
            logger.warn('Rate limit excedido en TCP action');
            return;
        }
        try {
            tcpClient.write(JSON.stringify(actionObj) + "\n");
        } catch(e) {
            logger.error("Error enviando acción TCP:", e.message);
        }
    }
});

ipcMain.on('send-audio-reference', (event, filePath) => {
    try {
        const stats = fs.statSync(filePath);
        const MAX_SIZE = 2 * 1024 * 1024 * 1024; // 2GB
        if (stats.size > MAX_SIZE) {
            logger.error(`Error: Archivo supera 2GB (${filePath})`);
            event.reply('command-response', `Error: El archivo supera el límite de 2GB.`);
            return;
        }
        logger.info(`[Multimodal] Referencia de audio soltada: ${filePath} (Tamaño OK)`);
        event.reply('command-response', `Audio ${path.basename(filePath)} verificado (Tamaño OK).`);
    } catch(e) {
        logger.error(`Error procesando audio:`, e.message);
    }
});

// Health Check IPC
ipcMain.on('health-check', (event) => {
    const isConnected = tcpClient && !tcpClient.destroyed && !tcpClient.connecting;
    const status = {
        tcp_connected: isConnected,
        osc_ready: true, // Simulado en esta capa
        midi_ready: true, // Simulado en esta capa
        timestamp: new Date().toISOString()
    };
    logger.info(`Health check solicitado: ${JSON.stringify(status)}`);
    event.reply('health-status', status);
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
