class TCPClient {
  constructor() {
    this.host = '127.0.0.1';
    this.port = 9001;
    this.token = null;
    this.connected = false;
    this.reconnectDelay = 2000;
    this.pendingRequests = new Map();
    this.messageQueue = [];
    this.requestIdCounter = 0;
    this.onConnected = null;
    this.onDisconnected = null;
    this.onLog = null;
    this.socket = null;
  }

  connect() {
    try {
      const net = window.require ? window.require('net') : null;
      if (!net) {
        this._log('warning', 'Node net not available, using mock');
        setTimeout(() => {
          this._handleData(JSON.stringify({token: 'mock-token'}));
        }, 500);
        return;
      }
      this.socket = new net.Socket();
      this.socket.connect(this.port, this.host, () => {
        this._discover();
      });
      this.socket.on('data', data => this._handleData(data.toString()));
      this.socket.on('close', () => {
        this.connected = false;
        this._updateStatusUI(false);
        if (this.onDisconnected) this.onDisconnected();
        setTimeout(() => this.connect(), this.reconnectDelay);
      });
      this.socket.on('error', err => this._log('error', err.message));
    } catch (e) {
      this._log('error', e.message);
    }
  }

  _discover() {
    this.socket.write(JSON.stringify({action:"discover", protocol:"2"}) + "\n");
  }

  _handleData(rawText) {
    try {
      const data = JSON.parse(rawText);
      if (data.token) {
        this.token = data.token;
        this.connected = true;
        this._updateStatusUI(true);
        this._flushQueue();
        if (this.onConnected) this.onConnected();
      }
      if (data.id && this.pendingRequests.has(data.id)) {
        this.pendingRequests.get(data.id).resolve(data);
        this.pendingRequests.delete(data.id);
      }
    } catch (e) {
      this._log('error', 'Parse error');
    }
  }

  send(action, params={}) {
    return new Promise((resolve, reject) => {
      const id = ++this.requestIdCounter;
      const msg = { action, params, id, token: this.token };
      
      this.pendingRequests.set(id, { resolve, reject });
      setTimeout(() => {
        if (this.pendingRequests.has(id)) {
          this.pendingRequests.get(id).reject(new Error('Timeout'));
          this.pendingRequests.delete(id);
        }
      }, 5000);

      const payload = JSON.stringify(msg) + "\n";
      
      if (this.connected && this.socket) {
        this.socket.write(payload);
        this._log('info', `Sent: ${action}`);
      } else if (this.connected) {
        this._log('info', `Mock sent: ${action}`);
        setTimeout(() => resolve({status:"ok", id}), 100);
      } else {
        this.messageQueue.push(payload);
        this._log('info', `Queued: ${action}`);
      }
    });
  }

  _flushQueue() {
    while (this.messageQueue.length > 0) {
      const msg = this.messageQueue.shift();
      if (this.socket) this.socket.write(msg);
    }
  }

  _updateStatusUI(connected) {
    const dot = document.getElementById('tcp-dot');
    const label = document.getElementById('tcp-label');
    if (dot) dot.className = connected ? 'dot connected' : 'dot error';
    if (label) label.textContent = connected ? 'Conectado' : 'Desconectado';
  }

  _log(level, message) {
    const ts = new Date().toLocaleTimeString();
    if (this.onLog) this.onLog(level, `[${ts}] ${message}`);
  }
}

window.tcpClient = new TCPClient();
