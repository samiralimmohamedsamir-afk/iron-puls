// captures.js — captures d'écran mobile (375 px) et ordinateur (1280 px) pour le test responsive.
// Usage : node outils/captures.js page.html [dossier_sortie]
// Signale aussi tout défilement horizontal (contenu plus large que l'écran).
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const page = process.argv[2] || 'index.html';
  const sortie = process.argv[3] || '/tmp/captures';
  require('fs').mkdirSync(sortie, { recursive: true });
  const navigateur = await chromium.launch();
  for (const largeur of [375, 768, 1280]) {
    const onglet = await navigateur.newPage({ viewport: { width: largeur, height: 900 } });
    await onglet.goto('file://' + path.resolve(page));
    await onglet.waitForTimeout(300);
    const debord = await onglet.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    const nom = `${sortie}/${path.basename(page, '.html')}-${largeur}.png`;
    await onglet.screenshot({ path: nom, fullPage: true });
    console.log(`${nom}${debord > 0 ? `  ATTENTION : débordement horizontal de ${debord}px` : '  OK (pas de débordement)'}`);
    await onglet.close();
  }
  await navigateur.close();
})();
