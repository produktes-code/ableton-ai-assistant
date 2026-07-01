const fs = require('fs');
const path = require('path');

const logDir = path.join(__dirname, 'logs');
if (!fs.existsSync(logDir)) {
    fs.mkdirSync(logDir);
}

const logFile = path.join(logDir, 'ableton_ai.log');

function getTimestamp() {
    return new Date().toISOString();
}

function writeLog(level, message, ...args) {
    const formattedArgs = args.map(a => typeof a === 'object' ? JSON.stringify(a) : a).join(' ');
    const logLine = `${getTimestamp()} - ableton_ai - ${level} - ${message} ${formattedArgs}\n`;
    
    // Escribir a archivo
    fs.appendFileSync(logFile, logLine);
}

module.exports = {
    info: (msg, ...args) => writeLog('INFO', msg, ...args),
    error: (msg, ...args) => writeLog('ERROR', msg, ...args),
    warn: (msg, ...args) => writeLog('WARN', msg, ...args)
};
