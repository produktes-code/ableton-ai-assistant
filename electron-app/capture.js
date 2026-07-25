const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Set viewport to a nice desktop size
  await page.setViewport({ width: 1200, height: 800 });
  
  // Load the index.html file
  const filePath = `file://${path.join(__dirname, 'index.html')}`;
  await page.goto(filePath, { waitUntil: 'networkidle0' });
  
  // Take a screenshot of the whole page
  await page.screenshot({ 
      path: path.join(__dirname, '../docs/screenshot-UI.png'),
      fullPage: true 
  });

  await browser.close();
  console.log('Screenshot captured successfully.');
})();
