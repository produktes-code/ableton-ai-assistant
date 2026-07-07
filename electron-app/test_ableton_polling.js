const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const htmlPath = path.resolve(__dirname, 'index.html');
const htmlContent = fs.readFileSync(htmlPath, 'utf8');

// Mock setInterval
let intervalTime = null;
global.setInterval = (fn, time) => {
    intervalTime = time;
};

const dom = new JSDOM(htmlContent, {
    url: "http://localhost/",
    runScripts: 'dangerously',
    beforeParse(window) {
        window.setInterval = global.setInterval;
        window.assistantAPI = {
            onHealthStatus: () => {},
            healthCheck: () => {}
        };
        window.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    }
});

setTimeout(() => {
    if (intervalTime === 2000) {
        console.log("✅ TEST PASSED: Polling is correctly implemented with 2000ms via JSDOM.");
        process.exit(0);
    } else {
        console.error("❌ TEST FAILED: Polling not found or not 2000ms.");
        process.exit(1);
    }
}, 500);
