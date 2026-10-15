const playwright = require('/Users/crazyrock/Antigravity/IGCSE_miniMax/node_modules/playwright-core');
const path = require('path');

async function verifyG8ExamRush() {
  console.log('================================================================');
  console.log('🚀 TESTING G8 EXAM RUSH (10.19) INTERACTIVE SUITE');
  console.log('================================================================');

  const browser = await playwright.chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });
  page.on('pageerror', err => consoleErrors.push(err.message));

  const htmlUrl = 'file://' + path.resolve(__dirname, 'g8_exam_rush.html');
  console.log(`Loading URL: ${htmlUrl}`);
  await page.goto(htmlUrl, { waitUntil: 'commit', timeout: 15000 });
  await page.waitForSelector('.rush-card');

  // 1. Console check
  if (consoleErrors.length > 0) {
    console.error('❌ Console errors detected:', consoleErrors);
    process.exit(1);
  }
  console.log('✅ Page loaded cleanly with 0 console errors.');

  // 2. Data check
  const meta = await page.evaluate(() => ({
    title: document.title,
    questionCount: RUSH_QUESTIONS.length,
    initialScore: parseInt(document.getElementById('rush-score').textContent, 10),
    initialTimer: document.getElementById('rush-timer-seconds').textContent
  }));
  console.log('Page Meta:', meta);
  if (meta.questionCount !== 18) {
    throw new Error(`Expected 18 questions, found ${meta.questionCount}`);
  }
  console.log('✅ Verified full 18 questions loaded.');

  // 3. Test Level Switching via pills
  const levelSwitchTest = await page.evaluate(() => {
    switchLevel(2); // Jump to Q7
    const q7Idx = currentIdx;
    const q7Tag = document.getElementById('rush-topic-tag').textContent;
    switchLevel(3); // Jump to Q13
    const q13Idx = currentIdx;
    const q13Tag = document.getElementById('rush-topic-tag').textContent;
    switchLevel(1); // Back to Q1
    const q1Idx = currentIdx;
    return { q7Idx, q7Tag, q13Idx, q13Tag, q1Idx };
  });
  console.log('Level Switch Test:', levelSwitchTest);
  if (levelSwitchTest.q7Idx !== 6 || levelSwitchTest.q13Idx !== 12 || levelSwitchTest.q1Idx !== 0) {
    throw new Error('Level switching failed!');
  }
  console.log('✅ Level navigation pills verified (L1: Q1, L2: Q7, L3: Q13).');

  // 4. Test Bilingual Toggle
  const langTest = await page.evaluate(() => {
    const initialCnDisplay = document.getElementById('rush-prompt-cn').style.display;
    toggleLanguage();
    const afterEnDisplay = document.getElementById('rush-prompt-cn').style.display;
    toggleLanguage();
    const afterRestoreDisplay = document.getElementById('rush-prompt-cn').style.display;
    return { initialCnDisplay, afterEnDisplay, afterRestoreDisplay };
  });
  console.log('Language Toggle Test:', langTest);
  if (langTest.afterEnDisplay !== 'none' || langTest.afterRestoreDisplay !== 'block') {
    throw new Error('Language toggle failed!');
  }
  console.log('✅ Bilingual / Pure English toggle verified.');

  // 5. Test Question Answering and Scoring across all 18 questions
  console.log('\n--- Answering All 18 Questions (Simulating High-Score Run) ---');
  let currentScore = 0;
  for (let i = 0; i < 18; i++) {
    const qResult = await page.evaluate((idx) => {
      const q = RUSH_QUESTIONS[idx];
      // Click correct option
      const correctBtn = document.querySelector(`.option-btn[data-letter="${q.correct}"]`);
      if (!correctBtn) return { error: `Button for ${q.correct} not found!` };
      correctBtn.click();

      const isBtnCorrect = correctBtn.classList.contains('correct');
      const fbDisplay = document.getElementById('rush-feedback-box').style.display;
      const conceptText = document.getElementById('fb-concept').textContent;
      const trapText = document.getElementById('fb-trap').textContent;
      const citationText = document.getElementById('fb-citation').textContent;
      const newScore = parseInt(document.getElementById('rush-score').textContent, 10);

      // Advance to next
      advanceToNextQuestion();

      return {
        qId: q.id,
        level: q.level,
        topic: q.topic,
        isBtnCorrect,
        fbDisplay,
        hasConcept: !!conceptText,
        hasTrap: !!trapText,
        hasCitation: !!citationText,
        newScore
      };
    }, i);

    if (qResult.error) throw new Error(qResult.error);
    if (!qResult.isBtnCorrect || qResult.fbDisplay !== 'block' || !qResult.hasConcept || !qResult.hasTrap) {
      throw new Error(`Question ${i + 1} (${qResult.qId}) failed verification!`);
    }
    if (qResult.newScore <= currentScore) {
      throw new Error(`Score did not increment on Question ${i + 1}!`);
    }
    currentScore = qResult.newScore;
    console.log(`✓ Q${i + 1} [L${qResult.level} ${qResult.topic}]: Correct -> Score ${qResult.newScore}`);
  }

  // 6. Test Completion View & Certificate
  const compResult = await page.evaluate(() => {
    const compBox = document.getElementById('rush-completion-box');
    const arenaBox = document.getElementById('rush-arena-box');
    const isCompVisible = compBox.style.display === 'block';
    const isArenaHidden = arenaBox.style.display === 'none';
    const accuracy = document.getElementById('res-accuracy').textContent;
    const scoreVal = document.getElementById('res-score').textContent;
    const gradeBadge = document.getElementById('cert-grade-badge').textContent;

    return {
      isCompVisible,
      isArenaHidden,
      accuracy,
      scoreVal,
      gradeBadge
    };
  });

  console.log('\nCompletion Results:', compResult);
  if (!compResult.isCompVisible || !compResult.isArenaHidden) {
    throw new Error('Completion view not displayed after Q18!');
  }
  if (!compResult.accuracy.includes('100%')) {
    throw new Error(`Expected 100% accuracy, got ${compResult.accuracy}`);
  }
  if (!compResult.gradeBadge.includes('A* Master')) {
    throw new Error(`Expected A* Master grade, got ${compResult.gradeBadge}`);
  }
  console.log('✅ Completion view, 100% accuracy, and A* Master certificate verified.');

  // 7. Test Restart Button
  await page.evaluate(() => restartRushGame());
  const restartCheck = await page.evaluate(() => ({
    arenaVisible: document.getElementById('rush-arena-box').style.display === 'block',
    compHidden: document.getElementById('rush-completion-box').style.display === 'none',
    idx: currentIdx,
    score: parseInt(document.getElementById('rush-score').textContent, 10)
  }));
  if (!restartCheck.arenaVisible || restartCheck.compHidden !== true || restartCheck.idx !== 0 || restartCheck.score !== 0) {
    throw new Error('Restart rush failed!');
  }
  console.log('✅ Restart functionality verified.');

  await browser.close();
  console.log('\n================================================================');
  console.log('🎉 G8 EXAM RUSH (10.19) ALL 18 QUESTIONS 100% VERIFIED PASS!');
  console.log('================================================================');
}

verifyG8ExamRush().catch(err => {
  console.error('\n❌ VERIFICATION ERROR:', err);
  process.exit(1);
});
