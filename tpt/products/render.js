// Render pack.html to an A4 PDF with page-number footers (skipped on the cover).
const { chromium } = require('playwright');
const [,, src, out, footer] = process.argv;  // footer = product title, or omit for none
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(src), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: !!footer, headerTemplate: '<span></span>',
    footerTemplate: `<div style="width:100%;margin:0 18mm;font:7pt Lato,sans-serif;color:#5b6475;display:flex;justify-content:space-between;border-top:0.5px solid #e2dccf;padding-top:4px">
      <span><b style="color:#16233f;letter-spacing:.12em">PASSWITHPURPOSE</b> · ${footer}</span><span class="pageNumber"></span></div>`,
  });
  await browser.close();
})();
