/* ============================================================================
 * Inquiry Topic 1: Electrolysed Acidic Bubble Water & Skin pH Lab
 * HiDPI DPR <= 2, clamped dt, single-instance RAF with cancelAnimationFrame,
 * visibilitychange pause/resume, bilingual EN/ZH support.
 * ============================================================================ */

const LANG_KEY = "sky_inquiry_lang";
let currentLang = localStorage.getItem(LANG_KEY) || "zh";

let animationFrameId = null;
let lastFrameTime = 0;

const simState = {
  mode: "electrolysis", // "electrolysis" | "carbonated"
  voltage: 8,           // 0 ~ 12 V
  chloride: 25,         // 0 ~ 100 mg/L (trace Cl-)
  bubblesAnode: [],
  bubblesCathode: [],
  ionsH: [],
  ionsOH: [],
  elapsed: 0
};

const SCENARIOS = {
  intact_cleansing: {
    level: "green",
    title_zh: "🟢 完整健康皮肤日常轻度清洁（短时接触）",
    title_en: "🟢 Intact Healthy Skin — Mild Daily Cleansing (Brief Contact)",
    detail_zh: "弱酸性水（pH 4.5–5.5）接近皮肤天然酸性保护膜（Acid Mantle），短时冲洗后擦干通常温和；若含微量 HOCl 仅作表面轻度抑菌，并非药物。",
    detail_en: "Weakly acidic water (pH 4.5–5.5) sits close to the skin's natural Acid Mantle. Brief rinsing on intact skin is generally gentle; trace HOCl offers mild surface sanitisation, not medical therapy."
  },
  oily_skin: {
    level: "amber",
    title_zh: "🟡 青春期轻度出油 / 闭口肌（需控制 pH 与频次）",
    title_en: "🟡 Mildly Oily / Acne-Prone Skin (Monitor pH & Frequency)",
    detail_zh: "酸水不能根治青春痘！过低 pH（< 3.5）或高频湿敷会破坏皮脂膜引发泛红脱皮；规范治疗需遵循皮肤科医生建议（如水杨酸/过氧苯甲酰等循证方案）。",
    detail_en: "Acidic water CANNOT cure acne! Overly low pH (< 3.5) or frequent wet compresses disrupt the lipid barrier and cause irritation. Evidence-based dermatology care is required for acne."
  },
  sunburn_blister: {
    level: "red",
    title_zh: "🔴 晒伤起泡 / 破皮 / 皮肤屏障受损（严禁涂抹！）",
    title_en: "🔴 Blistered / Peeling Sunburn or Broken Skin (STRICTLY PROHIBITED!)",
    detail_zh: "严禁涂抹电解酸性水或碳酸水！酸性 H⁺ 与微量氧化性 HOCl 会直接灼伤暴露真皮层，加重刺痛与延迟愈合。正确处理：凉水冷敷降温、温和保湿、严重起泡立即就医。",
    detail_en: "NEVER apply electrolysed acidic water or carbonated water! Acidic H⁺ and trace oxidising HOCl irritate exposed dermis and worsen tissue injury. Cool gently with plain cool water and seek medical care for blisters."
  },
  drinking: {
    level: "red",
    title_zh: "🔴 直接饮用电解酸性水（严禁饮用！）",
    title_en: "🔴 Drinking Electrolysed Acidic Water (DO NOT DRINK!)",
    detail_zh: "电解水机阳极产出的酸性水通常含微量次氯酸（HOCl）及富集阴离子，属于外用清洁水，绝对禁止作为饮用水饮用！",
    detail_en: "Anode-chamber electrolysed acidic water may contain trace hypochlorous acid (HOCl) and concentrated anions. It is for external use only and must NEVER be consumed."
  }
};

const QUIZ_DATA = [
  {
    q_zh: "1. 在离子膜电解水机的阳极（Anode）室，气泡与酸性的主要化学来源分别是什么？",
    q_en: "1. In the anode chamber of a membrane water electrolyser, what are the primary chemical sources of the fine bubbles and the acidity?",
    options_zh: [
      "A. 气泡是 CO₂，酸性来自碳酸 H₂CO₃",
      "B. 气泡是 O₂，酸性来自阳极水氧化富集的 H⁺ 离子",
      "C. 气泡是 H₂，酸性来自 OH⁻ 离子",
      "D. 气泡是水蒸气，酸性来自电解加热"
    ],
    options_en: [
      "A. Bubbles are CO₂; acidity comes from carbonic acid H₂CO₃",
      "B. Bubbles are O₂; acidity comes from H⁺ ions enriched by water oxidation at the anode",
      "C. Bubbles are H₂; acidity comes from OH⁻ ions",
      "D. Bubbles are steam; acidity comes from heating"
    ],
    answer: 1,
    exp_zh: "阳极发生氧化半反应 2H₂O(l) → O₂(g) + 4H⁺(aq) + 4e⁻，因此细密气泡为氧气 O₂，溶液呈酸性是因为 H⁺ 浓度升高（阴极则生成 H₂ 与 OH⁻）。",
    exp_en: "At the anode, oxidation occurs: 2H₂O(l) → O₂(g) + 4H⁺(aq) + 4e⁻. Fine bubbles are O₂ gas, while accumulated H⁺ ions lower the pH (the cathode generates H₂ and OH⁻)."
  },
  {
    q_zh: "2. 若自来水中含有微量氯离子（Cl⁻），阳极副反应生成的抑菌微粒主要是什么？",
    q_en: "2. When trace chloride ions (Cl⁻) are present in tap water, which weak oxidising species formed via anode side-reactions provides mild antimicrobial action?",
    options_zh: [
      "A. 次氯酸 HOCl（Cl₂ + H₂O ⇌ HOCl + HCl）",
      "B. 氢氧化钠 NaOH",
      "C. 碳酸钙 CaCO₃",
      "D. 氢气 H₂"
    ],
    options_en: [
      "A. Hypochlorous acid HOCl (Cl₂ + H₂O ⇌ HOCl + HCl)",
      "B. Sodium hydroxide NaOH",
      "C. Calcium carbonate CaCO₃",
      "D. Hydrogen gas H₂"
    ],
    answer: 0,
    exp_zh: "少量 Cl⁻ 在阳极被氧化为 Cl₂，随后与水建立平衡 Cl₂ + H₂O ⇌ HOCl + HCl；HOCl 是中性小分子弱氧化剂，能穿透微生物细胞膜产生轻度抑菌作用，但也因此严禁饮用。",
    exp_en: "Trace Cl⁻ oxidises to Cl₂ at the anode and equilibrates with water (Cl₂ + H₂O ⇌ HOCl + HCl). Neutral HOCl acts as a mild oxidising antimicrobial agent, which is also why electrolysed acidic water must not be drunk."
  },
  {
    q_zh: "3. 如何用 IGCSE 0620 标准化学方法鉴别“电解酸性水”与“碳酸气泡水”？",
    q_en: "3. Which IGCSE 0620 chemical test best distinguishes electrolysed acidic water from carbonated sparkling water?",
    options_zh: [
      "A. 仅看是否有气泡即可区分",
      "B. 加热煮沸脱气后测 pH，并将逸出气体通入澄清石灰水：碳酸水使石灰水变浑浊且脱气后 pH 明显回升，电解酸水石灰水不变浑浊",
      "C. 用磁铁吸引气泡",
      "D. 滴加酚酞观察是否变深红"
    ],
    options_en: [
      "A. Observing bubbles alone is sufficient",
      "B. Heat to degas, test escaping gas with limewater, and re-check pH: carbonated water turns limewater milky and its pH rises toward neutral, whereas electrolysed acidic water does not turn limewater milky",
      "C. Test the bubbles with a magnet",
      "D. Add phenolphthalein to look for deep pink"
    ],
    answer: 1,
    exp_zh: "碳酸水遵循 CO₂ + H₂O ⇌ H₂CO₃，受热时 CO₂ 逸出可使澄清石灰水 Ca(OH)₂ 变浑浊，且平衡左移使 pH 回升；电解酸水逸出的是 O₂，不能使石灰水变浑浊。",
    exp_en: "Carbonated water (CO₂ + H₂O ⇌ H₂CO₃) releases CO₂ on warming, turning limewater milky and shifting equilibrium left so pH rises. Electrolysed acidic water releases O₂, giving no precipitate with limewater."
  },
  {
    q_zh: "4. 某杯电解酸水测得 pH = 4.0，而纯水中性 pH = 7.0。二者的氢离子浓度 [H⁺] 相差多少倍？",
    q_en: "4. An electrolysed acidic water sample has pH = 4.0 compared to neutral water at pH = 7.0. How many times higher is its [H⁺] concentration?",
    options_zh: [
      "A. 3 倍",
      "B. 30 倍",
      "C. 100 倍",
      "D. 1,000 倍（10³ 倍）"
    ],
    options_en: [
      "A. 3 times",
      "B. 30 times",
      "C. 100 times",
      "D. 1,000 times (10³)"
    ],
    answer: 3,
    exp_zh: "pH 是以 10 为底的负对数标度（pH = -log₁₀[H⁺]），每降低 1 个单位 [H⁺] 增大 10 倍。pH 4 与 pH 7 相差 3 个单位，故 [H⁺] 高出 10³ = 1,000 倍！",
    exp_en: "pH is a base-10 logarithmic scale (pH = -log₁₀[H⁺]). Each 1-unit drop increases [H⁺] by 10×. A 3-unit difference (7 → 4) means 10³ = 1,000 times higher [H⁺]."
  },
  {
    q_zh: "5. 关于“酸水与皮肤健康”的科学边界，以下哪项陈述是完全准确的？",
    q_en: "5. Which statement accurately reflects the scientific and medical boundary regarding acidic water and skin health?",
    options_zh: [
      "A. 电解酸水能直接治好起泡晒伤和根治青春痘",
      "B. 健康皮肤酸性保护膜 pH 约 4.5–5.5；酸水不能治疗晒伤或根治青春痘，起泡/破皮晒伤严禁涂抹，电解酸水严禁饮用",
      "C. pH 越低（如 pH 1.5）越适合敷脸抑菌",
      "D. 电解酸水可以直接当矿泉水每天饮用"
    ],
    options_en: [
      "A. Electrolysed acidic water cures blistered sunburns and acne",
      "B. Healthy skin's acid mantle is pH 4.5–5.5; acidic water cannot cure sunburn or acne, must never be applied to blistered/broken skin, and must never be drunk",
      "C. Lower pH (such as pH 1.5) is always better for facial care",
      "D. Electrolysed acidic water is safe for daily drinking"
    ],
    answer: 1,
    exp_zh: "健康皮肤表面酸性保护膜约 pH 4.5–5.5。酸水不是药物，不能治疗晒伤或根治青春痘；皮肤起泡破皮时严禁涂抹酸水；电解酸性水亦严禁饮用。",
    exp_en: "The natural acid mantle is pH 4.5–5.5. Acidic water is not a medical treatment for sunburn or acne, must never be applied to broken/blistered skin, and is strictly non-potable."
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

function computeElectrolysisMetrics() {
  if (simState.mode === "carbonated") {
    const ph = 4.1;
    return {
      anodePH: ph,
      cathodePH: 7.0,
      hConc: Math.pow(10, -ph),
      hoclPpm: 0,
      gasLabel: currentLang === "en" ? "CO₂ bubbles (H₂CO₃)" : "CO₂ 气泡（碳酸分解）"
    };
  }
  const intensity = simState.voltage / 12;
  const anodePH = Math.max(2.6, 7.0 - intensity * 3.8);
  const cathodePH = Math.min(11.4, 7.0 + intensity * 3.8);
  const hoclPpm = +(intensity * simState.chloride * 0.45).toFixed(1);
  return {
    anodePH: +anodePH.toFixed(2),
    cathodePH: +cathodePH.toFixed(2),
    hConc: Math.pow(10, -anodePH),
    hoclPpm,
    gasLabel: currentLang === "en" ? "Anode O₂ : Cathode H₂ = 1 : 2" : "阳极 O₂ : 阴极 H₂ = 1 : 2"
  };
}

function updateSimulation(dt) {
  simState.elapsed += dt;
  const intensity = simState.mode === "carbonated" ? 0.65 : simState.voltage / 12;

  // Spawn anode bubbles (O2 or CO2)
  if (intensity > 0.05 && Math.random() < intensity * 26 * dt) {
    simState.bubblesAnode.push({
      x: 115 + (Math.random() - 0.5) * 60,
      y: 270 - Math.random() * 110,
      r: 2 + Math.random() * 3.2,
      vy: 38 + Math.random() * 44
    });
  }

  // Spawn cathode bubbles (H2 at 2x rate in electrolysis mode)
  if (simState.mode === "electrolysis" && intensity > 0.05) {
    for (let k = 0; k < 2; k++) {
      if (Math.random() < intensity * 26 * dt) {
        simState.bubblesCathode.push({
          x: 525 + (Math.random() - 0.5) * 60,
          y: 270 - Math.random() * 110,
          r: 2 + Math.random() * 3.4,
          vy: 46 + Math.random() * 52
        });
      }
    }
  }

  // Update bubbles
  for (let i = simState.bubblesAnode.length - 1; i >= 0; i--) {
    const b = simState.bubblesAnode[i];
    b.y -= b.vy * dt;
    b.x += Math.sin(simState.elapsed * 5 + i) * 10 * dt;
    if (b.y < 102) simState.bubblesAnode.splice(i, 1);
  }
  for (let i = simState.bubblesCathode.length - 1; i >= 0; i--) {
    const b = simState.bubblesCathode[i];
    b.y -= b.vy * dt;
    b.x += Math.cos(simState.elapsed * 5 + i) * 10 * dt;
    if (b.y < 102) simState.bubblesCathode.splice(i, 1);
  }

  // Keep subtle H+ / OH- particle count synced
  const targetIons = Math.round(6 + intensity * 14);
  while (simState.ionsH.length < targetIons) {
    simState.ionsH.push({
      x: 75 + Math.random() * 225,
      y: 115 + Math.random() * 175,
      vx: (Math.random() - 0.5) * 24,
      vy: (Math.random() - 0.5) * 24
    });
  }
  if (simState.ionsH.length > targetIons) simState.ionsH.length = targetIons;

  while (simState.ionsOH.length < targetIons) {
    simState.ionsOH.push({
      x: 380 + Math.random() * 225,
      y: 115 + Math.random() * 175,
      vx: (Math.random() - 0.5) * 24,
      vy: (Math.random() - 0.5) * 24
    });
  }
  if (simState.ionsOH.length > targetIons) simState.ionsOH.length = targetIons;

  simState.ionsH.forEach(p => {
    p.x += p.vx * dt;
    p.y += p.vy * dt;
    if (p.x < 70 || p.x > 315) p.vx *= -1;
    if (p.y < 110 || p.y > 295) p.vy *= -1;
  });

  simState.ionsOH.forEach(p => {
    p.x += p.vx * dt;
    p.y += p.vy * dt;
    if (p.x < 365 || p.x > 610) p.vx *= -1;
    if (p.y < 110 || p.y > 295) p.vy *= -1;
  });
}

function renderCanvas() {
  const canvas = document.getElementById("acidWaterCanvas");
  if (!canvas) return;
  const { ctx, W, H } = setupHiDPICanvas(canvas);
  const metrics = computeElectrolysisMetrics();
  const isEn = currentLang === "en";

  ctx.clearRect(0, 0, W, H);
  const bg = ctx.createLinearGradient(0, 0, 0, H);
  bg.addColorStop(0, "#081021");
  bg.addColorStop(1, "#111c33");
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, W, H);

  if (simState.mode === "carbonated") {
    // Single carbonated beaker comparison view
    const leftX = 160, rightX = 520, topY = 78, bottomY = 308, liqY = 104;
    ctx.fillStyle = "rgba(56, 189, 248, 0.22)";
    ctx.fillRect(leftX + 4, liqY, rightX - leftX - 8, bottomY - liqY - 4);

    // CO2 bubbles across whole beaker
    ctx.fillStyle = "rgba(255, 255, 255, 0.82)";
    simState.bubblesAnode.forEach(b => {
      const bx = 200 + ((b.x * 3.1) % 280);
      ctx.beginPath();
      ctx.arc(bx, b.y, b.r + 0.8, 0, Math.PI * 2);
      ctx.fill();
    });

    ctx.strokeStyle = "#cbd5e1";
    ctx.lineWidth = 3;
    ctx.strokeRect(leftX, topY, rightX - leftX, bottomY - topY);

    ctx.fillStyle = "#e0f2fe";
    ctx.font = "bold 14px -apple-system, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(
      isEn ? "Carbonated Water Control: CO₂(g) + H₂O(l) ⇌ H₂CO₃(aq)" : "对照杯：碳酸气泡水 CO₂(g) + H₂O(l) ⇌ H₂CO₃(aq)",
      W / 2,
      42
    );
    ctx.fillStyle = "#fcd34d";
    ctx.font = "bold 13px monospace";
    ctx.fillText(
      isEn ? "pH ≈ 4.1 | Escaping gas turns limewater MILKY (CaCO₃↓)" : "pH ≈ 4.1 | 逸出 CO₂ 使澄清石灰水变浑浊，加热脱气后 pH 回升",
      W / 2,
      336
    );
    return;
  }

  // Dual-chamber ion-exchange membrane electrolyser
  const tankX = 55, tankY = 78, tankW = 570, tankH = 230, liqY = 104;
  const midX = tankX + tankW / 2;

  // Anode chamber liquid (acidic tint: yellow-orange-pink by pH)
  const acidStrength = Math.max(0, (7 - metrics.anodePH) / 4.4);
  ctx.fillStyle = `rgba(249, 115, 22, ${0.14 + acidStrength * 0.32})`;
  ctx.fillRect(tankX + 3, liqY, tankW / 2 - 5, tankY + tankH - liqY - 3);

  // Cathode chamber liquid (alkaline tint: blue-violet)
  ctx.fillStyle = `rgba(99, 102, 241, ${0.14 + acidStrength * 0.34})`;
  ctx.fillRect(midX + 2, liqY, tankW / 2 - 5, tankY + tankH - liqY - 3);

  // Ion-exchange membrane
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 4;
  ctx.setLineDash([7, 5]);
  ctx.beginPath();
  ctx.moveTo(midX, tankY + 6);
  ctx.lineTo(midX, tankY + tankH - 4);
  ctx.stroke();
  ctx.setLineDash([]);

  // Electrodes
  ctx.fillStyle = "#ef4444";
  ctx.fillRect(102, 128, 22, 152);
  ctx.fillStyle = "#3b82f6";
  ctx.fillRect(516, 128, 22, 152);

  // Power supply bar
  ctx.strokeStyle = "#94a3b8";
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  ctx.moveTo(113, 128);
  ctx.lineTo(113, 38);
  ctx.lineTo(527, 38);
  ctx.lineTo(527, 128);
  ctx.stroke();

  ctx.fillStyle = "#0f172a";
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 2;
  ctx.fillRect(midX - 76, 20, 152, 34);
  ctx.strokeRect(midX - 76, 20, 152, 34);
  ctx.fillStyle = "#f8fafc";
  ctx.font = "bold 12px monospace";
  ctx.textAlign = "center";
  ctx.fillText(`DC ${simState.voltage.toFixed(1)} V`, midX, 41);

  // Draw H+ and OH- ions
  ctx.font = "bold 10px monospace";
  simState.ionsH.forEach(p => {
    ctx.fillStyle = "rgba(251, 146, 60, 0.9)";
    ctx.beginPath();
    ctx.arc(p.x, p.y, 9, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = "#0f172a";
    ctx.fillText("H⁺", p.x, p.y + 3.5);
  });

  simState.ionsOH.forEach(p => {
    ctx.fillStyle = "rgba(129, 140, 248, 0.9)";
    ctx.beginPath();
    ctx.arc(p.x, p.y, 10, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = "#0f172a";
    ctx.fillText("OH⁻", p.x, p.y + 3.5);
  });

  // Draw bubbles
  ctx.fillStyle = "rgba(255, 255, 255, 0.82)";
  simState.bubblesAnode.forEach(b => {
    ctx.beginPath();
    ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
    ctx.fill();
  });
  simState.bubblesCathode.forEach(b => {
    ctx.beginPath();
    ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
    ctx.fill();
  });

  // Tank glass border
  ctx.strokeStyle = "rgba(226, 232, 240, 0.75)";
  ctx.lineWidth = 3;
  ctx.strokeRect(tankX, tankY, tankW, tankH);

  // Labels
  ctx.fillStyle = "#fca5a5";
  ctx.font = "bold 12px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(isEn ? "ANODE (+) · Acidic Water" : "阳极 (+) · 电解酸性水室", 190, 70);
  ctx.fillStyle = "#93c5fd";
  ctx.fillText(isEn ? "CATHODE (−) · Alkaline Water" : "阴极 (−) · 电解碱性水室", 490, 70);

  ctx.fillStyle = "#fde68a";
  ctx.font = "bold 11px monospace";
  ctx.fillText(`pH ${metrics.anodePH.toFixed(2)} | O₂↑ + H⁺`, 190, 329);
  ctx.fillStyle = "#bfdbfe";
  ctx.fillText(`pH ${metrics.cathodePH.toFixed(2)} | H₂↑ + OH⁻`, 490, 329);
  ctx.fillStyle = "#38bdf8";
  ctx.fillText(isEn ? "Ion Membrane" : "离子交换膜", midX, 347);
}

function updateTelemetryUI() {
  const m = computeElectrolysisMetrics();
  document.getElementById("valVoltage").textContent = `${simState.voltage.toFixed(1)} V`;
  document.getElementById("valChloride").textContent = `${simState.chloride} mg/L`;
  document.getElementById("teleAnodePH").textContent = m.anodePH.toFixed(2);
  document.getElementById("teleCathodePH").textContent = simState.mode === "carbonated" ? "—" : m.cathodePH.toFixed(2);
  document.getElementById("teleHConc").textContent = `${m.hConc.toExponential(2)} mol/dm³`;
  document.getElementById("teleHocl").textContent = simState.mode === "carbonated" ? "0.0 ppm" : `${m.hoclPpm} ppm`;
  document.getElementById("teleGasRatio").textContent = m.gasLabel;
}

function updateLogConverter() {
  const phA = parseFloat(document.getElementById("phSliderA").value);
  const phB = parseFloat(document.getElementById("phSliderB").value);
  document.getElementById("valPhA").textContent = `pH ${phA.toFixed(1)}`;
  document.getElementById("valPhB").textContent = `pH ${phB.toFixed(1)}`;
  const diff = Math.abs(phB - phA);
  const ratio = Math.pow(10, diff);
  const formattedRatio = ratio >= 1000 ? Math.round(ratio).toLocaleString("en-US") : ratio.toFixed(ratio < 10 ? 2 : 1);
  const moreAcidic = phA < phB ? `pH ${phA.toFixed(1)}` : (phB < phA ? `pH ${phB.toFixed(1)}` : null);
  const out = document.getElementById("logResultBox");

  if (!moreAcidic) {
    out.textContent = currentLang === "en"
      ? `Equal acidity: both samples have [H⁺] = ${Math.pow(10, -phA).toExponential(2)} mol/dm³ (1× ratio).`
      : `酸度相等：两者 [H⁺] 均为 ${Math.pow(10, -phA).toExponential(2)} mol/dm³（1 倍）。`;
  } else {
    out.textContent = currentLang === "en"
      ? `ΔpH = ${diff.toFixed(1)} → ${moreAcidic} has ${formattedRatio}× higher [H⁺] concentration (10^${diff.toFixed(1)}).`
      : `ΔpH = ${diff.toFixed(1)} → ${moreAcidic} 的氢离子浓度 [H⁺] 高出 ${formattedRatio} 倍（10^${diff.toFixed(1)}）！`;
  }
}

function renderScenarioValidator(key) {
  const sc = SCENARIOS[key] || SCENARIOS.intact_cleansing;
  document.querySelectorAll("[data-scenario]").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.scenario === key);
  });
  const box = document.getElementById("trafficResultBox");
  box.className = `traffic-box ${sc.level}`;
  box.innerHTML = `<strong>${currentLang === "en" ? sc.title_en : sc.title_zh}</strong><p style="margin-top:0.35rem;font-size:0.88rem;">${currentLang === "en" ? sc.detail_en : sc.detail_zh}</p>`;
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
  updateLogConverter();
  const activeScBtn = document.querySelector("[data-scenario].active");
  renderScenarioValidator(activeScBtn ? activeScBtn.dataset.scenario : "intact_cleansing");
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
  const langBtn = document.getElementById("langToggleBtn");
  if (langBtn) {
    langBtn.addEventListener("click", () => {
      currentLang = currentLang === "zh" ? "en" : "zh";
      localStorage.setItem(LANG_KEY, currentLang);
      applyLanguage();
    });
  }

  const vSlider = document.getElementById("voltageSlider");
  const clSlider = document.getElementById("chlorideSlider");
  if (vSlider) {
    vSlider.addEventListener("input", () => {
      simState.voltage = parseFloat(vSlider.value);
      updateTelemetryUI();
    });
  }
  if (clSlider) {
    clSlider.addEventListener("input", () => {
      simState.chloride = parseFloat(clSlider.value);
      updateTelemetryUI();
    });
  }

  document.querySelectorAll("[data-sim-mode]").forEach(btn => {
    btn.addEventListener("click", () => {
      simState.mode = btn.dataset.simMode;
      document.querySelectorAll("[data-sim-mode]").forEach(b => b.classList.toggle("active", b === btn));
      updateTelemetryUI();
    });
  });

  document.getElementById("phSliderA")?.addEventListener("input", updateLogConverter);
  document.getElementById("phSliderB")?.addEventListener("input", updateLogConverter);

  document.querySelectorAll("[data-scenario]").forEach(btn => {
    btn.addEventListener("click", () => renderScenarioValidator(btn.dataset.scenario));
  });

  document.getElementById("quizResetBtn")?.addEventListener("click", () => {
    quizSelections.fill(null);
    renderQuiz();
  });

  applyLanguage();
  startAnimation();
});
