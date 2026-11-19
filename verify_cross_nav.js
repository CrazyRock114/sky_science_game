/**
 * Cross-Navigation, Streamlined UX & Static Regression Verifier
 * Tests index.html, exercise_lab.html, g8_exam_rush.html, and reactivity/app.js
 *
 * Verifies:
 * 1. Static regression vaccines (HiDPI devicePixelRatio + cancelAnimationFrame + visibilitychange,
 *    unified www ecosystem-nav.* + sticky on all 3 main HTML pages,
 *    z-index >= 100000 for fullscreen overlays, and removal of stale root ecosystem-nav copies).
 * 2. Offline-safe Playwright multi-viewport check (mocks www ecosystem-nav.*
 *    without depending on deleted root copies; skips browser phase cleanly if playwright-core
 *    is unavailable in isolated environments).
 */

const fs = require('fs');
const path = require('path');
const assert = require('assert');

const CANONICAL_HOST = 'https://' + 'www.' + 'igcse.xyz';
const LEGACY_HOST = 'https://' + 'igcse.xyz';
const NAV_JS_URL = `${CANONICAL_HOST}/ecosystem-nav.js`;
const NAV_CSS_URL = `${CANONICAL_HOST}/ecosystem-nav.css`;

const VIEWPORTS = [
  { name: 'Desktop (1280x800)', width: 1280, height: 800 },
  { name: 'iPad / Tablet (768x1024)', width: 768, height: 1024 },
  { name: 'Mobile / iPhone (390x844)', width: 390, height: 844 }
];

const MOCK_NAV_JS = `
  if (!customElements.get('igcse-nav')) {
    customElements.define('igcse-nav', class extends HTMLElement {
      connectedCallback() {
        this.setAttribute('data-mock-mounted', 'true');
        this.style.display = 'block';
        this.style.height = '44px';
        if (this.hasAttribute('sticky')) {
          this.style.position = 'sticky';
          this.style.top = '0';
          this.style.zIndex = '99990';
        }
      }
    });
  }
`;

function runStaticRegressionAssertions() {
  console.log('================================================================');
  console.log('🛡️  RUNNING STATIC REGRESSION VACCINE ASSERTIONS');
  console.log('================================================================');

  // 1. Stale root copies must be removed
  for (const stale of ['ecosystem-nav.js', 'ecosystem-nav.css']) {
    const stalePath = path.resolve(__dirname, stale);
    assert.strictEqual(
      fs.existsSync(stalePath),
      false,
      `Stale root file still exists: ${stale}`
    );
  }
  console.log('  ✓ Stale root ecosystem-nav.js & ecosystem-nav.css are removed');

  // 2. reactivity/app.js must enforce HiDPI scaling and single-instance RAF lifecycle
  const reactivityApp = fs.readFileSync(
    path.resolve(__dirname, 'reactivity', 'app.js'),
    'utf-8'
  );
  assert.ok(
    reactivityApp.includes('devicePixelRatio'),
    'reactivity/app.js must include devicePixelRatio HiDPI scaling'
  );
  assert.ok(
    reactivityApp.includes('cancelAnimationFrame'),
    'reactivity/app.js must include cancelAnimationFrame lifecycle cleanup'
  );
  assert.ok(
    reactivityApp.includes('visibilitychange'),
    'reactivity/app.js must pause/resume RAF on visibilitychange'
  );
  assert.ok(
    reactivityApp.includes('let animationFrameId = null'),
    'reactivity/app.js must manage a module-scoped animationFrameId handle'
  );
  console.log('  ✓ reactivity/app.js HiDPI & RAF lifecycle assertions passed');

  // 3. All 3 main HTML pages must use canonical www ecosystem-nav.js and sticky
  const mainPages = ['index.html', 'exercise_lab.html', 'g8_exam_rush.html'];
  for (const file of mainPages) {
    const html = fs.readFileSync(path.resolve(__dirname, file), 'utf-8');
    assert.ok(
      html.includes(NAV_JS_URL),
      `${file} must reference ${NAV_JS_URL}`
    );
    assert.ok(
      html.includes(NAV_CSS_URL),
      `${file} must reference ${NAV_CSS_URL}`
    );
    assert.ok(
      !html.includes(`${LEGACY_HOST}/ecosystem-nav.`),
      `${file} must not reference non-www ${LEGACY_HOST}/ecosystem-nav.*`
    );
    assert.ok(
      /<igcse-nav\b[^>]*\bactive="sky"[^>]*\bsticky\b[^>]*>/.test(html),
      `${file} must contain <igcse-nav active="sky" sticky>`
    );
  }
  console.log(`  ✓ All 3 main HTML pages reference ${CANONICAL_HOST}/ecosystem-nav.* with sticky`);

  // 4. Fullscreen confetti overlay z-index >= 100000 in g8_exam_rush.html
  const rushHtml = fs.readFileSync(path.resolve(__dirname, 'g8_exam_rush.html'), 'utf-8');
  const confettiMatch = rushHtml.match(/#confetti-canvas\s*\{[^}]*z-index:\s*(\d+)\s*;/);
  assert.ok(confettiMatch, 'g8_exam_rush.html #confetti-canvas z-index rule not found');
  assert.ok(
    Number(confettiMatch[1]) >= 100000,
    `g8_exam_rush.html #confetti-canvas z-index must be >= 100000, got ${confettiMatch[1]}`
  );
  console.log(`  ✓ g8_exam_rush.html #confetti-canvas z-index verified (${confettiMatch[1]})`);
}

function loadPlaywrightOrNull() {
  const candidates = [
    'playwright-core',
    'playwright',
    '/Users/crazyrock/Antigravity/IGCSE_miniMax/node_modules/playwright-core'
  ];
  for (const mod of candidates) {
    try {
      return require(mod);
    } catch (_) {}
  }
  return null;
}

async function runCrossNavVerification() {
  runStaticRegressionAssertions();

  const playwright = loadPlaywrightOrNull();
  if (!playwright) {
    console.log('\nℹ️  playwright-core not accessible in current sandbox; offline static regression audit passed 100%.');
    return;
  }

  console.log('\n================================================================');
  console.log('🌐 RUNNING STREAMLINED UX & ZERO-HIDE ACCEPTANCE AUDIT');
  console.log('================================================================');

  const browser = await playwright.chromium.launch({ headless: true });

  for (const vp of VIEWPORTS) {
    console.log(`\n📱 Testing Viewport: ${vp.name}`);
    const context = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: 2
    });

    // Offline mock fallback for canonical ecosystem-nav assets (no dependency on removed local copies)
    await context.route(`${CANONICAL_HOST}/**`, route => {
      const u = route.request().url();
      if (u.includes('ecosystem-nav.js')) {
        route.fulfill({ status: 200, contentType: 'application/javascript', body: MOCK_NAV_JS });
      } else if (u.includes('ecosystem-nav.css')) {
        route.fulfill({ status: 200, contentType: 'text/css', body: '' });
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

    const indexAudit = await page.evaluate((navJsUrl) => {
      const igcseNav = document.querySelector('igcse-nav');
      const navScript = document.querySelector(`script[src="${navJsUrl}"]`);
      const subnav = document.querySelector('.sky-subnav');
      const header = document.querySelector('header.word-header');
      const exerciseLink = header ? header.querySelector('a[href="exercise_lab.html"]') : null;
      const rushLink = header ? header.querySelector('a[href="g8_exam_rush.html"]') : null;
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSticky: !!(igcseNav && igcseNav.hasAttribute('sticky')),
        hasWwwNavScript: !!navScript,
        hasSubnav: !!subnav,
        hasExerciseLink: !!exerciseLink,
        hasRushLink: !!rushLink,
        overflowX
      };
    }, NAV_JS_URL);

    console.log('    Index Audit:', indexAudit);
    if (!indexAudit.hasIgcseNav || !indexAudit.hasSticky || !indexAudit.hasWwwNavScript) {
      throw new Error('index.html failed <igcse-nav sticky> or canonical nav script check');
    }
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

    const exerciseAudit = await page.evaluate((navJsUrl) => {
      const igcseNav = document.querySelector('igcse-nav');
      const navScript = document.querySelector(`script[src="${navJsUrl}"]`);
      const subnav = document.querySelector('.sky-subnav');
      const header = document.querySelector('header.lab-header');
      const backHomeLink = header ? header.querySelector('a.btn-back-home[href="index.html"]') : null;
      const rushLink = header ? header.querySelector('a[href="g8_exam_rush.html"]') : null;
      const overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth;

      return {
        hasIgcseNav: !!igcseNav,
        hasSticky: !!(igcseNav && igcseNav.hasAttribute('sticky')),
        hasWwwNavScript: !!navScript,
        hasSubnav: !!subnav,
        hasBackHomeLink: !!backHomeLink,
        hasRushLink: !!rushLink,
        overflowX
      };
    }, NAV_JS_URL);

    console.log('    Exercise Lab Audit:', exerciseAudit);
    if (!exerciseAudit.hasIgcseNav || !exerciseAudit.hasSticky || !exerciseAudit.hasWwwNavScript) {
      throw new Error('exercise_lab.html failed <igcse-nav sticky> or canonical nav script check');
    }
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

    const rushAudit = await page.evaluate((navJsUrl) => {
      const igcseNav = document.querySelector('igcse-nav');
      const navScript = document.querySelector(`script[src="${navJsUrl}"]`);
      const subnav = document.querySelector('.sky-subnav');
      const header = document.querySelector('header.rush-header');
      const backHomeLink = header ? header.querySelector('a.btn-back-home[href="index.html"]') : null;
      const headerPos = header ? window.getComputedStyle(header).position : 'none';
      const tabs = Array.from(document.querySelectorAll('.nav-tabs .tab-btn'));
      const vh = window.innerHeight;

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
        hasSticky: !!(igcseNav && igcseNav.hasAttribute('sticky')),
        hasWwwNavScript: !!navScript,
        hasSubnav: !!subnav,
        hasBackHomeLink: !!backHomeLink,
        headerPosition: headerPos,
        tabsCount: tabs.length,
        allTabsVisibleOnFirstScreen: allTabsVisible,
        tabsDetails: tabsVisibility,
        overflowX
      };
    }, NAV_JS_URL);

    console.log('    Exam Rush Audit:', rushAudit);
    if (!rushAudit.hasIgcseNav || !rushAudit.hasSticky || !rushAudit.hasWwwNavScript) {
      throw new Error('g8_exam_rush.html failed <igcse-nav sticky> or canonical nav script check');
    }
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
