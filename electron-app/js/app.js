function addLog(level, message) {
  const term = document.getElementById('terminal-output');
  if (!term) return;
  const div = document.createElement('div');
  div.className = `log-line ${level}`;
  div.textContent = message;
  term.appendChild(div);
  if (term.childNodes.length > 200) {
    term.removeChild(term.firstChild);
  }
  term.scrollTop = term.scrollHeight;
}

function clearLog() {
  const term = document.getElementById('terminal-output');
  if (term) term.innerHTML = '';
}

function toggleTerminal() {
  const term = document.querySelector('.log-terminal');
  if (term) {
    term.style.height = term.style.height === '40px' ? '120px' : '40px';
  }
}

function transport(action) {
  if (action === 'play') {
    window.tcpClient.send('transport_play');
    document.getElementById('btn-play').classList.add('active');
  } else if (action === 'stop') {
    window.tcpClient.send('transport_stop');
    document.getElementById('btn-play').classList.remove('active');
    document.getElementById('btn-record').classList.remove('active');
  } else if (action === 'record') {
    window.tcpClient.send('transport_record');
    document.getElementById('btn-record').classList.toggle('active');
  }
}

function sendSuggestion(btn) {
  const input = document.getElementById('chat-input');
  if (input) {
    input.value = btn.textContent.trim();
    input.focus();
  }
}

function sendChat() {
  const input = document.getElementById('chat-input');
  if (!input) return;
  const text = input.value.trim();
  if (!text) return;
  
  addMessageToChat('user', text);
  input.value = '';
  
  const cmd = tryDirectCommand(text);
  if (cmd === null) {
    setTimeout(() => {
      addMessageToChat('assistant', 'Comando genérico procesado.');
    }, 500);
  }
}

function tryDirectCommand(text) {
  const lower = text.toLowerCase();
  if (lower.includes('play') || lower.includes('reproduce')) {
    window.tcpClient.send('transport_play');
    return 'play';
  }
  if (lower.includes('stop') || lower.includes('para')) {
    window.tcpClient.send('transport_stop');
    return 'stop';
  }
  if (lower.includes('bpm')) {
    window.tcpClient.send('set_bpm', {bpm: 120});
    return 'bpm';
  }
  if (lower.includes('lista') || lower.includes('pistas')) {
    window.tcpClient.send('get_all_tracks');
    return 'tracks';
  }
  if (lower.includes('house') || lower.includes('techno') || lower.includes('trap') || lower.includes('dnb')) {
    addLog('info', 'Generando groove...');
    return 'groove';
  }
  return null;
}

async function syncSession() {
  try {
    const bpmRes = await window.tcpClient.send('get_bpm');
    const bpmEl = document.getElementById('bpm-value');
    if (bpmEl && bpmRes && bpmRes.bpm) bpmEl.textContent = Math.round(bpmRes.bpm);
    
    const keyRes = await window.tcpClient.send('get_key');
    const keyEl = document.getElementById('key-value');
    if (keyEl && keyRes && keyRes.root_note !== undefined) keyEl.textContent = keyRes.root_note;
    
    const state = await window.tcpClient.send('get_session_state');
    if (state && state.tracks) renderTracks(state.tracks);
  } catch(e) {
    addLog('error', 'Sync failed');
  }
}

function addMessageToChat(role, text) {
  const history = document.getElementById('chat-history');
  if (!history) return;
  const div = document.createElement('div');
  div.className = `message ${role}-msg`;
  const avatar = role === 'user' ? '🎹' : '🎵';
  div.innerHTML = `<div class="msg-content"><p>${avatar} ${text}</p></div>`;
  history.appendChild(div);
  history.scrollTop = history.scrollHeight;
}

function autoResize(e) {
  e.target.style.height = 'auto';
  e.target.style.height = e.target.scrollHeight + 'px';
}

async function init() {
  addLog('info', 'Antigravity V2.0.0 iniciando...');
  window.tcpClient.onLog = (level, msg) => addLog(level, msg);
  window.tcpClient.onConnected = async () => {
    addLog('success', 'Conectado a Ableton Live');
    await syncSession();
  };
  window.tcpClient.onDisconnected = () => {
    addLog('warning', 'Desconectado. Reconectando...');
  };
  
  await window.tcpClient.connect();
  
  const sendBtn = document.getElementById('send-btn');
  if (sendBtn) sendBtn.addEventListener('click', sendChat);
  
  const input = document.getElementById('chat-input');
  if (input) {
    input.addEventListener('keydown', e => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendChat();
      }
    });
    input.addEventListener('input', autoResize);
  }
  
  const refreshBtn = document.getElementById('refresh-session');
  if (refreshBtn) refreshBtn.addEventListener('click', syncSession);
  
  setInterval(syncSession, 10000);
  addLog('success', 'Antigravity V2.0.0 listo.');
}

document.addEventListener('DOMContentLoaded', init);
