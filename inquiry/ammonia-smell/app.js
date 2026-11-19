/* ============================================================================
 * Inquiry Topic 2: Toilet Ammonia Generation, Solubility Equilibrium & Corridor Diffusion
 * HiDPI DPR <= 2, clamped dt, single-instance RAF with cancelAnimationFrame,
 * visibilitychange pause/resume, bilingual EN/ZH support.
 * ============================================================================ */

const LANG_KEY = "sky_inquiry_lang";
let currentLang = localStorage.getItem(LANG_KEY) || "zh";

let animationFrameId = null;
let lastFrameTime = 0;

const simState = {
  scale: 65,        // Urine scale / urease load (0 ~ 100)
  humidity: 70,     // Wall moisture film (%) (10 ~ 95)
  ventilation: 30,  // Exhaust / corridor airflow (0 ~ 100)
  citricAcid: 0,    // Citric acid neutraliser dosage (0 ~ 100)
  nh3Particles: [],
  airParticles: [],
  elapsed: 0
};

const QUIZ_DATA = [
  {
    q_zh: "1. 新鲜尿液几乎没有刺鼻氨味，为何放置一段时间后厕所会出现强烈氨臭？",
    q_en: "1. Fresh urine has almost no pungent ammonia odour. Why does a strong ammonia smell develop over time in a restroom?",
    options_zh: [
      "A. 尿液中的水直接电解产生了氨气",
      "B. 细菌分泌的脲酶催化无味尿素水解：CO(NH₂)₂ + H₂O → 2NH₃(g) + CO₂(g)",
      "C. 空气中的氮气在常温下直接与水反应生成氨气",
      "D. 瓷砖中的钙离子挥发变成氨气"
    ],
    options_en: [
      "A. Water in urine electrolyses spontaneously into ammonia",
      "B. Bacterial urease catalyses the hydrolysis of odourless urea: CO(NH₂)₂ + H₂O → 2NH₃(g) + CO₂(g)",
      "C. Atmospheric N₂ reacts directly with water at room temperature",
      "D. Calcium ions from tiles evaporate as ammonia"
    ],
    answer: 1,
    exp_zh: "新鲜尿液的主要含氮成分是无味尿素 CO(NH₂)₂；环境细菌分泌的脲酶（Urease）将其水解生成挥发性氨气 NH₃ 与 CO₂。",
    exp_en: "Fresh urine contains odourless urea CO(NH₂)₂. Environmental bacteria secrete urease, catalysing hydrolysis into volatile NH₃ and CO₂."
  },
  {
    q_zh: "2. 依据相对分子质量 Mr 与 Graham 扩散速率定律，为何氨气比空气中多数重分子扩散更快且容易飘向走廊？",
    q_en: "2. Using relative molecular mass (Mr) and Graham's law of diffusion, why does NH₃ diffuse faster and spread easily down a corridor?",
    options_zh: [
      "A. Mr(NH₃) = 17 远小于空气平均 Mr ≈ 29，分子质量更轻、热运动速率更快、密度更小易上浮，再叠加走廊空气对流",
      "B. Mr(NH₃) = 64，比空气重，沿着地板滚动",
      "C. 氨气分子完全静止，仅靠重力扩散",
      "D. 氨气不发生随机热运动"
    ],
    options_en: [
      "A. Mr(NH₃) = 17 is much lower than air's average Mr ≈ 29, so NH₃ molecules move faster, rise due to lower density, and ride corridor convection currents",
      "B. Mr(NH₃) = 64, making it heavier than air so it rolls along the floor",
      "C. NH₃ molecules are stationary and move only by gravity",
      "D. NH₃ does not undergo random thermal motion"
    ],
    answer: 0,
    exp_zh: "Mr(NH₃) = 14 + 3×1 = 17 < 29，由 r₁/r₂ = √(M₂/M₁) 可得氨气扩散速率约为空气平均分子的 √(29/17) ≈ 1.31 倍，且密度低于空气易上浮并随走廊气流远距离传播。",
    exp_en: "Mr(NH₃) = 17 < 29. By Graham's law (r₁/r₂ = √(M₂/M₁)), NH₃ diffuses ~√(29/17) ≈ 1.31× faster than average air molecules, rises due to lower density, and is carried by corridor airflow."
  },
  {
    q_zh: "3. IGCSE 0620 考纲中，检验氨气（NH₃）的标准实验室方法与现象是什么？",
    q_en: "3. In the IGCSE 0620 syllabus, what is the standard chemical test and positive observation for ammonia gas (NH₃)?",
    options_zh: [
      "A. 使燃着木条发出爆鸣声",
      "B. 使澄清石灰水变浑浊",
      "C. 使潮湿的红色石蕊试纸变为蓝色（NH₃ + H₂O ⇌ NH₄⁺ + OH⁻）",
      "D. 使干燥蓝色石蕊试纸变红"
    ],
    options_en: [
      "A. Gives a squeaky pop with a lighted splint",
      "B. Turns limewater milky",
      "C. Turns damp red litmus paper blue (NH₃ + H₂O ⇌ NH₄⁺ + OH⁻)",
      "D. Turns dry blue litmus paper red"
    ],
    answer: 2,
    exp_zh: "氨气极易溶于水（约 1:700）并发生可逆电离生成 OH⁻，使试纸呈碱性，因此检验氨气的标准方法是【潮湿红色石蕊试纸变蓝】。",
    exp_en: "NH₃ is highly soluble in water (~1:700) and establishes NH₃ + H₂O ⇌ NH₄⁺ + OH⁻, producing alkaline OH⁻ ions that turn damp red litmus paper blue."
  },
  {
    q_zh: "4. 为什么柠檬酸（弱酸）能从化学上消除氨臭，而不是像香水一样仅仅掩盖气味？",
    q_en: "4. Why does citric acid (a weak acid) chemically remove ammonia odour rather than merely masking it like air freshener?",
    options_zh: [
      "A. 柠檬酸将氨气氧化为黄金",
      "B. 柠檬酸提供 H⁺ 与挥发性碱性气体 NH₃ 发生中和反应，转化为无味、不挥发的水溶性铵盐离子 NH₄⁺",
      "C. 柠檬酸把厕所温度降到绝对零度",
      "D. 柠檬酸与氮气反应生成塑料"
    ],
    options_en: [
      "A. Citric acid oxidises ammonia into solid metal",
      "B. Citric acid donates H⁺ to neutralise volatile alkaline NH₃ gas into non-volatile, odourless soluble ammonium ions (NH₄⁺)",
      "C. Citric acid cools the restroom to absolute zero",
      "D. Citric acid converts nitrogen into plastic"
    ],
    answer: 1,
    exp_zh: "挥发性的氨分子 NH₃ 接受酸提供的质子 H⁺ 后变为离子态 NH₄⁺（铵盐），离子化合物蒸气压极低不再挥发到空气中，从而彻底去味。",
    exp_en: "Volatile NH₃ molecules accept H⁺ from citric acid to form ionic ammonium salts (NH₄⁺). Ionic salts are non-volatile and cannot escape into the air as odour."
  },
  {
    q_zh: "5. 【致命安全红线】为什么严禁将盐酸洁厕灵（HCl）与 84 消毒液（NaClO）混合使用？",
    q_en: "5. [FATAL SAFETY RULE] Why must hydrochloric acid toilet cleaner (HCl) NEVER be mixed with bleach (NaClO)?",
    options_zh: [
      "A. 混合后只产生纯水，没有清洁力",
      "B. 发生剧烈氧化还原反应释放剧毒黄绿色氯气：NaClO + 2HCl → NaCl + H₂O + Cl₂↑",
      "C. 会产生大量氧气使人精力充沛",
      "D. 会结冰堵塞下水道"
    ],
    options_en: [
      "A. They only form pure water and lose cleaning power",
      "B. They react vigorously to release highly toxic chlorine gas: NaClO + 2HCl → NaCl + H₂O + Cl₂↑",
      "C. They release pure oxygen gas",
      "D. They freeze and block the drain"
    ],
    answer: 1,
    exp_zh: "次氯酸钠与盐酸混合立即反应生成剧毒氯气 Cl₂↑（NaClO + 2HCl → NaCl + H₂O + Cl₂↑），吸入高浓度氯气可引发严重呼吸道化学灼伤、肺水肿甚至危及生命！",
    exp_en: "Bleach (NaClO) + HCl immediately generates toxic yellow-green chlorine gas (NaClO + 2HCl → NaCl + H₂O + Cl₂↑), which causes severe respiratory burns and pulmonary oedema."
  }
];

const quizSelections = new Array(QUIZ_DATA.length).fill(null);

function setupHiDPICanvas(canvas) {
  const logicalW = Number(canvas.dataset.logicalWidth) || canvas.width || 680;
  const logicalH = Number(canvas.dataset.logicalHeight) || canvas.height || 360;
  if (!canvas.dataset.logicalWidth) canvas.dataset.logicalWidth = String(logicalW);
  if (!canvas.dataset.logicalHeight) canvas.dataset.logicalHeight = String(logicalH);

  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const targetW = Math.round(logicalW * dpr);
  const targetH = Math.round(logicalH * dpr);
  if (canvas.width !== targetW || canvas.height !== targetH) {
    canvas.width = targetW;
    canvas.height = targetH;
  }

  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  return { ctx, W: logicalW, H: logicalH, dpr };
}

function stopAnimation() {
  if (animationFrameId !== null) {
    cancelAnimationFrame(animationFrameId);
    animationFrameId = null;
  }
}

function startAnimation() {
  stopAnimation();
  if (document.hidden) return;
  lastFrameTime = performance.now();
  animationFrameId = requestAnimationFrame(tickSimulation);
}

function tickSimulation(now) {
  animationFrameId = null;
  if (document.hidden) return;
  const dt = Math.min(Math.max((now - lastFrameTime) / 1000, 0), 0.05);
  lastFrameTime = now;
  updateSimulation(dt);
  renderCanvas();
  animationFrameId = requestAnimationFrame(tickSimulation);
}

function computeAmmoniaMetrics() {
  // Effective ammonia generation rate reduced by citric acid neutralisation
  const rawGen = simState.scale / 100;
  const neutralFactor = 1 - (simState.citricAcid / 100) * 0.92;
  const activeGen = Math.max(0, rawGen * neutralFactor);

  // Humidity traps NH3 in wall film (persistence), ventilation flushes corridor
  const filmTrap = (simState.humidity / 100) * (0.4 + activeGen * 0.6);
  const ventReduction = 1 - (simState.ventilation / 100) * 0.78;
  const corridorPpm = +(activeGen * 42 * ventReduction + filmTrap * 12 * ventReduction).toFixed(1);
  const grahamRatio = Math.sqrt(29 / 17); // ~1.306
  const litmusBlue = corridorPpm >= 3.5;

  return {
    activeGen,
    filmTrap,
    corridorPpm,
    grahamRatio,
    litmusBlue
  };
}

function updateSimulation(dt) {
  simState.elapsed += dt;
  const m = computeAmmoniaMetrics();

  // Spawn NH3 particles from restroom urine scale zone
  const targetNH3 = Math.round(6 + m.activeGen * 46 + m.filmTrap * 14);
  if (simState.nh3Particles.length < targetNH3 && Math.random() < 28 * dt) {
    simState.nh3Particles.push({
      x: 75 + Math.random() * 125,
      y: 255 + Math.random() * 25,
      vx: 26 + Math.random() * 48, // fast diffusion (Mr=17)
      vy: -(24 + Math.random() * 36), // lighter than air -> rises
      absorbed: false
    });
  }
  if (simState.nh3Particles.length > targetNH3 + 8) {
    simState.nh3Particles.splice(0, simState.nh3Particles.length - targetNH3);
  }

  // Background heavier air molecules (Mr ~ 29) for diffusion speed contrast
  while (simState.airParticles.length < 18) {
    simState.airParticles.push({
      x: 40 + Math.random() * 600,
      y: 70 + Math.random() * 220,
      vx: (Math.random() - 0.5) * 34,
      vy: (Math.random() - 0.5) * 28
    });
  }

  const ventDrift = (simState.ventilation / 100) * 42;
  for (let i = simState.nh3Particles.length - 1; i >= 0; i--) {
    const p = simState.nh3Particles[i];
    // Convection toward corridor or out exhaust vent
    const corridorPush = simState.ventilation > 60 ? -ventDrift * 0.55 : (18 + (100 - simState.ventilation) * 0.25);
    p.x += (p.vx * 0.45 + corridorPush) * dt;
    p.y += (p.vy * 0.5 + Math.sin(simState.elapsed * 3 + i) * 14) * dt;

    // Ceiling & floor bounds
    if (p.y < 76) {
      p.y = 76;
      p.vy = Math.abs(p.vy) * 0.4;
    }
    if (p.y > 286) {
      p.y = 286;
      p.vy = -Math.abs(p.vy);
    }

    // Restroom wall doorway at x=255 (opening y: 120..280)
    if (p.x > 248 && p.x < 262 && p.y < 122) {
      p.vx = -Math.abs(p.vx);
    }

    // Recycle particles leaving right corridor edge or exhausted
    if (p.x > 640 || p.x < 38) {
      simState.nh3Particles.splice(i, 1);
    }
  }

  simState.airParticles.forEach(a => {
    a.x += a.vx * dt;
    a.y += a.vy * dt;
    if (a.x < 40 || a.x > 640) a.vx *= -1;
    if (a.y < 72 || a.y > 288) a.vy *= -1;
  });
}

function renderCanvas() {
  const canvas = document.getElementById("ammoniaCanvas");
  if (!canvas) return;
  const { ctx, W, H } = setupHiDPICanvas(canvas);
  const m = computeAmmoniaMetrics();
  const isEn = currentLang === "en";

  ctx.clearRect(0, 0, W, H);
  const bg = ctx.createLinearGradient(0, 0, 0, H);
  bg.addColorStop(0, "#090f1f");
  bg.addColorStop(1, "#131e36");
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, W, H);

  // Restroom chamber (left) & Corridor (right)
  ctx.strokeStyle = "#64748b";
  ctx.lineWidth = 3;
  ctx.strokeRect(36, 66, 608, 230);

  // Partition wall with doorway
  ctx.beginPath();
  ctx.moveTo(255, 66);
  ctx.lineTo(255, 122);
  ctx.stroke();

  // Wall moisture film (absorbs NH3 into NH4+ + OH-)
  const filmAlpha = 0.08 + (simState.humidity / 100) * 0.42;
  ctx.fillStyle = `rgba(56, 189, 248, ${filmAlpha})`;
  ctx.fillRect(38, 68, 12, 226);
  ctx.fillRect(247, 68, 8, 54);

  // Urine scale deposit at bottom of restroom
  const scaleH = Math.max(4, (simState.scale / 100) * 26);
  ctx.fillStyle = simState.citricAcid > 50 ? "#10b981" : "#eab308";
  ctx.fillRect(58, 294 - scaleH, 165, scaleH);

  // Exhaust fan indicator at top left
  ctx.fillStyle = simState.ventilation > 40 ? "#38bdf8" : "#475569";
  ctx.fillRect(110, 56, 70, 12);

  // Air molecules (slower, grey-blue, Mr ~ 29)
  simState.airParticles.forEach(a => {
    ctx.fillStyle = "rgba(148, 163, 184, 0.35)";
    ctx.beginPath();
    ctx.arc(a.x, a.y, 5, 0, Math.PI * 2);
    ctx.fill();
  });

  // NH3 molecules (faster, glowing amber/green, Mr = 17)
  simState.nh3Particles.forEach(p => {
    ctx.fillStyle = "rgba(250, 204, 21, 0.88)";
    ctx.beginPath();
    ctx.arc(p.x, p.y, 4.2, 0, Math.PI * 2);
    ctx.fill();
  });

  // Damp red litmus strip in corridor (IGCSE 0620 test)
  const stripX = 568, stripY = 128;
  ctx.fillStyle = m.litmusBlue ? "#3b82f6" : "#ef4444";
  ctx.fillRect(stripX, stripY, 24, 72);
  ctx.strokeStyle = "#e2e8f0";
  ctx.lineWidth = 1.5;
  ctx.strokeRect(stripX, stripY, 24, 72);

  ctx.fillStyle = "#e2e8f0";
  ctx.font = "bold 10px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(isEn ? "Damp Litmus" : "潮湿石蕊试纸", stripX + 12, stripY - 8);
  ctx.fillStyle = m.litmusBlue ? "#93c5fd" : "#fca5a5";
  ctx.fillText(m.litmusBlue ? (isEn ? "BLUE (NH₃)" : "变蓝 (含NH₃)") : (isEn ? "RED (Clean)" : "红色 (洁净)"), stripX + 12, stripY + 86);

  // Zone headers & legend
  ctx.fillStyle = "#fde047";
  ctx.font = "bold 12px -apple-system, sans-serif";
  ctx.textAlign = "left";
  ctx.fillText(isEn ? "Restroom Source (Urea + Urease → 2NH₃↑)" : "厕所源头（尿素 + 脲酶 → 2NH₃↑）", 44, 44);
  ctx.fillStyle = "#7dd3fc";
  ctx.fillText(isEn ? "Corridor Diffusion & Airflow (Mr = 17 vs Air 29)" : "走廊扩散与对流区（NH₃ Mr=17 轻于空气 Mr≈29）", 272, 44);

  ctx.fillStyle = "#cbd5e1";
  ctx.font = "bold 11px monospace";
  ctx.fillText(
    isEn
      ? `● Yellow: NH₃ (Mr=17, ~1.31× faster)   ● Grey: Air (Mr≈29)   Corridor NH₃: ${m.corridorPpm} ppm`
      : `● 黄色：NH₃ 分子 (Mr=17, 速率约1.31倍)   ● 灰色：空气分子 (Mr≈29)   走廊浓度：${m.corridorPpm} ppm`,
    40,
    330
  );
}

function updateTelemetryUI() {
  const m = computeAmmoniaMetrics();
  const isEn = currentLang === "en";
  document.getElementById("valScale").textContent = `${simState.scale}%`;
  document.getElementById("valHumidity").textContent = `${simState.humidity}%`;
  document.getElementById("valVent").textContent = `${simState.ventilation}%`;
  document.getElementById("valCitric").textContent = `${simState.citricAcid}%`;

  document.getElementById("telePpm").textContent = `${m.corridorPpm} ppm`;
  document.getElementById("teleGraham").textContent = `${m.grahamRatio.toFixed(2)}×`;
  document.getElementById("teleFilm").textContent = `${Math.round(m.filmTrap * 100)}%`;
  document.getElementById("teleLitmus").textContent = m.litmusBlue
    ? (isEn ? "Blue (Alkaline NH₃)" : "变蓝（检出碱性 NH₃）")
    : (isEn ? "Red (Low NH₃)" : "保持红色（低浓度）");
}

function evaluateCleanerMix(mixKey) {
  document.querySelectorAll("[data-mix]").forEach(b => b.classList.toggle("active", b.dataset.mix === mixKey));
  const box = document.getElementById("mixResultBox");
  const isEn = currentLang === "en";

  if (mixKey === "hcl_bleach") {
    box.className = "traffic-box red";
    box.innerHTML = isEn
      ? `<strong>🔴 FATAL HAZARD: HCl Toilet Cleaner + NaClO Bleach!</strong><p style="margin-top:0.35rem;font-size:0.88rem;">Immediately generates toxic chlorine gas: <code>NaClO + 2HCl → NaCl + H₂O + Cl₂↑</code>. NEVER mix acidic cleaners with chlorine bleach!</p>`
      : `<strong>🔴 致命剧毒警报：盐酸洁厕灵 + 84 消毒液（NaClO）！</strong><p style="margin-top:0.35rem;font-size:0.88rem;">立即剧烈反应释放剧毒氯气：<code>NaClO + 2HCl → NaCl + H₂O + Cl₂↑</code>。严禁混用，如误混请立即撤离并开窗通风！</p>`;
  } else if (mixKey === "citric_only") {
    box.className = "traffic-box green";
    box.innerHTML = isEn
      ? `<strong>🟢 SAFE & EFFECTIVE: Citric Acid + Ventilation + Water Flush</strong><p style="margin-top:0.35rem;font-size:0.88rem;">Weak citric acid dissolves alkaline urine scale and neutralises volatile NH₃ into non-volatile NH₄⁺ salts without releasing chlorine gas.</p>`
      : `<strong>🟢 科学安全方案：柠檬酸弱酸除垢 + 清水冲洗 + 排风</strong><p style="margin-top:0.35rem;font-size:0.88rem;">柠檬酸可安全溶解碱性尿垢，并将挥发性 NH₃ 中和为无味、不挥发的铵盐（NH₄⁺），零毒气风险。</p>`;
  } else {
    box.className = "traffic-box amber";
    box.innerHTML = isEn
      ? `<strong>🟡 MASKING ONLY: Perfume / Air Freshener Spray</strong><p style="margin-top:0.35rem;font-size:0.88rem;">Fragrance does not remove urine scale or neutralise NH₃ molecules; ammonia remains dissolved in damp wall films and continues to evaporate.</p>`
      : `<strong>🟡 仅能短暂遮盖：空气清新剂 / 香水喷雾</strong><p style="margin-top:0.35rem;font-size:0.88rem;">香精无法清除尿垢或中和 NH₃ 分子；潮湿墙面水膜中的氨仍会随蒸发反复释放，治标不治本。</p>`;
  }
}

function renderQuiz() {
  const container = document.getElementById("quizList");
  if (!container) return;
  container.innerHTML = "";
  const isEn = currentLang === "en";
  let score = 0;
  let answeredCount = 0;

  QUIZ_DATA.forEach((item, qIdx) => {
    const picked = quizSelections[qIdx];
    if (picked !== null) {
      answeredCount++;
      if (picked === item.answer) score++;
    }

    const card = document.createElement("div");
    card.className = "quiz-card";
    const qText = isEn ? item.q_en : item.q_zh;
    const opts = isEn ? item.options_en : item.options_zh;
    const exp = isEn ? item.exp_en : item.exp_zh;

    const optsHtml = opts.map((opt, idx) => {
      let cls = "quiz-opt-btn";
      if (picked !== null) {
        if (idx === item.answer) cls += " correct";
        else if (idx === picked) cls += " wrong";
      }
      return `<button type="button" class="${cls}" data-q="${qIdx}" data-o="${idx}" ${picked !== null ? "disabled" : ""}>${opt}</button>`;
    }).join("");

    card.innerHTML = `
      <div class="quiz-q">${qText}</div>
      <div class="quiz-options">${optsHtml}</div>
      <div class="quiz-explain ${picked !== null ? "show" : ""}">
        <strong>${picked === item.answer ? (isEn ? "✅ Correct! " : "✅ 回答正确！") : (isEn ? "❌ Review: " : "❌ 解析纠正：")}</strong>${exp}
      </div>
    `;
    container.appendChild(card);
  });

  container.querySelectorAll(".quiz-opt-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const qIdx = Number(btn.dataset.q);
      const oIdx = Number(btn.dataset.o);
      if (quizSelections[qIdx] !== null) return;
      quizSelections[qIdx] = oIdx;
      renderQuiz();
    });
  });

  const scoreEl = document.getElementById("quizScoreText");
  if (scoreEl) {
    scoreEl.textContent = isEn
      ? `Score: ${score} / ${QUIZ_DATA.length} (${answeredCount} answered)`
      : `当前得分：${score} / ${QUIZ_DATA.length}（已答 ${answeredCount} 题）`;
  }
}

function applyLanguage() {
  const isEn = currentLang === "en";
  document.documentElement.lang = isEn ? "en" : "zh-CN";
  document.querySelectorAll("[data-zh][data-en]").forEach(el => {
    el.innerHTML = isEn ? el.dataset.en : el.dataset.zh;
  });
  const btn = document.getElementById("langToggleBtn");
  if (btn) btn.textContent = isEn ? "🌐 切换中文" : "🌐 Switch to EN";

  updateTelemetryUI();
  const activeMixBtn = document.querySelector("[data-mix].active");
  evaluateCleanerMix(activeMixBtn ? activeMixBtn.dataset.mix : "citric_only");
  renderQuiz();
}

document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    stopAnimation();
  } else {
    startAnimation();
  }
});

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("langToggleBtn")?.addEventListener("click", () => {
    currentLang = currentLang === "zh" ? "en" : "zh";
    localStorage.setItem(LANG_KEY, currentLang);
    applyLanguage();
  });

  document.getElementById("scaleSlider")?.addEventListener("input", e => {
    simState.scale = parseFloat(e.target.value);
    updateTelemetryUI();
  });
  document.getElementById("humiditySlider")?.addEventListener("input", e => {
    simState.humidity = parseFloat(e.target.value);
    updateTelemetryUI();
  });
  document.getElementById("ventSlider")?.addEventListener("input", e => {
    simState.ventilation = parseFloat(e.target.value);
    updateTelemetryUI();
  });
  document.getElementById("citricSlider")?.addEventListener("input", e => {
    simState.citricAcid = parseFloat(e.target.value);
    updateTelemetryUI();
  });

  document.querySelectorAll("[data-mix]").forEach(btn => {
    btn.addEventListener("click", () => evaluateCleanerMix(btn.dataset.mix));
  });

  document.getElementById("quizResetBtn")?.addEventListener("click", () => {
    quizSelections.fill(null);
    renderQuiz();
  });

  applyLanguage();
  startAnimation();
});
