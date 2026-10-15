# -*- coding: utf-8 -*-
"""
Builder for Cambridge G8 Science 2-Hour Exam Rush Hub
Generates g8_exam_rush.html with:
1. Core Concept Cards & Mindmaps (3 major topics)
2. Objective Practice Arena (48 questions: 16 Transport, 16 Kidneys, 16 Glucose)
3. Written Theory & Mark Scheme Arena (10 authentic Cambridge structured questions)
4. 40-Minute Mock Exam Simulator (15 MCQs + 3 Theory Questions, 30 Marks, Radar Diagnosis)
"""

import json

# ----------------- 1. OBJECTIVE QUESTIONS (48 ITEMS) -----------------
OBJECTIVE_QUESTIONS = [
    # ========== LEVEL 1: MOVEMENT IN AND OUT OF CELLS (Q1 - Q16) ==========
    {
        "id": "rush_q01",
        "level": 1,
        "topic": "Diffusion Principle",
        "prompt_en": "Which statement correctly describes the net movement of particles during diffusion?",
        "prompt_cn": "下列关于扩散过程中微观粒子净移动的描述，哪一项是完全正确的？",
        "options": [
            {"letter": "A", "text_en": "Movement from a region of lower concentration to higher concentration using metabolic ATP.", "text_cn": "从低浓度向高浓度移动，消耗代谢能量 ATP。"},
            {"letter": "B", "text_en": "Net movement of particles from a region of higher concentration to lower concentration down a concentration gradient as a result of their random kinetic motion.", "text_cn": "由于粒子的随机热运动，粒子从高浓度区域向低浓度区域沿着浓度梯度的净移动。"},
            {"letter": "C", "text_en": "Movement of water molecules only across a fully impermeable cell wall.", "text_cn": "水分子穿过完全不透水细胞壁的单一方向移动。"},
            {"letter": "D", "text_en": "Complete cessation of particle motion once dynamic equilibrium is attained.", "text_cn": "一旦达到动态平衡，所有微观粒子的运动立即完全停止。"}
        ],
        "correct": "B",
        "concept_en": "Diffusion is the passive net movement of particles down a concentration gradient driven entirely by random kinetic energy. It requires NO metabolic energy (ATP).",
        "concept_cn": "扩散是粒子完全由其自身的随机动能驱动、沿浓度梯度进行的被动净移动，不需要消耗任何细胞代谢能量（ATP）。",
        "trap_en": "Option A describes active transport. Option D is a frequent misconception: at dynamic equilibrium, particles continue to move equally in all directions with zero NET change.",
        "trap_cn": "选项 A 混淆了主动运输。选项 D 是极高频陷阱：达到动态平衡时，粒子依然在各个方向以相等速率自由运动，只是“净移动为零”，绝非粒子停止运动。",
        "citation": "《G8 Science》Chapter 3.01 Diffusion (pp. 24-26)"
    },
    {
        "id": "rush_q02",
        "level": 1,
        "topic": "Factors Affecting Diffusion Rate",
        "prompt_en": "Which combination of physiological conditions produces the FASTEST rate of diffusion across a respiratory membrane?",
        "prompt_cn": "下列哪一组生理条件的组合，能使穿过呼吸膜的扩散速率达到最快？",
        "options": [
            {"letter": "A", "text_en": "High temperature, large surface area, steep concentration gradient, and thin membrane (short diffusion distance).", "text_cn": "高温、大表面积、陡峭浓度梯度、极薄的膜结构（超短扩散距离）。"},
            {"letter": "B", "text_en": "Low temperature, small surface area, steep concentration gradient, and thick membrane.", "text_cn": "低温、小表面积、陡峭浓度梯度、厚膜结构。"},
            {"letter": "C", "text_en": "High temperature, small surface area, shallow concentration gradient, and long distance.", "text_cn": "高温、小表面积、平缓浓度梯度、超长距离。"},
            {"letter": "D", "text_en": "Zero concentration gradient, large surface area, and freezing temperature.", "text_cn": "零浓度梯度、大表面积、冰冻温度。"}
        ],
        "correct": "A",
        "concept_en": "Diffusion Rate is directly proportional to: Temperature (kinetic speed), Surface Area (collision opportunities), and Concentration Gradient (driving force); and inversely proportional to Diffusion Distance.",
        "concept_cn": "扩散速率与温度（动能大小）、表面积（碰撞几率）和浓度梯度（驱动力）成正比，与扩散距离（膜厚度）成反比。",
        "trap_en": "Thicker membranes increase diffusion distance, drastically slowing diffusion (Fick's Law).",
        "trap_cn": "膜越厚，微观粒子穿透所需时间越长，扩散速率显著下降。",
        "citation": "《G8 Science》Chapter 3.02 Factors Influencing Rate (pp. 27-29)"
    },
    {
        "id": "rush_q03",
        "level": 1,
        "topic": "Osmosis & Water Potential",
        "prompt_en": "Osmosis is defined specifically as the net movement of water molecules:",
        "prompt_cn": "渗透作用（Osmosis）在生物学中特异性地定义为水分子：",
        "options": [
            {"letter": "A", "text_en": "From a region of lower water potential to higher water potential through any open pore.", "text_cn": "从低水势区域向高水势区域穿过任意开放微孔的移动。"},
            {"letter": "B", "text_en": "From a region of higher water potential (dilute solution) to lower water potential (concentrated solution) through a partially permeable membrane.", "text_cn": "从高水势区域（低溶质稀溶液）穿过半透膜向低水势区域（高溶质浓溶液）的净移动。"},
            {"letter": "C", "text_en": "Driven by ATP pumps across a totally impermeable cell wall.", "text_cn": "由 ATP 泵驱动穿过完全不透水细胞壁的移动。"},
            {"letter": "D", "text_en": "Of solute particles dissolving until equal volume is established.", "text_cn": "溶质粒子溶解直到体积相等的移动。"}
        ],
        "correct": "B",
        "concept_en": "Osmosis is a special case of passive diffusion: ONLY water molecules move, and it REQUIRES a partially permeable (semi-permeable) membrane down a water potential gradient.",
        "concept_cn": "渗透是被动扩散的特例：仅限水分子移动，且必须穿过半透膜（选择透过性膜），从高水势向低水势移动。",
        "trap_en": "High water potential = dilute solution (lots of free water); Low water potential = concentrated solution (water bound to solutes).",
        "trap_cn": "高水势等同于稀溶液（自由水分子多）；低水势等同于浓溶液。水总是流向“浓溶液”那一侧以稀释它。",
        "citation": "《G8 Science》Chapter 3.03 Osmosis & Water Potential (pp. 30-31)"
    },
    {
        "id": "rush_q04",
        "level": 1,
        "topic": "Plant Cells & Turgor Pressure",
        "prompt_en": "When a crisp plant cell is placed in pure distilled water, what happens and what prevents it from bursting?",
        "prompt_cn": "当一个植物细胞被放入纯蒸馏水中时，会发生什么现象？是什么结构防止它涨破？",
        "options": [
            {"letter": "A", "text_en": "Water leaves the cell; the flexible cell membrane prevents bursting.", "text_cn": "水离开细胞；柔软的细胞膜防止其涨破。"},
            {"letter": "B", "text_en": "Water enters by osmosis; vacuole expands and cytoplasm pushes against the rigid cellulose cell wall, making the cell TURGID.", "text_cn": "水通过渗透作用进入细胞；液泡膨胀，原生质层压向刚性纤维素细胞壁，使细胞保持膨胀坚挺（Turgid）。"},
            {"letter": "C", "text_en": "The cell immediately lyses (bursts) because it absorbs too much sugar.", "text_cn": "细胞因吸收过多糖分立即发生破裂（Lysis）。"},
            {"letter": "D", "text_en": "The cell wall actively pumps all water out using metabolic energy.", "text_cn": "细胞壁消耗代谢能量主动将所有水分泵出。"}
        ],
        "correct": "B",
        "concept_en": "Pure water has a higher water potential than the plant cell sap. Water enters by osmosis. The inelastic cellulose cell wall exerts wall pressure, creating turgor pressure which supports non-woody plant stems.",
        "concept_cn": "纯水水势高于植物细胞液。水渗透进入，坚韧的纤维素细胞壁抵抗膨胀产生膨压（Turgor pressure），维持植物幼嫩茎叶直立挺拔。",
        "trap_en": "Plant cells DO NOT burst in pure water because of the rigid cell wall! Only animal cells burst.",
        "trap_cn": "高频易混点：植物细胞有刚性细胞壁，在纯水中只膨胀不涨破！涨破（Lysis）是无细胞壁的动物细胞特有现象。",
        "citation": "《G8 Science》Chapter 3.04 Plant Cells in Solutions (pp. 32-33)"
    },
    {
        "id": "rush_q05",
        "level": 1,
        "topic": "Plant Plasmolysis",
        "prompt_en": "When plant tissue (e.g. onion epidermal cells) is immersed in a concentrated sugar solution, what is observed under a microscope?",
        "prompt_cn": "当洋葱表皮植物细胞浸入高浓度浓糖水中时，在显微镜下会观察到什么现象？",
        "options": [
            {"letter": "A", "text_en": "Water enters and the cell bursts into fragments.", "text_cn": "水进入细胞，导致细胞破裂成碎片。"},
            {"letter": "B", "text_en": "Water leaves the cell by osmosis; cytoplasm and cell membrane shrink and pull away from the rigid cell wall (Plasmolysed).", "text_cn": "水通过渗透作用流出细胞；原生质层和细胞膜皱缩并从刚性细胞壁脱离（质壁分离 Plasmolysed）。"},
            {"letter": "C", "text_en": "Cell wall dissolves completely in the sugar solution.", "text_cn": "细胞壁在糖溶液中完全溶解。"},
            {"letter": "D", "text_en": "Chloroplasts multiply rapidly to replace lost volume.", "text_cn": "叶绿体迅速分裂以补充丢失的体积。"}
        ],
        "correct": "B",
        "concept_en": "External concentrated solution has a lower water potential than cell cytoplasm. Water leaves the vacuole by osmosis. The cell membrane pulls away from the cell wall, causing plasmolysis.",
        "concept_cn": "外界高浓度溶液水势低于细胞质。水分通过渗透作用流出液泡，原生质层与细胞壁分离，发生质壁分离（Plasmolysis）。",
        "trap_en": "The cell wall does NOT shrink significantly because it is rigid; only the inner protoplast shrinks away.",
        "trap_cn": "细胞壁不会剧烈皱缩（具有刚性），是内部的原生质层脱离细胞壁。",
        "citation": "《G8 Science》Chapter 3.04 Plasmolysis (pp. 33-34)"
    },
    {
        "id": "rush_q06",
        "level": 1,
        "topic": "Animal Cells: Lysis vs Crenation",
        "prompt_en": "What happens to human red blood cells when placed into concentrated salt solution versus pure distilled water?",
        "prompt_cn": "当人类红细胞分别置于高浓度浓盐水与纯蒸馏水中时，会发生什么变化？",
        "options": [
            {"letter": "A", "text_en": "Concentrated salt: cell bursts (lysis); Distilled water: cell shrivels (crenated).", "text_cn": "浓盐水：细胞涨破（Lysis）；蒸馏水：细胞皱缩（Crenated）。"},
            {"letter": "B", "text_en": "Concentrated salt: cell loses water and shrivels (crenated); Distilled water: cell gains water by osmosis, swells, and bursts (lysis).", "text_cn": "浓盐水：细胞渗透失水皱缩（Crenated）；蒸馏水：细胞渗透吸水膨胀并涨破（Lysis）。"},
            {"letter": "C", "text_en": "Both solutions cause the red blood cells to become plasmolysed.", "text_cn": "两种溶液都会导致红细胞发生质壁分离。"},
            {"letter": "D", "text_en": "Red blood cells remain completely unchanged due to their rigid cell walls.", "text_cn": "红细胞因具有刚性细胞壁而保持体积完全不变。"}
        ],
        "correct": "B",
        "concept_en": "Animal cells lack a cell wall. Hypertonic solution $\\to$ water leaves $\\to$ crenated (shrivelled). Hypotonic / pure water $\\to$ water enters $\\to$ swells and bursts (haemolysis).",
        "concept_cn": "动物细胞没有细胞壁。高渗失水 $\\to$ 皱缩（Crenated）；低渗吸水 $\\to$ 涨破（Lysis）。",
        "trap_en": "Red blood cells NEVER undergo plasmolysis because they have no cell wall! Plasmolysis is strictly for plant cells.",
        "trap_cn": "动物红细胞绝对没有细胞壁，因此绝对不能用“质壁分离”来描述动物细胞！",
        "citation": "《G8 Science》Chapter 3.05 Osmosis in Animal Cells (pp. 34-35)"
    },
    {
        "id": "rush_q07",
        "level": 1,
        "topic": "Active Transport Definition",
        "prompt_en": "How does active transport differ fundamentally from diffusion and osmosis?",
        "prompt_cn": "主动运输（Active Transport）在机理上与扩散和渗透有何根本不同？",
        "options": [
            {"letter": "A", "text_en": "It moves particles down a concentration gradient without any carrier proteins.", "text_cn": "它顺着浓度梯度移动粒子，不需要任何载体蛋白。"},
            {"letter": "B", "text_en": "It moves particles AGAINST (up) a concentration gradient using energy released from cellular respiration (ATP) via membrane carrier proteins.", "text_cn": "它利用细胞呼吸释放的代谢能量（ATP），通过细胞膜上的载体蛋白将粒子逆着（从低向高）浓度梯度转运。"},
            {"letter": "C", "text_en": "It only transports water molecules and stops at freezing temperatures.", "text_cn": "它只运输水分子，在冰冻温度下停止。"},
            {"letter": "D", "text_en": "It is completely passive and occurs outside living organisms.", "text_cn": "它完全是被动的，可以在非生命物质中自发发生。"}
        ],
        "correct": "B",
        "concept_en": "Active transport moves substances UP/AGAINST a concentration gradient (low to high conc.). It REQUIRES cellular respiration (ATP) and specific transmembrane carrier proteins.",
        "concept_cn": "主动运输逆浓度梯度转运物质（从低到高），必须消耗细胞呼吸产生的 ATP 能量，并依赖膜上的特异性载体蛋白。",
        "trap_en": "Poisoning mitochondria (respiration inhibitor like cyanide) immediately halts active transport, but does NOT stop passive diffusion.",
        "trap_cn": "若线粒体呼吸受阻（如氰化物毒素），主动运输立即停止，而被动扩散不受直接影响。",
        "citation": "《G8 Science》Chapter 3.06 Active Transport (pp. 35-37)"
    },
    {
        "id": "rush_q08",
        "level": 1,
        "topic": "Active Transport Sites",
        "prompt_en": "In the human body, where is active transport of vital importance for recovering nutrients?",
        "prompt_cn": "在人体内，主动运输在何处发挥至关重要的营养物质回收作用？",
        "options": [
            {"letter": "A", "text_en": "In the proximal convoluted tubule of the kidney nephron, recovering 100% of filtered glucose back into the blood.", "text_cn": "在肾单位的近曲小管处，将原尿中 100% 的葡萄糖逆浓度主动重吸收回血液中。"},
            {"letter": "B", "text_en": "In the stomach lumen to dissolve food bones.", "text_cn": "在胃腔中用以溶解食物骨骼。"},
            {"letter": "C", "text_en": "In the trachea to pump mucus down into lungs.", "text_cn": "在气管中将粘液主动泵入肺底。"},
            {"letter": "D", "text_en": "In the urinary bladder to synthesize urine.", "text_cn": "在膀胱中合成尿液。"}
        ],
        "correct": "A",
        "concept_en": "Kidney proximal convoluted tubule epithelial cells use active transport carrier proteins (powered by ATP from abundant mitochondria) to selectively reabsorb 100% of glucose and amino acids.",
        "concept_cn": "肾小管上皮细胞富含线粒体，利用 ATP 驱动载体蛋白逆浓度梯度将原尿中 100% 的葡萄糖和氨基酸完全重吸收回血液。",
        "trap_en": "Filtration in glomerulus is passive (driven by blood pressure); reabsorption in tubules is ACTIVE.",
        "trap_cn": "肾小球的超滤是被动的（由血压驱动），而肾小管回收葡萄糖是典型的主动运输过程！",
        "citation": "《G8 Science》Chapter 4: B9.06 Homeostasis & Kidney (pp. 54-56)"
    },
    {
        "id": "rush_q09",
        "level": 1,
        "topic": "Surface Area to Volume Ratio",
        "prompt_en": "Why can a single-celled Amoeba rely purely on diffusion for gas exchange, while a human requires a complex circulatory and respiratory system?",
        "prompt_cn": "为什么单细胞变形虫仅凭体表扩散就能满足气体交换，而人类必须拥有复杂的呼吸与循环系统？",
        "options": [
            {"letter": "A", "text_en": "Amoeba has a small surface area to volume ratio, so diffusion is fast.", "text_cn": "变形虫的表面积/体积比很小，因此扩散更快。"},
            {"letter": "B", "text_en": "Amoeba has a LARGE surface area to volume ratio and short diffusion distance; humans have a SMALL SA:V ratio and massive diffusion distances to interior cells.", "text_cn": "变形虫体型微小，具有极大的表面积/体积比（SA:V）且扩散距离极短；而人类体型庞大，SA:V 比极小，内部细胞与外界距离过长。"},
            {"letter": "C", "text_en": "Human cells do not need oxygen for cellular respiration.", "text_cn": "人体细胞进行细胞呼吸不需要氧气。"},
            {"letter": "D", "text_en": "Amoebas have thick impermeable keratin coverings.", "text_cn": "变形虫表面覆盖有厚重不透水的角质层。"}
        ],
        "correct": "B",
        "concept_en": "As organisms increase in size, their volume grows far faster than surface area (SA:V ratio decreases). Diffusion alone becomes too slow to supply interior cells, requiring specialized exchange surfaces and transport systems.",
        "concept_cn": "生物体越大，体积增长远快于表面积，SA:V 比急剧下降，纯扩散无法穿越长距离供给深层细胞，必须演化出专职呼吸器官和循环系统。",
        "trap_en": "Smaller organisms have LARGER surface area to volume ratios, not smaller!",
        "trap_cn": "高频混淆：体型越小，相对表面积/体积比（SA:V）越大；体型越大，SA:V 越小！",
        "citation": "《G8 Science》Chapter 3: B8.02 Gas Exchange & SA:V (pp. 38-40)"
    },
    {
        "id": "rush_q10",
        "level": 1,
        "topic": "Membrane Pore Size Selectivity",
        "prompt_en": "In a Visking tubing (dialysis tubing) experiment, why do water and glucose diffuse out into surrounding beaker water, while starch stays inside?",
        "prompt_cn": "在透析透膜管（Visking tubing）实验中，为什么水和葡萄糖能扩散到外围烧杯中，而淀粉分子却被截留在管内？",
        "options": [
            {"letter": "A", "text_en": "Starch is negatively charged and repelled by glass.", "text_cn": "淀粉带负电荷被玻璃排斥。"},
            {"letter": "B", "text_en": "Water and glucose molecules are small enough to pass through microscopic pores in the membrane; starch is a giant polymer molecule too large to fit through the pores.", "text_cn": "水和葡萄糖分子足够小，能穿过半透膜的微观孔隙；而淀粉是多糖大分子，分子体积过大无法穿过孔隙。"},
            {"letter": "C", "text_en": "Glucose is actively pumped out by enzymes in the artificial plastic.", "text_cn": "塑料管内的酶主动将葡萄糖泵出。"},
            {"letter": "D", "text_en": "Starch evaporates quickly into air.", "text_cn": "淀粉迅速蒸发到空气中。"}
        ],
        "correct": "B",
        "concept_en": "Partially permeable membranes discriminate strictly by physical molecular size. Monosaccharides (glucose) and water pass freely; macromolecules (starch, albumen) are physically excluded.",
        "concept_cn": "半透膜依据分子物理尺寸进行物理筛分：单糖（葡萄糖）和水小分子可自由穿透；大分子多糖（淀粉）和蛋白质被物理孔径截留。",
        "trap_en": "Dialysis tubing is non-living; it acts purely as a passive physical molecular sieve, not an active biological pump.",
        "trap_cn": "透析管属于无生命的物理膜，完全依赖分子孔径物理筛选，绝无酶的主动泵送作用。",
        "citation": "《G8 Science》Chapter 3.03 Dialysis Tubing Model (p. 31)"
    },
    {
        "id": "rush_q11",
        "level": 1,
        "topic": "Water Potential Scale",
        "prompt_en": "What is the water potential of pure distilled water at atmospheric pressure, and what happens when solute (e.g. NaCl) is dissolved in it?",
        "prompt_cn": "在标准大气压下，纯蒸馏水的水势是多少？当溶质（如食盐 NaCl）溶解于其中时，水势如何变化？",
        "options": [
            {"letter": "A", "text_en": "Pure water has a water potential of 0 kPa; adding solute LOWERS water potential to a negative value.", "text_cn": "纯水的水势最高，为 0 kPa；加入溶质会使水势降低为负值。"},
            {"letter": "B", "text_en": "Pure water has a water potential of +100 kPa; adding solute increases it to +1000 kPa.", "text_cn": "纯水水势为 +100 kPa；加入溶质使其上升到 +1000 kPa。"},
            {"letter": "C", "text_en": "Pure water has no water potential at all.", "text_cn": "纯水根本没有水势。"},
            {"letter": "D", "text_en": "Adding solute makes water potential turn positive.", "text_cn": "加入溶质会使水势变为正数。"}
        ],
        "correct": "A",
        "concept_en": "Pure liquid water at atmospheric pressure has the maximum possible water potential: exactly 0 kPa. All aqueous solutions have NEGATIVE water potentials (< 0 kPa) because solute particles bind water molecules, reducing their free kinetic motion.",
        "concept_cn": "纯净水水势最高，定义为 0 kPa。任何溶液溶入溶质后，溶质水合作用限制了自由水分子的动能，水势必然变为负数（< 0 kPa）。",
        "trap_en": "Water potential can never be positive in an open system! Concentrated solutions have very low (more negative) water potentials.",
        "trap_cn": "在开放体系中水势永远不可能为正数！溶液浓度越高，其水势越低（负值绝对值越大）。",
        "citation": "《G8 Science》Chapter 3.03 Water Potential (pp. 30-31)"
    },
    {
        "id": "rush_q12",
        "level": 1,
        "topic": "Dynamic Equilibrium in Diffusion",
        "prompt_en": "When dynamic equilibrium is reached during diffusion across a permeable membrane, what happens to the particles?",
        "prompt_cn": "在穿过透性膜的扩散过程达到动态平衡时，微观粒子处于何种状态？",
        "options": [
            {"letter": "A", "text_en": "Particles continue to move randomly in all directions at equal rates, resulting in ZERO NET movement.", "text_cn": "粒子仍在各个方向以相等的速率随机热运动，导致宏观上的净移动量为零。"},
            {"letter": "B", "text_en": "All molecular motion freezes and stops completely.", "text_cn": "所有分子的热运动瞬间冻结并完全停止。"},
            {"letter": "C", "text_en": "All particles migrate to one side of the membrane.", "text_cn": "所有粒子迁移到膜的同一侧。"},
            {"letter": "D", "text_en": "The concentration gradient becomes infinitely steep.", "text_cn": "浓度梯度变得无限陡峭。"}
        ],
        "correct": "A",
        "concept_en": "'Dynamic equilibrium' means movement is ongoing ('dynamic'), but rates of movement in opposing directions are equal, maintaining uniform concentration ('equilibrium').",
        "concept_cn": "“动态平衡”意味着分子的无规则微观热运动从未停止（Dynamic），但两侧相互穿透的速率完全相等，宏观浓度保持不变（Equilibrium）。",
        "trap_en": "Equilibrium DOES NOT mean particles stand still! Absolute zero (0 Kelvin) is required to stop particle motion.",
        "trap_cn": "极高频考题陷阱：达到平衡绝非粒子停止运动！微观粒子仍在以极高速率随机穿梭，只是净移动为零。",
        "citation": "《G8 Science》Chapter 3.01 Equilibrium (pp. 25-26)"
    },
    {
        "id": "rush_q13",
        "level": 1,
        "topic": "Flaccid Plant Cells",
        "prompt_en": "What happens to a leafy plant when its cells lose turgor pressure and become 'flaccid'?",
        "prompt_cn": "当草本阔叶植物的细胞失去膨压并变得松弛（Flaccid）时，植物整体外观会出现何种变化？",
        "options": [
            {"letter": "A", "text_en": "The plant stems stand rigid and tall.", "text_cn": "植物茎秆更加坚挺笔直。"},
            {"letter": "B", "text_en": "The plant leaves droop and the stem wilts.", "text_cn": "植物叶片下垂，茎秆出现萎蔫（Wilting）。"},
            {"letter": "C", "text_en": "The plant immediately begins flowering.", "text_cn": "植物立即开花。"},
            {"letter": "D", "text_en": "The roots explode due to water build-up.", "text_cn": "根部因水分积聚发生爆炸。"}
        ],
        "correct": "B",
        "concept_en": "Non-woody herbaceous plants rely on hydrostatic turgor pressure inside cells to push against cell walls and stay erect. When water is scarce, cells lose turgor, become flaccid, and the plant wilts.",
        "concept_cn": "草本非木本植物完全依赖细胞内液泡的充水膨压支持机体直立。失水时细胞松弛（Flaccid），失去支撑力导致整株植物发生萎蔫（Wilting）。",
        "trap_en": "Wilting actually helps the plant reduce further water loss by drooping leaves and closing stomata.",
        "trap_cn": "萎蔫是植物缺水时的外显病理状态，此时下垂叶片可减少阳光直射并促进气孔关闭以减少蒸腾失水。",
        "citation": "《G8 Science》Chapter 3.04 Turgor & Wilting (pp. 32-34)"
    },
    {
        "id": "rush_q14",
        "level": 1,
        "topic": "Passive Process Nature",
        "prompt_en": "[True / False] Diffusion and osmosis are strictly passive physical processes that occur without requiring ATP energy from cellular respiration.",
        "prompt_cn": "【正误判断】扩散与渗透作用完全属于被动的物理过程，不需要细胞呼吸提供任何 ATP 代谢能量。",
        "options": [
            {"letter": "A", "text_en": "TRUE (完全正确)", "text_cn": "TRUE (完全正确)"},
            {"letter": "B", "text_en": "FALSE (错误，需要线粒体ATP供能)", "text_cn": "FALSE (错误，需要线粒体ATP供能)"}
        ],
        "correct": "A",
        "concept_en": "Diffusion and osmosis are driven 100% by the inherent kinetic thermal energy of particles. They can happen in non-living systems (e.g. food dye in a glass of water, cellophane tubing).",
        "concept_cn": "扩散和渗透由粒子内在的热动能驱动，无需任何生命代谢消耗，在无生命的纯物理体系（如水中滴墨水、透析膜）中亦能发生。",
        "trap_en": "Only ACTIVE transport requires ATP energy from respiration.",
        "trap_cn": "只有【主动运输】才需要消耗线粒体呼吸释放的 ATP 代谢能量！",
        "citation": "《G8 Science》Chapter 3.01 Passive Transport (p. 24)"
    },
    {
        "id": "rush_q15",
        "level": 1,
        "topic": "Space in Plasmolysed Cells",
        "prompt_en": "When a plant cell undergoes plasmolysis in concentrated salt solution, what fills the space between the cell wall and the shrunken cell membrane?",
        "prompt_cn": "当植物细胞在浓盐水中发生质壁分离时，刚性细胞壁与皱缩的细胞膜之间的空隙被什么物质填充？",
        "options": [
            {"letter": "A", "text_en": "A pure physical vacuum (empty space).", "text_cn": "完全真空（空无一物）。"},
            {"letter": "B", "text_en": "Air and oxygen bubbles.", "text_cn": "空气与氧气气泡。"},
            {"letter": "C", "text_en": "The external concentrated salt solution (because the cellulose cell wall is fully permeable).", "text_cn": "外界的浓盐水溶液（因为纤维素细胞壁是全透性的）。"},
            {"letter": "D", "text_en": "Pure distilled water secreted by chloroplasts.", "text_cn": "由叶绿体分泌出的纯蒸馏水。"}
        ],
        "correct": "C",
        "concept_en": "The plant cell wall is FULLY PERMEABLE (freely allows water and dissolved salt ions to pass). Only the cell membrane is partially permeable. Therefore, the external solution freely passes through the wall into the gap.",
        "concept_cn": "植物纤维素细胞壁是【完全通透】的粗大网状结构，水分子和溶质盐均可自由穿过；只有细胞膜才具有选择透过性。因此空隙中充满外界高浓度溶液。",
        "trap_en": "Many students mistakenly think there is a vacuum or air! The cell wall is permeable, so external liquid fills the space.",
        "trap_cn": "极其经典的考卷易错题：学生极易误选“真空”或“空气”，实质上外部溶液完全通过全透性细胞壁充满了质壁分离间隙！",
        "citation": "《G8 Science》Chapter 3.04 Plasmolysis Mechanics (pp. 33-34)"
    },
    {
        "id": "rush_q16",
        "level": 1,
        "topic": "Root Hair Cell Adaptations",
        "prompt_en": "How are plant root hair cells structurally adapted to maximize the absorption of water and mineral ions from soil?",
        "prompt_cn": "植物根毛细胞在微观形态结构上具有什么适应性特征，以最大化从土壤中吸收水分和矿质离子？",
        "options": [
            {"letter": "A", "text_en": "A long, thin hair-like extension that greatly increases the surface area to volume ratio, and many mitochondria to supply ATP for active transport of ions.", "text_cn": "具有细长的毛状外突以极大增加表面积/体积比（SA:V），且富含线粒体为离子主动运输提供大量 ATP。"},
            {"letter": "B", "text_en": "A thick waxy cuticle covering to keep water out.", "text_cn": "覆盖着厚厚的防水角质层以隔绝水分。"},
            {"letter": "C", "text_en": "Zero vacuole and no cell membrane.", "text_cn": "完全没有液泡和细胞膜。"},
            {"letter": "D", "text_en": "Dense chloroplasts to carry out photosynthesis underground.", "text_cn": "含有大量叶绿体以便在地下进行光合作用。"}
        ],
        "correct": "A",
        "concept_en": "Root hair cells feature: 1) Elongated extension $\\to$ high SA:V for osmosis; 2) Abundant mitochondria $\\to$ ATP for active transport of nitrates/minerals from low soil concentrations.",
        "concept_cn": "根毛细胞的两大经典考纲结构特征：1) 细长突起极大增加表面积提高渗透效率；2) 大量线粒体供能保障主动吸收低浓度土壤无机盐。",
        "trap_en": "Root cells NEVER have chloroplasts because they live underground in darkness with no light for photosynthesis.",
        "trap_cn": "根毛细胞绝对没有叶绿体（在地下黑暗环境中生长，无法光合作用）。",
        "citation": "《G8 Science》Chapter 3.07 Specialised Plant Cells (pp. 37-38)"
    },

    # ========== LEVEL 2: EXCRETION & KIDNEY FUNCTION (Q17 - Q32) ==========
    {
        "id": "rush_q17",
        "level": 2,
        "topic": "Excretion vs Egestion",
        "prompt_en": "Which statement correctly distinguishes biological EXCRETION from EGESTION?",
        "prompt_cn": "下列哪一项陈述准确区分了生物学上的【排泄 (Excretion)】与【排遗 (Egestion)】？",
        "options": [
            {"letter": "A", "text_en": "Excretion is the removal of undigested food as faeces; Egestion is the removal of metabolic urine.", "text_cn": "排泄是指以粪便形式排出未消化食物；排遗是指排出代谢尿液。"},
            {"letter": "B", "text_en": "Excretion is the removal of toxic waste products of cellular metabolism (e.g. urea, CO2); Egestion is the expulsion of undigested food material (faeces) that never entered cells.", "text_cn": "排泄是清除细胞代谢产生的有毒副产物（如尿素、二氧化碳）；排遗则是将从未进入细胞参与代谢的未消化食物残渣（粪便）排出体外。"},
            {"letter": "C", "text_en": "Excretion only occurs in plants; Egestion only occurs in mammals.", "text_cn": "排泄只发生在植物中；排遗只发生在哺乳动物中。"},
            {"letter": "D", "text_en": "Both processes produce identical substances filtered by the kidney.", "text_cn": "两种生理过程排出的物质完全相同，均由肾脏滤过产生。"}
        ],
        "correct": "B",
        "concept_en": "EXCRETION: Removal of metabolic wastes produced by cellular chemical reactions (e.g. urea via kidneys, CO2 via lungs). EGESTION: Physical discharge of undigested dietary fibre (faeces) via anus.",
        "concept_cn": "排泄（Excretion）：排出细胞生化代谢产生的有毒废物（如肾脏排尿素、肺排CO2）。排遗（Egestion）：排出从未被吸收进细胞的未消化食物残渣（粪便）。",
        "trap_en": "Defaecation (passing faeces) is EGESTION, NOT excretion! Faeces is never made by cell metabolism.",
        "trap_cn": "高频考试陷阱：排便（Faeces）属于【排遗】，绝不是排泄！粪便从未进入人体组织细胞代谢。",
        "citation": "《G8 Science》Chapter 4: B9.06 Homeostasis (pp. 54-56)"
    },
    {
        "id": "rush_q18",
        "level": 2,
        "topic": "Urinary System Pathway",
        "prompt_en": "Which sequence correctly traces the flow of urine from its site of formation to its exit from the body?",
        "prompt_cn": "下列哪一项正确追踪了尿液从生成部位到排出体外的生理通路？",
        "options": [
            {"letter": "A", "text_en": "Kidney $\\to$ Urethra $\\to$ Bladder $\\to$ Ureter.", "text_cn": "肾脏 $\\to$ 尿道 $\\to$ 膀胱 $\\to$ 输尿管。"},
            {"letter": "B", "text_en": "Kidney $\\to$ Ureter $\\to$ Bladder $\\to$ Urethra.", "text_cn": "肾脏 $\\to$ 输尿管（Ureter） $\\to$ 膀胱（Bladder） $\\to$ 尿道（Urethra）。"},
            {"letter": "C", "text_en": "Renal vein $\\to$ Ureter $\\to$ Bladder $\\to$ Renal artery.", "text_cn": "肾静脉 $\\to$ 输尿管 $\\to$ 膀胱 $\\to$ 肾动脉。"},
            {"letter": "D", "text_en": "Bladder $\\to$ Kidney $\\to$ Ureter $\\to$ Urethra.", "text_cn": "膀胱 $\\to$ 肾脏 $\\to$ 输尿管 $\\to$ 尿道。"}
        ],
        "correct": "B",
        "concept_en": "Urine is formed in the kidney nephrons $\\to$ passes down the URETER (one from each kidney) $\\to$ stored in the muscular BLADDER $\\to$ discharged via the single URETHRA during micturition.",
        "concept_cn": "肾单位形成的尿液流入肾盂 $\\to$ 经两侧的输尿管（Ureter）流入膀胱（Bladder）暂存 $\\to$ 排尿时经单根尿道（Urethra）排出体外。",
        "trap_en": "Ureter has 2 tubes (from each kidney) and comes FIRST alphabetically before Urethra (single exit tube).",
        "trap_cn": "记忆技巧：Ureter（输尿管）有两个在上方；Urethra（尿道）只有一根在最下方，千万不可倒置！",
        "citation": "《G8 Science》Chapter 13.02 The Urinary System (pp. 142-143)"
    },
    {
        "id": "rush_q19",
        "level": 2,
        "topic": "Origin of Urea in Liver",
        "prompt_en": "Where in the body is the nitrogenous waste UREA synthesized, and from what substrate?",
        "prompt_cn": "人体内的含氮代谢废物【尿素 (Urea)】是在何处由什么原料合成的？",
        "options": [
            {"letter": "A", "text_en": "In the kidneys, from excess dietary sugars.", "text_cn": "在肾脏中，由多余的糖分合成。"},
            {"letter": "B", "text_en": "In the liver, by deamination of excess amino acids.", "text_cn": "在肝脏中，由多余氨基酸经脱氨基作用（Deamination）转化合成。"},
            {"letter": "C", "text_en": "In the lungs, by breakdown of carbon dioxide.", "text_cn": "在肺中，由二氧化碳分解产生。"},
            {"letter": "D", "text_en": "In the small intestine, by bacteria during digestion.", "text_cn": "在小肠中，由细菌在消化过程中产生。"}
        ],
        "correct": "B",
        "concept_en": "Excess amino acids cannot be stored in the body. The LIVER removes their nitrogen-containing amino group (deamination), producing toxic ammonia, which is rapidly converted into less toxic UREA and transported by blood plasma to the kidneys.",
        "concept_cn": "多余氨基酸无法在体内储存。肝脏将其脱氨基转化为毒性较低的尿素（Urea），随后溶于血浆运抵肾脏排泄。",
        "trap_en": "The kidneys do NOT manufacture urea! The kidneys only FILTER and excrete urea made by the LIVER.",
        "trap_cn": "极高频考点陷阱：肾脏不制造尿素！肾脏只负责过滤排泄，制造尿素的生化器官是【肝脏】！",
        "citation": "《G8 Science》Chapter 4: B9.06 Urea & Deamination (p. 55)"
    },
    {
        "id": "rush_q20",
        "level": 2,
        "topic": "Glomerular Ultrafiltration",
        "prompt_en": "What physical force drives ultrafiltration in the glomerulus, and what is formed inside Bowman's capsule?",
        "prompt_cn": "什么物理驱动力促使肾小球进行超微滤过（Ultrafiltration）？在肾小囊内形成了什么液体？",
        "options": [
            {"letter": "A", "text_en": "Active transport pumps using ATP; finished concentrated urine is formed.", "text_cn": "利用 ATP 的主动运输泵；形成了终尿。"},
            {"letter": "B", "text_en": "High hydrostatic blood pressure generated by the heart and narrow efferent arteriole; glomerular filtrate is formed.", "text_cn": "由心脏搏动和出球小动脉相对较窄形成的高流体静水压；在肾小囊中形成了原尿（Glomerular filtrate）。"},
            {"letter": "C", "text_en": "Gravitational pull of urine inside the bladder.", "text_cn": "膀胱中尿液的重力下坠拉力。"},
            {"letter": "D", "text_en": "Negative air pressure from deep inhalation.", "text_cn": "深吸气时产生的胸腔负压。"}
        ],
        "correct": "B",
        "concept_en": "The afferent arteriole is wider than the efferent arteriole. This narrowing creates high hydrostatic pressure in the glomerular capillaries, forcing water and small solutes through the basement membrane into Bowman's capsule (glomerular filtrate).",
        "concept_cn": "入球小动脉较粗，出球小动脉较细，在肾小球微血管网形成极高流体静水压，挤压小分子物质滤入肾小囊形成原尿。",
        "trap_en": "Ultrafiltration does NOT require ATP from kidney cells; it is powered mechanically by blood pressure.",
        "trap_cn": "超滤本身不直接消耗肾小球细胞的 ATP，其物理动力源自血液循环系统的流体静水压。",
        "citation": "《G8 Science》Chapter 4: B9.06 Glomerular Filtration (pp. 55-56)"
    },
    {
        "id": "rush_q21",
        "level": 2,
        "topic": "Glomerular Filtration Barrier",
        "prompt_en": "Which components of blood are normally BLOCKED from entering the Bowman's capsule during ultrafiltration?",
        "prompt_cn": "在肾小球超滤过程中，血液中的哪些成分在正常生理状态下绝对被阻拦在毛细血管内？",
        "options": [
            {"letter": "A", "text_en": "Glucose and mineral ions.", "text_cn": "葡萄糖和无机盐离子。"},
            {"letter": "B", "text_en": "Water and urea.", "text_cn": "水分子和尿素。"},
            {"letter": "C", "text_en": "Red blood cells, white blood cells, platelets, and large plasma proteins (e.g. albumen).", "text_cn": "红细胞、白细胞、血小板以及大分子血浆蛋白（如白蛋白）。"},
            {"letter": "D", "text_en": "Amino acids and dissolved vitamins.", "text_cn": "氨基酸和水溶性维生素。"}
        ],
        "correct": "C",
        "concept_en": "The capillary endothelium and basement membrane act as a molecular sieve. Blood cells (~7 μm) and large proteins are far too large to pass through the microscopic pores and remain in the blood.",
        "concept_cn": "肾小球毛细血管内皮与基底膜构成微观分子筛。血细胞和大分子蛋白质体积过大，无法通过滤孔，完整留存于血液循环中。",
        "trap_en": "Finding blood cells or protein in urine indicates damage to the glomerulus (e.g. nephritis, physical trauma).",
        "trap_cn": "在尿检中一旦发现红细胞或蛋白尿，代表肾小球滤过屏障受到病理损伤或破损！",
        "citation": "《G8 Science》Chapter 4: B9.06 Filtration Barrier (p. 55)"
    },
    {
        "id": "rush_q22",
        "level": 2,
        "topic": "100% Glucose Reabsorption",
        "prompt_en": "What percentage of filtered glucose is reabsorbed along the proximal convoluted tubule in a healthy individual?",
        "prompt_cn": "在健康人体内，原尿中被滤出的葡萄糖在流经近曲小管时被重吸收的比例是多少？",
        "options": [
            {"letter": "A", "text_en": "0% (all glucose is excreted as waste).", "text_cn": "0%（所有葡萄糖都作为废物排出）。"},
            {"letter": "B", "text_en": "50% (half is stored, half is excreted).", "text_cn": "50%（一半储存，一半排出）。"},
            {"letter": "C", "text_en": "100% (all glucose is actively recovered back into the bloodstream).", "text_cn": "100%（全部葡萄糖通过主动运输被完整回收回血液）。"},
            {"letter": "D", "text_en": "90% (10% always remains to lubricate the ureter).", "text_cn": "90%（留存10%用以润滑输尿管）。"}
        ],
        "correct": "C",
        "concept_en": "Glucose is a valuable metabolic fuel. The kidney epithelial cells actively reabsorb 100% of filtered glucose in the proximal tubule. Normal finished urine contains ZERO glucose.",
        "concept_cn": "葡萄糖是宝贵的细胞能量底物。健康人体近曲小管将其 100% 重吸收回毛细血管网，因此终尿中葡萄糖含量为 0。",
        "trap_en": "Glucose in urine is an abnormal symptom of Diabetes Mellitus, where blood glucose exceeds the renal threshold.",
        "trap_cn": "尿中出现葡萄糖是糖尿病的特征性病理表现，说明血糖过高超过了肾小管载体蛋白的主动转运极限（肾糖阈）。",
        "citation": "《G8 Science》Chapter 4: B9.06 Reabsorption (pp. 55-56)"
    },
    {
        "id": "rush_q23",
        "level": 2,
        "topic": "Water Reabsorption Percentage",
        "prompt_en": "Out of approximately 180 litres of fluid filtered by human kidneys daily, how much water is reabsorbed back into the body?",
        "prompt_cn": "健康人体两侧肾脏每天滤过约 180 升原尿，其中约有多少水分被重新吸收回体内？",
        "options": [
            {"letter": "A", "text_en": "About 10% (we excrete 160 litres of urine daily).", "text_cn": "约 10%（每天排出 160 升尿液）。"},
            {"letter": "B", "text_en": "About 99% (we excrete approximately 1.5 litres of concentrated urine daily).", "text_cn": "约 99%（机体仅排出约 1.5 升浓缩终尿）。"},
            {"letter": "C", "text_en": "Exactly 50%.", "text_cn": "恰好 50%。"},
            {"letter": "D", "text_en": "0% (water cannot be reabsorbed by kidneys).", "text_cn": "0%（肾脏无法重吸收水分）。"}
        ],
        "correct": "B",
        "concept_en": "About 99% of filtered water is reabsorbed by osmosis along the Loop of Henle and collecting ducts, conserving bodily hydration and producing ~1.5 L of finished urine daily.",
        "concept_cn": "约 99% 的滤过水在髓袢和集合管通过渗透作用被重新吸收回血液，防止人体脱水，每日终尿排出量仅约 1.5 升。",
        "trap_en": "Without selective reabsorption, humans would dehydrate and die within hours from losing all body water.",
        "trap_cn": "若无肾小管的高比例重吸收，人体将在数小时内丧失全身水分而因严重脱水休克致死。",
        "citation": "《G8 Science》Chapter 25 Task 25.6 Reabsorption (pp. 72-74)"
    },
    {
        "id": "rush_q24",
        "level": 2,
        "topic": "Fluid Composition Analysis",
        "prompt_en": "Comparing Blood Plasma, Glomerular Filtrate, and Urine in a healthy student, which row is completely accurate?",
        "prompt_cn": "对比健康人体内的【血浆】、【肾小球原尿】与【终尿】，下列哪一组成分对照是完全准确的？",
        "options": [
            {"letter": "A", "text_en": "Protein: Present in plasma, absent in filtrate, absent in urine; Glucose: Present in plasma, present in filtrate, absent in urine.", "text_cn": "蛋白质：血浆中有，原尿中无，终尿中无；葡萄糖：血浆中有，原尿中有，终尿中无。"},
            {"letter": "B", "text_en": "Protein: Present in all three; Glucose: Present in all three.", "text_cn": "蛋白质：三者均有；葡萄糖：三者均有。"},
            {"letter": "C", "text_en": "Urea: Absent in plasma, present in filtrate, absent in urine.", "text_cn": "尿素：血浆中无，原尿中有，终尿中无。"},
            {"letter": "D", "text_en": "RBCs: Present in filtrate and urine.", "text_cn": "红细胞：存在于原尿和终尿中。"}
        ],
        "correct": "A",
        "concept_en": "Plasma has proteins, glucose, urea. Filtrate has glucose, urea, water (proteins blocked). Urine has concentrated urea, excess salts, water (100% glucose reabsorbed, proteins absent).",
        "concept_cn": "蛋白质在滤过膜被截留（仅血浆有）；葡萄糖被超滤进入原尿，但在肾小管 100% 被重吸收（终尿中为 0）；尿素在终尿中高度浓缩。",
        "trap_en": "Urea concentration is highest in finished urine (~2.0 g/100 mL) because ~99% of water has been removed.",
        "trap_cn": "尿素在终尿中的相对百分比浓度最高（约 2%），因为绝大部分水分被回收，使尿素大幅浓缩。",
        "citation": "《G8 Science》Chapter 4 Table B9.03 Fluid Comparison (p. 55)"
    },
    {
        "id": "rush_q25",
        "level": 2,
        "topic": "Dehydration Urine Profile",
        "prompt_en": "On a hot summer day when a student exercises heavily and sweats profusely without drinking water, what will their urine be like?",
        "prompt_cn": "在炎热夏日，一名学生剧烈运动并大量出汗且未及时补水，其排出的尿液会呈现何种特征？",
        "options": [
            {"letter": "A", "text_en": "Large volume, pale clear colour, low concentration.", "text_cn": "大容量、清澈透明淡色、低渗透压。"},
            {"letter": "B", "text_en": "Small volume, dark yellow colour, high urea and salt concentration.", "text_cn": "小容量、深黄色、高浓度尿素与无机盐。"},
            {"letter": "C", "text_en": "Zero urea and filled with pure glucose.", "text_cn": "零尿素，完全充满葡萄糖。"},
            {"letter": "D", "text_en": "Urine production stops permanently forever.", "text_cn": "尿液生成永久停止。"}
        ],
        "correct": "B",
        "concept_en": "Sweating causes loss of water and ions. The body detects low water potential, secretes ADH, causing the kidneys to reabsorb maximum water. Urine becomes small in volume and highly concentrated (dark yellow).",
        "concept_cn": "出汗导致水分大量流失，血浆渗透压上升，机体刺激肾脏最大化重吸收水分以保水，最终排出少量深黄色浓缩尿液。",
        "trap_en": "Dark urine indicates dehydration, as kidneys work hard to conserve body water.",
        "trap_cn": "尿液颜色深黄是脱水保水的典型指征，代表肾小管在全力回收水分维持血容量。",
        "citation": "《G8 Science》Chapter 24 Review Q1 & Section A Q22 (p. 136)"
    },
    {
        "id": "rush_q26",
        "level": 2,
        "topic": "Dialysis Machine Principle",
        "prompt_en": "Why does dialysis fluid (dialysate) in a kidney dialysis machine flow in the OPPOSITE direction to the patient's blood (counter-current exchange)?",
        "prompt_cn": "为什么血液透析机中的透析液流动方向要与患者血液流动方向相反（逆流交换机制）？",
        "options": [
            {"letter": "A", "text_en": "To maintain a steep concentration gradient for urea across the entire length of the dialysis membrane.", "text_cn": "为了在整条透析膜管全程维持陡峭的尿素浓度梯度，实现最高效扩散清除。"},
            {"letter": "B", "text_en": "To freeze the blood so bacteria cannot reproduce.", "text_cn": "为了冻结血液防止细菌繁殖。"},
            {"letter": "C", "text_en": "To pump patient red blood cells into the dialysate fluid.", "text_cn": "为了将患者的红细胞抽入透析液中。"},
            {"letter": "D", "text_en": "To avoid electrical shocks from the machine pump.", "text_cn": "为了避免机器产生静电。"}
        ],
        "correct": "A",
        "concept_en": "Counter-current exchange ensures that blood always encounters fresher dialysate with lower urea concentration, maintaining a continuous diffusion gradient along the entire pathway.",
        "concept_cn": "逆流交换使含有尿素的血液全程都能接触到浓度更低的透析液，防止达到局部平衡，最大化清除尿素。",
        "trap_en": "Concurrent (same direction) flow would quickly reach 50% equilibrium, halting further diffusion halfway through.",
        "trap_cn": "若同向流动，很快就会达到 50% 平衡导致扩散停滞；逆流设计能将尿素清除率提高数倍。",
        "citation": "《G8 Science》Chapter 4: B9.06 Kidney Dialysis (pp. 56-57)"
    },
    {
        "id": "rush_q27",
        "level": 2,
        "topic": "Dialysis Fluid Composition",
        "prompt_en": "Why must kidney dialysis fluid contain the SAME concentration of glucose and mineral ions as normal blood plasma?",
        "prompt_cn": "为什么透析机中的透析液必须配制与正常血浆完全相同浓度的葡萄糖和无机盐离子？",
        "options": [
            {"letter": "A", "text_en": "To prevent essential glucose and ions from diffusing out of the patient's blood into the dialysis fluid.", "text_cn": "为了防止患者血液中宝贵的葡萄糖和必需离子因浓度差扩散流失到透析液中。"},
            {"letter": "B", "text_en": "To destroy patient white blood cells.", "text_cn": "为了消灭患者的白细胞。"},
            {"letter": "C", "text_en": "To turn the patient's blood colour blue.", "text_cn": "为了使血液变成蓝色。"},
            {"letter": "D", "text_en": "To force all glucose into the kidneys.", "text_cn": "为了迫使葡萄糖进入肾脏。"}
        ],
        "correct": "A",
        "concept_en": "Equal glucose/ion concentration (isotonic) means net diffusion rate is ZERO for valuable nutrients, preventing hypoglycaemia, while zero urea in fluid ensures maximum urea removal.",
        "concept_cn": "透析液与血浆葡萄糖/无机盐等浓度可确保净扩散为 0，防止患者营养底物流失；而透析液中尿素为 0，确保代谢废物完全排出。",
        "trap_en": "If dialysate contained pure water, all glucose and ions would rapidly diffuse out, and red blood cells would burst (lysis).",
        "trap_cn": "若透析液为纯水，患者血液中的葡萄糖和离子将瞬间流失殆尽，红细胞也会因渗透吸水而破裂致死。",
        "citation": "《G8 Science》Chapter 4: B9.06 Dialysis Fluid (p. 56)"
    },
    {
        "id": "rush_q28",
        "level": 2,
        "topic": "Excretory Functions of Skin",
        "prompt_en": "Which three substances are excreted from human body via sweat glands in the skin?",
        "prompt_cn": "人体皮肤汗腺排出的汗液中主要包含哪三种排泄物与生理成分？",
        "options": [
            {"letter": "A", "text_en": "Water, urea, and mineral salts (e.g. sodium chloride).", "text_cn": "水、尿素以及无机盐（如氯化钠）。"},
            {"letter": "B", "text_en": "Glucose, proteins, and bile pigments.", "text_cn": "葡萄糖、蛋白质与胆汁色素。"},
            {"letter": "C", "text_en": "Carbon dioxide, red blood cells, and starch.", "text_cn": "二氧化碳、红细胞与淀粉。"},
            {"letter": "D", "text_en": "Hormones, enzymes, and digestive fibre.", "text_cn": "激素、酶与膳食纤维。"}
        ],
        "correct": "A",
        "concept_en": "Sweat glands secrete sweat containing water, urea, and sodium chloride. Although sweating primarily serves thermoregulation (cooling via evaporation), it also acts as an excretory organ.",
        "concept_cn": "汗腺分泌的汗液包含水分、尿素和无机盐（NaCl）。出汗主要用于体温调节（蒸发散热），兼具部分排泄辅助功能。",
        "trap_en": "Healthy sweat does NOT contain glucose or proteins!",
        "trap_cn": "健康人的汗液中绝不包含葡萄糖或蛋白质等大分子营养物质。",
        "citation": "《G8 Science》Chapter 30 Part 1 Q1 & Chapter 4: B9.07 (p. 57)"
    },
    {
        "id": "rush_q29",
        "level": 2,
        "topic": "Kidney Blood Supply",
        "prompt_en": "Which blood vessel delivers unfiltered, oxygenated blood under high pressure to the kidneys?",
        "prompt_cn": "哪一根血管负责向肾脏输送高压、未过滤的富氧血液？",
        "options": [
            {"letter": "A", "text_en": "Renal vein (肾静脉)", "text_cn": "Renal vein (肾静脉)"},
            {"letter": "B", "text_en": "Renal artery (肾动脉)", "text_cn": "Renal artery (肾动脉)"},
            {"letter": "C", "text_en": "Pulmonary artery (肺动脉)", "text_cn": "Pulmonary artery (肺动脉)"},
            {"letter": "D", "text_en": "Hepatic portal vein (肝门静脉)", "text_cn": "Hepatic portal vein (肝门静脉)"}
        ],
        "correct": "B",
        "concept_en": "The RENAL ARTERY branches directly from the aorta, carrying oxygenated blood loaded with urea and metabolic waste to the kidneys for filtration.",
        "concept_cn": "肾动脉（Renal artery）直接分支自主动脉，运载富含氧气和尿素代谢废物的血液进入肾脏进行超微滤过。",
        "trap_en": "Renal VEIN carries clean (filtered), deoxygenated blood away from the kidneys back towards the vena cava.",
        "trap_cn": "肾静脉（Renal vein）运出的是已完成过滤（尿素浓度极低）的静脉脱氧血。",
        "citation": "《G8 Science》Chapter 13.02 Gross Renal Anatomy (p. 142)"
    },
    {
        "id": "rush_q30",
        "level": 2,
        "topic": "Ureter vs Urethra Distinction",
        "prompt_en": "A student confuses 'ureter' and 'urethra'. What is the exact anatomical difference?",
        "prompt_cn": "学生极易混淆‘输尿管 (ureter)’与‘尿道 (urethra)’。它们的精准解剖学区别是什么？",
        "options": [
            {"letter": "A", "text_en": "There are TWO ureters connecting kidneys to bladder; there is ONE urethra leading from bladder to the outside of the body.", "text_cn": "人体有两根输尿管（Ureters）连接肾脏与膀胱；只有一根尿道（Urethra）连接膀胱向体外排尿。"},
            {"letter": "B", "text_en": "The urethra connects the mouth to the stomach.", "text_cn": "尿道连接口腔与胃。"},
            {"letter": "C", "text_en": "Ureters are found only in birds, whereas urethra is found only in fish.", "text_cn": "输尿管只有鸟类才有，尿道只有鱼类才有。"},
            {"letter": "D", "text_en": "The urethra produces blood cells, while ureter filters glucose.", "text_cn": "尿道制造血细胞，输尿管过滤葡萄糖。"}
        ],
        "correct": "A",
        "concept_en": "Mnemonic: Uret-ER has 2 tubes (one from EACH kidney) and lies upstream. Urethra is the single terminal duct discharging urine outside.",
        "concept_cn": "输尿管（Ureter）为成对的双管，连接双肾至膀胱；尿道（Urethra）为单管，位于最下端连通体外。",
        "trap_en": "Spelling trap: Ureter vs Urethra. Notice 'th' in urethra as the single terminal 'threshold' exit.",
        "trap_cn": "拼写陷阱：Ureter（输尿管）在上，Urethra（尿道）在下，绝不可倒置拼写。",
        "citation": "《G8 Science》Section B Q9 & Lecture Notes (p. 54)"
    },
    {
        "id": "rush_q31",
        "level": 2,
        "topic": "True/False: Glucose in Healthy Urine",
        "prompt_en": "[True / False] Healthy human urine naturally contains a small concentration of glucose to provide energy for bladder bacteria.",
        "prompt_cn": "【正误判断】健康人尿液中天然含有少量葡萄糖，用以供给膀胱共生细菌营养能量。",
        "options": [
            {"letter": "A", "text_en": "FALSE (错误，健康人尿液中葡萄糖浓度严格为 0%)", "text_cn": "FALSE (错误，健康人尿液中葡萄糖浓度严格为 0%)"},
            {"letter": "B", "text_en": "TRUE (正确，正常尿液含有1%葡萄糖)", "text_cn": "TRUE (正确，正常尿液含有1%葡萄糖)"}
        ],
        "correct": "A",
        "concept_en": "FALSE! In healthy individuals, 100% of filtered glucose is reabsorbed. Glucose in urine (glycosuria) indicates that blood glucose has exceeded the renal threshold (>10 mmol/L), characteristic of diabetes.",
        "concept_cn": "完全错误！健康人尿中葡萄糖含量为 0。只有在糖尿病等病理状态下，血糖超过肾糖阈，才会出现糖尿。",
        "trap_en": "Any detectable glucose in urine is considered abnormal in clinical medicine.",
        "trap_cn": "临床尿常规检测中，一旦检出微量葡萄糖（斐林/本尼迪特试剂阳性），即提示病理异常。",
        "citation": "《G8 Science》Chapter 14.06 Clinical Diabetes (pp. 164-165)"
    },
    {
        "id": "rush_q32",
        "level": 2,
        "topic": "Nephron Functional Unit",
        "prompt_en": "What is the microscopic, functional filtering and processing unit of the human kidney called, and approximately how many exist per kidney?",
        "prompt_cn": "人类肾脏中执行过滤与尿液生成的微观结构与功能基本单位称为什么？每个肾脏约含有多少个？",
        "options": [
            {"letter": "A", "text_en": "Nephron (肾单位), approximately 1 million per kidney.", "text_cn": "Nephron (肾单位)，每个肾脏约含有 100 万个。"},
            {"letter": "B", "text_en": "Neuron (神经元), approximately 10 per kidney.", "text_cn": "Neuron (神经元)，每个肾脏约 10 个。"},
            {"letter": "C", "text_en": "Alveolus (肺泡), approximately 50 per kidney.", "text_cn": "Alveolus (肺泡)，每个肾脏约 50 个。"},
            {"letter": "D", "text_en": "Villus (小肠绒毛), approximately 5 million per kidney.", "text_cn": "Villus (小肠绒毛)，每个肾脏约 500 万个。"}
        ],
        "correct": "A",
        "concept_en": "Each human kidney contains roughly 1 to 1.25 million microscopic NEPHRONS, each comprising a glomerulus, Bowman's capsule, proximal tubule, Loop of Henle, distal tubule, and collecting duct.",
        "concept_cn": "每个肾脏包含约 100 万个微观【肾单位 (Nephron)】，由肾小体（肾小球与肾小囊）和肾小管系统构成。",
        "trap_en": "Do not confuse NEPHRON (kidney unit) with NEURON (nerve cell)!",
        "trap_cn": "不要混淆 Nephron（肾单位）与 Neuron（神经元）！拼写仅差一个字母，功能完全不同。",
        "citation": "《G8 Science》Chapter 4: B9.06 Nephron Anatomy (p. 54)"
    },

    # ========== LEVEL 3: BLOOD GLUCOSE REGULATION & HOMEOSTASIS (Q33 - Q48) ==========
    {
        "id": "rush_q33",
        "level": 3,
        "topic": "Homeostasis Definition",
        "prompt_en": "What is the biological definition of HOMEOSTASIS?",
        "prompt_cn": "生物学中【稳态 (Homeostasis)】的标准科学定义是什么？",
        "options": [
            {"letter": "A", "text_en": "The continuous growth of bones and muscle mass during childhood.", "text_cn": "儿童期骨骼和肌肉质量的持续增长。"},
            {"letter": "B", "text_en": "The maintenance of a relatively constant internal body environment despite fluctuations in external conditions.", "text_cn": "尽管外界环境剧烈波动，机体仍维持体内内环境相对恒定稳定的生理机制。"},
            {"letter": "C", "text_en": "The total cessation of heart beats during sleep.", "text_cn": "睡眠时心跳的完全暂停。"},
            {"letter": "D", "text_en": "The ability to run at constant speed forever.", "text_cn": "以恒定速度永久奔跑的能力。"}
        ],
        "correct": "B",
        "concept_en": "Homeostasis (from Greek 'similar standing') is the regulation of physiological internal conditions (body temperature 37°C, blood glucose 5.0 mmol/L, water potential, pH 7.4) within narrow limits.",
        "concept_cn": "稳态是指机体在外部变化时，通过自我调节将内部理化环境（体温、血糖、水盐平衡、酸碱度）维系在狭窄动态平衡范围的机制。",
        "trap_en": "Homeostasis does not mean internal variables never change; it means they oscillate closely around a specific SET POINT.",
        "trap_cn": "稳态并不意味着体内数值绝对静止不变，而是始终围绕一个“设定基准值 (Set point)”动态波动调整。",
        "citation": "《G8 Science》Chapter 4: B9.06 Homeostasis (p. 54)"
    },
    {
        "id": "rush_q34",
        "level": 3,
        "topic": "Negative Feedback Mechanism",
        "prompt_en": "How does a NEGATIVE FEEDBACK loop operate in physiological homeostasis?",
        "prompt_cn": "负反馈调节回路（Negative Feedback Loop）在生理稳态中是如何运作的？",
        "options": [
            {"letter": "A", "text_en": "A change in a variable triggers responses that AMPLIFY the change in the same direction, causing explosion.", "text_cn": "某一变量的改变触发使其沿相同方向无限放大的效应，引起系统崩溃。"},
            {"letter": "B", "text_en": "A deviation from the normal set point is detected by a receptor, triggering a corrective response that acts in the OPPOSITE direction to restore the variable to the set point.", "text_cn": "偏离正常设定基准值的改变被感受器检测到，触发沿【相反方向】发生纠正动作，将变量拉回正常设定基准值。"},
            {"letter": "C", "text_en": "It permanently shuts down the nervous system after every meal.", "text_cn": "每餐后永久切断神经系统。"},
            {"letter": "D", "text_en": "It stimulates body cells to burn out all metabolic fuel immediately.", "text_cn": "刺激体细胞立即耗尽所有代谢燃料。"}
        ],
        "correct": "B",
        "concept_en": "Negative feedback is an error-correcting control loop: Stimulus $\\to$ Receptor $\\to$ Control Centre $\\to$ Effector $\\to$ Corrective Action in OPPOSITE direction $\\to$ Return to Set Point.",
        "concept_cn": "负反馈是闭环自我纠错机制：刺激 $\\to$ 感受器 $\\to$ 中枢 $\\to$ 效应器 $\\to$ 相反方向纠正动作 $\\to$ 回归设定基准值。",
        "trap_en": "'Negative' means reversing/negating the change, NOT that the process is harmful!",
        "trap_cn": "“负”反馈的含义是逆转抵消偏离方向（恢复原状），绝不是指该机制对身体有害！",
        "citation": "《G8 Science》Chapter 4: B9.08 Negative Feedback (pp. 59-60)"
    },
    {
        "id": "rush_q35",
        "level": 3,
        "topic": "High Blood Glucose & Insulin",
        "prompt_en": "After eating a bowl of pasta, blood glucose rises above the 5.0 mmol/L set point. Which sequence restores normal blood glucose levels?",
        "prompt_cn": "进食一碗意面后，血糖升至正常设定值（5.0 mmol/L）之上。下列哪一生理调节通路能使血糖恢复正常？",
        "options": [
            {"letter": "A", "text_en": "Liver secretes glucagon $\\to$ pancreas converts glycogen into glucose.", "text_cn": "肝脏分泌胰高血糖素 $\\to$ 胰腺将糖原分解为葡萄糖。"},
            {"letter": "B", "text_en": "Pancreas detects high glucose and secretes INSULIN $\\to$ stimulates liver and muscle cells to absorb glucose and convert it into insoluble GLYCOGEN.", "text_cn": "胰腺感应到高血糖并分泌**胰岛素（Insulin）** $\\to$ 促使肝脏和肌肉细胞加速摄取葡萄糖，并将其聚合为不溶性**糖原（Glycogen）**储存。"},
            {"letter": "C", "text_en": "Kidneys filter all glucose directly into urine to reduce blood volume.", "text_cn": "肾脏将全部葡萄糖直接排入尿液以减少血容量。"},
            {"letter": "D", "text_en": "Pancreas secretes insulin to break down glycogen into glucose.", "text_cn": "胰腺分泌胰岛素将体内的糖原分解为葡萄糖。"}
        ],
        "correct": "B",
        "concept_en": "High glucose $\\to$ Pancreatic $\\beta$-cells secrete INSULIN $\\to$ Liver & Muscle cells take up glucose and convert it into GLYCOGEN (glycogenesis) $\\to$ Blood glucose falls to normal set point.",
        "concept_cn": "高血糖刺激胰岛分泌胰岛素 $\\to$ 作用于靶器官肝脏与肌肉 $\\to$ 促进摄取葡萄糖并合成糖原储存（葡萄糖 $\\to$ 糖原） $\\to$ 血糖回落正常。",
        "trap_en": "Pancreas is the gland that secretes the hormone; Liver is the target organ that stores glycogen. Insulin converts Glucose INTO Glycogen, never the reverse!",
        "trap_cn": "胰腺是分泌器官；肝脏是靶器官。胰岛素的作用是将可溶葡萄糖合成转化为糖原储存，绝非分解糖原。",
        "citation": "《G8 Science》Chapter 14.02 High Blood Glucose & Insulin (pp. 156-157)"
    },
    {
        "id": "rush_q36",
        "level": 3,
        "topic": "Low Blood Glucose & Glucagon",
        "prompt_en": "During a 10 km cross-country run, blood glucose drops below the set point. How does the body respond to prevent hypoglycaemia?",
        "prompt_cn": "在 10 公里长跑中，血液中葡萄糖浓度跌落至基准值以下。机体如何应对以防发生低血糖昏迷？",
        "options": [
            {"letter": "A", "text_en": "Pancreas secretes insulin to convert glucose into fat.", "text_cn": "胰腺分泌胰岛素将葡萄糖转化为脂肪。"},
            {"letter": "B", "text_en": "Pancreas detects low glucose and secretes GLUCAGON $\\to$ stimulates liver cells to break down stored GLYCOGEN into GLUCOSE and release it into the bloodstream.", "text_cn": "胰腺感应到低血糖并分泌**胰高血糖素（Glucagon）** $\\to$ 促使肝细胞将储备的**糖原（Glycogen）**分解为**葡萄糖（Glucose）**释放入血。"},
            {"letter": "C", "text_en": "Stomach releases digestive amylase directly into circulatory vessels.", "text_cn": "胃向血液循环管路中直接分泌消化性淀粉酶。"},
            {"letter": "D", "text_en": "Red blood cells release their stored hemoglobin as an alternative carbohydrate.", "text_cn": "红细胞释放其储备的血红蛋白作为替代碳水化合物。"}
        ],
        "correct": "B",
        "concept_en": "Low glucose $\\to$ Pancreatic $\\alpha$-cells secrete GLUCAGON $\\to$ Liver cells break down stored glycogen into glucose (glycogenolysis) $\\to$ Glucose diffuses into blood $\\to$ Blood glucose rises to set point.",
        "concept_cn": "低血糖刺激胰岛分泌胰高血糖素 $\\to$ 作用于肝脏靶细胞 $\\to$ 催化肝糖原分解为葡萄糖并释放入血（糖原 $\\to$ 葡萄糖） $\\to$ 血糖上升回归平衡。",
        "trap_en": "Mnemonic: 'When glucose is GONE, release GLUCAGON!'. Glucagon is the hormone; Glycogen is the stored carbohydrate in the liver.",
        "trap_cn": "英语速记谐音：“Glucose is gone, so release Glucagon!”。胰高血糖素促进糖原分解释放葡萄糖。",
        "citation": "《G8 Science》Chapter 14.03 Low Blood Glucose & Glucagon (pp. 158-159)"
    },
    {
        "id": "rush_q37",
        "level": 3,
        "topic": "3G Terminology Disambiguation",
        "prompt_en": "Which statement correctly pairs the 'Three Gs' of glucose regulation with their precise biochemical identities?",
        "prompt_cn": "下列关于血糖调节中‘三个 G 打头核心术语’的生化本质对照，哪一项是完全正确的？",
        "options": [
            {"letter": "A", "text_en": "Glucose = Storage starch in muscles; Glycogen = Pancreatic hormone; Glucagon = Blood sugar.", "text_cn": "Glucose = 肌肉中的淀粉；Glycogen = 胰腺激素；Glucagon = 血糖。"},
            {"letter": "B", "text_en": "Glucose = Soluble monosaccharide sugar in blood; Glycogen = Insoluble storage polysaccharide in liver; Glucagon = Peptide hormone secreted by pancreas that raises blood sugar.", "text_cn": "Glucose（葡萄糖）= 血液中游离的可溶性单糖；Glycogen（糖原）= 储存于肝脏和肌肉中的不溶性储能多糖；Glucagon（胰高血糖素）= 胰腺分泌的升高血糖的肽类激素。"},
            {"letter": "C", "text_en": "All three words mean the exact same molecule.", "text_cn": "这三个词在生物化学中代表完全相同的单一分子。"},
            {"letter": "D", "text_en": "Glucagon is an enzyme that digests proteins in the stomach.", "text_cn": "Glucagon 是胃部分解蛋白质的消化酶。"}
        ],
        "correct": "B",
        "concept_en": "1. Glucose: simple monosaccharide (C6H12O6); 2. Glycogen: complex polymer of glucose stored in liver/muscles; 3. Glucagon: endocrine hormone from pancreas that signals glycogen breakdown.",
        "concept_cn": "Glucose（葡萄糖，单糖能源）；Glycogen（糖原，动物淀粉储备）；Glucagon（胰高血糖素，升糖激素信使）。",
        "trap_en": "The single most common spelling and conceptual error in Cambridge IGCSE biology! Double check spellings: -ose vs -ogen vs -agon.",
        "trap_cn": "剑桥 IGCSE 考试最高频混淆点：词尾辨析 -ose（糖类分子）、-ogen（前体或多糖原）、-agon（激素信使）！",
        "citation": "《G8 Science》Chapter 14.04 The 3 Gs (p. 160)"
    },
    {
        "id": "rush_q38",
        "level": 3,
        "topic": "Type 1 vs Type 2 Diabetes",
        "prompt_en": "Which statement accurately contrasts Type 1 and Type 2 diabetes mellitus?",
        "prompt_cn": "下列关于 1 型糖尿病与 2 型糖尿病的对照阐述，哪一项是准确无误的？",
        "options": [
            {"letter": "A", "text_en": "Type 1 is caused by cell receptor insensitivity; Type 2 is an autoimmune destruction of pancreatic beta cells.", "text_cn": "1 型由细胞受体不敏感引起；2 型是自身免疫破坏胰岛细胞。"},
            {"letter": "B", "text_en": "Type 1 results from the pancreas failing to produce sufficient insulin (autoimmune destruction); Type 2 results from target cells becoming resistant/insensitive to insulin receptors (linked to diet and obesity).", "text_cn": "1 型由自身免疫攻击胰岛导致胰腺无法分泌胰岛素所致；2 型由靶细胞膜受体对胰岛素产生抵抗/不敏感所致（与高糖饮食肥胖紧密相关）。"},
            {"letter": "C", "text_en": "Both types are cured by taking oral sugar tablets before bed.", "text_cn": "两种类型的糖尿病都可以通过睡前服用口服糖片彻底治愈。"},
            {"letter": "D", "text_en": "Type 1 never requires insulin injections, whereas Type 2 always requires bone marrow surgery.", "text_cn": "1 型从不需要注射胰岛素，而 2 型必须进行骨髓手术。"}
        ],
        "correct": "B",
        "concept_en": "Type 1 Diabetes: Autoimmune destruction of pancreatic $\\beta$-cells $\\to$ zero insulin $\\to$ daily insulin injections. Type 2 Diabetes: Target cells insulin resistant, linked to obesity $\\to$ diet, exercise, and oral drugs.",
        "concept_cn": "1型糖尿病：自身免疫破坏胰岛 $\\beta$ 细胞，无法合成胰岛素，必须每日注射胰岛素。2型糖尿病：靶细胞受体产生胰岛素抵抗，通过控糖运动与口服药治疗。",
        "trap_en": "Injecting insulin into a typical Type 2 diabetic does not directly solve the root cause, which is receptor resistance, not hormone absence.",
        "trap_cn": "2型糖尿病的主要矛盾不是缺乏胰岛素，而是细胞“听不见”胰岛素信号（胰岛素受体抵抗）。",
        "citation": "《G8 Science》Chapter 14.05 Diabetes Mellitus (pp. 161-163)"
    },
    {
        "id": "rush_q39",
        "level": 3,
        "topic": "Glycosuria & Renal Threshold",
        "prompt_en": "Why does glucose appear in the urine of an uncontrolled diabetic patient (glycosuria)?",
        "prompt_cn": "为什么在未接受治疗的严重糖尿病患者尿液中会出现葡萄糖（糖尿现象）？",
        "options": [
            {"letter": "A", "text_en": "Glomerular capillaries become impermeable to all glucose molecules.", "text_cn": "肾小球毛细血管对所有葡萄糖分子完全变得不透。"},
            {"letter": "B", "text_en": "The excessively high blood glucose concentration causes filtered glucose to exceed the maximum active transport reabsorption capacity of the kidney tubules (renal threshold).", "text_cn": "血液中过高的葡萄糖浓度导致滤过的葡萄糖总量超过了肾小管主动运输重吸收的最大转运极限（肾糖阈），多余葡萄糖随尿排出。"},
            {"letter": "C", "text_en": "The urinary bladder starts synthesizing its own glucose from urine urea.", "text_cn": "膀胱本身开始利用尿液中的尿素自主合成新的葡萄糖。"},
            {"letter": "D", "text_en": "Insulin binds directly to urine proteins, precipitating them out as glucose crystals.", "text_cn": "胰岛素直接结合尿液蛋白，使其沉淀析出为葡萄糖晶体。"}
        ],
        "correct": "B",
        "concept_en": "In diabetics, blood glucose exceeds the renal threshold (~10-12 mmol/L). Glomerulus filters vast amounts of glucose. Carrier proteins in the proximal tubule become saturated (Vmax reached), and excess unabsorbed glucose is excreted in urine.",
        "concept_cn": "高血糖导致超滤出的葡萄糖总量大幅超过近曲小管载体蛋白的主动转运极限（肾糖阈）。载体饱和后，多余无法被重吸收的葡萄糖滞留于原尿中最终排出（糖尿）。",
        "trap_en": "The kidney tubules are NOT damaged here! They are simply overwhelmed because the glucose concentration is abnormally excessive.",
        "trap_cn": "并非肾脏本身受损，而是进入肾单位的原尿葡萄糖泛滥，超过了载体蛋白的生理负荷上限。可用本尼迪特试剂检测（蓝 $\\to$ 砖红沉淀）。",
        "citation": "《G8 Science》Chapter 14.06 Clinical Diabetes & Kidneys (pp. 164-165)"
    },
    {
        "id": "rush_q40",
        "level": 3,
        "topic": "Hormone Biological Definition",
        "prompt_en": "What is the biological definition of a HORMONE?",
        "prompt_cn": "在人体生理学中，【激素 / 荷尔蒙 (Hormone)】的标准生物学定义是什么？",
        "options": [
            {"letter": "A", "text_en": "A chemical substance produced by a gland and carried by the blood, which alters the activity of one or more specific target organs.", "text_cn": "由内分泌腺体产生并由血液运载的化学信使物质，能特异性改变一个或多个特定靶器官的代谢生理活动。"},
            {"letter": "B", "text_en": "An electrical impulse traveling down motor neurons.", "text_cn": "沿运动神经元传导的生物电脉冲。"},
            {"letter": "C", "text_en": "An enzyme secreted into the small intestine to digest fats.", "text_cn": "分泌到小肠中用以消化脂肪的消化酶。"},
            {"letter": "D", "text_en": "A mineral salt dissolved in saliva to kill bacteria.", "text_cn": "溶解在唾液中用以杀菌的无机盐。"}
        ],
        "correct": "A",
        "concept_en": "Hormones are chemical messengers synthesized by ductless endocrine glands, secreted directly into blood capillaries, and carried by plasma to specific target cells possessing complementary receptors.",
        "concept_cn": "激素是由无管内分泌腺合成并直接释放入血液的化学信使，随血浆循环到达表面具备特异性互补受体的靶器官发挥调控作用。",
        "trap_en": "Hormones travel in blood everywhere, but ONLY affect target cells with specific matching receptors.",
        "trap_cn": "激素随血液流遍全身，但只有具有互补受体蛋白的靶细胞才能感应并做出反应（锁钥配对）。",
        "citation": "《G8 Science》Chapter 4: B9.04 Hormones (pp. 54-55)"
    },
    {
        "id": "rush_q41",
        "level": 3,
        "topic": "Endocrine Gland Architecture",
        "prompt_en": "Why are endocrine glands (like the pancreas, thyroid, and adrenals) called 'ductless glands'?",
        "prompt_cn": "为什么内分泌腺（如胰岛、甲状腺、肾上腺）在解剖学上被称为‘无导管腺体 (ductless glands)’？",
        "options": [
            {"letter": "A", "text_en": "Because they have no tubes; they secrete their hormones directly into the interstitial fluid and surrounding blood capillaries.", "text_cn": "因为它们没有外输导管；它们将分泌的激素直接排入组织间隙液并渗入周围毛细血管血液中。"},
            {"letter": "B", "text_en": "Because they are completely invisible to the human eye.", "text_cn": "因为它们肉眼完全不可见。"},
            {"letter": "C", "text_en": "Because they only release secretions into the stomach lumen.", "text_cn": "因为它们只向胃腔中分泌物质。"},
            {"letter": "D", "text_en": "Because they are made entirely of dead connective bone tissue.", "text_cn": "因为它们完全由死亡的骨结缔组织构成。"}
        ],
        "correct": "A",
        "concept_en": "Exocrine glands (sweat glands, salivary glands, tear glands) possess ducts to deliver secretions to a specific surface. Endocrine glands have NO ducts; their secretions diffuse directly into the bloodstream.",
        "concept_cn": "外分泌腺（汗腺、唾液腺）有专门导管输送分泌物至体表或体腔；内分泌腺没有导管，激素直接渗透进入毛细血管循环。",
        "trap_en": "The pancreas is a dual gland: exocrine (pancreatic duct to duodenum) AND endocrine (Islets of Langerhans directly into blood).",
        "trap_cn": "胰腺是兼具双重功能的腺体：外分泌部分泌消化酶入胰管；内分泌部分泌胰岛素和胰高血糖素入血液！",
        "citation": "《G8 Science》Chapter 4: B9.04 Endocrine Glands (pp. 54-55)"
    },
    {
        "id": "rush_q42",
        "level": 3,
        "topic": "Adrenaline vs Glucagon",
        "prompt_en": "Both adrenaline and glucagon increase blood glucose levels. What is the fundamental difference in their physiological roles?",
        "prompt_cn": "肾上腺素（Adrenaline）与胰高血糖素（Glucagon）都能升高血糖。它们在生理职责上的根本区别是什么？",
        "options": [
            {"letter": "A", "text_en": "Glucagon is for routine homeostatic regulation; Adrenaline is secreted by adrenal glands in emergency 'fight-or-flight' stress situations.", "text_cn": "胰高血糖素负责日常基础稳态调节；肾上腺素则由肾上腺在生死攸关的应激/恐惧/战斗或逃跑（Fight-or-Flight）状态下紧急分泌。"},
            {"letter": "B", "text_en": "Adrenaline decreases heart rate, while glucagon increases eye blinking.", "text_cn": "肾上腺素降低心率，而胰高血糖素增加眨眼频率。"},
            {"letter": "C", "text_en": "Adrenaline is produced in the feet bones.", "text_cn": "肾上腺素产生于足部骨骼。"},
            {"letter": "D", "text_en": "Glucagon converts glucose into poisonous acid.", "text_cn": "胰高血糖素将葡萄糖转化为有毒酸。"}
        ],
        "correct": "A",
        "concept_en": "Glucagon maintains resting glucose baseline between meals. Adrenaline is released under acute emotional or physical threat, massively boosting heart rate, breathing rate, pupil dilation, and glycogen breakdown for immediate muscular action.",
        "concept_cn": "胰高血糖素维持空腹日常血糖基准；肾上腺素在遇险应激时爆发式分泌，大幅提高心率、呼吸和血糖，为骨骼肌战斗或逃跑提供充沛能量。",
        "trap_en": "Adrenaline acts rapidly in seconds; glucagon operates quietly in negative feedback.",
        "trap_cn": "肾上腺素启动极其迅速（数秒内），伴随瞳孔散大与心跳加速，属于应急神经内分泌反应。",
        "citation": "《G8 Science》Chapter 27 Task 27.2 Adrenaline & Homeostasis (pp. 85-88)"
    },
    {
        "id": "rush_q43",
        "level": 3,
        "topic": "Comparison: Nervous vs Endocrine",
        "prompt_en": "Comparing the nervous system and the endocrine system, which pair of characteristics is correct?",
        "prompt_cn": "对比神经调节与内分泌（激素）调节，下列哪一组生理特征是准确的？",
        "options": [
            {"letter": "A", "text_en": "Nervous: Extremely rapid response (milliseconds), brief duration; Endocrine: Slower response (seconds/minutes), long-lasting sustained effect.", "text_cn": "神经调节：反应极快（毫秒级电信号）、效应持续短暂；内分泌调节：反应相对较慢（需随血液运输）、效应持久深远。"},
            {"letter": "B", "text_en": "Nervous: Uses blood vessels; Endocrine: Uses electrical wires.", "text_cn": "神经：使用血管；内分泌：使用电线。"},
            {"letter": "C", "text_en": "Both have identical transmission speeds of 100 meters per millisecond.", "text_cn": "两者的传导速度完全相同。"},
            {"letter": "D", "text_en": "Nervous effects last for several months.", "text_cn": "神经冲动的生理效应可持续数月之久。"}
        ],
        "correct": "A",
        "concept_en": "Nervous system: electrical impulses along neurons $\\to$ ultra-fast $\\to$ localized and short-lived. Endocrine system: chemical hormones in blood $\\to$ slower transit $\\to$ widespread and sustained.",
        "concept_cn": "神经系统以神经电冲动沿轴突传导，毫秒级生效，冲动停止即终止；内分泌系统以激素随血液运输，起效较慢但调控持久广泛。",
        "trap_en": "Classic 4-mark Cambridge exam question! Remember: Speed (Fast vs Slower) and Duration (Short vs Long-lasting).",
        "trap_cn": "经典 4 分大题考点：从【反应速度】（快 vs 慢）和【持续时间】（短暂 vs 持久）两个维度精准对比！",
        "citation": "《G8 Science》Section B Q10 & Lesson 26 (p. 76)"
    },
    {
        "id": "rush_q44",
        "level": 3,
        "topic": "Adrenal Gland Location",
        "prompt_en": "Where in the human body are the adrenal glands located?",
        "prompt_cn": "在人体解剖学中，肾上腺（Adrenal glands）位于身体的什么确切位置？",
        "options": [
            {"letter": "A", "text_en": "Sitting like small caps directly on top of each kidney.", "text_cn": "像小帽子一样直接骑跨在两侧肾脏的顶端上方。"},
            {"letter": "B", "text_en": "Inside the eyeballs behind the retina.", "text_cn": "位于眼球内部视网膜后方。"},
            {"letter": "C", "text_en": "Floating freely inside the stomach acid.", "text_cn": "在胃酸中自由漂浮。"},
            {"letter": "D", "text_en": "Embedded inside the heel bone of the feet.", "text_cn": "嵌在足部脚后跟骨骼内部。"}
        ],
        "correct": "A",
        "concept_en": "The two adrenal glands sit atop the superior poles of the kidneys (ad-renal = 'near the renal/kidneys'). They consist of an outer cortex (steroids) and inner medulla (adrenaline/noradrenaline).",
        "concept_cn": "人体有两个肾上腺，分别贴附于两侧肾脏的上极顶端（Ad-renal 前缀意为靠近肾脏），内层髓质专职分泌肾上腺素。",
        "trap_en": "Adrenal glands are NOT part of the urinary excretion apparatus; they are endocrine glands positioned on top of the kidneys.",
        "trap_cn": "肾上腺虽位于肾脏顶端，但它属于内分泌系统，不参与生成尿液！",
        "citation": "《G8 Science》Section A Q26 & Lesson 27 (p. 85)"
    },
    {
        "id": "rush_q45",
        "level": 3,
        "topic": "Benedict's Test for Glycosuria",
        "prompt_en": "In a hospital lab, how is Benedict's reagent used to test for glucose in a diabetic patient's urine sample?",
        "prompt_cn": "在医院化验室中，本尼迪特试剂（Benedict's reagent）是如何检测糖尿病患者尿液样本中的葡萄糖的？",
        "options": [
            {"letter": "A", "text_en": "Add Benedict's solution and boil in a water bath; colour changes from clear blue to green/yellow/orange to a brick-red precipitate.", "text_cn": "加入本尼迪特试剂并在水浴中煮沸加热；颜色从初始的清澈天蓝色转变为绿色/黄色/橙色，最终形成砖红色沉淀。"},
            {"letter": "B", "text_en": "Add iodine solution at room temperature; turns blue-black.", "text_cn": "常温下加入碘液；变成蓝黑色。"},
            {"letter": "C", "text_en": "Add Biuret reagent; turns purple.", "text_cn": "加入双缩脲试剂；变成紫色。"},
            {"letter": "D", "text_en": "Mix with ethanol and water; forms cloudy white emulsion.", "text_cn": "加入乙醇和水；形成浑浊的白色乳浊液。"}
        ],
        "correct": "A",
        "concept_en": "Benedict's test detects reducing sugars (glucose). MUST be heated (>80°C in a water bath). Colour progression indicates semi-quantitative concentration: Blue (none) $\\to$ Green $\\to$ Yellow $\\to$ Orange $\\to$ Brick-red (high glucose).",
        "concept_cn": "本尼迪特试剂检测还原糖（葡萄糖），【必须水浴加热】。颜色渐变反映浓度：蓝色（无糖）$\\to$ 绿色 $\\to$ 黄色 $\\to$ 橙色 $\\to$ 砖红色沉淀（高糖）。",
        "trap_en": "Iodine is for starch; Biuret is for protein; Ethanol is for lipids; ONLY Benedict's is for glucose!",
        "trap_cn": "三大生物化学试剂易混点：碘液验淀粉（蓝黑）；双缩脲验蛋白质（紫）；乙醇乳化验脂质；唯有本尼迪特验葡萄糖（需加热成砖红）！",
        "citation": "《G8 Science》Chapter 1: Food Tests (pp. 8-10)"
    },
    {
        "id": "rush_q46",
        "level": 3,
        "topic": "Glycogen Storage Capacity",
        "prompt_en": "Why do animal cells convert excess soluble glucose into insoluble glycogen for storage rather than keeping it as free glucose in cytoplasm?",
        "prompt_cn": "为什么动物细胞要将多余的可溶性葡萄糖转化为不溶性糖原储存，而不是直接以葡萄糖形式留在细胞质中？",
        "options": [
            {"letter": "A", "text_en": "Soluble glucose would dramatically lower cellular water potential, causing massive osmotic water influx and cell rupture; insoluble glycogen has ZERO osmotic effect.", "text_cn": "大量可溶性葡萄糖会急剧拉低细胞内水势，导致外界水分疯狂涌入造成细胞吸水涨破；而不溶性糖原对细胞渗透压和水势零干扰。"},
            {"letter": "B", "text_en": "Glycogen smells like perfume to attract white blood cells.", "text_cn": "糖原有香味可吸引白细胞。"},
            {"letter": "C", "text_en": "Glucose turns into toxic gas inside cells.", "text_cn": "葡萄糖在细胞内会变成有毒气体。"},
            {"letter": "D", "text_en": "Animal cells cannot chemically break down glucose.", "text_cn": "动物细胞无法分解葡萄糖。"}
        ],
        "correct": "A",
        "concept_en": "Osmotic safety: Storing thousands of individual glucose molecules would create immense osmotic pressure, drawing in water until the cell bursts. Compacting them into large, insoluble glycogen molecules has NO osmotic effect.",
        "concept_cn": "渗透安全性：若细胞质内积累大量游离小分子单糖，细胞内水势急剧下降，大量水分子会渗透涌入导致细胞膨胀破裂。缩合为大分子不溶糖原对水势毫无影响。",
        "trap_en": "Insoluble storage compounds (glycogen in animals, starch in plants) do not alter the osmolarity of the cell.",
        "trap_cn": "高分拔高题：动物储存糖原、植物储存淀粉，核心优势均在于其【不溶性】，对细胞内部渗透压完全没有干扰！",
        "citation": "《G8 Science》Chapter 14.04 Glycogen Structure & Osmosis (p. 160)"
    },
    {
        "id": "rush_q47",
        "level": 3,
        "topic": "Negative Feedback Loop Summary",
        "prompt_en": "[True / False] In blood glucose regulation, when blood glucose returns to the normal 5.0 mmol/L set point, the pancreas STOPS secreting excess insulin or glucagon, shutting down the corrective action.",
        "prompt_cn": "【正误判断】在血糖负反馈调节中，一旦血糖浓度回归正常的 5.0 mmol/L 设定基准值，胰腺便会停止过量分泌胰岛素或胰高血糖素，使纠偏动作自动终止。",
        "options": [
            {"letter": "A", "text_en": "TRUE (完全正确，体现负反馈的闭环自我抑制)", "text_cn": "TRUE (完全正确，体现负反馈的闭环自我抑制)"},
            {"letter": "B", "text_en": "FALSE (错误，胰岛素分泌一旦启动将永久喷射)", "text_cn": "FALSE (错误，胰岛素分泌一旦启动将永久喷射)"}
        ],
        "correct": "A",
        "concept_en": "TRUE! This self-limiting nature is the defining hallmark of negative feedback. The correction of the error removes the stimulus that caused the hormone secretion in the first place.",
        "concept_cn": "完全正确！这正是负反馈调节的核心灵魂：当偏差被纠正回设定值，最初触发分泌的刺激消失，激素分泌便自动回归基础状态，防止过度调节。",
        "trap_en": "Positive feedback would keep increasing insulin until fatal hypoglycaemia occurs. Negative feedback SHUTS OFF the response once normal.",
        "trap_cn": "若为正反馈，胰岛素会无限分泌导致致命性低血糖；而负反馈能精确“踩刹车”维系动态平衡。",
        "citation": "《G8 Science》Chapter 4: B9.08 Negative Feedback (p. 60)"
    },
    {
        "id": "rush_q48",
        "level": 3,
        "topic": "Dual Endocrine Function of Pancreas",
        "prompt_en": "Which specialized cell clusters within the pancreas monitor blood glucose levels and secrete insulin and glucagon?",
        "prompt_cn": "胰腺内部负责实时监测血糖浓度、并分泌胰岛素和胰高血糖素的特化微观细胞团称为什么？",
        "options": [
            {"letter": "A", "text_en": "Islets of Langerhans (胰岛细胞群)", "text_cn": "Islets of Langerhans (胰岛细胞群)"},
            {"letter": "B", "text_en": "Alveolar capillaries (肺泡毛细血管网)", "text_cn": "Alveolar capillaries (肺泡毛细血管网)"},
            {"letter": "C", "text_en": "Gall bladder epithelium (胆囊上皮细胞)", "text_cn": "Gall bladder epithelium (胆囊上皮细胞)"},
            {"letter": "D", "text_en": "Tracheal cartilage rings (气管软骨环)", "text_cn": "Tracheal cartilage rings (气管软骨环)"}
        ],
        "correct": "A",
        "concept_en": "The Islets of Langerhans (endocrine micro-organs embedded within pancreatic acinar tissue) contain $\\beta$-cells (secrete insulin) and $\\alpha$-cells (secrete glucagon).",
        "concept_cn": "胰腺内的【胰岛 (Islets of Langerhans)】是内分泌微结构，其中的 $\\beta$ 细胞分泌胰岛素，$\\alpha$ 细胞分泌胰高血糖素。",
        "trap_en": "Most of the pancreas (~98%) makes digestive juice; only ~2% consists of the endocrine Islets of Langerhans.",
        "trap_cn": "胰腺 98% 的体积为外分泌消化腺组织；只有散布在其中的 2% 是专职调控血糖的内分泌胰岛细胞群。",
        "citation": "《G8 Science》Chapter 4: B9.08 Pancreatic Islets (p. 59)"
    }
]

print(f"Total Objective Questions compiled: {len(OBJECTIVE_QUESTIONS)}")

# ----------------- 2. WRITTEN THEORY QUESTIONS (10 ITEMS) -----------------
WRITTEN_THEORY_QUESTIONS = [
    {
        "id": "WT_01",
        "task_code": "Section B Q6",
        "topic": "Movement in/out of Cells",
        "command_word": "Explain",
        "marks": 3,
        "title_en": "Oxygen Diffusion Using 'Concentration Gradient'",
        "title_cn": "运用'浓度梯度'概念解释氧气向血液扩散的机理",
        "prompt_en": "Using the term 'concentration gradient', explain why oxygen diffuses from the air in the alveoli into the blood in the surrounding capillaries. [3 marks]",
        "prompt_cn": "明确使用'浓度梯度 (concentration gradient)'这一科学术语，解释为什么氧气会自发地从肺泡空气中扩散进入周围毛细血管血液中。[3分]",
        "keywords": ["concentration gradient", "higher concentration in alveoli", "lower concentration in blood", "passively down gradient", "diffusion"],
        "mark_scheme": [
            {"point": 1, "text_en": "There is a higher concentration of oxygen in freshly inhaled air inside the alveoli than in the deoxygenated blood arriving at the capillaries. [1]", "text_cn": "新鲜吸入肺泡内的气体具有较高的氧气浓度，而由肺动脉运抵毛细血管的脱氧静脉血中氧气浓度较低。[1分]"},
            {"point": 2, "text_en": "This concentration difference creates a steep concentration gradient between the alveolar air and the blood. [1]", "text_cn": "两侧巨大的氧气浓度差在肺泡与血液界面之间建立起了陡峭的【浓度梯度 (concentration gradient)】。[1分]"},
            {"point": 3, "text_en": "Oxygen particles move passively down this concentration gradient (from high to low concentration) by diffusion across the thin alveolar and capillary walls into red blood cells. [1]", "text_cn": "氧气粒子通过被动扩散，顺着浓度梯度（从高浓度向低浓度）穿过单层微薄的肺泡壁和毛细血管壁进入血液并与红细胞血红蛋白结合。[1分]"}
        ],
        "examiner_tips": "Cambridge 阅卷标准：必须明确出现 'concentration gradient' 术语，并指出是从 'alveoli (high)' 到 'blood (low)' 的顺梯度方向。若仅写 'oxygen moves' 没有解释浓度差，将失掉采分点2。",
        "citation": "《G8 Science.pdf》Chapter 3: B8.02 Gas exchange in humans (pp. 38-39)"
    },
    {
        "id": "WT_02",
        "task_code": "Section B Q7",
        "topic": "Excretion & Kidneys",
        "command_word": "Explain & Compare",
        "marks": 4,
        "title_en": "Difference between Excretion and Egestion with Examples",
        "title_cn": "排泄与排遗的本质生物学区别及实例分析",
        "prompt_en": "Explain the difference between excretion and egestion. Give one example of a substance removed by each process. [4 marks]",
        "prompt_cn": "解释排泄 (excretion) 与排遗 (egestion) 之间的本质生物学区别。并分别为每种生理过程列举一种被排出的具体物质实例。[4分]",
        "keywords": ["metabolic waste", "cellular metabolism", "urea / CO2", "undigested food", "never absorbed", "faeces / anus"],
        "mark_scheme": [
            {"point": 1, "text_en": "Excretion definition: The removal from the body of toxic waste products of cellular metabolism (chemical reactions inside cells), or substances in excess of requirements. [1]", "text_cn": "排泄科学定义：生物体将细胞内部生化代谢反应产生的有毒副产物或过剩物质清除出体外的过程。[1分]"},
            {"point": 2, "text_en": "Excretion example: Urea (in urine/sweat), or Carbon dioxide (from cellular respiration in lungs). [1]", "text_cn": "排泄实例：尿液中的尿素，或细胞呼吸产生并由肺部呼出的二氧化碳。[1分]"},
            {"point": 3, "text_en": "Egestion definition: The passing out of undigested and unabsorbed food material that was never absorbed into body cells or involved in cellular metabolism. [1]", "text_cn": "排遗科学定义：消化道将未被酶分解、未被肠道上皮吸收的食物残渣排出体外的物理过程，这些物质从未真正进入过体细胞代谢。[1分]"},
            {"point": 4, "text_en": "Egestion example: Faeces (dietary fibre/roughage) passed out through the anus. [1]", "text_cn": "排遗实例：经肛门排出的粪便（未消化的植物膳食纤维等）。[1分]"}
        ],
        "examiner_tips": "绝大多数扣分发生在此：学生写 'egestion is poo, excretion is pee' 无法得分。必须强调 'metabolic waste produced by cells' vs 'undigested food that never entered cells'。",
        "citation": "《G8 Science.pdf》Chapter 1 p. 12 & Chapter 4: B9.06 (pp. 54-56)"
    },
    {
        "id": "WT_03",
        "task_code": "Section B Q8",
        "topic": "Excretion & Kidneys",
        "command_word": "Describe",
        "marks": 5,
        "title_en": "How the Nephron Produces Urine (Filtration & Reabsorption)",
        "title_cn": "肾单位生成尿液的全过程（超微滤过与选择性重吸收）",
        "prompt_en": "Describe how the nephron produces urine. Refer to filtration in the glomerulus and selective reabsorption in the renal tubule. [5 marks]",
        "prompt_cn": "详细描述肾单位是如何生成终尿的。作答中必须明确论述肾小球处的超微滤过作用以及肾小管处的选择性重吸收作用。[5分]",
        "keywords": ["high hydrostatic pressure", "ultrafiltration", "Bowman's capsule", "filtrate", "selective reabsorption", "100% of glucose", "osmosis for water", "urea concentrated"],
        "mark_scheme": [
            {"point": 1, "text_en": "Ultrafiltration: Blood enters the glomerulus under high hydrostatic pressure via the renal artery / afferent arteriole. [1]", "text_cn": "高压入球：血液经肾小动脉在高流体静水压驱动下涌入肾小球毛细血管丛。[1分]"},
            {"point": 2, "text_en": "Filtrate formation: Small molecules (water, glucose, amino acids, urea, ions) are forced across the basement membrane into Bowman's capsule to form glomerular filtrate; red blood cells and large proteins are retained in blood. [1]", "text_cn": "超滤原尿：高压将小分子（水、葡萄糖、氨基酸、尿素和离子）挤过滤过膜进入肾小囊形成原尿；血细胞和大分子蛋白因孔径受阻留在血液中。[1分]"},
            {"point": 3, "text_en": "Selective reabsorption of glucose: In the proximal convoluted tubule, 100% of useful glucose and amino acids are actively reabsorbed back into the blood capillaries using carrier proteins. [1]", "text_cn": "葡萄糖100%回收：在近曲小管，100%的有价值葡萄糖与氨基酸被肾小管上皮细胞通过主动运输重吸收回毛细血管网。[1分]"},
            {"point": 4, "text_en": "Reabsorption of water and salts: Most water (~99%) is reabsorbed by osmosis (in Loop of Henle and collecting duct), and necessary mineral salts are reabsorbed according to body needs. [1]", "text_cn": "水分与盐类重吸收：绝大部分水分（约99%）通过渗透作用被重新回收，必需的无机盐根据机体渗透压需要被选择性重吸收。[1分]"},
            {"point": 5, "text_en": "Urine concentration & drainage: Unabsorbed wastes, especially urea, excess water, and excess salts, continue down the collecting duct as concentrated urine into the renal pelvis and ureter. [1]", "text_cn": "终尿形成：未被重吸收的有毒代谢废物尿素以及多余的水和多余盐类汇入集合管，浓缩形成终尿，排入肾盂和输尿管。[1分]"}
        ],
        "examiner_tips": "满分 5 分的综合大题：采分点分布极其工整：入球高压(1) + 滤出小分子阻留大蛋白(1) + 100%葡萄糖主动重吸收(1) + 水分渗透重吸收(1) + 尿素浓缩终尿排出(1)。",
        "citation": "《G8 Science.pdf》Chapter 4: B9.06 Homeostasis (pp. 54-56)"
    },
    {
        "id": "WT_04",
        "task_code": "Section B Q9",
        "topic": "Excretion & Kidneys",
        "command_word": "State & Describe",
        "marks": 3,
        "title_en": "Three Organs of Urinary System and Functions",
        "title_cn": "列举泌尿系统三大宏观器官并分别说明其生理功能",
        "prompt_en": "Name three macroscopic organs of the urinary system, and describe the specific function of each. [3 marks]",
        "prompt_cn": "列举泌尿系统的三个宏观器官名称，并分别描述每一个器官的具体生理功能。[3分]",
        "keywords": ["kidneys filter blood", "ureters transport urine", "bladder stores urine", "urethra carries urine outside"],
        "mark_scheme": [
            {"point": 1, "text_en": "Kidneys: Filter blood to remove metabolic wastes (urea, excess salts, water) and produce urine, while regulating water and ion balance. [1]", "text_cn": "肾脏 (Kidneys)：过滤血液以清除代谢废物（尿素、多余盐和水）并生成尿液，维持体液平衡。[1分]"},
            {"point": 2, "text_en": "Ureters: Muscular tubes that transport urine from the kidneys down to the urinary bladder by peristalsis. [1]", "text_cn": "输尿管 (Ureters)：肌性管道，通过蠕动将双肾生成的尿液向下输送导入膀胱。[1分]"},
            {"point": 3, "text_en": "Bladder (or Urethra): Bladder stores urine temporarily before urination; Urethra carries urine from the bladder to the outside of the body during urination. [1]", "text_cn": "膀胱或尿道 (Bladder / Urethra)：膀胱负责在排尿前暂存尿液；尿道负责在排尿时将尿液从膀胱导引排出体外。[1分]"}
        ],
        "examiner_tips": "任选 Kidneys, Ureters, Bladder, Urethra 中任意三个，器官名称配合准确的动词功能（Filter / Transport / Store / Discharges）。",
        "citation": "《G8 Science.pdf》Chapter 13.02 The Urinary System (pp. 142-143)"
    },
    {
        "id": "WT_05",
        "task_code": "Lesson 30 Part 2 Q2",
        "topic": "Excretion & Kidneys",
        "command_word": "Describe & Explain",
        "marks": 3,
        "title_en": "Glomerular Filtration & Retention of RBCs",
        "title_cn": "肾小球超滤过程及红细胞不被滤出的原因",
        "prompt_en": "Describe what happens to blood inside the glomerulus, and explain why red blood cells are not filtered out. [3 marks]",
        "prompt_cn": "描述血液流经肾小球时发生的生理过程，并阐明为什么红细胞绝对不能被滤过进原尿中。[3分]",
        "keywords": ["high hydrostatic pressure", "glomerular capillaries", "forced into Bowman's capsule", "RBCs too large", "basement membrane pores"],
        "mark_scheme": [
            {"point": 1, "text_en": "Blood enters the glomerulus under high hydrostatic pressure via the afferent arteriole. [1]", "text_cn": "血液经入球小动脉在高流体静水压下涌入肾小球毛细血管网。[1分]"},
            {"point": 2, "text_en": "This high pressure forces water and small dissolved solutes (glucose, urea, ions) through the capillary walls and basement membrane into Bowman's capsule, forming glomerular filtrate. [1]", "text_cn": "高压迫使水和小分子溶质（葡萄糖、氨基酸、尿素、无机盐）穿过毛细血管内皮与基底膜滤入肾小囊腔，形成原尿。[1分]"},
            {"point": 3, "text_en": "Red blood cells (and large plasma proteins) are far too large to pass through the microscopic pores of the basement membrane filtration barrier, so they are physically retained in the bloodstream. [1]", "text_cn": "红细胞（以及大分子血浆蛋白）细胞直径约 7 微米，远远大于基底膜的微观滤孔孔径，因此在物理上被截留在血液循环中。[1分]"}
        ],
        "examiner_tips": "重点突出 'high hydrostatic pressure' 和 'pore size exclusion'（孔径筛分效应）。",
        "citation": "《G8 Science.pdf》Chapter 4: B9.06 Homeostasis (pp. 54-56)"
    },
    {
        "id": "WT_06",
        "task_code": "Lesson 30 Part 2 Q3",
        "topic": "Excretion & Kidneys",
        "command_word": "Explain",
        "marks": 3,
        "title_en": "Selective Reabsorption & Vital Importance",
        "title_cn": "肾脏选择性重吸收的内涵及其生存必要性",
        "prompt_en": "What does 'selective reabsorption' mean in the kidney, and why is it vital for our survival? [3 marks]",
        "prompt_cn": "肾脏中的'选择性重吸收 (selective reabsorption)'是什么含义？为什么这一过程对人类生存是必不可少的？[3分]",
        "keywords": ["selective reabsorption", "useful substances returned to blood", "active transport", "prevent fatal dehydration", "prevent loss of glucose"],
        "mark_scheme": [
            {"point": 1, "text_en": "Definition: Selective reabsorption is the process in the renal tubules where useful substances (100% glucose, amino acids, and needed water/salts) are actively transported back into the surrounding blood capillaries. [1]", "text_cn": "科学定义：选择性重吸收是指肾小管上皮细胞特异性地将原尿中的有益物质（100%的葡萄糖、氨基酸及所需水分/无机盐）逆浓度主动吸收回周围毛细血管血液中。[1分]"},
            {"point": 2, "text_en": "Wastes left behind: Unwanted metabolic wastes like urea are not reabsorbed and remain in the tubule fluid to form urine. [1]", "text_cn": "废物滞留：未被吸收的有毒代谢废物（尿素）留在肾小管管腔内随终尿排出。[1分]"},
            {"point": 3, "text_en": "Vital for survival: Without it, the body would lose 180 litres of water daily leading to fatal dehydration in hours, and would lose all vital energy substrates (glucose), causing rapid hypoglycaemic collapse and death. [1]", "text_cn": "生存必要性：若无重吸收，人体每天会流失 180 升水导致数小时内致命性脱水休克，并丢失全部葡萄糖能量底物导致代谢崩溃死亡。[1分]"}
        ],
        "examiner_tips": "回答为什么 vital 时，必须提及若无此机制会丢失宝贵的葡萄糖燃料和海量水分（脱水致命）。",
        "citation": "《G8 Science.pdf》Chapter 4: B9.06 Review Exam p. 113"
    },
    {
        "id": "WT_07",
        "task_code": "Section B Q10",
        "topic": "Nervous vs Endocrine",
        "command_word": "Compare",
        "marks": 4,
        "title_en": "Nervous vs Endocrine Speed and Duration",
        "title_cn": "从反应速度与持续时间对比神经调节与内分泌调节",
        "prompt_en": "Compare the nervous system and the endocrine system in terms of (a) the speed of the response and (b) how long the effect lasts. [4 marks]",
        "prompt_cn": "从 (a) 反应发生的速度 和 (b) 生理效应持续的时间 两个方面，对比神经系统与内分泌系统的不同特征。[4分]",
        "keywords": ["speed of response", "nervous fast milliseconds", "endocrine slower", "duration of effect", "nervous short-lived", "endocrine long-lasting"],
        "mark_scheme": [
            {"point": 1, "text_en": "(a) Speed - Nervous: Extremely fast / almost instantaneous, as electrical impulses travel along nerve axons in milliseconds. [1]", "text_cn": "(a) 反应速度 - 神经系统：反应极快/几乎瞬间完成，电神经冲动在毫秒级沿轴突传导。[1分]"},
            {"point": 2, "text_en": "(a) Speed - Endocrine: Slower, because chemical hormones must be secreted into the blood and circulate through the cardiovascular system to reach target organs. [1]", "text_cn": "(a) 反应速度 - 内分泌系统：反应启动相对较慢，因为化学激素必须排入血液并随循环流动才能抵达靶器官。[1分]"},
            {"point": 3, "text_en": "(b) Duration - Nervous: Short-lived / brief, as the response ceases immediately once nerve impulses stop. [1]", "text_cn": "(b) 持续时间 - 神经系统：效应短暂，一旦神经冲动停止，肌肉收缩或反射动作瞬间终止。[1分]"},
            {"point": 4, "text_en": "(b) Duration - Endocrine: Long-lasting / sustained, as hormones remain active in the bloodstream until broken down by the liver or excreted by the kidneys. [1]", "text_cn": "(b) 持续时间 - 内分泌系统：效应持久且深远，激素在血液中持续发挥调控作用，直至被肝脏代谢灭活或肾脏清除。[1分]"}
        ],
        "examiner_tips": "清晰分段：Speed (Nervous Fast vs Endocrine Slower) 和 Duration (Nervous Brief vs Endocrine Long-lasting)。",
        "citation": "《G8 Science.pdf》Chapter 4: B9.01 Coordination & Hormones (pp. 47-51, 54-55)"
    },
    {
        "id": "WT_08",
        "task_code": "Section B Q11",
        "topic": "Blood Glucose Regulation",
        "command_word": "Describe & Explain",
        "marks": 5,
        "title_en": "Blood Glucose Response after Meal & Insulin Role",
        "title_cn": "进食后血糖动态曲线分析与胰岛素调节作用",
        "prompt_en": "Describe what happens to blood glucose concentration in the two hours after eating a carbohydrate meal, and explain the role of insulin in bringing the level back down to normal. [5 marks]",
        "prompt_cn": "描述进食富含碳水化合物的餐后两小时内血糖浓度的变化趋势，并解释胰岛素在使血糖水平恢复正常过程中的生理作用。[5分]",
        "keywords": ["trend rises after meal", "digestion and absorption", "peaks and falls", "pancreas secretes insulin", "liver converts glucose to glycogen", "negative feedback restores set point"],
        "mark_scheme": [
            {"point": 1, "text_en": "Trend - Rise: In the first 30–60 minutes after eating, blood glucose concentration rises sharply above the normal fasting baseline (~5.0 mmol/L) as carbohydrates are digested into glucose and absorbed into the bloodstream. [1]", "text_cn": "走势 - 上升：进餐后前 30 至 60 分钟内，随着食物中的碳水化合物被消化成葡萄糖并吸收进入血液，血糖浓度急剧攀升脱离正常基准值（~5.0 mmol/L）。[1分]"},
            {"point": 2, "text_en": "Trend - Peak & Fall: Blood glucose reaches a peak (at ~1 hour) and then steadily decreases over the next 1–2 hours back towards the fasting set point. [1]", "text_cn": "走势 - 达峰与回落：血糖浓度在 1 小时左右达到峰值，随后在接下来的 1 至 2 小时内平稳持续回落，回归空腹正常设定线。[1分]"},
            {"point": 3, "text_en": "Insulin Detection: The rise in blood glucose is detected by the beta cells of the pancreas, which respond by secreting the hormone insulin into the bloodstream. [1]", "text_cn": "胰岛素分泌：血糖升高被胰腺 $\\beta$ 细胞敏锐感知，随即加速向血液中分泌释放激素【胰岛素 (Insulin)】。[1分]"},
            {"point": 4, "text_en": "Cellular Uptake: Insulin stimulates body cells (muscle and adipose) to increase glucose uptake from blood to use in cellular respiration. [1]", "text_cn": "细胞摄取：胰岛素刺激全身外周肌细胞和脂肪细胞加速从血液中摄取葡萄糖，用于细胞呼吸氧化供能。[1分]"},
            {"point": 5, "text_en": "Glycogenesis in Liver: Insulin stimulates liver and skeletal muscle cells to convert soluble glucose into the insoluble storage carbohydrate glycogen (glycogenesis), clearing excess glucose and restoring homeostasis. [1]", "text_cn": "肝糖原合成：胰岛素促使肝脏和骨骼肌将可溶性葡萄糖催化合成为不溶性【糖原 (Glycogen)】储存起来，清除血液过多游离糖，恢复内环境稳态。[1分]"}
        ],
        "examiner_tips": "本题含 2 分曲线描述 (Curve Trend) + 3 分胰岛素生理机制 (Pancreas detects/secretes -> Uptake -> Converts to Glycogen)。缺一不可。",
        "citation": "《G8 Science.pdf》Chapter 5: B10.02 Hormones & Blood Glucose (pp. 64-67)"
    },
    {
        "id": "WT_09",
        "task_code": "Section B Q12",
        "topic": "Blood Glucose Regulation",
        "command_word": "Explain & Describe",
        "marks": 3,
        "title_en": "Pancreas Cannot Produce Insulin: Danger & Treatment",
        "title_cn": "胰腺无法产生胰岛素的危险性与现代医学治疗",
        "prompt_en": "A patient's pancreas cannot produce insulin (Type 1 diabetes). Explain why this is dangerous for the patient, and describe how the condition is normally treated. [3 marks]",
        "prompt_cn": "一名患者的胰腺完全无法生产胰岛素（1型糖尿病）。解释为什么这种情况对患者是极其危险的，并描述在现代医学中通常如何对该病症进行有效治疗。[3分]",
        "keywords": ["hyperglycaemia", "cells cannot take up glucose", "weight loss / coma", "insulin injections", "dietary management"],
        "mark_scheme": [
            {"point": 1, "text_en": "Danger - Hyperglycaemia & Starvation: Without insulin, body cells cannot take up glucose for cellular respiration, causing chronically high blood glucose (hyperglycaemia) which damages blood vessels, kidneys, nerves, and eyes. [1]", "text_cn": "危害 - 细胞饥饿与高糖损伤：缺乏胰岛素使体细胞无法摄取葡萄糖进行呼吸供能，导致血液长期高血糖，高渗状态严重损伤微血管、肾脏、神经与视网膜。[1分]"},
            {"point": 2, "text_en": "Danger - Ketoacidosis: Because cells cannot utilize glucose, the body breaks down fats and proteins uncontrollably, leading to rapid weight loss, toxic ketoacidosis, coma, and potential death. [1]", "text_cn": "危害 - 酮症酸中毒与昏迷：细胞因极度饥饿代偿性剧烈分解体脂与蛋白质，产生大量有毒酸性酮体，引发严重酮症酸中毒脱水昏迷乃至死亡。[1分]"},
            {"point": 3, "text_en": "Treatment: Managed by daily subcutaneous insulin injections (or an insulin pump), combined with careful dietary carbohydrate management and regular blood glucose monitoring. [1]", "text_cn": "治疗方案：每日定时皮下注射外源性胰岛素（或佩戴胰岛素泵），配合低糖健康饮食控制及规律的血糖动态监测。[1分]"}
        ],
        "examiner_tips": "必须写出注射胰岛素 (insulin injections)，不能写 'eat insulin'（因为胰岛素是蛋白质，口服会被胃蛋白酶消化失效）。",
        "citation": "《G8 Science.pdf》Chapter 4: B9.08 Blood glucose regulation (pp. 59-60)"
    },
    {
        "id": "WT_10",
        "task_code": "Lesson 30 Part 2 Q8",
        "topic": "Blood Glucose Regulation",
        "command_word": "Explain",
        "marks": 4,
        "title_en": "Insulin Negative Feedback Loop & Three Liver Commands",
        "title_cn": "胰岛素调节血糖的负反馈回路（对肝脏的三大指令）",
        "prompt_en": "Explain the homeostatic negative feedback loop of how insulin regulates blood sugar. What three specific biochemical actions does it command the liver to perform? [4 marks]",
        "prompt_cn": "详细解释胰岛素调节血糖的负反馈调节回路。具体阐明它向肝脏下达了哪三项具体的生化代谢生理指令？[4分]",
        "keywords": ["negative feedback loop", "insulin from beta cells", "command 1 increase glucose uptake", "command 2 convert glucose to glycogen", "command 3 increase respiration", "blood glucose falls to set point"],
        "mark_scheme": [
            {"point": 1, "text_en": "Negative Feedback Loop: After a meal, high blood glucose is detected by pancreatic beta cells, which secrete insulin. As glucose is cleared, blood sugar falls to 5.0 mmol/L set point, turning off high insulin secretion. [1]", "text_cn": "负反馈闭环：餐后高血糖被胰腺 $\\beta$ 细胞感知并释放胰岛素；随着游离糖被转移储存，血糖回落至 5.0 mmol/L 设定线，反馈抑制并关闭高胰岛素分泌。[1分]"},
            {"point": 2, "text_en": "Liver Command 1 - Glucose Uptake: Stimulates liver cells to increase the permeability of their cell membranes to absorb glucose from the blood at an accelerated rate. [1]", "text_cn": "对肝脏指令 1 - 加速摄取：指令肝细胞膜载体开放，成倍加速从血液中摄取转运游离葡萄糖进入细胞。[1分]"},
            {"point": 3, "text_en": "Liver Command 2 - Glycogenesis: Activates glycogen synthase enzymes to convert soluble glucose into the insoluble storage polymer glycogen (glycogenesis). [1]", "text_cn": "对肝脏指令 2 - 糖原合成：激活糖原合成酶，将可溶性葡萄糖脱水缩合为不溶性大分子糖原 (Glycogen) 储存。[1分]"},
            {"point": 4, "text_en": "Liver Command 3 - Respiration Rate: Stimulates the liver cells to increase the rate of glucose breakdown in cellular respiration for metabolic energy. [1]", "text_cn": "对肝脏指令 3 - 氧化分解：促进肝细胞线粒体加速葡萄糖的氧化分解呼吸反应，消耗多余糖分。[1分]"}
        ],
        "examiner_tips": "剑桥考官特别青睐要求考生清晰列出胰岛素对靶器官肝脏的 3 大作用：1) 摄取吸收；2) 合成为糖原 (Glycogen)；3) 氧化分解呼吸利用。",
        "citation": "《G8 Science.pdf》Chapter 4: B9.08 Blood glucose regulation (pp. 59-60, Fig B9.20)"
    }
]

print(f"Total Written Theory Questions compiled: {len(WRITTEN_THEORY_QUESTIONS)}")

# Save to temporary json to verify structure
with open("temp_rush_data.json", "w", encoding="utf-8") as f:
    json.dump({
        "objective": OBJECTIVE_QUESTIONS,
        "written": WRITTEN_THEORY_QUESTIONS
    }, f, ensure_ascii=False, indent=2)

print("Data successfully verified and saved to temp_rush_data.json.")
