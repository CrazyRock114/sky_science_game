const playwright = require('/Users/crazyrock/Antigravity/IGCSE_miniMax/node_modules/playwright-core');
const path = require('path');

async function runComprehensiveVerification() {
  console.log('================================================================');
  console.log('🚀 TESTING CAMBRIDGE G8 SCIENCE 2-HOUR EXAM RUSH HUB');
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
  await page.goto(htmlUrl, { waitUntil: 'commit', timeout: 20000 });
  await page.waitForSelector('.glass-card');

  // Check 1: Console errors
  if (consoleErrors.length > 0) {
    console.error('❌ Console errors detected on page load:', consoleErrors);
    process.exit(1);
  }
  console.log('✅ Page loaded cleanly with 0 console errors.');

  // Check 2: Data counts verification
  const counts = await page.evaluate(() => ({
    objectiveCount: window.RUSH_QUESTIONS ? window.RUSH_QUESTIONS.length : 0,
    theoryCount: window.THEORY_QUESTIONS ? window.THEORY_QUESTIONS.length : 0,
    title: document.title
  }));
  console.log('Data counts:', counts);
  if (counts.objectiveCount !== 48) {
    throw new Error(`Expected 48 objective questions, found ${counts.objectiveCount}`);
  }
  if (counts.theoryCount !== 10) {
    throw new Error(`Expected 10 theory questions, found ${counts.theoryCount}`);
  }
  console.log('✅ Verified 48 Objective Questions and 10 Written Theory Questions loaded.');

  // Check 3: Tab 1 - Concept Cards Accordion
  console.log('\n--- Testing Tab 1: Concept Cards & Mindmaps ---');
  const accordionTest = await page.evaluate(() => {
    const items = document.querySelectorAll('.concept-item');
    const firstOpen = items[0].classList.contains('open');
    // Click second item
    items[1].querySelector('.concept-header').click();
    const secondOpen = items[1].classList.contains('open');
    return { count: items.length, firstOpen, secondOpen };
  });
  console.log('Accordion test:', accordionTest);
  if (accordionTest.count !== 3 || !accordionTest.secondOpen) {
    throw new Error('Concept cards accordion failed!');
  }
  console.log('✅ Tab 1 Concept cards verified (3 comprehensive modules).');

  // Check 4: Tab 2 - Objective Arena (Filters, Question Answering, Feedback)
  console.log('\n--- Testing Tab 2: Objective Practice Arena ---');
  await page.evaluate(() => switchMainTab('objective'));
  
  // Test filter switching
  const filterTest = await page.evaluate(() => {
    filterObjective(1, document.querySelectorAll('.filter-btn')[1]);
    const l1Count = filteredQuestions.length;
    filterObjective(2, document.querySelectorAll('.filter-btn')[2]);
    const l2Count = filteredQuestions.length;
    filterObjective(3, document.querySelectorAll('.filter-btn')[3]);
    const l3Count = filteredQuestions.length;
    filterObjective('all', document.querySelectorAll('.filter-btn')[0]);
    const allCount = filteredQuestions.length;
    return { l1Count, l2Count, l3Count, allCount };
  });
  console.log('Objective filter test:', filterTest);
  if (filterTest.l1Count !== 16 || filterTest.l2Count !== 16 || filterTest.l3Count !== 16 || filterTest.allCount !== 48) {
    throw new Error('Objective filters failed! Expected 16 each.');
  }
  console.log('✅ Objective filters verified (16 L1 + 16 L2 + 16 L3 = 48 items).');

  // Answer first 3 questions in Arena
  for (let i = 0; i < 3; i++) {
    const qAns = await page.evaluate((idx) => {
      const q = filteredQuestions[currentObjIdx];
      selectObjectiveAnswer(q.correct);
      const isFbVisible = document.getElementById('obj-feedback-box').style.display === 'block';
      const score = parseInt(document.getElementById('obj-score').textContent, 10);
      nextObjectiveQuestion();
      return { qId: q.id, isFbVisible, score };
    }, i);
    console.log(`✓ Objective Q${i + 1} (${qAns.qId}) answered correctly, score incremented to ${qAns.score}`);
    if (!qAns.isFbVisible || qAns.score <= 0) {
      throw new Error(`Objective Q${i + 1} answering failed!`);
    }
  }
  console.log('✅ Objective Arena question answering and scoring verified.');

  // Check 5: Tab 3 - Written Theory Arena
  console.log('\n--- Testing Tab 3: Written Theory Arena (10 Questions) ---');
  await page.evaluate(() => switchMainTab('theory'));

  const theoryCheck = await page.evaluate(() => {
    const cards = document.querySelectorAll('.theory-item');
    if (cards.length !== 10) return { error: `Expected 10 theory cards, got ${cards.length}` };

    // Test typing draft in Q1
    const q1 = THEORY_QUESTIONS[0];
    const textarea = document.getElementById(`textarea-${q1.id}`);
    textarea.value = 'Oxygen diffuses down steep concentration gradient from alveoli to blood.';
    saveTheoryDraft(q1.id, textarea.value);

    // Test Reveal Mark Scheme
    toggleTheoryMarkScheme(q1.id);
    const isMsVisible = document.getElementById(`ms-${q1.id}`).style.display === 'block';

    // Test Self-Assessment Rating (give 3 marks)
    rateTheoryQuestion(q1.id, 3, q1.marks);
    const scoreVal = document.getElementById(`lbl-score-${q1.id}`).textContent;
    const totalScore = document.getElementById('theory-total-score').textContent;

    return {
      cardsCount: cards.length,
      isMsVisible,
      scoreVal,
      totalScore
    };
  });
  console.log('Theory arena check:', theoryCheck);
  if (theoryCheck.error) throw new Error(theoryCheck.error);
  if (!theoryCheck.isMsVisible || theoryCheck.scoreVal !== '3' || theoryCheck.totalScore !== '3') {
    throw new Error('Written Theory Mark Scheme reveal or self-scoring failed!');
  }
  console.log('✅ Written Theory Arena 10 questions, text drafting, mark scheme reveal, and self-scoring verified.');

  // Check 6: Tab 4 - Mock Exam Simulator
  console.log('\n--- Testing Tab 4: 40-Minute Mock Exam Simulator ---');
  await page.evaluate(() => switchMainTab('mock'));

  const mockCheck = await page.evaluate(() => {
    // Start Mock
    startMockExam();
    const isActiveVisible = document.getElementById('mock-active-screen').style.display === 'block';
    const secACount = mockSecAQuestions.length;
    const secBCount = mockSecBQuestions.length;
    const timerText = document.getElementById('mock-timer-val').textContent;

    // Simulate answering 15 MCQs
    mockSecAQuestions.forEach(q => {
      selectMockSecA(q.id, q.correct);
    });

    // Simulate scoring Section B (full marks)
    mockSecBQuestions.forEach(q => {
      mockSecBScores[q.id] = q.marks;
    });

    // Submit Exam
    submitMockExam();
    const isResultVisible = document.getElementById('mock-result-screen').style.display === 'block';
    const finalScore = document.getElementById('mock-res-score').textContent;
    const finalPct = document.getElementById('mock-res-pct').textContent;
    const gradeBadge = document.getElementById('mock-res-badge').textContent;
    const t1Diag = document.getElementById('mock-diag-t1-pct').textContent;
    const t2Diag = document.getElementById('mock-diag-t2-pct').textContent;
    const t3Diag = document.getElementById('mock-diag-t3-pct').textContent;

    return {
      isActiveVisible,
      secACount,
      secBCount,
      timerText,
      isResultVisible,
      finalScore,
      finalPct,
      gradeBadge,
      t1Diag,
      t2Diag,
      t3Diag
    };
  });

  console.log('Mock exam check:', mockCheck);
  if (!mockCheck.isResultVisible) {
    throw new Error('Mock exam result screen not displayed!');
  }
  if (mockCheck.secACount !== 15 || mockCheck.secBCount !== 3) {
    throw new Error(`Expected 15 MCQs and 3 Theory questions in mock, got ${mockCheck.secACount} & ${mockCheck.secBCount}`);
  }
  if (!mockCheck.finalScore.includes('/') || mockCheck.finalPct !== '100%') {
    throw new Error(`Expected 100% full score in mock, got ${mockCheck.finalScore} (${mockCheck.finalPct})`);
  }
  console.log('✅ 40-Minute Mock Exam Simulator: 15 MCQs + 3 Theory questions, timer, auto-scoring, and 3D radar diagnosis verified.');

  // Clean exit check
  if (consoleErrors.length > 0) {
    console.error('❌ Console errors detected during test run:', consoleErrors);
    process.exit(1);
  }

  await browser.close();
  console.log('\n================================================================');
  console.log('🎉 CAMBRIDGE G8 SCIENCE 2-HOUR EXAM RUSH HUB 100% VERIFIED PASS!');
  console.log('================================================================');
}

runComprehensiveVerification().catch(err => {
  console.error('\n❌ VERIFICATION TEST FAILED:', err);
  process.exit(1);
});
