/**
 * Sky G8 Chemistry Unit 2 Exam Rush Hall — Interactive Engine
 * Tabs:
 *   1. Core Cheatsheets (速记卡)
 *   2. School Mistakes & 1:2 Variants Mastery Tracker (localStorage persisted)
 *   3. Workbook & PPT Authentic Questions by Lesson / Review Unit
 *   4. 45-Minute Mock Exam Papers (Paper A & Paper B) + Auto-Grading + A4 Print Modes
 */
(function () {
  'use strict';

  const MASTERY_STORAGE_KEY = 'sky_chem_u2_mastery_v1';
  let globalLang = 'bilingual'; // 'bilingual' | 'en'
  let masteryMap = {};
  let currentSmFilter = 'all';
  let currentWbFilter = 'all';
  let currentPaperId = 'paperA';
  let mockTimerId = null;
  let mockRemainingSec = 45 * 60;
  let mockRunning = false;
  let mockSubmitted = false;
  let mockAnswers = {}; // { [paperId]: { mcq: {}, text: {}, selfScore: {} } }

  function loadMastery() {
    try {
      const raw = localStorage.getItem(MASTERY_STORAGE_KEY);
      masteryMap = raw ? JSON.parse(raw) : {};
    } catch (_) {
      masteryMap = {};
    }
  }

  function saveMastery() {
    try {
      localStorage.setItem(MASTERY_STORAGE_KEY, JSON.stringify(masteryMap));
    } catch (_) {}
  }

  function getAllChemData() {
    return Array.isArray(window.CHEMISTRY_U2_DATA) ? window.CHEMISTRY_U2_DATA : [];
  }

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function formatMultiline(str) {
    return escapeHtml(str).replace(/\n/g, '<br>');
  }

  // ==================== GLOBAL TABS & LANGUAGE ====================
  window.switchChemTab = function (tabId) {
    const order = ['cheatsheet', 'mistakes', 'workbook', 'mock'];
    document.querySelectorAll('.nav-tabs .tab-btn').forEach((btn, idx) => {
      btn.classList.toggle('active', order[idx] === tabId);
    });
    document.querySelectorAll('.tab-pane').forEach((pane) => {
      pane.classList.toggle('active', pane.id === 'pane-' + tabId);
    });
  };

  window.toggleChemLang = function () {
    globalLang = globalLang === 'bilingual' ? 'en' : 'bilingual';
    const btn = document.getElementById('btn-lang');
    const txt = document.getElementById('txt-lang');
    if (txt) txt.textContent = globalLang === 'bilingual' ? 'EN / 中文' : 'English Only';
    if (btn) btn.classList.toggle('active', globalLang === 'en');
    document.body.classList.toggle('lang-en-only', globalLang === 'en');
    renderSchoolMistakes();
    renderWorkbookList();
    renderMockPaper();
  };

  window.toggleConceptCard = function (headerEl) {
    const item = headerEl.closest('.concept-item');
    if (item) item.classList.toggle('open');
  };

  // ==================== TAB 2: SCHOOL MISTAKES + 1:2 VARIANTS ====================
  window.setSmFilter = function (filter, btn) {
    currentSmFilter = filter;
    document.querySelectorAll('#sm-filter-bar .filter-btn').forEach((b) => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    renderSchoolMistakes();
  };

  window.toggleMastery = function (qid, status) {
    masteryMap[qid] = status; // 'mastered' | 'review'
    saveMastery();
    updateMasteryStats();
    const card = document.getElementById('sm-card-' + qid);
    if (card) {
      card.classList.toggle('is-mastered', status === 'mastered');
      card.classList.toggle('is-review', status === 'review');
      const mBtn = card.querySelector('.btn-mark-mastered');
      const rBtn = card.querySelector('.btn-mark-review');
      if (mBtn) mBtn.classList.toggle('active', status === 'mastered');
      if (rBtn) rBtn.classList.toggle('active', status === 'review');
    }
    if (currentSmFilter === 'mastered' || currentSmFilter === 'review') {
      renderSchoolMistakes();
    }
  };

  function updateMasteryStats() {
    const pool = getAllChemData().filter(
      (q) => q.source_tag === 'school_mistake' || q.source_tag === 'school_mistake_variant'
    );
    const total = pool.length;
    const masteredCount = pool.filter((q) => masteryMap[q.id] === 'mastered').length;
    const reviewCount = pool.filter((q) => masteryMap[q.id] === 'review').length;
    const pct = total ? Math.round((masteredCount / total) * 100) : 0;

    const lbl = document.getElementById('sm-progress-text');
    const bar = document.getElementById('sm-progress-fill');
    const revLbl = document.getElementById('sm-review-count');
    if (lbl) lbl.textContent = `${masteredCount} / ${total} 已攻克 (${pct}%)`;
    if (bar) bar.style.width = `${pct}%`;
    if (revLbl) revLbl.textContent = String(reviewCount);
  }

  window.checkMcqCard = function (prefix, qid, chosenLetter, correctLetter) {
    const optsWrap = document.getElementById(`${prefix}-opts-${qid}`);
    if (optsWrap) {
      optsWrap.querySelectorAll('.opt-btn').forEach((btn) => {
        btn.disabled = true;
        const l = btn.dataset.letter;
        if (l === correctLetter) btn.classList.add('correct');
        else if (l === chosenLetter) btn.classList.add('wrong');
      });
    }
    const fb = document.getElementById(`${prefix}-fb-${qid}`);
    if (fb) {
      fb.style.display = 'block';
      const statusEl = fb.querySelector('.fb-status');
      if (statusEl) {
        const ok = chosenLetter === correctLetter;
        statusEl.textContent = ok
          ? `✅ 回答正确！(${correctLetter})`
          : `❌ 回答错误，正确答案是 ${correctLetter}`;
        statusEl.style.color = ok ? 'var(--success)' : 'var(--danger)';
      }
    }
  };

  function extractMcqOptions(q) {
    if (Array.isArray(q.options) && q.options.length) {
      return {
        stemEn: q.stem_en || q.prompt_en,
        stemCn: q.stem_cn || q.prompt_cn,
        options: q.options,
        correctLetter: q.correct_letter || (String(q.answer_en || '').trim()[0] || 'A')
      };
    }
    const enLines = String(q.prompt_en || '').split('\n');
    const cnLines = String(q.prompt_cn || '').split('\n');
    const enOpts = {};
    const cnOpts = {};
    const stemEnArr = [];
    const stemCnArr = [];
    enLines.forEach((line) => {
      const m = line.match(/^([A-D])\)\s*(.+)$/);
      if (m) enOpts[m[1]] = m[2];
      else stemEnArr.push(line);
    });
    cnLines.forEach((line) => {
      const m = line.match(/^([A-D])\)\s*(.+)$/);
      if (m) cnOpts[m[1]] = m[2];
      else stemCnArr.push(line);
    });
    const options = ['A', 'B', 'C', 'D']
      .filter((l) => enOpts[l])
      .map((l) => ({ letter: l, text_en: enOpts[l], text_cn: cnOpts[l] || '' }));
    let correctLetter = q.correct_letter;
    if (!correctLetter && q.options_breakdown && !Array.isArray(q.options_breakdown)) {
      const found = ['A', 'B', 'C', 'D'].find((l) => q.options_breakdown[l] && q.options_breakdown[l].correct);
      if (found) correctLetter = found;
    }
    if (!correctLetter) {
      const m = String(q.answer_en || '').trim().match(/^([A-D])/);
      correctLetter = m ? m[1] : 'A';
    }
    return {
      stemEn: stemEnArr.join('\n') || q.prompt_en,
      stemCn: stemCnArr.join('\n') || q.prompt_cn,
      options,
      correctLetter
    };
  }

  function renderMcqQuestionCard(q, prefix) {
    const isEnOnly = globalLang === 'en';
    const status = masteryMap[q.id] || '';
    const isSchool = q.source_tag === 'school_mistake';
    const isVariant = q.source_tag === 'school_mistake_variant';
    const isBaseline = q.source_tag === 'baseline';
    const tagBadge = isSchool
      ? `<span class="badge-pill pill-red">🩺 学校错题原题 Q${q.school_q_num}</span>`
      : isVariant
      ? `<span class="badge-pill pill-amber">🧬 1:2 靶向变式 (${escapeHtml(q.task_code)})</span>`
      : isBaseline
      ? `<span class="badge-pill pill-green">📚 基线巩固 · ${escapeHtml(q.task_code || 'MCQ')}</span>`
      : `<span class="badge-pill pill-blue">${escapeHtml(q.workbook_unit || q.task_code)}</span>`;

    const parsed = extractMcqOptions(q);
    const optsHtml = parsed.options
      .map(
        (opt) => `
      <button class="opt-btn" data-letter="${opt.letter}" onclick="checkMcqCard('${prefix}', '${q.id}', '${opt.letter}', '${parsed.correctLetter}')">
        <span class="opt-letter">${opt.letter}</span>
        <span class="opt-text">
          <span class="opt-text-en">${escapeHtml(opt.text_en)}</span>
          ${!isEnOnly && opt.text_cn ? `<span class="opt-text-cn">${escapeHtml(opt.text_cn)}</span>` : ''}
        </span>
      </button>
    `
      )
      .join('');

    const diagHtml =
      q.mistake_diagnosis_cn || q.mistake_diagnosis_en
        ? `<div class="fb-trap">
            <strong>⚠️ 典型错因诊断：</strong>${escapeHtml(q.mistake_diagnosis_en || '')}
            ${!isEnOnly && q.mistake_diagnosis_cn ? `<div class="cn-sub">${escapeHtml(q.mistake_diagnosis_cn)}</div>` : ''}
           </div>`
        : '';

    const kwsHtml =
      Array.isArray(q.examiner_keywords) && q.examiner_keywords.length
        ? `<div class="keywords-wrap"><span class="kw-label">🔑 得分关键词：</span>${q.examiner_keywords
            .map((k) => `<span class="kw-tag">${escapeHtml(k)}</span>`)
            .join('')}</div>`
        : '';

    const masteryBar =
      prefix === 'sm'
        ? `<div class="mastery-actions">
            <button class="btn-mastery btn-mark-mastered ${status === 'mastered' ? 'active' : ''}" onclick="toggleMastery('${q.id}', 'mastered')">✅ 已攻克</button>
            <button class="btn-mastery btn-mark-review ${status === 'review' ? 'active' : ''}" onclick="toggleMastery('${q.id}', 'review')">🔁 需再练</button>
           </div>`
        : '';

    return `
      <article class="q-card ${status === 'mastered' ? 'is-mastered' : ''} ${status === 'review' ? 'is-review' : ''}" id="${prefix}-card-${q.id}">
        <div class="q-card-top">
          <div class="q-badges">
            ${tagBadge}
            <span class="badge-pill pill-purple">${escapeHtml(q.workbook_unit || '')}</span>
            <span class="q-id-tag">${escapeHtml(q.id)}</span>
          </div>
          ${masteryBar}
        </div>
        <div class="q-prompt-en">${formatMultiline(parsed.stemEn)}</div>
        ${!isEnOnly && parsed.stemCn ? `<div class="q-prompt-cn">${formatMultiline(parsed.stemCn)}</div>` : ''}
        <div class="options-grid" id="${prefix}-opts-${q.id}">
          ${optsHtml}
        </div>
        <div class="feedback-box" id="${prefix}-fb-${q.id}">
          <div class="fb-status"></div>
          <div class="fb-concept">
            <strong>💡 考纲解析：</strong>${escapeHtml(q.rationale_en || '')}
            ${!isEnOnly && q.rationale_cn ? `<div class="cn-sub">${escapeHtml(q.rationale_cn)}</div>` : ''}
          </div>
          ${diagHtml}
          ${kwsHtml}
          <div class="fb-citation">📖 出处：${escapeHtml(q.citation_textbook || '')}</div>
        </div>
      </article>
    `;
  }

  function renderStructuredCard(q, prefix) {
    const isEnOnly = globalLang === 'en';
    const typeLabels = {
      structured: '📝 结构化简答 / 方程式',
      matching: '🔗 概念配对连线（基线）',
      cloze: '🧩 术语完形填空（基线）',
      sorting: '🔢 实验步骤排序（基线）'
    };
    const typeLabel = typeLabels[q.game_type] || '📝 专项练习';
    const msHtml = Array.isArray(q.mark_scheme)
      ? q.mark_scheme.map((pt, i) => `<div class="ms-point"><strong>Point ${i + 1}:</strong> ${escapeHtml(pt)}</div>`).join('')
      : '';
    const kwsHtml =
      Array.isArray(q.examiner_keywords) && q.examiner_keywords.length
        ? `<div class="keywords-wrap"><span class="kw-label">🔑 考官采分词：</span>${q.examiner_keywords
            .map((k) => `<span class="kw-tag">${escapeHtml(k)}</span>`)
            .join('')}</div>`
        : '';

    return `
      <article class="q-card structured-card" id="${prefix}-card-${q.id}">
        <div class="q-card-top">
          <div class="q-badges">
            <span class="badge-pill pill-purple">${typeLabel}</span>
            <span class="badge-pill pill-blue">${escapeHtml(q.workbook_unit || q.lesson_title_cn || '')}</span>
            ${q.marks ? `<span class="badge-mark">[${q.marks} marks]</span>` : ''}
            <span class="q-id-tag">${escapeHtml(q.id)}</span>
          </div>
        </div>
        <div class="q-prompt-en">${formatMultiline(q.prompt_en)}</div>
        ${!isEnOnly && q.prompt_cn ? `<div class="q-prompt-cn">${formatMultiline(q.prompt_cn)}</div>` : ''}
        <textarea class="theory-textarea" placeholder="在此输入方程式、配对/填空/排序草稿或英文/中文简答..."></textarea>
        <div class="q-card-footer">
          <button class="btn-reveal" onclick="toggleRevealBox('${prefix}-ms-${q.id}')">🔍 显示标准答案与解析</button>
          <span class="fb-citation">📖 ${escapeHtml(q.citation_textbook || '')}</span>
        </div>
        <div class="mark-scheme-box" id="${prefix}-ms-${q.id}">
          <div class="fb-concept">
            <strong>✅ 参考答案：</strong><br>${formatMultiline(q.answer_en || '')}
            ${!isEnOnly && q.answer_cn ? `<div class="cn-sub">${formatMultiline(q.answer_cn)}</div>` : ''}
          </div>
          ${q.rationale_en ? `<div style="margin-top:0.45rem;"><strong>💡 解析：</strong>${escapeHtml(q.rationale_en)}${!isEnOnly && q.rationale_cn ? `<div class="cn-sub">${escapeHtml(q.rationale_cn)}</div>` : ''}</div>` : ''}
          ${msHtml}
          ${kwsHtml}
        </div>
      </article>
    `;
  }

  window.toggleRevealBox = function (elId) {
    const el = document.getElementById(elId);
    if (!el) return;
    el.style.display = el.style.display === 'block' ? 'none' : 'block';
  };

  function renderSchoolMistakes() {
    const container = document.getElementById('sm-list-container');
    if (!container) return;
    const all = getAllChemData().filter(
      (q) => q.source_tag === 'school_mistake' || q.source_tag === 'school_mistake_variant'
    );
    let filtered = all;
    if (currentSmFilter === 'orig') filtered = all.filter((q) => q.source_tag === 'school_mistake');
    else if (currentSmFilter === 'variant') filtered = all.filter((q) => q.source_tag === 'school_mistake_variant');
    else if (currentSmFilter === 'review') filtered = all.filter((q) => masteryMap[q.id] === 'review');
    else if (currentSmFilter === 'mastered') filtered = all.filter((q) => masteryMap[q.id] === 'mastered');

    if (filtered.length === 0) {
      container.innerHTML = `<div class="empty-state">当前筛选条件下暂无题目，点击上方按钮切换筛选范围。</div>`;
    } else {
      container.innerHTML = filtered.map((q) => renderMcqQuestionCard(q, 'sm')).join('');
    }
    updateMasteryStats();
  }

  // ==================== TAB 3: WORKBOOK, PPT & BASELINE FULL BANK ====================
  window.setWbFilter = function (filter, btn) {
    currentWbFilter = filter;
    document.querySelectorAll('#wb-filter-bar .filter-btn').forEach((b) => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    renderWorkbookList();
  };

  function renderWorkbookList() {
    const container = document.getElementById('wb-list-container');
    if (!container) return;
    const fullData = getAllChemData();
    const wbAndPpt = fullData.filter(
      (q) => q.source_tag === 'workbook_pdf' || q.source_tag === 'student_ppt'
    );
    const baselineAll = fullData.filter((q) => q.source_tag === 'baseline');
    let filtered = wbAndPpt;
    let scopeLabel = `${wbAndPpt.length} 道练习册与 PPT 原题`;

    if (currentWbFilter === 'l6') {
      filtered = wbAndPpt.filter((q) => q.workbook_unit === 'Mid-unit Review 1');
    } else if (currentWbFilter === 'l7') {
      filtered = wbAndPpt.filter((q) => q.workbook_unit === 'Lesson 7');
    } else if (currentWbFilter === 'l7_11') {
      filtered = wbAndPpt.filter((q) => ['Lesson 7', 'Lesson 8', 'Lesson 9', 'Lesson 10', 'Lesson 11'].includes(q.workbook_unit));
    } else if (currentWbFilter === 'l12') {
      filtered = wbAndPpt.filter((q) => q.workbook_unit === 'Mid-unit Review 2');
    } else if (currentWbFilter === 'l13_16') {
      filtered = wbAndPpt.filter((q) => ['Lesson 13', 'Lesson 14', 'Lesson 15', 'Lesson 16'].includes(q.workbook_unit));
    } else if (currentWbFilter === 'rev') {
      filtered = wbAndPpt.filter((q) => q.workbook_unit === 'End-of-Unit Revision');
    } else if (currentWbFilter === 'gap') {
      filtered = wbAndPpt.filter((q) => String(q.id || '').startsWith('CHEM_U2_GAP_'));
    } else if (currentWbFilter === 'structured') {
      filtered = wbAndPpt.filter((q) => q.game_type === 'structured');
    } else if (currentWbFilter === 'baseline') {
      filtered = baselineAll;
      scopeLabel = `${baselineAll.length} 道基础巩固基线题（单选/配对/完形/排序）`;
    } else if (currentWbFilter === 'all_plus_base') {
      filtered = [...wbAndPpt, ...baselineAll];
      scopeLabel = `${filtered.length} 道原题+基线题（连同 Tab 2 90 题 = 全库 ${fullData.length} 题零隐藏）`;
    }

    const countEl = document.getElementById('wb-count-label');
    if (countEl) countEl.textContent = `当前显示 ${filtered.length} 题（所属范围：${scopeLabel}）`;

    container.innerHTML = filtered
      .map((q) => (q.game_type === 'mcq' ? renderMcqQuestionCard(q, 'wb') : renderStructuredCard(q, 'wb')))
      .join('');
  }

  // ==================== TAB 4: 45-MIN MOCK EXAM + A4 PRINT ====================
  function ensurePaperState(pid) {
    if (!mockAnswers[pid]) {
      mockAnswers[pid] = { mcq: {}, text: {}, selfScore: {} };
    }
    return mockAnswers[pid];
  }

  window.selectMockPaper = function (pid) {
    currentPaperId = pid;
    mockSubmitted = false;
    stopMockTimer();
    const paper = window.CHEM_MOCK_PAPERS && window.CHEM_MOCK_PAPERS[pid];
    mockRemainingSec = (paper ? paper.durationMin : 45) * 60;
    updateMockTimerDisplay();

    document.querySelectorAll('.paper-switch-btn').forEach((b) => {
      b.classList.toggle('active', b.dataset.paper === pid);
    });
    const diagBox = document.getElementById('mock-diagnosis-box');
    if (diagBox) diagBox.style.display = 'none';
    renderMockPaper();
  };

  function updateMockTimerDisplay() {
    const el = document.getElementById('mock-timer-digits');
    if (!el) return;
    const m = Math.floor(mockRemainingSec / 60);
    const s = mockRemainingSec % 60;
    el.textContent = `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
    el.style.color = mockRemainingSec <= 300 ? '#ef4444' : '#f8fafc';
  }

  function stopMockTimer() {
    if (mockTimerId) {
      clearInterval(mockTimerId);
      mockTimerId = null;
    }
    mockRunning = false;
    const btn = document.getElementById('btn-mock-timer');
    if (btn) btn.textContent = '▶ 开始 45 分钟计时';
  }

  window.toggleMockTimer = function () {
    const btn = document.getElementById('btn-mock-timer');
    if (mockRunning) {
      stopMockTimer();
      return;
    }
    mockRunning = true;
    if (btn) btn.textContent = '⏸ 暂停计时';
    mockTimerId = setInterval(() => {
      mockRemainingSec--;
      updateMockTimerDisplay();
      if (mockRemainingSec <= 0) {
        stopMockTimer();
        alert('⏰ 45 分钟模拟考试时间到！系统将自动核分。');
        window.submitChemMockPaper();
      }
    }, 1000);
  };

  window.resetMockTimer = function () {
    stopMockTimer();
    const paper = window.CHEM_MOCK_PAPERS && window.CHEM_MOCK_PAPERS[currentPaperId];
    mockRemainingSec = (paper ? paper.durationMin : 45) * 60;
    updateMockTimerDisplay();
  };

  window.recordMockMcq = function (qid, letter) {
    ensurePaperState(currentPaperId).mcq[qid] = letter;
  };

  window.recordMockText = function (qid, val) {
    ensurePaperState(currentPaperId).text[qid] = val;
  };

  window.recordMockSelfScore = function (qid, score, btn) {
    ensurePaperState(currentPaperId).selfScore[qid] = score;
    if (btn && btn.parentElement) {
      btn.parentElement.querySelectorAll('.score-btn').forEach((b) => b.classList.remove('selected'));
      btn.classList.add('selected');
    }
    if (mockSubmitted) computeAndRenderDiagnosis();
  };

  function renderMockPaper() {
    const paper = window.CHEM_MOCK_PAPERS && window.CHEM_MOCK_PAPERS[currentPaperId];
    const sheet = document.getElementById('mock-paper-sheet');
    if (!paper || !sheet) return;
    const state = ensurePaperState(currentPaperId);
    const isEnOnly = globalLang === 'en';

    const p1Html = paper.part1_mcq
      .map((q, idx) => {
        const chosen = state.mcq[q.id] || '';
        const optsHtml = q.options
          .map((opt) => {
            const checked = chosen === opt.letter ? 'checked' : '';
            let cls = '';
            if (mockSubmitted) {
              if (opt.letter === q.correct) cls = 'correct';
              else if (chosen === opt.letter) cls = 'wrong';
            }
            return `
              <label class="mock-opt ${cls}">
                <input type="radio" name="mock_${q.id}" value="${opt.letter}" ${checked} onchange="recordMockMcq('${q.id}', '${opt.letter}')">
                <span><strong>${opt.letter}.</strong> ${escapeHtml(opt.en)} ${!isEnOnly ? `<span class="cn-inline">(${escapeHtml(opt.cn)})</span>` : ''}</span>
              </label>
            `;
          })
          .join('');
        return `
          <div class="paper-q-item" id="pq-${q.id}">
            <div class="paper-q-head">
              <strong>Q${idx + 1}.</strong> <span class="q-topic-chip">${escapeHtml(q.topic)}</span>
              <span class="q-marks-chip">[${q.marks} mark]</span>
            </div>
            <div class="paper-q-en">${formatMultiline(q.prompt_en)}</div>
            ${!isEnOnly ? `<div class="paper-q-cn">${formatMultiline(q.prompt_cn)}</div>` : ''}
            <div class="mock-opts-list">${optsHtml}</div>
            <div class="answer-key-block" style="display:${mockSubmitted ? 'block' : 'none'};">
              <strong>✅ Answer: ${q.correct}</strong> — ${escapeHtml(q.explain_en)}
              ${!isEnOnly ? `<div class="cn-sub">${escapeHtml(q.explain_cn)}</div>` : ''}
              <div class="fb-citation">📖 ${escapeHtml(q.citation)}</div>
            </div>
          </div>
        `;
      })
      .join('');

    function renderOpenPart(list, startNum) {
      return list
        .map((q, idx) => {
          const savedVal = state.text[q.id] || '';
          const savedSc = state.selfScore[q.id];
          const scoreBtns = Array.from({ length: q.marks + 1 }, (_, s) => {
            const sel = savedSc === s ? 'selected' : '';
            return `<button type="button" class="score-btn ${sel}" onclick="recordMockSelfScore('${q.id}', ${s}, this)">${s}分</button>`;
          }).join('');
          const msLines = q.mark_scheme
            .map((m, mi) => `<div class="ms-point"><strong>P${mi + 1}:</strong> ${escapeHtml(m)}</div>`)
            .join('');
          return `
            <div class="paper-q-item" id="pq-${q.id}">
              <div class="paper-q-head">
                <strong>Q${startNum + idx}.</strong> <span class="q-topic-chip">${escapeHtml(q.topic)}</span>
                <span class="q-marks-chip">[${q.marks} marks]</span>
              </div>
              <div class="paper-q-en">${formatMultiline(q.prompt_en)}</div>
              ${!isEnOnly ? `<div class="paper-q-cn">${formatMultiline(q.prompt_cn)}</div>` : ''}
              <textarea class="theory-textarea no-print-input" placeholder="在此手打作答（打印空白卷时自动转为横线作答区）..." oninput="recordMockText('${q.id}', this.value)">${escapeHtml(savedVal)}</textarea>
              <div class="print-writing-lines" aria-hidden="true">
                <div class="w-line"></div><div class="w-line"></div><div class="w-line"></div>
                ${q.marks >= 4 ? '<div class="w-line"></div><div class="w-line"></div>' : ''}
              </div>
              <div class="answer-key-block" style="display:${mockSubmitted ? 'block' : 'none'};">
                <div><strong>✅ Model Answer:</strong><br>${formatMultiline(q.model_answer)}</div>
                <div style="margin-top:0.5rem;"><strong>🎯 Mark Scheme:</strong>${msLines}</div>
                <div class="self-score-bar no-print">
                  <span>对照采分点自评：</span>
                  ${scoreBtns}
                </div>
                <div class="fb-citation">📖 ${escapeHtml(q.citation)}</div>
              </div>
            </div>
          `;
        })
        .join('');
    }

    const p2Html = renderOpenPart(paper.part2_calc, paper.part1_mcq.length + 1);
    const p3Html = renderOpenPart(paper.part3_theory, paper.part1_mcq.length + paper.part2_calc.length + 1);

    sheet.innerHTML = `
      <div class="print-exam-header">
        <div class="print-exam-brand">Cambridge G8 Chemistry · Unit 2: Acids, Bases &amp; Salts</div>
        <h2 class="paper-title">${escapeHtml(paper.title_cn)}</h2>
        <div class="paper-subtitle">${escapeHtml(paper.title_en)} · ${escapeHtml(paper.subtitle_cn)}</div>
        <div class="print-student-meta">
          <span>Name: ________________________</span>
          <span>Date: _______________</span>
          <span>Time: ${paper.durationMin} mins</span>
          <span>Score: ______ / ${paper.totalMarks}</span>
        </div>
      </div>

      <section class="paper-section">
        <h3 class="paper-sec-title">Part 1 · Multiple Choice Questions (${paper.part1_mcq.length} Marks)</h3>
        ${p1Html}
      </section>

      <section class="paper-section">
        <h3 class="paper-sec-title">Part 2 · Equations &amp; Quantitative Calculations (${paper.part2_calc.reduce((a, b) => a + b.marks, 0)} Marks)</h3>
        ${p2Html}
      </section>

      <section class="paper-section">
        <h3 class="paper-sec-title">Part 3 · Experimental Design &amp; Structured Short Answers (${paper.part3_theory.reduce((a, b) => a + b.marks, 0)} Marks)</h3>
        ${p3Html}
      </section>
    `;
  }

  function computeAndRenderDiagnosis() {
    const paper = window.CHEM_MOCK_PAPERS && window.CHEM_MOCK_PAPERS[currentPaperId];
    const diagBox = document.getElementById('mock-diagnosis-box');
    if (!paper || !diagBox) return;
    const state = ensurePaperState(currentPaperId);

    let p1Got = 0;
    const topicStats = {};
    function addTopic(topic, got, max) {
      if (!topicStats[topic]) topicStats[topic] = { got: 0, max: 0 };
      topicStats[topic].got += got;
      topicStats[topic].max += max;
    }

    paper.part1_mcq.forEach((q) => {
      const ok = state.mcq[q.id] === q.correct ? q.marks : 0;
      p1Got += ok;
      addTopic(q.topic, ok, q.marks);
    });

    let openGot = 0;
    let openMax = 0;
    let openRated = 0;
    const openAll = [...paper.part2_calc, ...paper.part3_theory];
    openAll.forEach((q) => {
      openMax += q.marks;
      if (state.selfScore[q.id] !== undefined) {
        openRated++;
        openGot += state.selfScore[q.id];
        addTopic(q.topic, state.selfScore[q.id], q.marks);
      } else {
        addTopic(q.topic, 0, q.marks);
      }
    });

    const totalGot = p1Got + openGot;
    const totalMax = paper.totalMarks;
    const pct = Math.round((totalGot / totalMax) * 100);

    const barsHtml = Object.keys(topicStats)
      .map((t) => {
        const s = topicStats[t];
        const tp = s.max ? Math.round((s.got / s.max) * 100) : 0;
        const color = tp >= 80 ? '#10b981' : tp >= 60 ? '#f59e0b' : '#ef4444';
        return `
          <div class="diag-row">
            <div class="diag-row-top">
              <span>${escapeHtml(t)}</span>
              <strong>${s.got} / ${s.max} (${tp}%)</strong>
            </div>
            <div class="diag-bar-track"><div class="diag-bar-fill" style="width:${tp}%;background:${color};"></div></div>
          </div>
        `;
      })
      .join('');

    const weakTopics = Object.keys(topicStats).filter((t) => {
      const s = topicStats[t];
      return s.max > 0 && s.got / s.max < 0.7;
    });

    diagBox.style.display = 'block';
    diagBox.innerHTML = `
      <div class="diag-header">
        <div>
          <h3>📊 ${escapeHtml(paper.code)} 自动核分与薄弱项诊断</h3>
          <div class="diag-sub">Part 1 客观题已自动判分（${p1Got}/${paper.part1_mcq.length}）；Part 2 &amp; Part 3 主观题已自评 ${openRated}/${openAll.length} 题（可在下方逐题点击得分按钮实时更新总分）</div>
        </div>
        <div class="diag-total-score">${totalGot} / ${totalMax} <span>(${pct}%)</span></div>
      </div>
      ${
        weakTopics.length
          ? `<div class="weak-alert">⚠️ <strong>建议考前重点回炉模块：</strong>${weakTopics.map(escapeHtml).join('、')}</div>`
          : `<div class="strong-alert">🌟 <strong>全模块达标！</strong>所有考点得分率均在 70% 以上，状态极佳！</div>`
      }
      <div class="diag-grid">${barsHtml}</div>
    `;
  }

  window.submitChemMockPaper = function () {
    stopMockTimer();
    mockSubmitted = true;
    renderMockPaper();
    computeAndRenderDiagnosis();
    const diagBox = document.getElementById('mock-diagnosis-box');
    if (diagBox) diagBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  window.printChemPaper = function (mode) {
    // mode: 'blank' | 'answers'
    document.body.classList.remove('print-blank-paper', 'print-answer-key');
    document.body.classList.add(mode === 'answers' ? 'print-answer-key' : 'print-blank-paper');
    window.print();
    setTimeout(() => {
      document.body.classList.remove('print-blank-paper', 'print-answer-key');
    }, 800);
  };

  // ==================== BOOTSTRAP ====================
  window.addEventListener('DOMContentLoaded', () => {
    loadMastery();
    renderSchoolMistakes();
    renderWorkbookList();
    selectMockPaper('paperA');
  });
})();
