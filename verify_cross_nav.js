/**
 * Cross-Navigation and Streamlined UX Verifier
 * Tests index.html, exercise_lab.html, and g8_exam_rush.html
 * Across Desktop, iPad, and Mobile viewports.
 *
 * Verifies:
 * 1. .sky-subnav is COMPLETELY REMOVED from all pages.
 * 2. Only single mother-ship <igcse-nav active="sky"> remains.
 * 3. Zero-Hide acceptance criteria: 4 tabs on g8_exam_rush.html are 100% visible on first screen without scrolling.
 * 4. Inline header return link (← 返回 Sky 科学岛首页) works.
 * 5. Full round-trip navigation between all three pages without errors or horizontal overflow.
 */

const playwright = require('/Users/crazyrock/Antigravity/IGCSE_miniMax/node_modules/playwright-core');
const path = require('path');

const fs = require('fs');

const VIEWPORTS = [
  { name: 'Desktop (1280x800)', width: 1280, height: 800 },
  { name: 'iPad / Tablet (768x1024)', width: 768, height: 1024 },
  { name: 'Mobile / iPhone (390x844)', width: 390, height: 844 }
];

async function runCrossNavVerification() {
  console.log('================================================================');
  console.log('🌐 RUNNING STREAMLINED UX & ZERO-HIDE ACCEPTANCE AUDIT');
  console.log('================================================================');

  const browser = await playwright.chromium.launch({ headless: true });

  for (const vp of VIEWPORTS) {
    console.log(`\n📱 Testing Viewport: ${vp.name}`);
    const context = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: 2
    });

    // Route external resources to local files for fast, isolated verification
    await context.route('https://igcse.xyz/**', route => {
      const u = route.request().url();
      if (u.includes('ecosystem-nav.js')) {
        route.fulfill({ status: 200, contentType: 'application/javascript', body: fs.readFileSync('ecosystem-nav.js') });
      } else if (u.includes('ecosystem-nav.css')) {
        route.fulfill({ status: 200, contentType: 'text/css', body: fs.readFileSync('ecosystem-nav.css') });
      } else {
        route.fulfill({ status: 200, body: '' });
      }
    });
    await context.route('https://fonts.**', route => route.fulfill({ status: 200, contentType: 'text/css', body: '' }));

    const page = await context.newPage();

    const consoleErrors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') {
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
      const header = document.querySelector('header.word-header');
      const exerciseLink = header ? header.querySelector('a[href="exercise_lab.html"]') : null;
      const rushLink = header ? header.querySelector('a[href="g8_exam_rush.html"]') : null;
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSubnav: !!subnav,
        hasExerciseLink: !!exerciseLink,
        hasRushLink: !!rushLink,
        overflowX
      };
    });

    console.log('    Index Audit:', indexAudit);
    if (!indexAudit.hasIgcseNav) throw new Error('index.html is missing <igcse-nav>');
    if (indexAudit.hasSubnav) throw new Error('index.html still has redundant .sky-subnav!');
    if (!indexAudit.hasExerciseLink || !indexAudit.hasRushLink) {
      throw new Error('index.html missing header navigation links');
    }
    if (indexAudit.overflowX) {
      throw new Error(`index.html has horizontal overflow on ${vp.name}!`);
    }

    // Navigate to Page 2: exercise_lab.html via header link
    console.log('  ➔ Clicking header link to exercise_lab.html...');
    await Promise.all([
      page.waitForNavigation({ waitUntil: 'domcontentloaded' }),
      page.click('header.word-header a[href="exercise_lab.html"]')
    ]);
    console.log('  ✓ Arrived on exercise_lab.html');

    const exerciseAudit = await page.evaluate(() => {
      const igcseNav = document.querySelector('igcse-nav');
      const subnav = document.querySelector('.sky-subnav');
      const header = document.querySelector('header.lab-header');
      const backHomeLink = header ? header.querySelector('a.btn-back-home[href="index.html"]') : null;
      const rushLink = header ? header.querySelector('a[href="g8_exam_rush.html"]') : null;
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSubnav: !!subnav,
        hasBackHomeLink: !!backHomeLink,
        hasRushLink: !!rushLink,
        overflowX
      };
    });

    console.log('    Exercise Lab Audit:', exerciseAudit);
    if (!exerciseAudit.hasIgcseNav) throw new Error('exercise_lab.html is missing <igcse-nav>');
    if (exerciseAudit.hasSubnav) throw new Error('exercise_lab.html still has redundant .sky-subnav!');
    if (!exerciseAudit.hasBackHomeLink) throw new Error('exercise_lab.html is missing header btn-back-home');
    if (!exerciseAudit.hasRushLink) throw new Error('exercise_lab.html is missing link to g8_exam_rush.html');
    if (exerciseAudit.overflowX) {
      throw new Error(`exercise_lab.html has horizontal overflow on ${vp.name}!`);
    }

    // Navigate to Page 3: g8_exam_rush.html via header link
    console.log('  ➔ Clicking header link to g8_exam_rush.html...');
    await Promise.all([
      page.waitForNavigation({ waitUntil: 'domcontentloaded' }),
      page.click('header.lab-header a[href="g8_exam_rush.html"]')
    ]);
    console.log('  ✓ Arrived on g8_exam_rush.html');

    const rushAudit = await page.evaluate(() => {
      const igcseNav = document.querySelector('igcse-nav');
      const subnav = document.querySelector('.sky-subnav');
      const header = document.querySelector('header.rush-header');
      const backHomeLink = header ? header.querySelector('a.btn-back-home[href="index.html"]') : null;
      const headerPos = header ? window.getComputedStyle(header).position : 'none';
      const tabs = Array.from(document.querySelectorAll('.nav-tabs .tab-btn'));
      const vh = window.innerHeight;

      // Check Zero-Hide: are all 4 tabs fully visible within the initial viewport without scrolling?
      const tabsVisibility = tabs.map(t => {
        const rect = t.getBoundingClientRect();
        const isVisibleOnFirstScreen = rect.top >= 0 && rect.bottom <= vh && rect.height > 0;
        return {
          text: t.innerText.trim(),
          top: Math.round(rect.top),
          bottom: Math.round(rect.bottom),
          isVisibleOnFirstScreen
        };
      });

      const allTabsVisible = tabsVisibility.length === 4 && tabsVisibility.every(t => t.isVisibleOnFirstScreen);
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSubnav: !!subnav,
        hasBackHomeLink: !!backHomeLink,
        headerPosition: headerPos,
        tabsCount: tabs.length,
        allTabsVisibleOnFirstScreen: allTabsVisible,
        tabsDetails: tabsVisibility,
        overflowX
      };
    });

    console.log('    Exam Rush Audit:', rushAudit);
    if (!rushAudit.hasIgcseNav) throw new Error('g8_exam_rush.html is missing <igcse-nav>');
    if (rushAudit.hasSubnav) throw new Error('g8_exam_rush.html still has redundant .sky-subnav!');
    if (!rushAudit.hasBackHomeLink) throw new Error('g8_exam_rush.html is missing header btn-back-home');
    if (rushAudit.headerPosition === 'sticky') {
      throw new Error('g8_exam_rush.html header still has sticky position!');
    }
    if (!rushAudit.allTabsVisibleOnFirstScreen) {
      throw new Error(`Zero-Hide VIOLATION on ${vp.name}! Tabs not 100% visible on first screen: ${JSON.stringify(rushAudit.tabsDetails)}`);
    }
    if (rushAudit.overflowX) {
      throw new Error(`g8_exam_rush.html has horizontal overflow on ${vp.name}!`);
    }

    // Navigate back to index.html using the inline header back link
    console.log('  ➔ Clicking inline header back link (← 返回 Sky 科学岛首页) back to index.html...');
    await Promise.all([
      page.waitForNavigation({ waitUntil: 'domcontentloaded' }),
      page.click('header a.btn-back-home[href="index.html"]')
    ]);
    console.log('  ✓ Returned safely to index.html via inline back button');

    if (consoleErrors.length > 0) {
      console.error(`❌ Console errors detected on ${vp.name}:`, consoleErrors);
      throw new Error(`Console errors found: ${consoleErrors.join(', ')}`);
    }

    await context.close();
  }

  await browser.close();

  console.log('\n================================================================');
  console.log('🎉 STREAMLINED UX & ZERO-HIDE ACCEPTANCE 100% VERIFIED!');
  console.log('================================================================');
}

runCrossNavVerification().catch(err => {
  console.error('\n❌ VERIFICATION TEST FAILED:', err);
  process.exit(1);
});
