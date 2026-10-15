// verify_lab_interactive.js
// High-fidelity headless verification script for exercise_lab.html

const fs = require('fs');
const vm = require('vm');

console.log('🧪 Starting Smoke Test & DOM Simulation for exercise_lab.html...');

// 1. Read files
const htmlContent = fs.readFileSync('exercise_lab.html', 'utf8');
const dataJsContent = fs.readFileSync('science_exercises_data.js', 'utf8');

class MockClassList {
  constructor(el) {
    this.el = el;
    this.set = new Set();
  }
  add(...tokens) { tokens.forEach(t => this.set.add(t)); }
  remove(...tokens) { tokens.forEach(t => this.set.delete(t)); }
  contains(token) { return this.set.has(token); }
  has(token) { return this.set.has(token); }
  toggle(token, force) {
    if (typeof force !== 'undefined') {
      if (force) this.set.add(token);
      else this.set.delete(token);
      return force;
    }
    if (this.set.has(token)) {
      this.set.delete(token);
      return false;
    } else {
      this.set.add(token);
      return true;
    }
  }
  toString() { return Array.from(this.set).join(' '); }
}

// 2. Build DOM element mock
class MockElement {
  constructor(tag, id = '') {
    this.tagName = (tag || 'DIV').toUpperCase();
    this.id = id;
    this.classList = new MockClassList(this);
    this.attributes = {};
    this.children = [];
    this.parentElement = null;
    this._innerHTML = '';
    this.textContent = '';
    this.style = {};
    this.value = '';
    this.onclick = null;
    this.oninput = null;
    this.onchange = null;
  }

  get innerHTML() {
    return this._innerHTML || '';
  }
  set innerHTML(val) {
    this._innerHTML = val;
    this.textContent = (val || '').replace(/<[^>]+>/g, '');
    if (val === '') {
      this.children = [];
    }
  }

  get className() {
    return this.classList.toString();
  }
  set className(val) {
    this.classList.set = new Set((val || '').split(/\s+/).filter(Boolean));
  }

  setAttribute(k, v) { this.attributes[k] = String(v); }
  getAttribute(k) { return this.attributes[k] || null; }
  hasAttribute(k) { return k in this.attributes; }

  appendChild(child) {
    child.parentElement = this;
    this.children.push(child);
    return child;
  }

  removeChild(child) {
    const idx = this.children.indexOf(child);
    if (idx >= 0) this.children.splice(idx, 1);
    return child;
  }

  querySelector(sel) {
    const res = this.querySelectorAll(sel);
    return res.length > 0 ? res[0] : null;
  }

  querySelectorAll(sel) {
    const results = [];
    const check = (el) => {
      if (!el || typeof el !== 'object') return;
      if (sel.startsWith('.')) {
        const cls = sel.slice(1);
        if (el.classList && el.classList.has(cls)) results.push(el);
      } else if (sel.startsWith('#')) {
        const id = sel.slice(1);
        if (el.id === id) results.push(el);
      } else if (sel.toLowerCase() === el.tagName.toLowerCase()) {
        results.push(el);
      }
      if (el.children) {
        for (const c of el.children) check(c);
      }
    };
    for (const c of this.children) check(c);
    return results;
  }
}

// Map of all elements by ID in the mock document
const elementMap = new Map();
function getOrCreateElement(id, tag = 'div') {
  if (!elementMap.has(id)) {
    elementMap.set(id, new MockElement(tag, id));
  }
  return elementMap.get(id);
}

// Pre-register IDs known in exercise_lab.html
const knownIds = [
  'header-subtitle', 'btn-lang-bilingual', 'btn-lang-en', 'btn-nav-vocab',
  'btn-part-1', 'btn-part-2', 'lbl-part-1', 'lbl-part-2', 'select-lesson', 'search-input',
  'lbl-tab-mcq', 'lbl-tab-match', 'lbl-tab-cloze', 'lbl-tab-sort', 'lbl-tab-explorer', 'lbl-tab-mistakes',
  'count-mcq', 'count-match', 'count-cloze', 'count-sort', 'count-all', 'count-mistakes',
  'mcq-task-tag', 'lbl-mcq-qnum', 'mcq-current-idx', 'mcq-total-count', 'lbl-mcq-score', 'mcq-score',
  'lbl-mcq-streak', 'mcq-streak', 'mcq-progress-fill', 'mcq-prompt-en', 'mcq-prompt-cn',
  'mcq-options-container', 'mcq-feedback-box', 'mcq-feedback-title', 'mcq-feedback-rationale',
  'mcq-citation-tag', 'mcq-options-breakdown', 'mcq-breakdown-title', 'breakdown-cards-container',
  'btn-mcq-prev', 'btn-mcq-next',
  'match-task-title', 'match-task-subtitle', 'btn-match-prev', 'btn-match-next', 'btn-match-reset',
  'match-left-col', 'match-right-col', 'match-complete-banner', 'match-complete-heading', 'match-citation-hint',
  'cloze-task-title', 'cloze-subtitle', 'btn-cloze-prev', 'btn-cloze-next', 'cloze-wb-title',
  'cloze-word-bank', 'cloze-passage-container', 'btn-cloze-check', 'btn-cloze-reveal',
  'cloze-feedback-box', 'cloze-rationale-text', 'cloze-citation-tag',
  'sort-task-title', 'sort-subtitle', 'btn-sort-prev', 'btn-sort-next', 'btn-sort-reset',
  'sort-items-container', 'btn-sort-check', 'sort-feedback-box',
  'explorer-intro-text', 'explorer-total-count', 'btn-exp-expand', 'btn-exp-collapse',
  'explorer-list-container',
  'mistake-heading', 'mistake-subtitle', 'mistake-count-display', 'mistake-pending-label',
  'btn-mistake-drill', 'btn-mistake-clear', 'mistake-list-container',
  'tab-mcq', 'tab-match', 'tab-cloze', 'tab-sort', 'tab-explorer', 'tab-mistakes',
  // Analytics & Timing additions
  'mcq-timer-badge', 'lbl-mcq-time', 'mcq-elapsed-time',
  'btn-mode-formal', 'btn-mode-trial',
  'analytics-heading', 'analytics-subtitle',
  'lbl-kpi-attempts', 'stat-total-attempts', 'stat-sub-attempts',
  'lbl-kpi-accuracy', 'stat-accuracy-rate', 'stat-sub-accuracy',
  'lbl-kpi-duration', 'stat-avg-duration', 'stat-sub-time',
  'lbl-kpi-mistakes', 'stat-pending-mistakes', 'stat-sub-mistakes',
  'mastery-heading', 'lbl-mastery-sub', 'mastery-list-container',
  'top-mistakes-heading', 'lbl-top-mistakes-sub', 'top-mistakes-container',
  'subtab-btn-mistakes', 'sub-mistake-count', 'subtab-btn-history', 'sub-history-count',
  'view-mistake-bank', 'view-attempt-history',
  'pill-filter-all', 'pill-filter-formal', 'pill-filter-excluded', 'pill-filter-wrong',
  'btn-hist-exclude-trial', 'btn-hist-include-all', 'btn-hist-clear-excluded', 'btn-hist-clear-all',
  'th-time', 'th-q', 'th-ans', 'th-result', 'th-time-spent', 'th-mode', 'th-status', 'th-actions',
  'history-table-body', 'history-empty-message'
];

knownIds.forEach(id => getOrCreateElement(id));
getOrCreateElement('select-lesson').value = 'all';

const documentMock = {
  body: new MockElement('BODY'),
  getElementById: (id) => getOrCreateElement(id),
  createElement: (tag) => new MockElement(tag),
  querySelectorAll: (sel) => {
    // Collect from document body or all created elements
    const matches = [];
    const check = (el) => {
      if (!el) return;
      if (sel.startsWith('.')) {
        const cls = sel.slice(1);
        if (el.classList && el.classList.has(cls)) matches.push(el);
      } else if (sel.startsWith('#')) {
        const id = sel.slice(1);
        if (el.id === id) matches.push(el);
      } else if (sel.toLowerCase() === el.tagName.toLowerCase()) {
        matches.push(el);
      }
      if (el.children) {
        for (const c of el.children) check(c);
      }
    };
    elementMap.forEach(el => check(el));
    return matches;
  },
  addEventListener: (event, handler) => {
    if (event === 'DOMContentLoaded') {
      documentMock._onLoad = handler;
    }
  }
};

const localStorageMock = {
  _store: {},
  getItem: (k) => localStorageMock._store[k] || null,
  setItem: (k, v) => { localStorageMock._store[k] = String(v); },
  removeItem: (k) => { delete localStorageMock._store[k]; }
};

// 3. Create Sandbox Context
const sandbox = {
  window: {
    addEventListener: (event, handler) => {
      if (event === 'DOMContentLoaded') sandbox.window._onLoad = handler;
    }
  },
  document: documentMock,
  localStorage: localStorageMock,
  console: console,
  alert: (msg) => console.log('  [Alert]:', msg),
  confirm: (msg) => { console.log('  [Confirm]:', msg); return true; },
  setTimeout: (fn) => fn(),
  setInterval: (fn) => 1,
  clearInterval: (id) => {},
  Math: Math,
  Date: Date,
  parseInt: parseInt
};

sandbox.window.document = documentMock;
sandbox.window.localStorage = localStorageMock;

vm.createContext(sandbox);

// 4. Load Science Data
vm.runInContext(dataJsContent, sandbox);
console.log('  Loaded PART1:', sandbox.window.SCIENCE_DATA_PART1.length, 'questions');
console.log('  Loaded PART2:', sandbox.window.SCIENCE_DATA_PART2.length, 'questions');

// 5. Extract and execute script from exercise_lab.html
const scriptMatch = htmlContent.match(/<script>([\s\S]*?)<\/script>\s*<\/body>/);
if (!scriptMatch) {
  throw new Error('Could not find main <script> tag in exercise_lab.html');
}
const mainScript = scriptMatch[1];

vm.runInContext(mainScript, sandbox);
console.log('  Script parsed successfully.');

// Trigger DOMContentLoaded
if (sandbox.window._onLoad) {
  sandbox.window._onLoad();
  console.log('  DOMContentLoaded triggered.');
}

// 6. Test Suite Execution
const exec = (code) => vm.runInContext(code, sandbox);

function runTests() {
  console.log('\n--- Running Automated Assertions ---');

  // Test 1: Part 2 Switch & MCQ Pool
  exec('switchCoursePart(2)');
  const part2PoolSize = exec('mcqPool.length');
  console.log(`✓ Test 1: Switched to Part 2. MCQ Pool count = ${part2PoolSize} (Expected: 60)`);
  if (part2PoolSize !== 60) throw new Error(`Expected 60 MCQs, got ${part2PoolSize}`);

  // Test 2: MCQ Render & Options
  exec('currentMcqIdx = 0; initMcq()');
  const q0 = exec('mcqPool[0]');
  console.log(`✓ Test 2: Question 1 Initialized -> [${q0.task_code}]`);
  const optsContainer = getOrCreateElement('mcq-options-container');
  console.log(`  Options rendered: ${optsContainer.children.length} buttons`);
  if (optsContainer.children.length !== 4) throw new Error('Expected 4 options rendered');

  // Test 3: Select Correct Option
  exec('selectMcqOption("B", "B", mcqPool[0])');
  const score = exec('mcqScore');
  const streak = exec('mcqStreak');
  console.log(`✓ Test 3: Selected correct Option B. Streak = ${streak}, Score = ${score}`);
  if (score !== 10) throw new Error('Expected mcqScore to be 10');

  // Test 4: Check Option-by-Option Breakdown
  const breakdownCardsContainer = getOrCreateElement('breakdown-cards-container');
  console.log(`✓ Test 4: Option Breakdown Cards count = ${breakdownCardsContainer.children.length} (Expected: 4)`);
  if (breakdownCardsContainer.children.length !== 4) throw new Error('Expected 4 breakdown cards');
  const cardA = breakdownCardsContainer.children[0];
  const cardB = breakdownCardsContainer.children[1];
  console.log(`  Card A classes: "${cardA.className}" (Incorrect distractor)`);
  console.log(`  Card B classes: "${cardB.className}" (Correct answer)`);
  if (!cardA.classList.has('incorrect-card')) throw new Error('Card A should have incorrect-card class');
  if (!cardB.classList.has('correct-card')) throw new Error('Card B should have correct-card class');

  // Test 5: Switch Language to 'en' (English Only Mode)
  exec('setLanguageMode("en")');
  console.log('✓ Test 5: Switched to "en" mode');
  if (!documentMock.body.classList.has('lang-mode-en')) throw new Error('Body should have lang-mode-en class');
  const lblMcq = getOrCreateElement('lbl-tab-mcq').textContent;
  console.log(`  Tab label for MCQ: "${lblMcq}" (Expected: "🎯 MCQ Arena")`);
  if (lblMcq !== '🎯 MCQ Arena') throw new Error('Expected "🎯 MCQ Arena" in English mode');

  // Test 6: Verify English Only MCQ Prompt and Distractors
  exec('initMcq()');
  const promptEnElem = getOrCreateElement('mcq-prompt-en');
  const promptCnElem = getOrCreateElement('mcq-prompt-cn');
  console.log(`  Prompt EN visible: "${promptEnElem.textContent.substring(0, 50)}..."`);
  console.log(`  Prompt CN display: "${promptCnElem.style.display}" (Expected: "none")`);
  if (promptCnElem.style.display !== 'none') throw new Error('Chinese prompt should be hidden in English mode');

  exec('selectMcqOption("A", "B", mcqPool[0])'); // Select wrong option
  const breakdownTitle = getOrCreateElement('mcq-breakdown-title').textContent;
  console.log(`  Breakdown Title in EN: "${breakdownTitle}"`);
  if (!breakdownTitle.includes('Option-by-Option Distractor Analysis')) throw new Error('Expected English breakdown title');

  // Test 7: Verify Mistake Bank logging
  const mistakeLen = exec('mistakeBank.length');
  console.log(`✓ Test 7: Mistake bank size after wrong answer = ${mistakeLen}`);
  if (mistakeLen !== 1) throw new Error('Mistake should have been logged');

  // Test 8: Switch back to 'bilingual' Mode
  exec('setLanguageMode("bilingual")');
  console.log('✓ Test 8: Switched to "bilingual" mode');
  if (!documentMock.body.classList.has('lang-mode-bilingual')) throw new Error('Body should have lang-mode-bilingual class');
  const lblMcqBi = getOrCreateElement('lbl-tab-mcq').textContent;
  console.log(`  Tab label for MCQ: "${lblMcqBi}" (Expected: "🎯 单选真题闯关")`);
  if (lblMcqBi !== '🎯 单选真题闯关') throw new Error('Expected "🎯 单选真题闯关" in bilingual mode');

  // Test 9: Model Answers Explorer in both modes
  exec('renderExplorerList()');
  const expContainer = getOrCreateElement('explorer-list-container');
  console.log(`✓ Test 9: Explorer items rendered = ${expContainer.children.length}`);
  if (expContainer.children.length === 0) throw new Error('Explorer items should not be empty');
  // Check if MCQs in explorer contain options breakdown box
  const hasBreakdownInExplorer = expContainer.children.some(c => c.innerHTML.includes('options-breakdown-box'));
  console.log(`  Contains distractor breakdown in explorer items: ${hasBreakdownInExplorer}`);
  if (!hasBreakdownInExplorer) throw new Error('Explorer items for MCQs should include distractor breakdown');

  // Test 10: Concept Match English Pair Sanitization
  const sampleMatchItem = exec('window.SCIENCE_DATA_PART2.find(d => d.game_type === "matching") || window.SCIENCE_DATA_PART1[0]');
  const pairsEn = exec(`parseMatchingPairs(${JSON.stringify(sampleMatchItem)})`);
  console.log(`✓ Test 10: Concept match pairs generated in English mode (${pairsEn.length} pairs):`);
  pairsEn.forEach(p => console.log(`   • "${p.left}" -> "${p.right.substring(0, 40)}..."`));
  const hasChineseInLeft = pairsEn.some(p => /[\u4e00-\u9fa5]/.test(p.left));
  console.log(`  Left side terms contain Chinese characters: ${hasChineseInLeft} (Expected: false)`);
  if (hasChineseInLeft) throw new Error('English mode matching pairs should strip Chinese annotations');

  // Test 11: Diagram Image Rendering in MCQ Arena & Explorer
  const q9Idx = exec('mcqPool.findIndex(q => q.id === "Rev_SecA_Q09")');
  console.log(`✓ Test 11: Testing Diagram Image Rendering (Rev_SecA_Q09 at index ${q9Idx}):`);
  if (q9Idx === -1) throw new Error('Rev_SecA_Q09 not found in mcqPool');
  exec(`currentMcqIdx = ${q9Idx}; initMcq();`);
  const diagramBox = getOrCreateElement('mcq-diagram-container');
  const diagramImg = getOrCreateElement('mcq-diagram-img');
  console.log(`  Diagram box display: "${diagramBox.style.display}" (Expected: "block")`);
  console.log(`  Diagram img src: "${diagramImg.src}"`);
  if (diagramBox.style.display !== 'block') throw new Error('Diagram box should be visible for Rev_SecA_Q09');
  if (!diagramImg.src.includes('fig_revision_respiratory_system.jpeg')) throw new Error('Diagram image src incorrect');
  // Check answer selection for B
  exec(`selectMcqOption("B", "B", mcqPool[${q9Idx}])`);
  const q9Feedback = getOrCreateElement('mcq-feedback-title').textContent;
  console.log(`  Selecting Option B -> Feedback: "${q9Feedback}"`);
  if (!q9Feedback.includes('正确') && !q9Feedback.includes('Correct')) throw new Error('Option B should be graded correct for Rev_SecA_Q09');

  // Test 12: MCQ Timer & Attempt Log Recording
  const attemptsCount = exec('attemptsLog.length');
  console.log(`✓ Test 12: Attempt Log size = ${attemptsCount}`);
  if (attemptsCount === 0) throw new Error('Attempts should have been logged in attemptsLog');
  const firstAttempt = exec('attemptsLog[0]');
  console.log(`  Latest Attempt: Q=[${firstAttempt.taskCode}], Choice=[${firstAttempt.selectedOption}], Key=[${firstAttempt.correctOption}], Correct=[${firstAttempt.isCorrect}], Time=[${firstAttempt.timeSpentSeconds}s], Mode=[${firstAttempt.sessionMode}], Excluded=[${firstAttempt.isExcluded}]`);
  if (!firstAttempt.timeString) throw new Error('Attempt must contain formatted timeString timestamp');
  if (typeof firstAttempt.timeSpentSeconds !== 'number' || firstAttempt.timeSpentSeconds <= 0) throw new Error('Attempt must contain valid timeSpentSeconds');

  // Test 13: Session Mode & Trial Run Exclusion Mechanics
  console.log('✓ Test 13: Testing Trial Run Mode & Exclusion Mechanics...');
  exec('setSessionMode("trial")');
  const modeVal = exec('currentSessionMode');
  if (modeVal !== 'trial') throw new Error('Session mode should be "trial"');
  // Answer next question in trial mode (wrong answer intentionally)
  exec('currentMcqIdx = 1; initMcq(); selectMcqOption("A", "C", mcqPool[1])');
  const trialAttempt = exec('attemptsLog[0]');
  console.log(`  Trial Attempt recorded: Mode=[${trialAttempt.sessionMode}], Excluded=[${trialAttempt.isExcluded}] (Expected: true)`);
  if (trialAttempt.sessionMode !== 'trial' || trialAttempt.isExcluded !== true) {
    throw new Error('Trial attempt should default to isExcluded = true');
  }

  // Verify trial attempt is excluded from KPI accuracy & valid count
  const validCountBefore = exec('attemptsLog.filter(a => !a.isExcluded).length');
  const totalCountBefore = exec('attemptsLog.length');
  console.log(`  Total attempts: ${totalCountBefore}, Valid non-excluded attempts: ${validCountBefore}`);
  if (totalCountBefore <= validCountBefore) throw new Error('Total count should exceed valid count due to excluded trial attempt');

  // Toggle exclusion back and forth
  exec(`toggleAttemptExclude("${trialAttempt.id}")`);
  const isExcludedAfterToggle = exec('attemptsLog[0].isExcluded');
  console.log(`  After toggleAttemptExclude: isExcluded = ${isExcludedAfterToggle} (Expected: false)`);
  if (isExcludedAfterToggle !== false) throw new Error('Toggling attempt exclusion should flip isExcluded to false');
  
  // Toggle back to excluded
  exec(`toggleAttemptExclude("${trialAttempt.id}")`);
  if (exec('attemptsLog[0].isExcluded') !== true) throw new Error('Toggling attempt exclusion should flip isExcluded back to true');

  // Test 14: Batch Exclude & English Mode Analytics Dashboard
  console.log('✓ Test 14: Testing Batch Exclude, Include, and English Localization...');
  exec('includeAllAttempts()');
  const anyExcluded = exec('attemptsLog.some(a => a.isExcluded)');
  console.log(`  After includeAllAttempts(): any excluded? ${anyExcluded} (Expected: false)`);
  if (anyExcluded) throw new Error('All attempts should be included');

  exec('excludeAllTrialAttempts()');
  const trialStillExcluded = exec('attemptsLog.find(a => a.sessionMode === "trial").isExcluded');
  console.log(`  After excludeAllTrialAttempts(): trial attempt excluded? ${trialStillExcluded} (Expected: true)`);
  if (!trialStillExcluded) throw new Error('Trial attempt should be re-excluded');

  // Test English Mode localization of dashboard
  exec('setLanguageMode("en")');
  const lblTabMisEn = getOrCreateElement('lbl-tab-mistakes').textContent;
  const anHeadEn = getOrCreateElement('analytics-heading').textContent;
  const kpiAttEn = getOrCreateElement('lbl-kpi-attempts').textContent;
  const thTimeEn = getOrCreateElement('th-time').textContent;
  console.log(`  English Tab label: "${lblTabMisEn}" (Expected: "📊 Mistakes & Analytics")`);
  console.log(`  English Dashboard Heading: "${anHeadEn}"`);
  console.log(`  English KPI label: "${kpiAttEn}"`);
  console.log(`  English Table header: "${thTimeEn}"`);
  if (lblTabMisEn !== '📊 Mistakes & Analytics') throw new Error('Tab label in English mode should be "📊 Mistakes & Analytics"');
  if (!anHeadEn.includes('Learning Analytics')) throw new Error('Dashboard heading should be in English');
  if (kpiAttEn !== 'Valid Practice Attempts') throw new Error('KPI attempts label should be in English');
  if (thTimeEn !== 'Timestamp') throw new Error('Table header time should be "Timestamp"');

  console.log('\n🎉 ALL 14 TESTS PASSED WITH 100% SUCCESS!');
}

runTests();
