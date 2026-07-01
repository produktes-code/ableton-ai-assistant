class RateLimiter {
    constructor(limit, windowMs) {
        this.limit = limit;
        this.windowMs = windowMs;
        this.requests = [];
    }

    checkLimit() {
        const now = Date.now();
        // Eliminar peticiones más antiguas que la ventana de tiempo
        this.requests = this.requests.filter(timestamp => now - timestamp < this.windowMs);
        
        if (this.requests.length >= this.limit) {
            return false; // Bloquear
        }
        
        this.requests.push(now);
        return true; // Permitir
    }
}

// Límite de TCP: 100 mensajes por segundo
const tcpLimiter = new RateLimiter(100, 1000);

module.exports = tcpLimiter;
