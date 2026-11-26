/**
 * Sky G8 Chemistry Unit 2 (Acids, Bases & Salts) — 45-Minute Full Mock Exam Papers
 * Paper A: Foundation Core Paper (基础必拿卷 — 40 Marks, 45 Minutes)
 * Paper B: Extended Trap-Buster Paper (拔高防坑卷 — 45 Marks, 45 Minutes)
 * Aligned strictly to Cambridge IGCSE 0620 & G8_U2_Acids_and_Bases_Workbook_PDF.pdf.
 */
window.CHEM_MOCK_PAPERS = {
  paperA: {
    id: 'paperA',
    code: 'PAPER A',
    title_cn: 'Paper A · 基础必拿卷（覆盖核心考点与学校高频错题）',
    title_en: 'Paper A · Foundation Core Paper (45 min · 40 Marks)',
    subtitle_cn: 'Part 1 选择题 (15×1=15分) + Part 2 方程式与计算 (5×2=10分) + Part 3 实验设计与简答 (3题=15分)',
    subtitle_en: 'Part 1 MCQs (15 marks) + Part 2 Equations & Calculations (10 marks) + Part 3 Practical & Structured Theory (15 marks)',
    durationMin: 45,
    totalMarks: 40,
    part1_mcq: [
      {
        id: 'PA_M01', topic: 'Everyday Acids', marks: 1,
        citation: 'School Review Q3 & Workbook p.19',
        prompt_en: 'What is the chemical name for Vitamin C?',
        prompt_cn: '维生素 C 的化学名称是什么？',
        options: [
          { letter: 'A', en: 'Citric acid', cn: '柠檬酸' },
          { letter: 'B', en: 'Ascorbic acid', cn: '抗坏血酸' },
          { letter: 'C', en: 'Carbonic acid', cn: '碳酸' },
          { letter: 'D', en: 'Ethanoic acid', cn: '乙酸' }
        ],
        correct: 'B',
        explain_cn: '维生素 C 的化学名称是抗坏血酸（Ascorbic acid）；柠檬酸是柑橘果实中的酸，切勿混淆。',
        explain_en: 'Vitamin C is ascorbic acid (citric acid is found in lemons/oranges).'
      },
      {
        id: 'PA_M02', topic: 'Lab Safety & Hazards', marks: 1,
        citation: 'PPT Slide 3 & Workbook pp.19, 135 (Corrosive / Irritant)',
        prompt_en: 'Concentrated sulfuric acid carries the Corrosive hazard symbol. Which procedure is essential when diluting it safely in the lab?',
        prompt_cn: '浓硫酸瓶贴有腐蚀性（Corrosive）危险标志。实验室安全稀释浓酸的必备规范是？',
        options: [
          { letter: 'A', en: 'Wear safety goggles and slowly ADD ACID TO WATER while stirring', cn: '佩戴护目镜，搅拌下将酸缓慢注入水中（Add acid to water）' },
          { letter: 'B', en: 'Pour cold water quickly into the concentrated acid', cn: '将冷水快速倒入浓酸中' },
          { letter: 'C', en: 'Dilute it without goggles because it becomes an irritant', cn: '稀释后会变为刺激性，无需护目镜' },
          { letter: 'D', en: 'Taste a drop to check acidity', cn: '品尝一滴确认酸度' }
        ],
        correct: 'A',
        explain_cn: '浓酸稀释剧烈放热，必须佩戴护目镜并严格遵循“酸入水（Add acid to water）”，严防水入酸暴沸飞溅。',
        explain_en: 'Always wear goggles and add acid slowly to water to disperse exothermic heat safely.'
      },
      {
        id: 'PA_M03', topic: 'Indicators', marks: 1,
        citation: 'School Review Q24 & Workbook p.61 (L6 Q12)',
        prompt_en: 'What are the colours of methyl orange in an acidic, neutral, and alkaline solution respectively?',
        prompt_cn: '甲基橙在酸性、中性、碱性溶液中分别呈什么颜色？',
        options: [
          { letter: 'A', en: 'Red | Orange | Yellow', cn: '红 | 橙 | 黄' },
          { letter: 'B', en: 'Yellow | Orange | Red', cn: '黄 | 橙 | 红' },
          { letter: 'C', en: 'Red | Purple | Blue', cn: '红 | 紫 | 蓝' },
          { letter: 'D', en: 'Colourless | Colourless | Blue', cn: '无色 | 无色 | 蓝' }
        ],
        correct: 'A',
        explain_cn: '甲基橙：酸红、中橙、碱黄。',
        explain_en: 'Methyl orange is red in acid, orange in neutral, and yellow in alkali.'
      },
      {
        id: 'PA_M04', topic: 'Indicators', marks: 1,
        citation: 'Workbook p.61 (L6 Q13) & p.151',
        prompt_en: 'Which indicator is colourless in acid and BLUE in alkali?',
        prompt_cn: '哪种指示剂在酸中无色、在碱中呈蓝色？',
        options: [
          { letter: 'A', en: 'Litmus', cn: '石蕊' },
          { letter: 'B', en: 'Methyl orange', cn: '甲基橙' },
          { letter: 'C', en: 'Thymolphthalein', cn: '百里酚酞' },
          { letter: 'D', en: 'Phenolphthalein', cn: '酚酞' }
        ],
        correct: 'C',
        explain_cn: '百里酚酞（Thymolphthalein）酸无色碱蓝；酚酞酸无色碱粉红。',
        explain_en: 'Thymolphthalein is colourless in acid and blue in alkali (phenolphthalein is pink in alkali).'
      },
      {
        id: 'PA_M05', topic: 'Indicators', marks: 1,
        citation: 'School Review Q27 & Workbook p.62 (L6 Q14)',
        prompt_en: 'Which indicator is best used to estimate the approximate pH value (0–14) of an unknown solution?',
        prompt_cn: '估算未知溶液 pH 数值（0–14）最适合用哪种指示剂？',
        options: [
          { letter: 'A', en: 'Litmus paper', cn: '石蕊试纸' },
          { letter: 'B', en: 'Universal indicator', cn: '广范指示剂' },
          { letter: 'C', en: 'Methyl orange', cn: '甲基橙' },
          { letter: 'D', en: 'Phenolphthalein', cn: '酚酞' }
        ],
        correct: 'B',
        explain_cn: '广范指示剂呈现完整 0–14 彩虹色谱，可用于估算具体 pH。',
        explain_en: 'Universal indicator displays a continuous colour spectrum across pH 0–14.'
      },
      {
        id: 'PA_M06', topic: 'Acid Reactions', marks: 1,
        citation: 'School Review Q6 & Workbook p.60 (L6 Q5)',
        prompt_en: 'What is the general word equation for a reactive metal reacting with a dilute acid?',
        prompt_cn: '活泼金属与稀酸反应的通用文字方程式是？',
        options: [
          { letter: 'A', en: 'Acid + Metal → Salt + Water', cn: '酸 + 金属 → 盐 + 水' },
          { letter: 'B', en: 'Acid + Metal → Salt + Hydrogen', cn: '酸 + 金属 → 盐 + 氢气' },
          { letter: 'C', en: 'Acid + Metal → Salt + Carbon dioxide', cn: '酸 + 金属 → 盐 + 二氧化碳' },
          { letter: 'D', en: 'Acid + Metal → Salt + Water + Carbon dioxide', cn: '酸 + 金属 → 盐 + 水 + 二氧化碳' }
        ],
        correct: 'B',
        explain_cn: '酸 + 活泼金属 → 盐 + 氢气（H₂）。',
        explain_en: 'Acid + Reactive Metal → Salt + Hydrogen.'
      },
      {
        id: 'PA_M07', topic: 'Gas Tests', marks: 1,
        citation: 'School Review Q7 & Workbook p.60 (L6 Q4)',
        prompt_en: 'How do you confirm that the gas produced from zinc and dilute hydrochloric acid is hydrogen?',
        prompt_cn: '如何确证锌与稀盐酸反应产生的气体是氢气？',
        options: [
          { letter: 'A', en: 'Glowing splint relights', cn: '带火星木条复燃' },
          { letter: 'B', en: 'Lit splint gives a squeaky pop', cn: '燃着木条发出尖锐爆鸣声' },
          { letter: 'C', en: 'Limewater turns milky', cn: '澄清石灰水变浑浊' },
          { letter: 'D', en: 'Damp red litmus turns blue', cn: '湿润红石蕊变蓝' }
        ],
        correct: 'B',
        explain_cn: '检验氢气必须用燃着的木条（lit splint）听见爆鸣声（squeaky pop）。',
        explain_en: 'Hydrogen burns with a squeaky pop when tested with a lit (burning) splint.'
      },
      {
        id: 'PA_M08', topic: 'Reactivity & Acids', marks: 1,
        citation: 'School Review Q9 & Workbook p.61 (L6 Q6-7)',
        prompt_en: 'Which metal will NOT react with dilute hydrochloric acid, and why?',
        prompt_cn: '哪一种金属不与稀盐酸反应？原因是什么？',
        options: [
          { letter: 'A', en: 'Zinc — because it is a non-metal', cn: '锌 — 因为是非金属' },
          { letter: 'B', en: 'Copper — because it is below hydrogen in the reactivity series', cn: '铜 — 因为在金属活动性顺序中位于氢下方' },
          { letter: 'C', en: 'Magnesium — because it is too reactive', cn: '镁 — 因为太活泼' },
          { letter: 'D', en: 'Iron — because it dissolves only in alkalis', cn: '铁 — 因为只溶于碱' }
        ],
        correct: 'B',
        explain_cn: '铜位于金属活动性顺序中氢的下方，不能置换出稀酸中的氢。',
        explain_en: 'Copper is below hydrogen in the reactivity series and cannot displace H⁺.'
      },
      {
        id: 'PA_M09', topic: 'Acid Reactions', marks: 1,
        citation: 'School Review Q18 & Workbook p.61 (L6 Q9)',
        prompt_en: 'Dilute sulfuric acid reacts with copper(II) carbonate. What are the three products?',
        prompt_cn: '稀硫酸与碳酸铜反应生成哪三种产物？',
        options: [
          { letter: 'A', en: 'Copper(II) sulfate + water + carbon dioxide', cn: '硫酸铜 + 水 + 二氧化碳' },
          { letter: 'B', en: 'Copper(II) chloride + water + carbon dioxide', cn: '氯化铜 + 水 + 二氧化碳' },
          { letter: 'C', en: 'Copper(II) sulfate + hydrogen + oxygen', cn: '硫酸铜 + 氢气 + 氧气' },
          { letter: 'D', en: 'Copper(II) nitrate + water + carbon dioxide', cn: '硝酸铜 + 水 + 二氧化碳' }
        ],
        correct: 'A',
        explain_cn: '酸 + 碳酸盐 → 盐 + 水 + 二氧化碳，硫酸对应硫酸盐（sulfate）。',
        explain_en: 'CuCO₃ + H₂SO₄ → CuSO₄ + H₂O + CO₂.'
      },
      {
        id: 'PA_M10', topic: 'Ions & pH', marks: 1,
        citation: 'Workbook p.107 (L12 Q1-2)',
        prompt_en: 'Which ions are responsible for acidity in acids and alkalinity in alkalis respectively?',
        prompt_cn: '水溶液呈现酸性与碱性分别由哪两种离子决定？',
        options: [
          { letter: 'A', en: 'Acids: OH⁻ | Alkalis: H⁺', cn: '酸：OH⁻ | 碱：H⁺' },
          { letter: 'B', en: 'Acids: H⁺ | Alkalis: OH⁻', cn: '酸：H⁺ | 碱：OH⁻' },
          { letter: 'C', en: 'Acids: Cl⁻ | Alkalis: Na⁺', cn: '酸：Cl⁻ | 碱：Na⁺' },
          { letter: 'D', en: 'Acids: H₂O | Alkalis: NH₄⁺', cn: '酸：H₂O | 碱：NH₄⁺' }
        ],
        correct: 'B',
        explain_cn: '酸释放 H⁺，碱释放 OH⁻。',
        explain_en: 'All aqueous acids release H⁺ ions; all aqueous alkalis release OH⁻ ions.'
      },
      {
        id: 'PA_M11', topic: 'Ions & pH', marks: 1,
        citation: 'Workbook p.108 (L12 Q10)',
        prompt_en: 'A solution of pH 2 is how many times more acidic than a solution of pH 4?',
        prompt_cn: 'pH 为 2 的溶液比 pH 为 4 的溶液酸性强多少倍？',
        options: [
          { letter: 'A', en: '2 times', cn: '2 倍' },
          { letter: 'B', en: '20 times', cn: '20 倍' },
          { letter: 'C', en: '100 times', cn: '100 倍' },
          { letter: 'D', en: '1000 times', cn: '1000 倍' }
        ],
        correct: 'C',
        explain_cn: '相差 2 个 pH 单位 → 10² = 100 倍。',
        explain_en: 'pH is logarithmic: 4 − 2 = 2 units → 10² = 100 times higher [H⁺].'
      },
      {
        id: 'PA_M12', topic: 'Neutralisation', marks: 1,
        citation: 'Workbook p.108 (L12 Q12 & Q14)',
        prompt_en: 'Which ionic equation and energy change describe acid-alkali neutralisation?',
        prompt_cn: '哪一项正确描述了酸碱中和反应的离子方程式与热量变化？',
        options: [
          { letter: 'A', en: 'H⁺ + OH⁻ → H₂O (exothermic)', cn: 'H⁺ + OH⁻ → H₂O（放热反应）' },
          { letter: 'B', en: 'H⁺ + OH⁻ → H₂O (endothermic)', cn: 'H⁺ + OH⁻ → H₂O（吸热反应）' },
          { letter: 'C', en: 'Na⁺ + Cl⁻ → NaCl (exothermic)', cn: 'Na⁺ + Cl⁻ → NaCl（放热反应）' },
          { letter: 'D', en: 'H⁺ + Cl⁻ → HCl (endothermic)', cn: 'H⁺ + Cl⁻ → HCl（吸热反应）' }
        ],
        correct: 'A',
        explain_cn: '中和反应实质是 H⁺ + OH⁻ → H₂O，且为放热反应（温度升高）。',
        explain_en: 'Neutralisation is H⁺(aq) + OH⁻(aq) → H₂O(l) and is always exothermic.'
      },
      {
        id: 'PA_M13', topic: 'Proton Theory', marks: 1,
        citation: 'Workbook p.109 (L12 Q15-16)',
        prompt_en: 'According to the Brønsted-Lowry (BAAD) definition, an acid is a proton ______ and a base is a proton ______.',
        prompt_cn: '按质子理论（BAAD 法则），酸是质子______，碱是质子______。',
        options: [
          { letter: 'A', en: 'acceptor ; donor', cn: '受体 ; 给体' },
          { letter: 'B', en: 'donor ; acceptor', cn: '给体 ; 受体' },
          { letter: 'C', en: 'donor ; donor', cn: '给体 ; 给体' },
          { letter: 'D', en: 'acceptor ; acceptor', cn: '受体 ; 受体' }
        ],
        correct: 'B',
        explain_cn: 'BAAD：Bases Accept（碱接受质子），Acids Donate（酸给出质子）。',
        explain_en: 'BAAD: Bases Accept protons, Acids Donate protons.'
      },
      {
        id: 'PA_M14', topic: 'Salt Preparation', marks: 1,
        citation: 'Workbook p.119 (L13 Task 13.3 Q3)',
        prompt_en: 'Why is excess copper(II) oxide powder added to warm dilute sulfuric acid when making copper(II) sulfate?',
        prompt_cn: '用氧化铜和温热稀硫酸制备硫酸铜时，为何要加入过量氧化铜？',
        options: [
          { letter: 'A', en: 'To ensure all the sulfuric acid has completely reacted', cn: '确保全部稀硫酸完全反应耗尽' },
          { letter: 'B', en: 'To make the reaction endothermic', cn: '使反应变为吸热' },
          { letter: 'C', en: 'To prevent filtration', cn: '避免进行过滤' },
          { letter: 'D', en: 'To produce hydrogen gas', cn: '为了产生氢气' }
        ],
        correct: 'A',
        explain_cn: '过量难溶 CuO 确保酸 100% 耗尽，多余 CuO 可直接过滤除去。',
        explain_en: 'Adding excess insoluble CuO ensures 100% of the acid is neutralised; leftover solid is filtered off.'
      },
      {
        id: 'PA_M15', topic: 'Solubility & Salts', marks: 1,
        citation: 'Workbook p.137 (L16) & p.149 (Short Q2)',
        prompt_en: 'Which of the following salts is INSOLUBLE in water?',
        prompt_cn: '下列哪一种盐不溶于水？',
        options: [
          { letter: 'A', en: 'Sodium carbonate', cn: '碳酸钠' },
          { letter: 'B', en: 'Potassium nitrate', cn: '硝酸钾' },
          { letter: 'C', en: 'Magnesium carbonate', cn: '碳酸镁' },
          { letter: 'D', en: 'Ammonium chloride', cn: '氯化铵' }
        ],
        correct: 'C',
        explain_cn: '除 Na⁺、K⁺、NH₄⁺ 外，大多数碳酸盐难溶，故碳酸镁难溶于水。',
        explain_en: 'Most carbonates are insoluble (except Na⁺, K⁺, NH₄⁺), so MgCO₃ is insoluble.'
      }
    ],
    part2_calc: [
      {
        id: 'PA_C01', topic: 'Equations', marks: 2,
        citation: 'School Review Q19 & Workbook p.142',
        prompt_en: 'Write the balanced symbol equation (with state symbols) for dilute hydrochloric acid neutralising aqueous sodium hydroxide. [2]',
        prompt_cn: '写出稀盐酸中和氢氧化钠水溶液的配平符号方程式（含物态符号）。[2]',
        model_answer: 'HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(l)',
        mark_scheme: [
          'Correct formulae & balancing: HCl + NaOH → NaCl + H₂O [1]',
          'Correct state symbols: (aq), (aq) → (aq), (l) — water must be (l) [1]'
        ]
      },
      {
        id: 'PA_C02', topic: 'Equations', marks: 2,
        citation: 'Workbook p.142 (Revision Q1) & p.149',
        prompt_en: 'Write the balanced symbol equation for magnesium reacting with dilute sulfuric acid. [2]',
        prompt_cn: '写出镁与稀硫酸反应的配平符号方程式。[2]',
        model_answer: 'Mg + H₂SO₄ → MgSO₄ + H₂',
        mark_scheme: [
          'Correct reactants and salt formula MgSO₄ [1]',
          'Correct hydrogen molecule H₂ and balanced equation [1]'
        ]
      },
      {
        id: 'PA_C03', topic: 'Ionic Equations', marks: 2,
        citation: 'Workbook p.88 (L9 Q4) & p.111 (L12 Q3c)',
        prompt_en: 'Write the ionic equation for neutralisation and explain why the resulting solution has pH 7. [2]',
        prompt_cn: '写出中和反应的离子方程式，并从粒子层面解释为何最终溶液 pH 为 7。[2]',
        model_answer: 'H⁺(aq) + OH⁻(aq) → H₂O(l). Equal amounts of acidic H⁺ and alkaline OH⁻ combine completely to form neutral water molecules, leaving no excess H⁺ or OH⁻.',
        mark_scheme: [
          'H⁺(aq) + OH⁻(aq) → H₂O(l) [1]',
          'H⁺ and OH⁻ are used up / cancel out to form neutral water molecules [1]'
        ]
      },
      {
        id: 'PA_C04', topic: 'pH Calculations', marks: 2,
        citation: 'Workbook p.78 (Task 8.3 Q1 & Q5)',
        prompt_en: '(a) Write [H⁺] at pH 4 in standard form. [1]\n(b) How many times more acidic is pH 1 than pH 4? [1]',
        prompt_cn: '(a) 用科学计数法写出 pH 4 时的 [H⁺]。[1]\n(b) pH 1 比 pH 4 酸性强多少倍？[1]',
        model_answer: '(a) 1.0 × 10⁻⁴ mol/dm³\n(b) 10³ = 1000 times more acidic.',
        mark_scheme: [
          '1.0 × 10⁻⁴ (or 10⁻⁴) mol/dm³ [1]',
          '1000 times (10³) [1]'
        ]
      },
      {
        id: 'PA_C05', topic: 'Titration Calculations', marks: 2,
        citation: 'Workbook p.124 & PPT Slide 159',
        prompt_en: 'In a titration, three accurate titres are 22.40 cm³, 22.30 cm³, and 22.50 cm³. Calculate the mean titre to 2 decimal places. [2]',
        prompt_cn: '三次精确滴定读数为 22.40 cm³、22.30 cm³、22.50 cm³，计算平均滴定体积（保留两位小数）。[2]',
        model_answer: 'All three are within 0.20 cm³ (concordant). Mean = (22.40 + 22.30 + 22.50) / 3 = 67.20 / 3 = 22.40 cm³.',
        mark_scheme: [
          'Correct sum divided by 3: (22.40 + 22.30 + 22.50) / 3 [1]',
          'Final answer 22.40 cm³ (2 d.p. with unit) [1]'
        ]
      }
    ],
    part3_theory: [
      {
        id: 'PA_T01', topic: 'Soluble Salt Preparation (Route 1)', marks: 5,
        citation: 'Workbook pp.117-119 (Lesson 13 Tasks 13.2-13.3)',
        prompt_en: 'Describe how to prepare pure, dry blue crystals of copper(II) sulfate starting from dilute sulfuric acid and insoluble copper(II) oxide powder. [5]',
        prompt_cn: '写出以稀硫酸和不溶性氧化铜粉末为原料，制备纯净干燥蓝色硫酸铜晶体的完整 5 步实验操作。[5]',
        model_answer: '1. Warm dilute H₂SO₄ gently in a beaker (do not boil). 2. Add copper(II) oxide powder in excess while stirring until unreacted black solid remains at the bottom. 3. Filter the mixture to remove excess CuO and collect the blue CuSO₄ filtrate. 4. Heat the filtrate in an evaporating basin until the crystallisation point (half volume / crystals form at edge — do NOT evaporate to dryness). 5. Leave to cool so crystals form, filter off crystals, and pat dry gently between filter papers.',
        mark_scheme: [
          'Warm dilute sulfuric acid gently [1]',
          'Add excess copper(II) oxide until no more dissolves/reacts [1]',
          'Filter to remove unreacted excess CuO (keep blue filtrate) [1]',
          'Evaporate filtrate partially to crystallisation point (not to dryness) [1]',
          'Cool to crystallise and dry crystals gently between filter papers [1]'
        ]
      },
      {
        id: 'PA_T02', topic: 'Antacids, Acid Rain & Carbonate Test', marks: 5,
        citation: 'PPT Slide 21, 58 & Workbook p.63 (L6 Q2)',
        prompt_en: 'Calcium carbonate (CaCO₃) is used in antacid tablets to neutralise excess stomach hydrochloric acid, and is also corroded by acid rain.\n(a) Write the word equation for calcium carbonate reacting with stomach hydrochloric acid. [2]\n(b) Describe the chemical test for the gas produced and state the positive result. [2]\n(c) Name ONE pollutant gas from burning fossil fuels that causes acid rain. [1]',
        prompt_cn: '碳酸钙（CaCO₃）既可用于抗酸药中和过多胃酸（HCl），也会被酸雨腐蚀。\n(a) 写出碳酸钙与胃中稀盐酸反应的文字方程式。[2]\n(b) 描述所产气体的检验方法与阳性现象。[2]\n(c) 写出一种化石燃料燃烧引发酸雨的污染气体名称。[1]',
        model_answer: '(a) hydrochloric acid + calcium carbonate → calcium chloride + water + carbon dioxide.\n(b) Bubble the gas through limewater (aqueous calcium hydroxide) → turns cloudy / milky.\n(c) Sulfur dioxide (SO₂) or nitrogen oxides (NOₓ).',
        mark_scheme: [
          'calcium chloride [1] + water + carbon dioxide [1]',
          'Bubble gas into limewater [1] → turns cloudy/milky [1]',
          'Sulfur dioxide (SO₂) or nitrogen oxide(s) (NOₓ) [1]'
        ]
      },
      {
        id: 'PA_T03', topic: 'Bases, Alkalis & Ammonia Test', marks: 5,
        citation: 'Workbook p.64 (L6 Theory Q4) & p.150 (Short Q6)',
        prompt_en: '(a) Explain why every alkali is a base, but not every base is an alkali. Give one example of an insoluble base. [2]\n(b) Ammonium chloride is warmed with calcium hydroxide. Name the gas released, describe its test with positive result, and name the salt formed. [3]',
        prompt_cn: '(a) 解释“所有 alkali 都是 base，但并非所有 base 都是 alkali”，并举一例不溶性碱。[2]\n(b) 氯化铵与氢氧化钙共热：写出释放气体名称、检验方法与现象，以及生成的盐名称。[3]',
        model_answer: '(a) A base neutralises an acid; an alkali is a water-soluble base. Copper(II) oxide (CuO) or MgO is a base that does not dissolve in water, so it is not an alkali.\n(b) Gas: ammonia (NH₃). Test: damp red litmus paper turns blue. Salt formed: calcium chloride.',
        mark_scheme: [
          'Alkali = soluble base; base neutralises acid [1]',
          'Valid insoluble base example (e.g., CuO, MgO, Fe₂O₃) [1]',
          'Ammonia [1] + damp red litmus turns blue [1] + calcium chloride [1]'
        ]
      }
    ]
  },

  paperB: {
    id: 'paperB',
    code: 'PAPER B',
    title_cn: 'Paper B · 拔高防坑卷（强弱酸/质子理论/滴定平行读数/沉淀与水检验）',
    title_en: 'Paper B · Extended Trap-Buster Paper (45 min · 45 Marks)',
    subtitle_cn: 'Part 1 高频陷阱选择题 (15×1=15分) + Part 2 进阶方程式与定量计算 (5×3=15分) + Part 3 实验设计与拓展简答 (3×5=15分)',
    subtitle_en: 'Part 1 High-Trap MCQs (15 marks) + Part 2 Advanced Equations & Calculations (15 marks) + Part 3 Practical & Extended Theory (15 marks)',
    durationMin: 45,
    totalMarks: 45,
    part1_mcq: [
      {
        id: 'PB_M01', topic: 'Strong vs Weak Acids', marks: 1,
        citation: 'PPT Slides 124-125 & Workbook p.105',
        prompt_en: '25 cm³ of 1.0 mol/dm³ HCl and 25 cm³ of 1.0 mol/dm³ CH₃COOH each react with EXCESS magnesium ribbon. Which statement is correct?',
        prompt_cn: '25 cm³ 1.0 mol/dm³ 盐酸与 25 cm³ 1.0 mol/dm³ 乙酸分别与过量镁条反应，哪项正确？',
        options: [
          { letter: 'A', en: 'HCl reacts faster and produces twice the final volume of H₂', cn: '盐酸更快且最终产气量是乙酸两倍' },
          { letter: 'B', en: 'HCl reacts faster, but both produce the SAME final total volume of H₂', cn: '盐酸初始速率更快，但最终总产氢量完全相同' },
          { letter: 'C', en: 'Both react at the exact same initial rate', cn: '两者初始反应速率完全相同' },
          { letter: 'D', en: 'CH₃COOH produces more H₂ because it has 4 H atoms per molecule', cn: '乙酸分子含 4 个氢原子，产气更多' }
        ],
        correct: 'B',
        explain_cn: '强酸初始 [H⁺] 高→初始速率更快；但二者同体积同浓度、可置换 H⁺ 总量相等，故最终氢气总体积完全相同！',
        explain_en: 'HCl has higher initial [H⁺] (faster rate), but both have identical total moles of replaceable H⁺, yielding the same final H₂ volume.'
      },
      {
        id: 'PB_M02', topic: 'Strength vs Concentration', marks: 1,
        citation: 'Workbook p.104 (L11 Q2a) & p.112 (L12 Q5c)',
        prompt_en: 'Which statement correctly distinguishes a concentrated weak acid from a dilute strong acid?',
        prompt_cn: '哪一项正确区分了“浓弱酸”与“稀强酸”？',
        options: [
          { letter: 'A', en: 'Concentrated weak acid has many acid molecules per dm³ but only a small fraction dissociates into H⁺', cn: '浓弱酸单位体积酸分子多，但只有极小比例电离成 H⁺' },
          { letter: 'B', en: 'Dilute strong acid only partially dissociates because of extra water', cn: '稀强酸因为加水所以只能部分电离' },
          { letter: 'C', en: 'Concentrated weak acid always has pH 0', cn: '浓弱酸 pH 总是 0' },
          { letter: 'D', en: 'Strength and concentration mean the exact same thing', cn: '强弱与浓稀含义相同' }
        ],
        correct: 'A',
        explain_cn: '浓度看单位体积溶质分子数，强弱看电离比例（强酸无论多稀都完全电离，弱酸无论多浓都仅部分电离）。',
        explain_en: 'Concentration = moles per dm³; strength = extent of dissociation. A concentrated weak acid still only partially dissociates.'
      },
      {
        id: 'PB_M03', topic: 'Proton Theory', marks: 1,
        citation: 'Workbook p.96 (L10 Q6) & p.111 (L12 Q4)',
        prompt_en: 'In the reaction NH₃(aq) + H₂O(l) ⇌ NH₄⁺(aq) + OH⁻(aq), which substance acts as an acid and what term describes water’s ability to act as either acid or base?',
        prompt_cn: '在 NH₃ + H₂O ⇌ NH₄⁺ + OH⁻ 中，谁作为酸？水既能作酸又能作碱的性质称为什么？',
        options: [
          { letter: 'A', en: 'NH₃ ; neutral', cn: 'NH₃ ; 中性' },
          { letter: 'B', en: 'H₂O ; amphoteric', cn: 'H₂O ; 两性 (amphoteric)' },
          { letter: 'C', en: 'OH⁻ ; exothermic', cn: 'OH⁻ ; 放热' },
          { letter: 'D', en: 'NH₄⁺ ; anhydrous', cn: 'NH₄⁺ ; 无水' }
        ],
        correct: 'B',
        explain_cn: '水给出质子给 NH₃，因此水作酸；能兼作酸和碱的物质称为两性物质（Amphoteric）。',
        explain_en: 'H₂O donates H⁺ to NH₃ (acting as an acid). Substances that can act as both acid and base are amphoteric.'
      },
      {
        id: 'PB_M04', topic: 'Classification of Oxides & Amphoteric', marks: 1,
        citation: 'Workbook p.5, p.140 & PPT Slide 97 (Oxide Classification)',
        prompt_en: 'Which pair contains ONLY amphoteric oxides (reacting with BOTH dilute acids and aqueous alkalis)?',
        prompt_cn: '哪一组全部是两性氧化物（Amphoteric oxides，既能与稀酸又能与碱水溶液反应）？',
        options: [
          { letter: 'A', en: 'SO₂ and CO₂', cn: '二氧化硫和二氧化碳（酸性氧化物）' },
          { letter: 'B', en: 'CuO and MgO', cn: '氧化铜和氧化镁（碱性氧化物）' },
          { letter: 'C', en: 'CO and NO', cn: '一氧化碳和一氧化氮（中性氧化物）' },
          { letter: 'D', en: 'Al₂O₃ and ZnO', cn: '氧化铝和氧化锌（两性氧化物）' }
        ],
        correct: 'D',
        explain_cn: 'Al₂O₃ 与 ZnO 是 IGCSE 必考的两性氧化物；SO₂/CO₂ 为酸性氧化物，CuO/MgO 为碱性氧化物，CO/NO 为中性氧化物。',
        explain_en: 'Aluminium oxide (Al₂O₃) and zinc oxide (ZnO) are amphoteric oxides.'
      },
      {
        id: 'PB_M05', topic: 'State Symbols', marks: 1,
        citation: 'Workbook p.142 (Revision Q4)',
        prompt_en: 'Which equation has ALL state symbols written accurately for aqueous NaOH neutralising dilute HNO₃?',
        prompt_cn: '下列哪一个氢氧化钠中和稀硝酸的方程式所有物态符号全部规范正确？',
        options: [
          { letter: 'A', en: 'NaOH(aq) + HNO₃(aq) → NaNO₃(aq) + H₂O(l)', cn: 'NaOH(aq) + HNO₃(aq) → NaNO₃(aq) + H₂O(l)' },
          { letter: 'B', en: 'NaOH(aq) + HNO₃(aq) → NaNO₃(aq) + H₂O(aq)', cn: 'NaOH(aq) + HNO₃(aq) → NaNO₃(aq) + H₂O(aq)' },
          { letter: 'C', en: 'NaOH(l) + HNO₃(l) → NaNO₃(l) + H₂O(l)', cn: 'NaOH(l) + HNO₃(l) → NaNO₃(l) + H₂O(l)' },
          { letter: 'D', en: 'NaOH(aq) + HNO₃(aq) → NaNO₃(s) + H₂O(l)', cn: 'NaOH(aq) + HNO₃(aq) → NaNO₃(s) + H₂O(l)' }
        ],
        correct: 'A',
        explain_cn: '纯水永远是 (l) 而不是 (aq)，硝酸钠全溶故为 (aq)。',
        explain_en: 'Aqueous solutions are (aq), soluble NaNO₃ stays (aq), and pure water is strictly (l).'
      },
      {
        id: 'PB_M06', topic: 'pH Dilution', marks: 1,
        citation: 'Workbook p.78 (Task 8.3 Q6)',
        prompt_en: 'A strong acid of pH 2.0 is diluted with distilled water until its total volume is 1000 times larger. What is its new pH?',
        prompt_cn: '将 pH 2.0 的强酸加水稀释至总体积扩大 1000 倍，新的 pH 是多少？',
        options: [
          { letter: 'A', en: 'pH 3.0', cn: 'pH 3.0' },
          { letter: 'B', en: 'pH 5.0', cn: 'pH 5.0' },
          { letter: 'C', en: 'pH 6.0', cn: 'pH 6.0' },
          { letter: 'D', en: 'pH 9.0', cn: 'pH 9.0' }
        ],
        correct: 'B',
        explain_cn: '稀释 1000 倍 = 10³ 倍，[H⁺] 降至 1/1000，pH 上升 3 个单位：2.0 + 3.0 = 5.0。',
        explain_en: 'Dilution by 1000× (10³) increases pH by 3 units: 2.0 + 3.0 = 5.0.'
      },
      {
        id: 'PB_M07', topic: 'Titration Analysis', marks: 1,
        citation: 'PPT Slide 159 & Workbook p.124',
        prompt_en: 'Titration results (cm³): Rough = 25.10, Run 1 = 24.20, Run 2 = 24.65, Run 3 = 24.10. Which runs are CONCORDANT (within 0.20 cm³) and what is the mean?',
        prompt_cn: '滴定结果（cm³）：粗测 25.10，第 1 次 24.20，第 2 次 24.65，第 3 次 24.10。哪几组是有效平行读数？均值是多少？',
        options: [
          { letter: 'A', en: 'Runs 1, 2, 3 → 24.32 cm³', cn: '第 1、2、3 次 → 24.32 cm³' },
          { letter: 'B', en: 'Runs 1 and 3 → 24.15 cm³', cn: '第 1 与第 3 次 → 24.15 cm³' },
          { letter: 'C', en: 'Rough and Run 2 → 24.88 cm³', cn: '粗测与第 2 次 → 24.88 cm³' },
          { letter: 'D', en: 'All four runs → 24.51 cm³', cn: '全部四次 → 24.51 cm³' }
        ],
        correct: 'B',
        explain_cn: '永远排除粗测与离群值 24.65；仅 24.20 与 24.10 差 0.10 ≤ 0.20 cm³，均值 24.15 cm³。',
        explain_en: 'Only 24.20 and 24.10 are within 0.20 cm³; mean = (24.20 + 24.10) / 2 = 24.15 cm³.'
      },
      {
        id: 'PB_M08', topic: 'Titration Indicators', marks: 1,
        citation: 'Workbook p.64 (L6 Theory Q3b) & PPT Slide 158',
        prompt_en: 'Why is universal indicator NOT suitable for determining the end point of a titration?',
        prompt_cn: '为什么广范指示剂不适合用于测定酸碱滴定的终点？',
        options: [
          { letter: 'A', en: 'It changes colour gradually over many pH values instead of giving one sharp colour change', cn: '它在很宽 pH 区间连续渐变，无法提供单一敏锐的突变终点' },
          { letter: 'B', en: 'It reacts with sodium chloride to form a precipitate', cn: '它会与氯化钠生成沉淀' },
          { letter: 'C', en: 'It is colourless in all alkalis', cn: '它在所有碱中无色' },
          { letter: 'D', en: 'It only works above 100°C', cn: '它只能在 100°C 以上工作' }
        ],
        correct: 'A',
        explain_cn: '滴定需要单滴突变色（如甲基橙或百里酚酞），广范指示剂渐变色无法精确定位终点。',
        explain_en: 'Titrations require a sharp single-drop colour change at the end point.'
      },
      {
        id: 'PB_M09', topic: 'Salt Preparation Routes', marks: 1,
        citation: 'Workbook p.114 (L13) & p.120 (L14)',
        prompt_en: 'Which method MUST be used to prepare pure sodium nitrate (NaNO₃) crystals?',
        prompt_cn: '制备纯净的硝酸钠（NaNO₃）晶体必须采用哪一条制盐路线？',
        options: [
          { letter: 'A', en: 'Add excess sodium metal to dilute nitric acid', cn: '向稀硝酸中加入过量金属钠' },
          { letter: 'B', en: 'Titration of aqueous NaOH with dilute HNO₃, then repeat without indicator and crystallise', cn: '用稀硝酸滴定氢氧化钠溶液，测得体积后不加指示剂重复混合再结晶' },
          { letter: 'C', en: 'Precipitation by mixing NaCl(aq) and AgNO₃(aq) and filtering off NaNO₃ solid', cn: '沉淀法过滤出硝酸钠固体' },
          { letter: 'D', en: 'Add excess insoluble sodium oxide and filter', cn: '加过量不溶氧化钠后过滤' }
        ],
        correct: 'B',
        explain_cn: '钠盐/钾盐/铵盐的碱和碳酸盐全都可溶且金属钠遇酸爆炸，必须采用路线二（酸碱滴定法）！',
        explain_en: 'Na/K/NH₄ compounds are all soluble and Na metal reacts explosively with acid, so titration (Route 2) is mandatory.'
      },
      {
        id: 'PB_M10', topic: 'Salt Preparation Traps', marks: 1,
        citation: 'Workbook p.119 (L13 Task 13.3 Q4)',
        prompt_en: 'A student evaporates blue CuSO₄(aq) completely to dryness over a roaring Bunsen flame. What is left in the basin?',
        prompt_cn: '某同学用大火将蓝色硫酸铜溶液彻底蒸干，蒸发皿中最终剩下什么？',
        options: [
          { letter: 'A', en: 'Large hydrated blue crystals', cn: '大颗粒蓝色结晶水合物晶体' },
          { letter: 'B', en: 'White anhydrous copper(II) sulfate powder', cn: '白色无水硫酸铜粉末' },
          { letter: 'C', en: 'Black copper(II) oxide', cn: '黑色氧化铜' },
          { letter: 'D', en: 'Reddish-brown copper metal', cn: '紫红色铜单质' }
        ],
        correct: 'B',
        explain_cn: '强热蒸干会驱走 5 个结晶水，使蓝色 CuSO₄·5H₂O 变为白色无水 CuSO₄ 粉末。',
        explain_en: 'Evaporating to dryness removes water of crystallisation, leaving white anhydrous CuSO₄.'
      },
      {
        id: 'PB_M11', topic: 'Water Tests', marks: 1,
        citation: 'Workbook p.128 (L15 Practical Assessment)',
        prompt_en: 'A colourless liquid turns white anhydrous copper(II) sulfate blue, and boils over the range 101°C–104°C at 1 atm. What can you conclude?',
        prompt_cn: '某无色液体能使白色无水硫酸铜变蓝，但在 1 标准大气压下沸点范围为 101°C–104°C，可得什么结论？',
        options: [
          { letter: 'A', en: 'It is 100% pure water', cn: '它是 100% 纯水' },
          { letter: 'B', en: 'It contains water, but it is IMPURE (contains dissolved solutes)', cn: '它含有水，但不纯（含有溶解杂质）' },
          { letter: 'C', en: 'It contains no water at all', cn: '它完全不含水' },
          { letter: 'D', en: 'It is pure ethanol', cn: '它是纯乙醇' }
        ],
        correct: 'B',
        explain_cn: '无水硫酸铜变蓝证明“含水”；但纯水沸点应恒定在 100°C，沸点升高且有沸程说明含有可溶杂质（不纯）。',
        explain_en: 'White → blue proves water is present; boiling above 100°C over a range proves it is impure.'
      },
      {
        id: 'PB_M12', topic: 'Solubility Rules', marks: 1,
        citation: 'Workbook p.131 (Fig 16.2) & p.138 (Task 16.4)',
        prompt_en: 'Which pair of aqueous solutions will NOT form a precipitate when mixed?',
        prompt_cn: '下列哪一对水溶液混合后【不会】产生沉淀？',
        options: [
          { letter: 'A', en: 'Silver nitrate + Sodium chloride', cn: '硝酸银 + 氯化钠' },
          { letter: 'B', en: 'Barium chloride + Potassium sulfate', cn: '氯化钡 + 硫酸钾' },
          { letter: 'C', en: 'Lead(II) nitrate + Potassium iodide', cn: '硝酸铅 + 碘化钾' },
          { letter: 'D', en: 'Sodium chloride + Potassium nitrate', cn: '氯化钠 + 硝酸钾' }
        ],
        correct: 'D',
        explain_cn: 'NaCl + KNO₃ 交换离子后仍全为 SPAN 可溶盐（NaNO₃ 与 KCl），无沉淀；A 产 AgCl、B 产 BaSO₄、C 产 PbI₂。',
        explain_en: 'All Na⁺, K⁺, NO₃⁻, and Cl⁻ (except Ag/Pb) salts here are soluble, so no precipitate forms.'
      },
      {
        id: 'PB_M13', topic: 'Precipitation Purification', marks: 1,
        citation: 'Workbook p.130 (L16 Catching the Precipitate)',
        prompt_en: 'After filtering off a freshly formed barium sulfate precipitate, why must it be washed with distilled water?',
        prompt_cn: '沉淀法过滤得到硫酸钡滤渣后，为什么必须用蒸馏水洗涤？',
        options: [
          { letter: 'A', en: 'To dissolve the barium sulfate', cn: '溶解硫酸钡' },
          { letter: 'B', en: 'To remove soluble impurities / spectator ions adhering to the solid', cn: '洗去附着在固体表面的可溶性副产物杂质与旁观离子' },
          { letter: 'C', en: 'To turn it into a soluble salt', cn: '将其转化为可溶盐' },
          { letter: 'D', en: 'To cool down the filter paper', cn: '冷却滤纸' }
        ],
        correct: 'B',
        explain_cn: '蒸馏水不会溶解难溶的 BaSO₄，却能洗净残留的 Na⁺、Cl⁻ 等可溶性旁观离子。',
        explain_en: 'Washing with distilled water removes clinging soluble spectator ions without dissolving the insoluble precipitate.'
      },
      {
        id: 'PB_M14', topic: 'Soil Lime & Ammonium Fertiliser Trap', marks: 1,
        citation: 'PPT Slide 21, 59 & Workbook p.145 (Slaked Lime + NH₄⁺)',
        prompt_en: 'A farmer spreads slaked lime, Ca(OH)₂, to neutralise acidic soil. Why must ammonium nitrate fertiliser NOT be added at the same time?',
        prompt_cn: '农民撒施熟石灰 Ca(OH)₂ 中和酸性土壤时，为什么严禁同时施用硝酸铵（铵态氮肥）？',
        options: [
          { letter: 'A', en: 'Slaked lime turns the soil strongly acidic', cn: '熟石灰会使土壤变强酸' },
          { letter: 'B', en: 'The alkali reacts with ammonium ions to release ammonia gas (NH₃), losing nitrogen fertiliser', cn: '碱性的熟石灰与铵根反应释放氨气（NH₃）逸出，导致氮肥流失' },
          { letter: 'C', en: 'It produces explosive hydrogen gas', cn: '会产生易爆氢气' },
          { letter: 'D', en: 'Ammonium nitrate is insoluble in rainwater', cn: '硝酸铵不溶于雨水' }
        ],
        correct: 'B',
        explain_cn: '熟石灰（Ca(OH)₂）与铵盐反应放出氨气（NH₃↑），导致农作物必需的氮元素挥发流失！',
        explain_en: 'Alkaline slaked lime reacts with ammonium salts to release NH₃(g), wasting nitrogen from the fertiliser.'
      },
      {
        id: 'PB_M15', topic: 'Conductivity & Ions', marks: 1,
        citation: 'Workbook p.107 (L12 Q3-4) & p.110 (Short Q1)',
        prompt_en: 'Why does aqueous hydrochloric acid conduct electricity much better than aqueous ethanoic acid of the SAME concentration?',
        prompt_cn: '相同浓度下，为什么盐酸水溶液的导电性远强于乙酸水溶液？',
        options: [
          { letter: 'A', en: 'HCl contains free delocalised electrons', cn: '盐酸含有自由离域电子' },
          { letter: 'B', en: 'HCl dissociates completely, giving a much higher concentration of free mobile ions', cn: '盐酸完全电离，单位体积内自由移动离子浓度远高于部分电离的乙酸' },
          { letter: 'C', en: 'Ethanoic acid has zero ions in water', cn: '乙酸在水中完全没有离子' },
          { letter: 'D', en: 'HCl has a higher pH value', cn: '盐酸的 pH 值更高' }
        ],
        correct: 'B',
        explain_cn: '水溶液导电靠自由移动离子（非自由电子）；完全电离的强酸离子浓度远高于部分电离的弱酸。',
        explain_en: 'Complete dissociation of HCl yields far more free mobile ions per dm³ to carry electrical current.'
      }
    ],
    part2_calc: [
      {
        id: 'PB_C01', topic: 'Precipitation Equations', marks: 3,
        citation: 'Workbook p.137 (L16 Task 16.3 Part C)',
        prompt_en: 'Write the balanced symbol equation WITH state symbols for mixing aqueous lead(II) nitrate and aqueous potassium iodide to form yellow lead(II) iodide precipitate. [3]',
        prompt_cn: '写出硝酸铅水溶液与碘化钾水溶液混合生成黄色碘化铅沉淀的配平符号方程式（含全部物态符号）。[3]',
        model_answer: 'Pb(NO₃)₂(aq) + 2KI(aq) → PbI₂(s) + 2KNO₃(aq)',
        mark_scheme: [
          'Correct formulae Pb(NO₃)₂, KI, PbI₂, KNO₃ [1]',
          'Balanced coefficients (2KI and 2KNO₃) [1]',
          'All state symbols correct: (aq) + (aq) → (s) + (aq) [1]'
        ]
      },
      {
        id: 'PB_C02', topic: 'Concordant Titre Calculation', marks: 3,
        citation: 'Workbook p.124 & PPT Slide 159',
        prompt_en: 'A student records four burette volumes (cm³): Rough = 24.80, Run 1 = 23.60, Run 2 = 24.10, Run 3 = 23.50.\n(a) State which values are concordant (within 0.20 cm³) and explain why Rough and Run 2 are excluded. [2]\n(b) Calculate the mean concordant titre. [1]',
        prompt_cn: '四次滴定读数（cm³）：粗测 24.80、第 1 次 23.60、第 2 次 24.10、第 3 次 23.50。\n(a) 指出哪几次是有效平行读数，并说明为何剔除粗测与第 2 次。[2]\n(b) 计算平均有效滴定体积。[1]',
        model_answer: '(a) Run 1 (23.60 cm³) and Run 3 (23.50 cm³) are concordant (difference = 0.10 cm³ ≤ 0.20 cm³). Rough is always an overshoot estimate; Run 2 (24.10) differs by >0.20 cm³ (anomalous outlier).\n(b) Mean = (23.60 + 23.50) / 2 = 23.55 cm³.',
        mark_scheme: [
          'Identifies Run 1 (23.60) and Run 3 (23.50) [1]',
          'Excludes Rough (estimate) and Run 2 (not within 0.20 cm³ / outlier) [1]',
          'Mean = 23.55 cm³ [1]'
        ]
      },
      {
        id: 'PB_C03', topic: 'pH Logarithmic Dilution', marks: 3,
        citation: 'Workbook p.78 (Task 8.3 Q4, Q6, Q7)',
        prompt_en: '(a) A neutral solution at pH 7 has [H⁺] = 1.0 × 10⁻⁷ mol/dm³. State [H⁺] at pH 5 in standard form. [1]\n(b) A strong acid has pH 3.0. It is diluted so its total volume becomes 100 times larger. Calculate its new pH and explain your reasoning. [2]',
        prompt_cn: '(a) 中性 pH 7 时 [H⁺] = 1.0×10⁻⁷，用科学计数法写出 pH 5 时的 [H⁺]。[1]\n(b) pH 3.0 的强酸稀释至体积扩大 100 倍，计算新 pH 并说明理由。[2]',
        model_answer: '(a) 1.0 × 10⁻⁵ mol/dm³.\n(b) New pH = 5.0. Increasing volume by 100× (10²) lowers [H⁺] by 100×, which increases pH by 2 units (3.0 + 2.0 = 5.0).',
        mark_scheme: [
          '1.0 × 10⁻⁵ mol/dm³ [1]',
          'New pH = 5.0 [1]',
          '100× dilution = 10² lower [H⁺] → pH rises by 2 units [1]'
        ]
      },
      {
        id: 'PB_C04', topic: 'Ammonium Salt Equation', marks: 3,
        citation: 'Workbook p.150 (Revision Short Q6)',
        prompt_en: 'Write the balanced symbol equation for warming ammonium chloride with calcium hydroxide to produce calcium chloride, water, and ammonia gas. [3]',
        prompt_cn: '写出氯化铵与氢氧化钙共热生成氯化钙、水和氨气的配平符号方程式。[3]',
        model_answer: '2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2H₂O + 2NH₃',
        mark_scheme: [
          'Correct reactant formulae NH₄Cl and Ca(OH)₂ [1]',
          'Correct product formulae CaCl₂, H₂O, NH₃ [1]',
          'Correct balancing: 2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2H₂O + 2NH₃ [1]'
        ]
      },
      {
        id: 'PB_C05', topic: 'Proton Transfer Identification', marks: 3,
        citation: 'Workbook p.96-97 (L10 Q6-9) & p.147 (Revision Q22)',
        prompt_en: 'In Reaction 1: CH₃COOH + H₂O ⇌ CH₃COO⁻ + H₃O⁺. In Reaction 2: NH₃ + H₂O ⇌ NH₄⁺ + OH⁻.\nIdentify the role of water (proton donor / acid OR proton acceptor / base) in EACH reaction and explain why water is called amphoteric. [3]',
        prompt_cn: '在反应 1（CH₃COOH + H₂O）和反应 2（NH₃ + H₂O）中，分别指出水的角色（质子给体/酸 或 质子受体/碱），并解释为何水称为两性物质。[3]',
        model_answer: 'Reaction 1: H₂O accepts H⁺ to form H₃O⁺ → base (proton acceptor).\nReaction 2: H₂O donates H⁺ to NH₃ (becoming OH⁻) → acid (proton donor).\nBecause water can act as both an acid and a base depending on its partner, it is amphoteric.',
        mark_scheme: [
          'Reaction 1: water is proton acceptor / base [1]',
          'Reaction 2: water is proton donor / acid [1]',
          'Amphoteric = substance that can act as both acid and base [1]'
        ]
      }
    ],
    part3_theory: [
      {
        id: 'PB_T01', topic: 'Titration Salt Prep (Route 2)', marks: 5,
        citation: 'Workbook pp.120-127 & PPT Slides 154-159',
        prompt_en: 'Describe step by step how to prepare pure, dry sodium chloride crystals from aqueous sodium hydroxide and dilute hydrochloric acid using titration. [5]',
        prompt_cn: '分步骤描述如何用滴定法由氢氧化钠溶液与稀盐酸制备纯净干燥的氯化钠晶体。[5]',
        model_answer: '1. Use a pipette to transfer 25.0 cm³ of NaOH(aq) into a conical flask and add 2–3 drops of methyl orange (or thymolphthalein). 2. Fill a burette with dilute HCl and add slowly (drop by drop near end point) while swirling until the sharp indicator colour change occurs; record exact titre volume. 3. Repeat using the EXACT same 25.0 cm³ NaOH and recorded HCl volume WITHOUT any indicator so the salt is not contaminated. 4. Evaporate the pure NaCl(aq) partially to crystallisation point. 5. Cool to crystallise and dry between filter papers.',
        mark_scheme: [
          'Pipette 25.0 cm³ NaOH into conical flask + add few drops of suitable indicator [1]',
          'Add HCl from burette drop by drop near end point until sharp colour change & record volume [1]',
          'Repeat with exact same volumes WITHOUT indicator [1]',
          'Evaporate filtrate partially to crystallisation point [1]',
          'Cool to form crystals and dry between filter papers [1]'
        ]
      },
      {
        id: 'PB_T02', topic: 'Precipitation Salt Prep (Route 3)', marks: 5,
        citation: 'Workbook pp.130 & 136-138 (Lesson 16)',
        prompt_en: 'Describe how to prepare a pure, dry sample of insoluble barium sulfate (BaSO₄) starting from two suitable soluble salts. Include the names of both reagents, the balanced equation, and the purification steps. [5]',
        prompt_cn: '设计实验由两种合适可溶盐制备纯净干燥的难溶硫酸钡（BaSO₄）。写出两种试剂名称、配平方程式及提纯干燥步骤。[5]',
        model_answer: 'Reagents: aqueous barium chloride (or barium nitrate) and aqueous sodium sulfate (or potassium sulfate). Equation: BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq). Steps: 1. Mix the two aqueous solutions in a beaker so white BaSO₄ precipitates. 2. Filter the mixture to collect BaSO₄ residue on filter paper. 3. Wash the residue thoroughly with distilled water to remove soluble spectator ions (Na⁺, Cl⁻). 4. Dry the pure solid in a warm oven or between filter papers.',
        mark_scheme: [
          'Two valid soluble reagents (e.g., barium chloride/nitrate + sodium/potassium sulfate) [1]',
          'Balanced equation with state symbols: BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq) [1]',
          'Mix solutions and filter to collect solid BaSO₄ residue [1]',
          'Wash precipitate with distilled water to remove soluble impurities [1]',
          'Dry solid in warm oven / between filter papers [1]'
        ]
      },
      {
        id: 'PB_T03', topic: 'Water Test & Strong/Weak Acid Analysis', marks: 5,
        citation: 'Workbook p.112 (L12 Q5) & p.128 (L15)',
        prompt_en: '(a) A student has a sample of colourless liquid. State the chemical test to prove it CONTAINS water AND the physical test to prove it is PURE water. [3]\n(b) Equal concentrations of HCl (pH 1) and CH₃COOH (pH 3) are compared. Explain in terms of dissociation and [H⁺] why their pH differs, yet equal volumes need the SAME volume of NaOH to neutralise. [2]',
        prompt_cn: '(a) 写出证明某无色液体“含有水”的化学检验方法，以及证明其为“纯水”的物理检验方法。[3]\n(b) 同浓度 HCl（pH 1）与 CH₃COOH（pH 3）为何 pH 不同，但等体积时中和所需的 NaOH 体积却完全相同？[2]',
        model_answer: '(a) Presence of water: add to white anhydrous copper(II) sulfate → turns blue (or blue anhydrous cobalt(II) chloride → turns pink). Purity: measure boiling point at 1 atm → boils sharply at exactly 100°C (or melts sharply at 0°C).\n(b) HCl dissociates completely giving higher [H⁺] and lower pH, whereas CH₃COOH dissociates partially. However, both have the exact same total number of moles of replaceable H⁺ (both are monoprotic at equal concentration and volume), so both require the exact same volume of NaOH to neutralise completely.',
        mark_scheme: [
          'Anhydrous CuSO₄ turns white → blue (or CoCl₂ blue → pink) [2]',
          'Pure water boils sharply at 100°C (or melts at 0°C) [1]',
          'HCl completely dissociates (higher [H⁺], lower pH) vs CH₃COOH partially dissociates [1]',
          'Equal total moles of replaceable H⁺ → same volume of NaOH needed [1]'
        ]
      }
    ]
  }
};
