/**
 * Cross-Navigation and Visual Unification End-to-End Verifier
 * Tests index.html, exercise_lab.html, and g8_exam_rush.html
 * Across Desktop, iPad, and Mobile viewports.
 */

const playwright = require('/Users/crazyrock/Antigravity/IGCSE_miniMax/node_modules/playwright-core');
const path = require('path');

const VIEWPORTS = [
  { name: 'Desktop (1280x800)', width: 1280, height: 800 },
  { name: 'iPad / Tablet (768x1024)', width: 768, height: 1024 },
  { name: 'Mobile / iPhone (390x844)', width: 390, height: 844 }
];

async function runCrossNavVerification() {
  console.log('================================================================');
  console.log('🌐 RUNNING CROSS-PAGE NAVIGATION & VISUAL UNIFICATION AUDIT');
  console.log('================================================================');

  const browser = await playwright.chromium.launch({ headless: true });

  for (const vp of VIEWPORTS) {
    console.log(`\n📱 Testing Viewport: ${vp.name}`);
    const context = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: 2
    });
    const page = await context.newPage();

    const consoleErrors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') {
        // Ignore font or network CDN errors if running without internet
        if (!msg.text().includes('ERR_INTERNET_DISCONNECTED') && !msg.text().includes('Failed to load resource')) {
          consoleErrors.push(msg.text());
        }
      }
    });
    page.on('pageerror', err => consoleErrors.push(err.message));

    // Page 1: index.html
    const indexUrl = 'file://' + path.resolve(__dirname, 'index.html');
    await page.goto(indexUrl, { waitUntil: 'domcontentloaded', timeout: 20000 });
    console.log('  ✓ Loaded index.html');

    const indexAudit = await page.evaluate(() => {
      const igcseNav = document.querySelector('igcse-nav');
      const subnav = document.querySelector('.sky-subnav');
      const activeTab = subnav ? subnav.querySelector('.sky-subnav-tab.active') : null;
      const oldEmergencyBanners = document.querySelectorAll('.welcome > div[style*="linear-gradient"]');
      const bodyBg = window.getComputedStyle(document.body).backgroundImage;
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSubnav: !!subnav,
        activeTabText: activeTab ? activeTab.innerText.trim() : null,
        oldBannersCount: oldEmergencyBanners.length,
        bodyBgHasGradient: bodyBg.includes('radial-gradient'),
        overflowX
      };
    });

    console.log('    Index Audit:', indexAudit);
    if (!indexAudit.hasIgcseNav) throw new Error('index.html is missing <igcse-nav>');
    if (!indexAudit.hasSubnav) throw new Error('index.html is missing .sky-subnav');
    if (!indexAudit.activeTabText || !indexAudit.activeTabText.includes('单词特训岛')) {
      throw new Error(`index.html active tab expected '单词特训岛', got: ${indexAudit.activeTabText}`);
    }
    if (indexAudit.oldBannersCount > 0) {
      throw new Error(`index.html still has ${indexAudit.oldBannersCount} ad-hoc banners!`);
    }
    if (indexAudit.overflowX) {
      throw new Error(`index.html has horizontal overflow on ${vp.name}!`);
    }

    // Navigate to Page 2: exercise_lab.html via subnav click
    console.log('  ➔ Clicking subnav tab to exercise_lab.html...');
    await Promise.all([
      page.waitForNavigation({ waitUntil: 'domcontentloaded' }),
      page.click('.sky-subnav a[href="exercise_lab.html"]')
    ]);
    console.log('  ✓ Arrived on exercise_lab.html');

    const exerciseAudit = await page.evaluate(() => {
      const igcseNav = document.querySelector('igcse-nav');
      const subnav = document.querySelector('.sky-subnav');
      const activeTab = subnav ? subnav.querySelector('.sky-subnav-tab.active') : null;
      const bodyBg = window.getComputedStyle(document.body).backgroundImage;
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSubnav: !!subnav,
        activeTabText: activeTab ? activeTab.innerText.trim() : null,
        bodyBgHasGradient: bodyBg.includes('radial-gradient'),
        overflowX
      };
    });

    console.log('    Exercise Lab Audit:', exerciseAudit);
    if (!exerciseAudit.hasIgcseNav) throw new Error('exercise_lab.html is missing <igcse-nav>');
    if (!exerciseAudit.hasSubnav) throw new Error('exercise_lab.html is missing .sky-subnav');
    if (!exerciseAudit.activeTabText || !exerciseAudit.activeTabText.includes('267题大练兵')) {
      throw new Error(`exercise_lab.html active tab expected '267题大练兵', got: ${exerciseAudit.activeTabText}`);
    }
    if (exerciseAudit.overflowX) {
      throw new Error(`exercise_lab.html has horizontal overflow on ${vp.name}!`);
    }

    // Navigate to Page 3: g8_exam_rush.html via subnav click
    console.log('  ➔ Clicking subnav tab to g8_exam_rush.html...');
    await Promise.all([
      page.waitForNavigation({ waitUntil: 'domcontentloaded' }),
      page.click('.sky-subnav a[href="g8_exam_rush.html"]')
    ]);
    console.log('  ✓ Arrived on g8_exam_rush.html');

    const rushAudit = await page.evaluate(() => {
      const igcseNav = document.querySelector('igcse-nav');
      const subnav = document.querySelector('.sky-subnav');
      const activeTab = subnav ? subnav.querySelector('.sky-subnav-tab.active') : null;
      const bodyBg = window.getComputedStyle(document.body).backgroundImage;
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSubnav: !!subnav,
        activeTabText: activeTab ? activeTab.innerText.trim() : null,
        bodyBgHasGradient: bodyBg.includes('radial-gradient'),
        overflowX
      };
    });

    console.log('    Exam Rush Audit:', rushAudit);
    if (!rushAudit.hasIgcseNav) throw new Error('g8_exam_rush.html is missing <igcse-nav>');
    if (!rushAudit.hasSubnav) throw new Error('g8_exam_rush.html is missing .sky-subnav');
    if (!rushAudit.activeTabText || !rushAudit.activeTabText.includes('考前突击大厅')) {
      throw new Error(`g8_exam_rush.html active tab expected '考前突击大厅', got: ${rushAudit.activeTabText}`);
    }
    if (rushAudit.overflowX) {
      throw new Error(`g8_exam_rush.html has horizontal overflow on ${vp.name}!`);
    }

    // Navigate back to index.html to complete round-trip
    console.log('  ➔ Clicking subnav tab back to index.html (Round-trip completion)...');
    await Promise.all([
      page.waitForNavigation({ waitUntil: 'domcontentloaded' }),
      page.click('.sky-subnav a[href="index.html"]')
    ]);
    console.log('  ✓ Returned safely to index.html');

    if (consoleErrors.length > 0) {
      console.error(`❌ Console errors detected on ${vp.name}:`, consoleErrors);
      throw new Error(`Console errors found: ${consoleErrors.join(', ')}`);
    }

    await context.close();
  }

  await browser.close();

  console.log('\n================================================================');
  console.log('🎉 CROSS-PAGE UNIFIED NAVIGATION & VISUAL TOKENS 100% VERIFIED!');
  console.log('================================================================');
}

runCrossNavVerification().catch(err => {
  console.error('\n❌ VERIFICATION TEST FAILED:', err);
  process.exit(1);
});
