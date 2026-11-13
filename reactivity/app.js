// ============================================================================
// 金属活动性顺序表全套 24 元素科学数据库 (严格按照原图由上至下顺序)
// ============================================================================
const ELEMENTS_DATA = [
  // ================= 1. Reacts with water (与水反应 - 6种) =================
  {
    rank: 1,
    en: "Potassium",
    cn: "钾",
    symbol: "K",
    atomicNum: 19,
    potential: "-2.93 V",
    zone: "water",
    zoneLabel: "Reacts with water · 与水反应",
    metalColor: "#e2e8f0",
    ionColor: "rgba(244, 114, 182, 0.38)", // 酚酞变红
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 10, // 0~10 气泡与反应剧烈度
    acidRate: 10,
    flameColor: "#c084fc", // 浅紫色火焰 (透过蓝色钴玻璃)
    floatsInWater: true,
    meltsIntoBall: true,
    summary: "表中最活泼的金属！投入冷水中立即熔化成银白色闪亮小球，浮在水面四处疾速游动，发出嘶嘶声并直接点燃生成的氢气，产生淡紫色火焰。",
    waterEq: "2K + 2H₂O → 2KOH + H₂↑（剧烈燃烧，淡紫色火焰）",
    acidEq: "2K + 2HCl → 2KCl + H₂↑（极度剧烈，严禁直接实验以防爆炸）",
    extraction: "电解熔融氯化钾或金属钠置换法冶炼",
    tip: "实验室保存在煤油中以隔绝空气和水蒸气；与盐溶液反应先与水反应。"
  },
  {
    rank: 2,
    en: "Sodium",
    cn: "钠",
    symbol: "Na",
    atomicNum: 11,
    potential: "-2.71 V",
    zone: "water",
    zoneLabel: "Reacts with water · 与水反应",
    metalColor: "#f1f5f9",
    ionColor: "rgba(244, 114, 182, 0.35)",
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 9.2,
    acidRate: 10,
    flameColor: "#facc15", // 黄色火焰
    floatsInWater: true,
    meltsIntoBall: true,
    summary: "与冷水剧烈反应，经典现象概括为“浮、熔、游、响、红”：密度小于水而浮于水面，放热熔成银白小球，氢气推动小球游动，酚酞试液变红。",
    waterEq: "2Na + 2H₂O → 2NaOH + H₂↑（浮、熔、游、响、酚酞变红）",
    acidEq: "2Na + 2HCl → 2NaCl + H₂↑（比水更剧烈，瞬间燃烧爆炸）",
    extraction: "工业采用电解熔融 NaCl（唐氏电解池）冶炼",
    tip: "投入 CuSO₄ 溶液中不会析出红色铜，而是生成 H₂↑ 和蓝色 Cu(OH)₂↓ 沉淀！"
  },
  {
    rank: 3,
    en: "Lithium",
    cn: "锂",
    symbol: "Li",
    atomicNum: 3,
    potential: "-3.04 V",
    zone: "water",
    zoneLabel: "Reacts with water · 与水反应",
    metalColor: "#cbd5e1",
    ionColor: "rgba(244, 114, 182, 0.30)",
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 6.8,
    acidRate: 9.0,
    flameColor: null,
    floatsInWater: true,
    meltsIntoBall: false,
    summary: "密度最小的固体单质（0.534 g/cm³）。投入冷水中浮于水面平稳产生大量氢气气泡，因熔点较高（180.5℃）且反应放热相对温和，不会熔成小球或自燃。",
    waterEq: "2Li + 2H₂O → 2LiOH + H₂↑（浮于水面平稳冒泡，不熔化）",
    acidEq: "2Li + 2HCl → 2LiCl + H₂↑（剧烈冒泡放热）",
    extraction: "电解熔融 LiCl-KCl 混合盐冶炼",
    tip: "因密度极小，不能保存在煤油中（会浮起），通常封存在液体石蜡中。"
  },
  {
    rank: 4,
    en: "Barium",
    cn: "钡",
    symbol: "Ba",
    atomicNum: 56,
    potential: "-2.91 V",
    zone: "water",
    zoneLabel: "Reacts with water · 与水反应",
    metalColor: "#94a3b8",
    ionColor: "rgba(244, 114, 182, 0.34)",
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 7.8,
    acidRate: 9.2,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "高活性碱土金属，密度大于水，投入冷水中迅速沉底并剧烈产生大量氢气气泡，生成的氢氧化钡 Ba(OH)₂ 易溶于水形成强碱性溶液。",
    waterEq: "Ba + 2H₂O → Ba(OH)₂ + H₂↑（沉入水底，剧烈冒泡）",
    acidEq: "Ba + 2HCl → BaCl₂ + H₂↑（剧烈反应，若遇稀硫酸会生成 BaSO₄ 白色沉淀）",
    extraction: "电解熔融氯化钡或铝热真空还原氧化钡",
    tip: "可溶性钡盐有剧毒，但硫酸钡 BaSO₄ 难溶于水和酸，可作医疗“钡餐”。"
  },
  {
    rank: 5,
    en: "Strontium",
    cn: "锶",
    symbol: "Sr",
    atomicNum: 38,
    potential: "-2.89 V",
    zone: "water",
    zoneLabel: "Reacts with water · 与水反应",
    metalColor: "#cbd5e1",
    ionColor: "rgba(244, 114, 182, 0.30)",
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 6.5,
    acidRate: 8.8,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "碱土金属，活动性介于钡和钙之间。沉入冷水底部，持续、快速地放出氢气气泡，生成氢氧化锶使酚酞变红。",
    waterEq: "Sr + 2H₂O → Sr(OH)₂ + H₂↑（沉底快速产生气泡）",
    acidEq: "Sr + 2HCl → SrCl₂ + H₂↑（迅速溶解并产生大量氢气）",
    extraction: "电解熔融氯化锶或铝热还原法",
    tip: "锶化合物焰色反应呈绚丽的洋红色，常用于制造节日烟花和信号弹。"
  },
  {
    rank: 6,
    en: "Calcium",
    cn: "钙",
    symbol: "Ca",
    atomicNum: 20,
    potential: "-2.87 V",
    zone: "water",
    zoneLabel: "Reacts with water · 与水反应",
    metalColor: "#d1d5db",
    ionColor: "rgba(251, 207, 232, 0.45)", // 微溶浑浊+酚酞粉红
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 5.5,
    acidRate: 8.5,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "粉红区（与冷水反应）的最后一个金属。钙粒沉入水底，平稳快速地产生大量气泡，生成的微溶物 Ca(OH)₂ 使溶液变白浑浊，滴加酚酞呈粉红色。",
    waterEq: "Ca + 2H₂O → Ca(OH)₂ + H₂↑（沉底冒泡，生成微溶白色浑浊）",
    acidEq: "Ca + 2HCl → CaCl₂ + H₂↑（剧烈放热，迅速涌出大量气泡）",
    extraction: "工业采用电解熔融氯化钙 CaCl₂ 制取",
    tip: "与钠不同，钙与冷水反应温和可控，实验室有时可用钙与水反应收集纯氢气。"
  },

  // ================= 2. Reacts with acids (与酸反应 - 10种) =================
  {
    rank: 7,
    en: "Magnesium",
    cn: "镁",
    symbol: "Mg",
    atomicNum: 12,
    potential: "-2.37 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#e2e8f0",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.08)",
    waterRate: 0.2, // 冷水极微弱，几乎看不到
    acidRate: 8.0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "黄色区（与酸反应）排第一！在冷水中几乎无明显现象（仅在沸水或水蒸气中明显反应），但投入稀盐酸中会剧烈冒泡、快速溶解并明显放热。",
    waterEq: "与冷水几乎不反应（加热沸水：Mg + 2H₂O(l) △→ Mg(OH)₂ + H₂↑）",
    acidEq: "Mg + 2HCl → MgCl₂ + H₂↑（剧烈冒泡，试管外壁发烫）",
    extraction: "电解熔融氯化镁 MgCl₂（从海水中提取镁）",
    tip: "课堂对比实验常选 Mg、Zn、Fe、Cu 四种金属投入稀盐酸，Mg 产生气泡最快！"
  },
  {
    rank: 8,
    en: "Aluminium",
    cn: "铝",
    symbol: "Al",
    atomicNum: 13,
    potential: "-1.66 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#cbd5e1",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.08)",
    waterRate: 0,
    acidRate: 7.0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "地壳中含量最高的金属元素。表面天然覆盖一层致密的氧化铝 (Al₂O₃) 保护膜，不与冷水反应；投入稀盐酸中待氧化膜溶解后，会产生大量气泡。",
    waterEq: "与冷水不反应（致密 Al₂O₃ 氧化膜保护）",
    acidEq: "2Al + 6HCl → 2AlCl₃ + 3H₂↑（由慢变快，剧烈放热）",
    extraction: "霍尔-埃鲁法：电解熔融氧化铝 Al₂O₃（冰晶石作助熔剂）",
    tip: "铝具有两性，不仅能与酸反应放出 H₂，还能与强碱 NaOH 溶液反应放出 H₂！"
  },
  {
    rank: 9,
    en: "Manganese",
    cn: "锰",
    symbol: "Mn",
    atomicNum: 25,
    potential: "-1.18 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#9ca3af",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(251, 207, 232, 0.22)", // Mn2+ 极浅肉粉色
    waterRate: 0,
    acidRate: 5.8,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "较活泼的过渡金属，排在铝与锌之间。不与冷水反应，易溶于稀盐酸或稀硫酸，置换出氢气并生成极浅肉粉色的二价锰离子 (Mn²⁺)。",
    waterEq: "与冷水不反应",
    acidEq: "Mn + 2HCl → MnCl₂ + H₂↑（持续产生气泡，溶液呈极浅粉色）",
    extraction: "工业常用铝热还原法或电解硫酸锰溶液制取",
    tip: "锰钢硬度极高且耐磨，广泛用于制造铁路道岔、桥梁和挖掘机铲齿。"
  },
  {
    rank: 10,
    en: "Zinc",
    cn: "锌",
    symbol: "Zn",
    atomicNum: 30,
    potential: "-0.76 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#cbd5e1",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.06)",
    waterRate: 0,
    acidRate: 5.0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "中等活动性金属的代表！不与冷水反应，与稀盐酸或稀硫酸反应速率适中、平稳可控，因此是中学化学实验室制取氢气 (H₂) 的首选金属。",
    waterEq: "与冷水不反应（高温下与水蒸气反应生成 ZnO 和 H₂）",
    acidEq: "Zn + 2HCl → ZnCl₂ + H₂↑（反应速率适中，实验室制 H₂ 标准反应）",
    extraction: "热还原法（碳还原氧化锌）或湿法电解硫酸锌",
    tip: "在钢铁表面镀锌（白铁皮），即使镀层破损，更活泼的锌也会优先腐蚀从而保护铁。"
  },
  {
    rank: 11,
    en: "Chromium",
    cn: "铬",
    symbol: "Cr",
    atomicNum: 24,
    potential: "-0.74 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#e2e8f0",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(56, 189, 248, 0.28)", // Cr2+ 亮蓝色，接触空气变绿 Cr3+
    waterRate: 0,
    acidRate: 4.2,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "硬度最高的银白色金属之一，是不锈钢抗腐蚀的核心成分。隔绝空气时与稀盐酸反应生成天蓝色 Cr²⁺（接触空气后迅速被氧化为绿色 Cr³⁺）。",
    waterEq: "与冷水不反应（表面极易形成致密钝化膜）",
    acidEq: "Cr + 2HCl → CrCl₂ + H₂↑（持续冒泡，溶液呈蓝色后转绿）",
    extraction: "铝热还原法（2Al + Cr₂O₃ 高温→ 2Cr + Al₂O₃）",
    tip: "常温下铬在浓硝酸或浓硫酸中会发生“钝化”，表面生成极薄的致密氧化膜阻止继续反应。"
  },
  {
    rank: 12,
    en: "Iron",
    cn: "铁",
    symbol: "Fe",
    atomicNum: 26,
    potential: "-0.44 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#94a3b8",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(74, 222, 128, 0.28)", // Fe2+ 特征浅绿色
    waterRate: 0,
    acidRate: 3.2,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "人类使用最广泛的金属。不与冷水反应，与稀盐酸、稀硫酸缓慢平稳冒泡，溶液逐渐由无色变为特征性的浅绿色（二价亚铁离子 Fe²⁺）。",
    waterEq: "与冷水不反应（高温红热铁与水蒸气：3Fe + 4H₂O(g) → Fe₃O₄ + 4H₂）",
    acidEq: "Fe + 2HCl → FeCl₂ + H₂↑（缓慢产生气泡，溶液变为浅绿色）",
    extraction: "高炉炼铁：一氧化碳高温还原赤铁矿（Fe₂O₃ + 3CO → 2Fe + 3CO₂）",
    tip: "必考重点：铁与稀盐酸/稀硫酸或 CuSO₄ 发生置换反应时，永远只生成 +2 价的亚铁盐 (Fe²⁺)！"
  },
  {
    rank: 13,
    en: "Cadmium",
    cn: "镉",
    symbol: "Cd",
    atomicNum: 48,
    potential: "-0.40 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#cbd5e1",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 0,
    acidRate: 2.6,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "活动性略弱于铁的银白色金属。不与冷水反应，能与稀盐酸缓慢反应置换出氢气。",
    waterEq: "与水不反应",
    acidEq: "Cd + 2HCl → CdCl₂ + H₂↑（缓慢冒泡）",
    extraction: "炼锌工业副产物，通过锌粉置换或电解精炼提取",
    tip: "常用于镍镉充电电池和核反应堆控制棒（强中子吸收能力），但重金属镉离子有毒。"
  },
  {
    rank: 14,
    en: "Cobalt",
    cn: "钴",
    symbol: "Co",
    atomicNum: 27,
    potential: "-0.28 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#94a3b8",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(244, 63, 94, 0.26)", // Co2+ 水合离子粉红色
    waterRate: 0,
    acidRate: 2.0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "具有铁磁性的银灰色硬金属。不与水反应，在稀盐酸中缓慢溶解并释放细小氢气泡，水合钴离子 [Co(H₂O)₆]²⁺ 使溶液呈美丽的粉红色。",
    waterEq: "与水不反应",
    acidEq: "Co + 2HCl → CoCl₂ + H₂↑（缓慢产生细密气泡，溶液呈粉红色）",
    extraction: "热还原法或湿法冶金电解提取",
    tip: "氯化钴试纸在无水时呈蓝色，吸水后变为粉红色，实验室常用来检验水分的存在。"
  },
  {
    rank: 15,
    en: "Nickel",
    cn: "镍",
    symbol: "Ni",
    atomicNum: 28,
    potential: "-0.25 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#cbd5e1",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(16, 185, 129, 0.28)", // Ni2+ 翠绿色
    waterRate: 0,
    acidRate: 1.7,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "光泽明亮、耐腐蚀的铁磁性金属。不与水反应，与稀盐酸反应非常缓慢，产生少量细小气泡，溶液逐渐显现二价镍离子 (Ni²⁺) 的翠绿色。",
    waterEq: "与水不反应",
    acidEq: "Ni + 2HCl → NiCl₂ + H₂↑（反应缓慢，溶液渐呈翠绿色）",
    extraction: "火法冶炼结合电解精炼或蒙德法（四羰基镍热分解）",
    tip: "广泛用于制造不锈钢、硬币、电镀防护层以及有机加氢反应的催化剂。"
  },
  {
    rank: 16,
    en: "Tin",
    cn: "锡",
    symbol: "Sn",
    atomicNum: 50,
    potential: "-0.14 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#e2e8f0",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.05)",
    waterRate: 0,
    acidRate: 1.2,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "低熔点（231.9℃）、质软有延展性的金属。排在氢前靠近分界线的位置，与稀盐酸在常温下仅表面缓慢产生微弱气泡（加热后明显加快）。",
    waterEq: "与水不反应",
    acidEq: "Sn + 2HCl → SnCl₂ + H₂↑（常温极缓慢，表面附着微小氢气泡）",
    extraction: "用碳在高温下还原锡石（SnO₂ + C → Sn + CO₂↑）",
    tip: "马口铁是镀锡铁皮，无毒耐弱酸，用于食品罐头；但一旦镀层破损，铁比锡活泼，铁会加速生锈！"
  },
  {
    rank: 17,
    en: "Lead",
    cn: "铅",
    symbol: "Pb",
    atomicNum: 82,
    potential: "-0.13 V",
    zone: "acid",
    zoneLabel: "Reacts with acids · 与酸反应",
    metalColor: "#64748b",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.08)",
    waterRate: 0,
    acidRate: 0.7,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "黄色区（氢前金属）的最后一名！虽然排在 H 之前能与酸发生反应，但生成的 PbCl₂ 或 PbSO₄ 微溶/难溶于水，覆盖在铅表面阻止反应继续进行。",
    waterEq: "与水不反应",
    acidEq: "Pb + 2HCl → PbCl₂↓ + H₂↑（表面产生极少量气泡后即被难溶盐覆盖停止）",
    extraction: "火法冶炼：方铅矿 (PbS) 焙烧成氧化物再用一氧化碳还原",
    tip: "铅密度大（11.34 g/cm³），常用于制造铅酸蓄电池极板和医院 X 射线防辐射服。"
  },

  // ================= 3. Hydrogen (氢基准 - 1种) =================
  {
    rank: 18,
    en: "Hydrogen",
    cn: "氢 (比较基准)",
    symbol: "H",
    atomicNum: 1,
    potential: "0.00 V",
    zone: "hydrogen",
    zoneLabel: "Included for comparison · 比较基准",
    metalColor: "#93c5fd",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: true,
    meltsIntoBall: false,
    summary: "唯一的非金属参照系！电化学上将标准氢电极 (2H⁺ + 2e⁻ ⇌ H₂) 的电势定义为 0.00 V。它是判断金属能否与酸发生置换反应放出 H₂ 的分界线。",
    waterEq: "H₂ 难溶于水，不与水发生化学反应",
    acidEq: "H₂ 与稀盐酸中 H⁺ 同属氢元素，不发生置换反应",
    extraction: "实验室用 Zn + 稀 H₂SO₄ 制取；工业用电解水或天然气水蒸气重整制取",
    tip: "记住黄金法则：【氢前金属】能置换酸中氢生成 H₂↑；【氢后金属】不能置换酸中氢！"
  },

  // ================= 4. Highly unreactive (极不活泼 - 7种) =================
  {
    rank: 19,
    en: "Antimony",
    cn: "锑",
    symbol: "Sb",
    atomicNum: 51,
    potential: "+0.20 V",
    zone: "unreactive",
    zoneLabel: "Highly unreactive · 极不活泼",
    metalColor: "#94a3b8",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "紧随氢之后的类金属/不活泼金属。标准电极电势为正值，不能从水或稀盐酸、稀硫酸中置换出氢气。",
    waterEq: "不与水反应 (No reaction)",
    acidEq: "与稀盐酸/稀硫酸不反应（不产生 H₂）",
    extraction: "辉锑矿 (Sb₂S₃) 焙烧氧化后用碳还原，或用铁屑直接置换还原",
    tip: "锑具有罕见的“热缩冷胀”特性，古代常加入铅锡合金中制造字迹清晰的活字印刷铅字。"
  },
  {
    rank: 20,
    en: "Bismuth",
    cn: "铋",
    symbol: "Bi",
    atomicNum: 83,
    potential: "+0.31 V",
    zone: "unreactive",
    zoneLabel: "Highly unreactive · 极不活泼",
    metalColor: "#d8b4fe",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "带有微粉红/彩虹氧化膜光泽的重金属。排在氢之后，不与水或非氧化性稀酸反应。",
    waterEq: "不与水反应 (No reaction)",
    acidEq: "与稀盐酸/稀硫酸不反应（仅溶于浓硝酸等强氧化性酸）",
    extraction: "碳还原氧化铋 (Bi₂O₃) 冶炼",
    tip: "铋晶体表面会形成厚度不均的氧化膜，因薄膜干涉呈现出绚丽的彩虹阶梯状外观；伍德合金含铋熔点仅 70℃。"
  },
  {
    rank: 21,
    en: "Copper",
    cn: "铜",
    symbol: "Cu",
    atomicNum: 29,
    potential: "+0.34 V",
    zone: "unreactive",
    zoneLabel: "Highly unreactive · 极不活泼",
    metalColor: "#d97706", // 紫红色金属光泽
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "紫红色金属，中学化学检验“氢后不活泼金属”的标杆！投入水或稀盐酸中完全无气泡；但能把排在它后面的银 (Ag⁺) 和汞 (Hg²⁺) 从盐溶液中置换出来。",
    waterEq: "不与水反应 (No reaction)",
    acidEq: "Cu + HCl → 不反应（排在 H 之后，无气泡产生）",
    extraction: "火法炼铜或湿法炼铜（Fe + CuSO₄ → FeSO₄ + Cu）",
    tip: "铜虽然不溶于稀盐酸，但能溶于浓硝酸或稀硝酸（生成 NO₂/NO 气体和蓝色 Cu(NO₃)₂，非置换反应）。"
  },
  {
    rank: 22,
    en: "Mercury",
    cn: "汞 (水银)",
    symbol: "Hg",
    atomicNum: 80,
    potential: "+0.85 V",
    zone: "unreactive",
    zoneLabel: "Highly unreactive · 极不活泼",
    metalColor: "#cbd5e1",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: true, // 常温液态银白液滴
    summary: "常温下唯一呈液态的金属（俗称水银，熔点 -38.8℃）。排在铜之后、银之前，不与水和稀酸反应。",
    waterEq: "不与水反应 (No reaction)",
    acidEq: "与稀盐酸/稀硫酸不反应",
    extraction: "热分解法：直接加热辰砂/氧化汞（2HgO △→ 2Hg + O₂↑，拉瓦锡经典实验）",
    tip: "汞蒸气有剧毒！实验室内若水银温度计打破，需立即撒上硫粉使其转化为难挥发的硫化汞 (HgS)。"
  },
  {
    rank: 23,
    en: "Silver",
    cn: "银",
    symbol: "Ag",
    atomicNum: 47,
    potential: "+0.80 V",
    zone: "unreactive",
    zoneLabel: "Highly unreactive · 极不活泼",
    metalColor: "#f8fafc",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "导电性和导热性最好的银白色贵金属。化学性质十分稳定，不与水、氧气（常温）及稀酸反应，可被铜片从硝酸银溶液中置换出来形成美丽的“银树”。",
    waterEq: "不与水反应 (No reaction)",
    acidEq: "Ag + HCl → 不反应",
    extraction: "热分解法（2Ag₂O △→ 4Ag + O₂↑）或氰化法湿法提银",
    tip: "原图遵循经典欧洲教材电势序列将 Hg 列于 Ag 之上，二者电势极为接近（约 +0.80V ~ +0.85V），均属贵金属。"
  },
  {
    rank: 24,
    en: "Gold",
    cn: "金",
    symbol: "Au",
    atomicNum: 79,
    potential: "+1.50 V",
    zone: "unreactive",
    zoneLabel: "Highly unreactive · 极不活泼",
    metalColor: "#facc15", // 金黄色
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "延展性极佳的金黄色贵金属，“真金不怕火炼”即指金在高温下也不与氧气反应，更不与水、稀盐酸或浓硝酸单独反应。",
    waterEq: "不与水反应 (No reaction)",
    acidEq: "与稀盐酸、稀硫酸、浓硝酸均不反应（仅溶于王水）",
    extraction: "自然界以游离态单质（沙金/狗头金）存在，通过物理淘洗或氰化法富集",
    tip: "有时奸商用铜锌合金（黄铜，含 Cu、Zn）冒充黄金，只需滴加稀盐酸，冒气泡的即为假黄金（Zn 与酸反应）！"
  },
  {
    rank: 25,
    en: "Platinum",
    cn: "铂 (白金)",
    symbol: "Pt",
    atomicNum: 78,
    potential: "+1.18 V ~ +1.50 V",
    zone: "unreactive",
    zoneLabel: "Highly unreactive · 极不活泼",
    metalColor: "#e2e8f0",
    ionColor: "rgba(255, 255, 255, 0.02)",
    acidIonColor: "rgba(255, 255, 255, 0.02)",
    waterRate: 0,
    acidRate: 0,
    flameColor: null,
    floatsInWater: false,
    meltsIntoBall: false,
    summary: "位于整张活动性顺序表最底端的极度惰性贵金属！抗腐蚀能力极强，在空气、水、强酸中均保持稳定，是电化学惰性电极与汽车尾气三元催化剂的核心材料。",
    waterEq: "不与水反应 (No reaction)",
    acidEq: "与单一酸均不反应（仅缓慢溶于热王水生成 H₂PtCl₆）",
    extraction: "自然界游离态伴生矿富集精炼",
    tip: "实验室进行焰色反应实验时，常用铂丝蘸取待测液灼烧，正是因为铂本身不反应且无焰色干扰。"
  }
];

// 修正序号显示为 1~24（共24行：6水 + 11酸? 让我们核对原图行数！）
// 原图行数核对：
// Water (6): Potassium, Sodium, Lithium, Barium, Strontium, Calcium
// Acids (11): Magnesium, Aluminium, Manganese, Zinc, Chromium, Iron, Cadmium, Cobalt, Nickel, Tin, Lead
// Hydrogen (1): Hydrogen
// Unreactive (7): Antimony, Bismuth, Copper, Mercury, Silver, Gold, Platinum
// 总计 6 + 11 + 1 + 7 = 25 行！自动按数组下标赋值 1~25
ELEMENTS_DATA.forEach((item, idx) => {
  item.rank = idx + 1;
});

// ============================================================================
// 状态管理
// ============================================================================
let selectedElement = ELEMENTS_DATA[0]; // 默认选中 Potassium (K)
let currentZoneFilter = "all";
let showBilingual = true;

// 实验一 (水/酸反应) 动画状态
const lab1State = {
  running: false,
  metal: ELEMENTS_DATA[0],
  medium: "compare", // 'water' | 'acid' | 'compare'
  elapsed: 0,
  bubblesLeft: [],
  bubblesRight: [],
  sparks: [],
  sampleXLeft: 0.5,
  sampleVLeft: 0.004
};

// 实验二 (置换反应) 动画状态
const dispState = {
  running: false,
  stripMetal: ELEMENTS_DATA.find(e => e.symbol === "Fe"),
  solutionKey: "Cu",
  progress: 0, // 0 ~ 1
  bubbles: []
};

const SOLUTIONS_MAP = {
  Cu: {
    formula: "CuSO₄",
    name: "硫酸铜溶液",
    metalSym: "Cu",
    ionSymbol: "Cu²⁺",
    valence: 2,
    initColor: [14, 165, 233, 0.52], // 天蓝色
    depositColor: "#b45309", // 紫红色铜析出
    depositName: "紫红色海绵状金属铜 (Cu)"
  },
  Ag: {
    formula: "AgNO₃",
    name: "硝酸银溶液",
    metalSym: "Ag",
    ionSymbol: "Ag⁺",
    valence: 1,
    initColor: [226, 232, 240, 0.12], // 无色
    depositColor: "#f8fafc", // 银白色银树结晶
    depositName: "银白色闪亮银结晶 (Ag)"
  },
  Fe: {
    formula: "FeSO₄",
    name: "硫酸亚铁溶液",
    metalSym: "Fe",
    ionSymbol: "Fe²⁺",
    valence: 2,
    initColor: [74, 222, 128, 0.34], // 浅绿色
    depositColor: "#64748b", // 铁灰色
    depositName: "灰黑色金属铁 (Fe)"
  },
  Zn: {
    formula: "ZnSO₄",
    name: "硫酸锌溶液",
    metalSym: "Zn",
    ionSymbol: "Zn²⁺",
    valence: 2,
    initColor: [226, 232, 240, 0.12],
    depositColor: "#cbd5e1",
    depositName: "银灰色金属锌 (Zn)"
  },
  Mg: {
    formula: "MgSO₄",
    name: "硫酸镁溶液",
    metalSym: "Mg",
    ionSymbol: "Mg²⁺",
    valence: 2,
    initColor: [226, 232, 240, 0.12],
    depositColor: "#e2e8f0",
    depositName: "银白色金属镁 (Mg)"
  },
  Pb: {
    formula: "Pb(NO₃)₂",
    name: "硝酸铅溶液",
    metalSym: "Pb",
    ionSymbol: "Pb²⁺",
    valence: 2,
    initColor: [226, 232, 240, 0.12],
    depositColor: "#475569",
    depositName: "暗灰色铅树结晶 (Pb)"
  },
  H: {
    formula: "HCl",
    name: "稀盐酸溶液",
    metalSym: "H",
    ionSymbol: "H⁺",
    valence: 1,
    initColor: [226, 232, 240, 0.10],
    depositColor: null,
    depositName: "无固体析出（产生无色氢气气泡 H₂↑）"
  }
};

// ============================================================================
// 随堂测验题库 (覆盖原图全部核心知识点)
// ============================================================================
const QUIZ_QUESTIONS = [
  {
    q: "1. 根据图中金属活动性顺序表，下列哪种金属投入冷水中就能剧烈反应并产生氢气？",
    options: [
      "A. 镁 (Magnesium, Mg)",
      "B. 钙 (Calcium, Ca)",
      "C. 锌 (Zinc, Zn)",
      "D. 铜 (Copper, Cu)"
    ],
    answer: 1,
    explanation: "解析：图中粉红色区域（Reacts with water）包含 K、Na、Li、Ba、Sr、Ca 共 6 种金属，它们都能与冷水直接剧烈或明显反应放出 H₂；而 Mg 属于黄色区域（Reacts with acids），与冷水几乎不反应。"
  },
  {
    q: "2. 为什么非金属元素“氢 (Hydrogen)”会被单独列在金属活动性顺序表的灰色区域中？",
    options: [
      "A. 因为固态氢具有金属光泽",
      "B. 作为判断金属能否与冷水反应的基准",
      "C. 作为比较基准（Included for comparison），判断金属能否从酸中置换出氢气",
      "D. 因为氢气可以还原所有金属氧化物"
    ],
    answer: 2,
    explanation: "解析：图中明确标注 Hydrogen 为 'Included for comparison'。排在氢前面的金属（K ~ Pb）能与非氧化性酸（稀盐酸、稀硫酸）发生置换反应放出 H₂↑；排在氢后面的金属（Sb ~ Pt）则不能。"
  },
  {
    q: "3. 把一块洁净的铁片 (Iron) 浸入天蓝色的硫酸铜 (CuSO₄) 溶液中，会观察到什么现象？",
    options: [
      "A. 铁片表面析出紫红色铜，溶液逐渐变为黄色 (Fe³⁺)",
      "B. 铁片表面析出紫红色铜，溶液逐渐变为浅绿色 (Fe²⁺)",
      "C. 铁片表面产生大量气泡，溶液颜色不变",
      "D. 不发生任何反应，因为铁排在铜后面"
    ],
    answer: 1,
    explanation: "解析：图中 Iron (Fe) 位于黄色区，Copper (Cu) 位于蓝色极不活泼区，铁比铜活泼。铁与硫酸铜发生置换反应：Fe + CuSO₄ → FeSO₄ + Cu，生成紫红色铜单质和浅绿色的二价亚铁离子 (Fe²⁺)。"
  },
  {
    q: "4. 某同学将一小块金属钠 (Sodium) 投入硫酸铜 (CuSO₄) 溶液中，实验现象是：",
    options: [
      "A. 钠表面析出一层紫红色的金属铜",
      "B. 钠沉入水底，没有任何现象",
      "C. 钠浮在液面熔成小球四处游动，放出氢气并产生蓝色絮状沉淀 Cu(OH)₂",
      "D. 只产生氢气，溶液依然保持澄清天蓝色"
    ],
    answer: 2,
    explanation: "解析：极易错考点！粉红区的 6 种金属（K, Na, Li, Ba, Sr, Ca）非常活泼，投入盐溶液中时，会优先与水剧烈反应生成碱和氢气（2Na + 2H₂O → 2NaOH + H₂↑），生成的 NaOH 再与 CuSO₄ 反应生成蓝色 Cu(OH)₂ 沉淀，不会置换出铜单质！"
  },
  {
    q: "5. 有 X、Y、Z 三种金属：X 能与冷水剧烈反应；Y 不与稀盐酸反应；Z 能与稀盐酸反应放出氢气但不能与冷水反应。它们在表中从上到下（活动性由强到弱）的顺序是：",
    options: [
      "A. X > Z > Y",
      "B. Z > X > Y",
      "C. Y > Z > X",
      "D. X > Y > Z"
    ],
    answer: 0,
    explanation: "解析：X 在粉红区（与水反应，如 Na/Ca），Z 在黄色区（与酸反应，如 Zn/Fe），Y 在蓝色区（氢后不活泼金属，如 Cu/Ag）。图中箭头朝上活动性递增，因此从上到下顺序为 X > Z > Y。"
  },
  {
    q: "6. 不法商贩常使用铜锌合金（黄铜，外观金黄）冒充纯金 (Gold)。利用本表知识，下列哪种简便方法可立即鉴别真假黄金？",
    options: [
      "A. 放入冷水中观察是否熔化成小球",
      "B. 滴加稀盐酸，表面有气泡产生的是假黄金",
      "C. 观察金属的颜色是否呈金黄色",
      "D. 放入氯化钠溶液中观察是否溶解"
    ],
    answer: 1,
    explanation: "解析：真金 (Au) 位于蓝色区最底部，与酸完全不反应；而假黄金中的锌 (Zn) 位于黄色区（排在氢前），滴加稀盐酸会发生 Zn + 2HCl → ZnCl₂ + H₂↑，立即冒出气泡。"
  }
];

let quizIndex = 0;
let quizScore = 0;
const quizAnswered = new Array(QUIZ_QUESTIONS.length).fill(null);

// ============================================================================
// 初始化与 DOM 渲染
// ============================================================================
document.addEventListener("DOMContentLoaded", () => {
  updateFilterPillsCounts();
  renderMetalsTable();
  populateLabSelects();
  selectElementBySymbol("K");
  initTabs();
  initFilterButtons();
  initLab1Events();
  initDisplacementEvents();
  initQuiz();
  requestAnimationFrame(animateAllCanvases);
});

function updateFilterPillsCounts() {
  const pills = document.querySelectorAll("#zoneFilterGroup .pill");
  pills[0].textContent = `全部元素 (${ELEMENTS_DATA.length})`;
  pills[1].textContent = `🔴 与水反应 (6)`;
  pills[2].textContent = `🟡 与酸反应 (11)`;
  pills[3].textContent = `⚪ 氢基准 (1)`;
  pills[4].textContent = `🔵 极不活泼 (7)`;

  // 同步更新右侧黄色区块文字计数
  const acidCountEl = document.querySelector(".zone-acid .zone-elements-count");
  if (acidCountEl) {
    acidCountEl.textContent = "Mg, Al, Mn, Zn, Cr, Fe, Cd, Co, Ni, Sn, Pb (共11种)";
  }
  const acidZoneBlock = document.querySelector(".zone-acid");
  if (acidZoneBlock) {
    acidZoneBlock.style.flex = "11";
  }
}

function renderMetalsTable() {
  const container = document.getElementById("metalsListContainer");
  container.innerHTML = "";

  ELEMENTS_DATA.forEach(item => {
    const row = document.createElement("div");
    row.className = `metal-row zone-${item.zone}-row`;
    row.dataset.symbol = item.symbol;
    if (item.symbol === selectedElement.symbol) {
      row.classList.add("selected");
    }
    if (currentZoneFilter !== "all" && item.zone !== currentZoneFilter) {
      row.classList.add("dimmed");
    }

    const displayName = showBilingual ? `${item.en} · ${item.cn.split(" ")[0]}` : item.en;

    row.innerHTML = `
      <span class="metal-rank">#${item.rank}</span>
      <span class="metal-name-wrap">${displayName}</span>
      <span class="metal-sym-badge">${item.symbol}</span>
    `;

    row.addEventListener("click", () => {
      selectElementBySymbol(item.symbol);
    });

    container.appendChild(row);
  });
}

function selectElementBySymbol(sym) {
  const found = ELEMENTS_DATA.find(e => e.symbol === sym);
  if (!found) return;
  selectedElement = found;

  // 高亮表格行
  document.querySelectorAll(".metal-row").forEach(r => {
    r.classList.toggle("selected", r.dataset.symbol === sym);
  });

  // 更新右侧顶部详情卡片
  const symBox = document.getElementById("inspSymbolBox");
  const badge = document.getElementById("inspZoneBadge");

  const zoneColors = {
    water: "linear-gradient(135deg, #ff2e63, #e11d48)",
    acid: "linear-gradient(135deg, #f59e0b, #d97706)",
    hydrogen: "linear-gradient(135deg, #64748b, #475569)",
    unreactive: "linear-gradient(135deg, #06b6d4, #0284c7)"
  };
  const badgeColors = {
    water: { bg: "#ff2e63", color: "#ffffff" },
    acid: { bg: "#ffea28", color: "#111827" },
    hydrogen: { bg: "#cbd5e1", color: "#1e293b" },
    unreactive: { bg: "#5ce1e6", color: "#0f172a" }
  };

  symBox.style.background = zoneColors[found.zone];
  badge.style.background = badgeColors[found.zone].bg;
  badge.style.color = badgeColors[found.zone].color;

  document.getElementById("inspAtomicNum").textContent = found.atomicNum;
  document.getElementById("inspSymbol").textContent = found.symbol;
  document.getElementById("inspPotential").textContent = `E° = ${found.potential}`;
  document.getElementById("inspName").textContent = `${found.en} · ${found.cn} (第 ${found.rank} 位)`;
  badge.textContent = found.zoneLabel;
  document.getElementById("inspSummary").textContent = found.summary;
  document.getElementById("inspWaterEq").textContent = found.waterEq;
  document.getElementById("inspAcidEq").textContent = found.acidEq;
  document.getElementById("inspExtraction").textContent = found.extraction;
  document.getElementById("inspTip").textContent = found.tip;

  // 同步到实验一和实验二下拉框并自动触发演示
  const lab1Sel = document.getElementById("lab1MetalSelect");
  if (lab1Sel) {
    lab1Sel.value = found.symbol;
    startLab1Simulation(found.symbol);
  }
  const dispSel = document.getElementById("dispStripSelect");
  if (dispSel && found.symbol !== "H") {
    dispSel.value = found.symbol;
    updateDisplacementPreview();
  }
}

function populateLabSelects() {
  const lab1Sel = document.getElementById("lab1MetalSelect");
  const dispSel = document.getElementById("dispStripSelect");
  lab1Sel.innerHTML = "";
  dispSel.innerHTML = "";

  ELEMENTS_DATA.forEach(item => {
    const opt1 = document.createElement("option");
    opt1.value = item.symbol;
    opt1.textContent = `#${item.rank} ${item.en} (${item.cn} ${item.symbol}) — [${item.zoneLabel.split("·")[1].trim()}]`;
    lab1Sel.appendChild(opt1);

    if (item.symbol !== "H") {
      const opt2 = document.createElement("option");
      opt2.value = item.symbol;
      opt2.textContent = `#${item.rank} ${item.en} (${item.cn} ${item.symbol})`;
      dispSel.appendChild(opt2);
    }
  });

  dispSel.value = "Fe";
}

// ============================================================================
// 顶部筛选与中英双语切换
// ============================================================================
function initFilterButtons() {
  document.querySelectorAll("#zoneFilterGroup .pill").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("#zoneFilterGroup .pill").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentZoneFilter = btn.dataset.zone;
      renderMetalsTable();
    });
  });

  // 点击原图右侧四大色块也可筛选并高亮对应区域代表元素
  document.querySelectorAll(".zone-block").forEach(block => {
    block.addEventListener("click", () => {
      const z = block.dataset.zoneSelect;
      currentZoneFilter = currentZoneFilter === z ? "all" : z;
      document.querySelectorAll("#zoneFilterGroup .pill").forEach(b => {
        b.classList.toggle("active", b.dataset.zone === currentZoneFilter);
      });
      renderMetalsTable();
      const firstInZone = ELEMENTS_DATA.find(e => e.zone === z);
      if (firstInZone) selectElementBySymbol(firstInZone.symbol);
    });
  });

  document.getElementById("langToggleBtn").addEventListener("click", () => {
    showBilingual = !showBilingual;
    document.getElementById("langToggleBtn").textContent = showBilingual ? "中 / EN 双语" : "仅英文 (Original EN)";
    renderMetalsTable();
  });

  document.getElementById("loadToWaterAcidBtn").addEventListener("click", () => {
    switchTab("tab-water-acid");
    startLab1Simulation(selectedElement.symbol);
  });

  document.getElementById("loadToDisplaceBtn").addEventListener("click", () => {
    switchTab("tab-displacement");
    if (selectedElement.symbol !== "H") {
      document.getElementById("dispStripSelect").value = selectedElement.symbol;
    }
    startDisplacementSimulation();
  });
}

function initTabs() {
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      switchTab(btn.dataset.tab);
    });
  });
}

function switchTab(tabId) {
  document.querySelectorAll(".tab-btn").forEach(b => {
    b.classList.toggle("active", b.dataset.tab === tabId);
  });
  document.querySelectorAll(".tab-content").forEach(c => {
    c.classList.toggle("active", c.id === tabId);
  });
}

// ============================================================================
// 实验一：与水 / 与酸反应对比实验室
// ============================================================================
function initLab1Events() {
  const metalSel = document.getElementById("lab1MetalSelect");
  const mediumSel = document.getElementById("lab1MediumSelect");

  metalSel.addEventListener("change", () => {
    selectElementBySymbol(metalSel.value);
  });

  mediumSel.addEventListener("change", () => {
    lab1State.medium = mediumSel.value;
    startLab1Simulation(metalSel.value);
  });

  document.getElementById("lab1StartBtn").addEventListener("click", () => {
    startLab1Simulation(metalSel.value);
  });

  document.getElementById("lab1ResetBtn").addEventListener("click", () => {
    lab1State.running = false;
    lab1State.elapsed = 0;
    lab1State.bubblesLeft = [];
    lab1State.bubblesRight = [];
    lab1State.sparks = [];
    document.getElementById("lab1StateBadge").textContent = "已重置：点击“投入样品开始实验”观察反应";
    document.getElementById("teleTemp").textContent = "25.0 °C";
    document.getElementById("teleTempBar").style.width = "15%";
    document.getElementById("teleGasRate").textContent = "0.0 mL/s";
    document.getElementById("teleGasBar").style.width = "0%";
  });
}

function startLab1Simulation(symbol) {
  const el = ELEMENTS_DATA.find(e => e.symbol === symbol) || ELEMENTS_DATA[0];
  lab1State.metal = el;
  lab1State.medium = document.getElementById("lab1MediumSelect").value;
  lab1State.running = true;
  lab1State.elapsed = 0;
  lab1State.bubblesLeft = [];
  lab1State.bubblesRight = [];
  lab1State.sparks = [];
  lab1State.sampleXLeft = 0.5;

  updateLab1Telemetry();
}

function updateLab1Telemetry() {
  const el = lab1State.metal;
  const medium = lab1State.medium;

  const activeRate = medium === "water" ? el.waterRate : el.acidRate;
  const temp = (25 + activeRate * 7.2).toFixed(1);
  const gasFlow = (activeRate * 4.5).toFixed(1);

  document.getElementById("teleTemp").textContent = `${temp} °C`;
  document.getElementById("teleTempBar").style.width = `${Math.min(100, 15 + activeRate * 8.5)}%`;

  document.getElementById("teleGasRate").textContent = `${gasFlow} mL/s`;
  document.getElementById("teleGasBar").style.width = `${Math.min(100, activeRate * 10)}%`;

  const badge = document.getElementById("lab1StateBadge");
  const colorDesc = document.getElementById("teleColorDesc");
  const eqBox = document.getElementById("teleEquation");
  const phenomBox = document.getElementById("telePhenomenon");

  if (medium === "water") {
    badge.textContent = `实验进行中：${el.en} (${el.symbol}) 投入冷水（含酚酞）`;
    eqBox.textContent = el.waterEq;
    if (el.zone === "water") {
      colorDesc.textContent = "酚酞由无色变为深粉红色 (生成强碱 OH⁻，pH > 12)";
      phenomBox.textContent = el.summary;
    } else {
      colorDesc.textContent = "无色透明 (pH = 7.0，不生成碱)";
      phenomBox.textContent = `${el.cn} (${el.symbol}) 排在钙 (Ca) 之后，不能与冷水发生明显置换反应，烧杯中无气泡产生。`;
    }
  } else if (medium === "acid") {
    badge.textContent = `实验进行中：${el.en} (${el.symbol}) 投入稀盐酸 (HCl)`;
    eqBox.textContent = el.acidEq;
    if (el.symbol === "Fe") {
      colorDesc.textContent = "溶液逐渐变为浅绿色 (生成二价亚铁离子 Fe²⁺)";
    } else if (el.symbol === "Co") {
      colorDesc.textContent = "溶液逐渐变为粉红色 (生成 Co²⁺)";
    } else if (el.symbol === "Ni") {
      colorDesc.textContent = "溶液逐渐变为翠绿色 (生成 Ni²⁺)";
    } else if (el.symbol === "Cr") {
      colorDesc.textContent = "溶液变为天蓝色 Cr²⁺（接触空气转绿 Cr³⁺）";
    } else {
      colorDesc.textContent = "无色透明溶液";
    }
    phenomBox.textContent = el.summary;
  } else {
    // 双烧杯对比模式
    badge.textContent = `双烧杯同屏对比：${el.en} (${el.symbol}) 【左：冷水+酚酞 | 右：稀盐酸 HCl】`;
    eqBox.textContent = `水：${el.waterEq}  |  酸：${el.acidEq}`;
    if (el.zone === "water") {
      colorDesc.textContent = "左杯酚酞变红 (OH⁻) + 剧烈冒泡；右杯在酸中极度剧烈冒泡！";
    } else if (el.zone === "acid") {
      colorDesc.textContent = "左杯冷水中无明显反应；右杯稀盐酸中产生氢气气泡 (H₂↑)！";
    } else if (el.zone === "hydrogen") {
      colorDesc.textContent = "氢 (H) 为比较基准元素，两杯均无置换反应。";
    } else {
      colorDesc.textContent = "排在氢 (H) 之后，左杯冷水与右杯稀盐酸中均不产生氢气！";
    }
    phenomBox.textContent = el.summary;
  }
}

// ============================================================================
// 实验二：金属置换反应 (湿法冶金)
// ============================================================================
function initDisplacementEvents() {
  const stripSel = document.getElementById("dispStripSelect");
  const solSel = document.getElementById("dispSolutionSelect");

  stripSel.addEventListener("change", () => {
    selectElementBySymbol(stripSel.value);
    startDisplacementSimulation();
  });

  solSel.addEventListener("change", () => {
    startDisplacementSimulation();
  });

  document.getElementById("dispStartBtn").addEventListener("click", () => {
    startDisplacementSimulation();
  });

  document.getElementById("dispResetBtn").addEventListener("click", () => {
    dispState.running = false;
    dispState.progress = 0;
    dispState.bubbles = [];
    updateDisplacementPreview();
  });

  // 经典预设按钮
  document.querySelectorAll(".chip-btn").forEach(chip => {
    chip.addEventListener("click", () => {
      const s = chip.dataset.strip;
      const sol = chip.dataset.sol;
      stripSel.value = s;
      solSel.value = sol;
      selectElementBySymbol(s);
      startDisplacementSimulation();
    });
  });

  updateDisplacementPreview();
}

function startDisplacementSimulation() {
  const stripSym = document.getElementById("dispStripSelect").value;
  const solKey = document.getElementById("dispSolutionSelect").value;
  dispState.stripMetal = ELEMENTS_DATA.find(e => e.symbol === stripSym) || ELEMENTS_DATA[11];
  dispState.solutionKey = solKey;
  dispState.running = true;
  dispState.progress = 0.02;
  dispState.bubbles = [];
  updateDisplacementPreview();
}

function updateDisplacementPreview() {
  const stripSym = document.getElementById("dispStripSelect").value;
  const solKey = document.getElementById("dispSolutionSelect").value;
  const m1 = ELEMENTS_DATA.find(e => e.symbol === stripSym) || ELEMENTS_DATA[11];
  const sol = SOLUTIONS_MAP[solKey];
  const m2 = ELEMENTS_DATA.find(e => e.symbol === sol.metalSym);

  dispState.stripMetal = m1;
  dispState.solutionKey = solKey;

  document.getElementById("dispRankCompare").textContent =
    `${m1.symbol} (第 ${m1.rank} 位) vs ${m2.symbol} (第 ${m2.rank} 位)`;

  const verdictEl = document.getElementById("dispVerdict");
  const eqEl = document.getElementById("dispEquation");
  const phenomEl = document.getElementById("dispPhenomenon");

  if (m1.symbol === m2.symbol) {
    verdictEl.textContent = "⚪ 同种金属元素，不发生置换";
    verdictEl.style.color = "#94a3b8";
    eqEl.textContent = `${m1.symbol} + ${sol.formula} → 不发生置换反应`;
    phenomEl.textContent = "金属单质与溶液中金属阳离子属于同种元素，动态平衡无宏观变化。";
  } else if (m1.zone === "water") {
    // K, Na, Li, Ba, Sr, Ca 投入水溶液特例！
    verdictEl.textContent = "⚠️ 极活泼金属：先与水剧烈反应（不置换出金属单质！）";
    verdictEl.style.color = "#facc15";
    eqEl.textContent = `2${m1.symbol} + 2H₂O → 2${m1.symbol}OH + H₂↑（生成的 OH⁻ 再与 ${sol.ionSymbol} 反应）`;
    phenomEl.textContent = `${m1.cn} (${m1.symbol}) 属于粉红区（与水反应），投入 ${sol.name} 中会立即与水剧烈反应放出氢气 H₂↑，不会析出 ${m2.cn} 单质！`;
  } else if (m1.rank < m2.rank) {
    // 强换弱成功
    verdictEl.textContent = `✅ 反应发生！${m1.symbol} 排在 ${m2.symbol} 之前（强换弱）`;
    verdictEl.style.color = "#4ade80";
    if (solKey === "H") {
      eqEl.textContent = m1.acidEq;
      phenomEl.textContent = `${m1.cn}排在氢 (H) 之前，从稀盐酸中置换出无色氢气气泡 H₂↑。`;
    } else {
      eqEl.textContent = `${m1.symbol} + ${sol.ionSymbol} → ${m1.symbol}²⁺ + ${m2.symbol}↓`;
      phenomEl.textContent = `${m1.cn}片表面逐渐析出${sol.depositName}；同时 ${m1.cn} 失去电子进入溶液。`;
    }
  } else {
    // 弱不能换强
    verdictEl.textContent = `❌ 不反应！${m1.symbol} 排在 ${m2.symbol} 之后（弱不能换强）`;
    verdictEl.style.color = "#f87171";
    eqEl.textContent = `${m1.symbol} + ${sol.formula} → No Reaction (不反应)`;
    phenomEl.textContent = `因为 ${m1.cn} (#${m1.rank}) 的活动性比 ${m2.cn} (#${m2.rank}) 弱，无法从溶液中夺取电子，金属片表面洁净无变化。`;
  }
}

// ============================================================================
// Canvas 实时渲染引擎 (实验一 & 实验二)
// ============================================================================
function animateAllCanvases() {
  renderLab1Canvas();
  renderDisplacementCanvas();
  requestAnimationFrame(animateAllCanvases);
}

function renderLab1Canvas() {
  const canvas = document.getElementById("beakerCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const W = canvas.width;
  const H = canvas.height;

  ctx.clearRect(0, 0, W, H);

  // 绘制实验台背景底座
  const bgGrad = ctx.createLinearGradient(0, 0, 0, H);
  bgGrad.addColorStop(0, "#0b1325");
  bgGrad.addColorStop(1, "#162238");
  ctx.fillStyle = bgGrad;
  ctx.fillRect(0, 0, W, H);

  // 实验台桌面
  ctx.fillStyle = "#1e293b";
  ctx.fillRect(0, H - 34, W, 34);
  ctx.strokeStyle = "#334155";
  ctx.beginPath();
  ctx.moveTo(0, H - 34);
  ctx.lineTo(W, H - 34);
  ctx.stroke();

  if (lab1State.running) {
    lab1State.elapsed += 0.016;
  }

  const el = lab1State.metal;
  const mode = lab1State.medium;

  if (mode === "compare") {
    // 左烧杯：冷水 + 酚酞；右烧杯：稀盐酸 HCl
    drawSingleBeaker(ctx, {
      cx: W * 0.27,
      bottomY: H - 36,
      bw: 210,
      bh: 235,
      title: "💧 冷水 + 酚酞 (Cold Water)",
      rate: el.waterRate,
      liquidColor: lab1State.running && el.zone === "water"
        ? `rgba(244, 63, 94, ${Math.min(0.45, 0.08 + lab1State.elapsed * 0.08)})`
        : "rgba(56, 189, 248, 0.14)",
      bubblesArr: lab1State.bubblesLeft,
      element: el,
      isWater: true
    });

    drawSingleBeaker(ctx, {
      cx: W * 0.73,
      bottomY: H - 36,
      bw: 210,
      bh: 235,
      title: "🧪 稀盐酸 (Dilute HCl)",
      rate: el.acidRate,
      liquidColor: lab1State.running ? getAcidLiquidColor(el, lab1State.elapsed) : "rgba(226, 232, 240, 0.13)",
      bubblesArr: lab1State.bubblesRight,
      element: el,
      isWater: false
    });
  } else {
    const isWater = mode === "water";
    const rate = isWater ? el.waterRate : el.acidRate;
    const liqCol = isWater
      ? (lab1State.running && el.zone === "water"
          ? `rgba(244, 63, 94, ${Math.min(0.45, 0.08 + lab1State.elapsed * 0.08)})`
          : "rgba(56, 189, 248, 0.14)")
      : (lab1State.running ? getAcidLiquidColor(el, lab1State.elapsed) : "rgba(226, 232, 240, 0.13)");

    drawSingleBeaker(ctx, {
      cx: W * 0.5,
      bottomY: H - 36,
      bw: 280,
      bh: 240,
      title: isWater ? "💧 冷水 + 酚酞指示剂 (Cold Water)" : "🧪 稀盐酸溶液 (Dilute HCl)",
      rate,
      liquidColor: liqCol,
      bubblesArr: lab1State.bubblesLeft,
      element: el,
      isWater
    });
  }
}

function getAcidLiquidColor(el, elapsed) {
  const alpha = Math.min(0.42, 0.12 + elapsed * 0.05);
  if (el.symbol === "Fe") return `rgba(74, 222, 128, ${alpha})`; // Fe2+ 浅绿
  if (el.symbol === "Co") return `rgba(244, 114, 182, ${alpha})`; // Co2+ 粉红
  if (el.symbol === "Ni") return `rgba(16, 185, 129, ${alpha})`; // Ni2+ 翠绿
  if (el.symbol === "Cr") return `rgba(56, 189, 248, ${alpha})`; // Cr2+ 蓝色
  if (el.symbol === "Mn") return `rgba(251, 207, 232, ${alpha * 0.7})`;
  return "rgba(226, 232, 240, 0.15)";
}

function drawSingleBeaker(ctx, cfg) {
  const { cx, bottomY, bw, bh, title, rate, liquidColor, bubblesArr, element, isWater } = cfg;
  const leftX = cx - bw / 2;
  const rightX = cx + bw / 2;
  const topY = bottomY - bh;
  const liquidTopY = bottomY - bh * 0.72;

  // 标题标签
  ctx.fillStyle = "#e2e8f0";
  ctx.font = "bold 13px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(title, cx, topY - 12);

  // 溶液填充
  ctx.fillStyle = liquidColor;
  ctx.beginPath();
  ctx.roundRect(leftX + 3, liquidTopY, bw - 6, bottomY - liquidTopY - 3, [0, 0, 12, 12]);
  ctx.fill();

  // 若是钙与水反应，绘制微溶 Ca(OH)2 白色浑浊颗粒
  if (lab1State.running && isWater && element.symbol === "Ca") {
    ctx.fillStyle = "rgba(255, 255, 255, 0.22)";
    ctx.fillRect(leftX + 6, liquidTopY + 20, bw - 12, bottomY - liquidTopY - 24);
  }

  // 绘制金属样品位置
  if (lab1State.running) {
    let sampleX = cx;
    let sampleY = bottomY - 18;

    if (element.floatsInWater) {
      sampleY = liquidTopY + 4;
      if (rate > 6) {
        sampleX = cx + Math.sin(lab1State.elapsed * (rate * 0.8)) * (bw * 0.3);
      }
    }

    // 繪制金属块或熔融小球
    ctx.save();
    ctx.fillStyle = element.metalColor;
    ctx.strokeStyle = "#0f172a";
    ctx.lineWidth = 1.5;

    if (element.meltsIntoBall) {
      ctx.beginPath();
      ctx.arc(sampleX, sampleY, 11, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    } else if (element.symbol === "H") {
      // 氢基准绘制虚线气体标识
      ctx.strokeStyle = "#38bdf8";
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.arc(sampleX, liquidTopY + 50, 16, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);
    } else {
      ctx.beginPath();
      ctx.roundRect(sampleX - 18, sampleY - 10, 36, 18, 4);
      ctx.fill();
      ctx.stroke();
    }

    // 金属元素符号标记
    ctx.fillStyle = element.symbol === "Au" || element.symbol === "Na" || element.symbol === "K" ? "#0f172a" : "#0f172a";
    ctx.font = "bold 11px monospace";
    ctx.textAlign = "center";
    ctx.fillText(element.symbol, sampleX, sampleY + 4);
    ctx.restore();

    // 火焰特效 (K 紫焰 / Na 黄焰，或酸中极剧烈反应)
    if ((isWater && element.flameColor) || (!isWater && element.zone === "water")) {
      const fCol = element.flameColor || "#f97316";
      for (let i = 0; i < 3; i++) {
        const flameH = 18 + Math.random() * 18;
        const grad = ctx.createRadialGradient(sampleX, sampleY - 8, 2, sampleX, sampleY - 12, flameH);
        grad.addColorStop(0, "#ffffff");
        grad.addColorStop(0.4, fCol);
        grad.addColorStop(1, "rgba(255, 255, 255, 0)");
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(sampleX + (Math.random() - 0.5) * 10, sampleY - 10, flameH, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // 气泡生成与运动 (H2 气体)
    if (rate > 0) {
      const spawnProb = rate / 10;
      const count = Math.ceil(rate / 3);
      for (let i = 0; i < count; i++) {
        if (Math.random() < spawnProb) {
          bubblesArr.push({
            x: sampleX + (Math.random() - 0.5) * 32,
            y: sampleY - 4,
            r: 2 + Math.random() * 3.5,
            vy: 1.0 + (rate * 0.25) + Math.random() * 1.2,
            vx: (Math.random() - 0.5) * 0.8
          });
        }
      }
    }

    // 更新并绘制气泡
    ctx.fillStyle = "rgba(255, 255, 255, 0.78)";
    ctx.strokeStyle = "rgba(148, 163, 184, 0.9)";
    ctx.lineWidth = 1;
    for (let i = bubblesArr.length - 1; i >= 0; i--) {
      const b = bubblesArr[i];
      b.y -= b.vy;
      b.x += b.vx;
      if (b.y <= liquidTopY) {
        bubblesArr.splice(i, 1);
        continue;
      }
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    }

    // 状态文字提示
    ctx.font = "bold 12px sans-serif";
    if (rate >= 7) {
      ctx.fillStyle = "#fda4af";
      ctx.fillText("⚡ 剧烈产生 H₂↑", cx, liquidTopY - 10);
    } else if (rate >= 2) {
      ctx.fillStyle = "#fde047";
      ctx.fillText("🫧 持续产生 H₂↑", cx, liquidTopY - 10);
    } else if (rate > 0) {
      ctx.fillStyle = "#93c5fd";
      ctx.fillText("· 极缓慢微弱气泡", cx, liquidTopY - 10);
    } else {
      ctx.fillStyle = "#94a3b8";
      ctx.fillText("✖ 无明显反应 (No H₂)", cx, liquidTopY - 10);
    }
  }

  // 液面高光椭圆线
  ctx.strokeStyle = "rgba(255, 255, 255, 0.35)";
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(leftX + 4, liquidTopY);
  ctx.lineTo(rightX - 4, liquidTopY);
  ctx.stroke();

  // 烧杯玻璃外壁与刻度线
  ctx.strokeStyle = "rgba(226, 232, 240, 0.65)";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(leftX, topY);
  ctx.lineTo(leftX, bottomY - 12);
  ctx.quadraticCurveTo(leftX, bottomY, leftX + 12, bottomY);
  ctx.lineTo(rightX - 12, bottomY);
  ctx.quadraticCurveTo(rightX, bottomY, rightX, bottomY - 12);
  ctx.lineTo(rightX, topY);
  ctx.stroke();

  // 烧杯刻度
  ctx.strokeStyle = "rgba(226, 232, 240, 0.3)";
  ctx.lineWidth = 1;
  ctx.font = "10px monospace";
  ctx.fillStyle = "rgba(226, 232, 240, 0.45)";
  ctx.textAlign = "right";
  for (let m = 1; m <= 3; m++) {
    const my = bottomY - m * 50;
    ctx.beginPath();
    ctx.moveTo(rightX - 18, my);
    ctx.lineTo(rightX - 6, my);
    ctx.stroke();
    ctx.fillText(`${m * 100}mL`, rightX - 22, my + 3);
  }
}

// ============================================================================
// 实验二 Canvas：金属置换反应 (烧杯 + 浸入式金属片 + 离子微粒与表面析出层)
// ============================================================================
function renderDisplacementCanvas() {
  const canvas = document.getElementById("displacementCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const W = canvas.width;
  const H = canvas.height;

  ctx.clearRect(0, 0, W, H);

  // 背景
  const bgGrad = ctx.createLinearGradient(0, 0, 0, H);
  bgGrad.addColorStop(0, "#0b1325");
  bgGrad.addColorStop(1, "#162238");
  ctx.fillStyle = bgGrad;
  ctx.fillRect(0, 0, W, H);

  const m1 = dispState.stripMetal;
  const sol = SOLUTIONS_MAP[dispState.solutionKey];
  const m2 = ELEMENTS_DATA.find(e => e.symbol === sol.metalSym);

  const canDisplace = m1.zone !== "water" && m1.rank < m2.rank && m1.symbol !== m2.symbol;
  const reactsWithWaterFirst = m1.zone === "water";

  if (dispState.running && dispState.progress < 1) {
    dispState.progress = Math.min(1, dispState.progress + 0.004);
  }

  const cx = W * 0.38;
  const bottomY = H - 32;
  const bw = 260;
  const bh = 235;
  const leftX = cx - bw / 2;
  const rightX = cx + bw / 2;
  const topY = bottomY - bh;
  const liquidTopY = bottomY - bh * 0.72;

  // 计算溶液动态颜色插值
  let r = sol.initColor[0];
  let g = sol.initColor[1];
  let b = sol.initColor[2];
  let a = sol.initColor[3];

  if (canDisplace && dispState.running && dispState.solutionKey !== "H") {
    const p = dispState.progress;
    // 目标离子颜色
    let tr = 226, tg = 232, tb = 240, ta = 0.12;
    if (m1.symbol === "Fe") { tr = 74; tg = 222; tb = 128; ta = 0.38; }
    else if (m1.symbol === "Co") { tr = 244; tg = 114; tb = 182; ta = 0.34; }
    else if (m1.symbol === "Ni") { tr = 16; tg = 185; tb = 129; ta = 0.35; }
    else if (m1.symbol === "Cu") { tr = 14; tg = 165; tb = 233; ta = 0.48; }

    r = Math.round(r + (tr - r) * p);
    g = Math.round(g + (tg - g) * p);
    b = Math.round(b + (tb - b) * p);
    a = a + (ta - a) * p;
  }

  // 绘制溶液
  ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${a})`;
  ctx.beginPath();
  ctx.roundRect(leftX + 3, liquidTopY, bw - 6, bottomY - liquidTopY - 3, [0, 0, 12, 12]);
  ctx.fill();

  // 绘制斜插入烧杯的金属片 (M1)
  const stripW = 36;
  const stripH = 210;
  const stripX = cx - stripW / 2;
  const stripTopY = topY - 22;

  // 上半部分（液面以上）
  ctx.fillStyle = m1.metalColor;
  ctx.strokeStyle = "#0f172a";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.roundRect(stripX, stripTopY, stripW, stripH, 6);
  ctx.fill();
  ctx.stroke();

  // 浸入液面以下的置换析出涂层 (M2)
  const submergedY = liquidTopY + 4;
  const submergedH = stripTopY + stripH - submergedY;

  if (dispState.running && canDisplace && sol.depositColor && submergedH > 0) {
    const coatAlpha = Math.min(0.95, dispState.progress * 1.15);
    ctx.save();
    ctx.fillStyle = sol.depositColor;
    ctx.globalAlpha = coatAlpha;
    const growPad = dispState.progress * 5;
    ctx.beginPath();
    ctx.roundRect(stripX - growPad, submergedY, stripW + growPad * 2, submergedH + growPad, 8);
    ctx.fill();
    ctx.restore();
  }

  // 若是与 H+ 或水反应产生气泡
  if (dispState.running && (reactsWithWaterFirst || (canDisplace && dispState.solutionKey === "H"))) {
    if (Math.random() < 0.65) {
      dispState.bubbles.push({
        x: cx + (Math.random() - 0.5) * 44,
        y: submergedY + Math.random() * submergedH,
        r: 2.5 + Math.random() * 3,
        vy: 1.6 + Math.random() * 1.5
      });
    }
    ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
    for (let i = dispState.bubbles.length - 1; i >= 0; i--) {
      const bub = dispState.bubbles[i];
      bub.y -= bub.vy;
      if (bub.y <= liquidTopY) {
        dispState.bubbles.splice(i, 1);
        continue;
      }
      ctx.beginPath();
      ctx.arc(bub.x, bub.y, bub.r, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  // 金属片标签
  ctx.fillStyle = "#0f172a";
  ctx.font = "bold 13px monospace";
  ctx.textAlign = "center";
  ctx.fillText(m1.symbol, cx, stripTopY + 26);

  // 烧杯外壁
  ctx.strokeStyle = "rgba(226, 232, 240, 0.7)";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(leftX, topY);
  ctx.lineTo(leftX, bottomY - 12);
  ctx.quadraticCurveTo(leftX, bottomY, leftX + 12, bottomY);
  ctx.lineTo(rightX - 12, bottomY);
  ctx.quadraticCurveTo(rightX, bottomY, rightX, bottomY - 12);
  ctx.lineTo(rightX, topY);
  ctx.stroke();

  // 右侧微观电子转移放大视窗
  const microX = W * 0.76;
  const microY = H * 0.5;
  const microR = 112;

  ctx.save();
  ctx.beginPath();
  ctx.arc(microX, microY, microR, 0, Math.PI * 2);
  ctx.fillStyle = "#0f172a";
  ctx.fill();
  ctx.lineWidth = 2.5;
  ctx.strokeStyle = canDisplace ? "#22c55e" : (reactsWithWaterFirst ? "#facc15" : "#64748b");
  ctx.stroke();

  ctx.fillStyle = "#e2e8f0";
  ctx.font = "bold 12px sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("🔬 微观粒子与电子转移视角", microX, microY - microR - 12);

  if (reactsWithWaterFirst) {
    ctx.fillStyle = "#fde047";
    ctx.font = "bold 13px sans-serif";
    ctx.fillText(`${m1.symbol} 极度活泼！`, microX, microY - 25);
    ctx.fillStyle = "#cbd5e1";
    ctx.font = "12px sans-serif";
    ctx.fillText("优先将电子传给水中的 H₂O", microX, microY + 2);
    ctx.fillText(`生成 H₂↑ 和 OH⁻ 氢氧化物沉淀`, microX, microY + 24);
  } else if (canDisplace) {
    ctx.fillStyle = "#4ade80";
    ctx.font = "bold 13px sans-serif";
    ctx.fillText(`电子转移：${m1.symbol} → ${sol.ionSymbol}`, microX, microY - 38);

    ctx.fillStyle = "#93c5fd";
    ctx.font = "12px monospace";
    ctx.fillText(`氧化：${m1.symbol} - ne⁻ → ${m1.symbol}ⁿ⁺ (溶入)`, microX, microY - 8);
    ctx.fillStyle = "#fda4af";
    ctx.fillText(`还原：${sol.ionSymbol} + ne⁻ → ${m2.symbol}↓ (析出)`, microX, microY + 18);

    ctx.fillStyle = "#fde047";
    ctx.font = "bold 12px sans-serif";
    ctx.fillText(`置换进度: ${Math.round(dispState.progress * 100)}%`, microX, microY + 52);
  } else {
    ctx.fillStyle = "#f87171";
    ctx.font = "bold 13px sans-serif";
    ctx.fillText("无电子转移 (No e⁻ transfer)", microX, microY - 14);
    ctx.fillStyle = "#94a3b8";
    ctx.font = "12px sans-serif";
    ctx.fillText(`${m1.symbol} 失电子能力弱于 ${m2.symbol}`, microX, microY + 14);
    ctx.fillText("微观界面保持静止", microX, microY + 34);
  }
  ctx.restore();
}

// ============================================================================
// 随堂闯关问答逻辑
// ============================================================================
function initQuiz() {
  renderQuizQuestion();

  document.getElementById("quizPrevBtn").addEventListener("click", () => {
    if (quizIndex > 0) {
      quizIndex--;
      renderQuizQuestion();
    }
  });

  document.getElementById("quizNextBtn").addEventListener("click", () => {
    if (quizIndex < QUIZ_QUESTIONS.length - 1) {
      quizIndex++;
      renderQuizQuestion();
    }
  });

  document.getElementById("quizRestartBtn").addEventListener("click", () => {
    quizIndex = 0;
    quizScore = 0;
    quizAnswered.fill(null);
    document.getElementById("quizScoreVal").textContent = "0";
    renderQuizQuestion();
  });
}

function renderQuizQuestion() {
  const item = QUIZ_QUESTIONS[quizIndex];
  document.getElementById("quizStepBadge").textContent = `第 ${quizIndex + 1} / ${QUIZ_QUESTIONS.length} 题`;
  document.getElementById("quizQuestionText").textContent = item.q;

  const optsBox = document.getElementById("quizOptionsBox");
  const fbBox = document.getElementById("quizFeedbackBox");
  optsBox.innerHTML = "";

  const userAns = quizAnswered[quizIndex];

  item.options.forEach((optText, idx) => {
    const btn = document.createElement("button");
    btn.className = "quiz-option-btn";
    btn.textContent = optText;

    if (userAns !== null) {
      btn.disabled = true;
      if (idx === item.answer) btn.classList.add("correct");
      else if (idx === userAns) btn.classList.add("wrong");
    }

    btn.addEventListener("click", () => {
      if (quizAnswered[quizIndex] !== null) return;
      quizAnswered[quizIndex] = idx;
      if (idx === item.answer) {
        quizScore++;
        document.getElementById("quizScoreVal").textContent = String(quizScore);
      }
      renderQuizQuestion();
    });

    optsBox.appendChild(btn);
  });

  if (userAns !== null) {
    fbBox.classList.remove("hidden");
    const isRight = userAns === item.answer;
    fbBox.style.borderLeftColor = isRight ? "#22c55e" : "#ef4444";
    fbBox.innerHTML = `<strong>${isRight ? "✅ 回答正确！" : "❌ 回答有误"}</strong> ${item.explanation}`;
  } else {
    fbBox.classList.add("hidden");
  }

  document.getElementById("quizPrevBtn").disabled = quizIndex === 0;
  document.getElementById("quizNextBtn").disabled = quizIndex === QUIZ_QUESTIONS.length - 1;
}
