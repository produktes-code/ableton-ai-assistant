class DSPVisualizer {
  constructor() {
    this.wsUrl = 'ws://127.0.0.1:9002';
    this.canvas = document.getElementById('spectrogram-canvas');
    this.chromaCanvas = document.getElementById('chroma-canvas');
    this.ctx = this.canvas ? this.canvas.getContext('2d') : null;
    this.chromaCtx = this.chromaCanvas ? this.chromaCanvas.getContext('2d') : null;
    this.frozen = false;
    this.currentData = {bands: new Array(8).fill(0), chroma: new Array(12).fill(0), anti_clash_score: 1.0, lufs: -100};
    this.targetData = {bands: new Array(8).fill(0), chroma: new Array(12).fill(0), anti_clash_score: 1.0, lufs: -100};
    this.BAND_COLORS = ['#ff3366', '#ff8833', '#ffd700', '#aaff00', '#00ff88', '#00d4ff', '#3366ff', '#8a2be2'];
    this.NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
    
    this._bindEvents();
    this._connect();
    this._startRenderLoop();
  }

  _connect() {
    try {
      this.ws = new WebSocket(this.wsUrl);
      this.ws.onmessage = (e) => {
        if (!this.frozen) {
          try {
            this.targetData = JSON.parse(e.data);
            this._updateMetrics(this.targetData);
          } catch(err){}
        }
      };
      this.ws.onclose = () => {
        setTimeout(() => this._connect(), 3000);
      };
      this.ws.onerror = () => {};
    } catch(e) {}
  }

  _startRenderLoop() {
    const render = () => {
      this._interpolate(0.12);
      this._drawBands();
      this._drawChroma();
      requestAnimationFrame(render);
    };
    requestAnimationFrame(render);
  }

  _interpolate(factor) {
    if (!this.targetData.bands) return;
    for(let i=0; i<8; i++) {
      this.currentData.bands[i] += (this.targetData.bands[i] - this.currentData.bands[i]) * factor;
    }
    for(let i=0; i<12; i++) {
      this.currentData.chroma[i] += (this.targetData.chroma[i] - this.currentData.chroma[i]) * factor;
    }
  }

  _drawBands() {
    if (!this.ctx) return;
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.fillStyle = 'rgba(0,0,0,0.4)';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    
    const w = this.canvas.width / 8;
    for (let i=0; i<8; i++) {
      const val = this.currentData.bands[i] || 0;
      const h = val * (this.canvas.height - 10);
      const x = i * w + 5;
      const y = this.canvas.height - h;
      
      this.ctx.fillStyle = this.BAND_COLORS[i];
      if (val > 0.05) {
        this.ctx.shadowBlur = 10;
        this.ctx.shadowColor = this.BAND_COLORS[i];
      } else {
        this.ctx.shadowBlur = 0;
      }
      this.ctx.fillRect(x, y, w-10, h);
    }
    this.ctx.shadowBlur = 0;
  }

  _drawChroma() {
    if (!this.chromaCtx) return;
    this.chromaCtx.clearRect(0, 0, this.chromaCanvas.width, this.chromaCanvas.height);
    const w = this.chromaCanvas.width / 12;
    for (let i=0; i<12; i++) {
      const val = this.currentData.chroma[i] || 0;
      this.chromaCtx.fillStyle = `rgba(138,43,226,${0.2 + val * 0.8})`;
      this.chromaCtx.fillRect(i*w + 2, 10, w-4, this.chromaCanvas.height-30);
      
      this.chromaCtx.fillStyle = '#fff';
      this.chromaCtx.font = '10px monospace';
      this.chromaCtx.fillText(this.NOTE_NAMES[i], i*w + 6, this.chromaCanvas.height - 5);
    }
  }

  _updateMetrics(data) {
    const lufsEl = document.getElementById('lufs-value');
    if (lufsEl) lufsEl.textContent = data.lufs ? data.lufs.toFixed(1) : '-100';
    
    const clashEl = document.getElementById('clash-value');
    const fillEl = document.getElementById('clash-meter-fill');
    if (clashEl && data.anti_clash_score !== undefined) {
      const score = data.anti_clash_score;
      clashEl.textContent = (score * 100).toFixed(0) + '%';
      if (score > 0.8) clashEl.style.color = '#00ff88';
      else if (score > 0.5) clashEl.style.color = '#ffd700';
      else clashEl.style.color = '#ff3366';
      
      if (fillEl) fillEl.style.width = (score * 100) + '%';
    }
  }

  _bindEvents() {
    const btn = document.getElementById('freeze-btn');
    if (btn) {
      btn.addEventListener('click', () => {
        this.frozen = !this.frozen;
        btn.textContent = this.frozen ? 'Unfreeze' : 'Freeze';
      });
    }
  }
}

window.dspVisualizer = new DSPVisualizer();
