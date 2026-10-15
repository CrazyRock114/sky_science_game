# -*- coding: utf-8 -*-
"""
data_deep_mcq_block2.py
Deep, concept-grounded distractor analyses for:
Cumulative Revision Exam Section A: Q1 to Q20 (20 MCQs)

Each option contains:
- correct: bool
- en: [Concept] ... [Comparison] ... [Confusion Trap/Key Criteria] ...
- cn: 【涉及知识点】... 【异同辨析】... 【混淆陷阱/核心考点】...
"""

BLOCK2_DISTRACTORS = {
    # ==================== CUMULATIVE REVISION SECTION A (Q1 - Q20) ====================
    "Rev_SecA_Q01": {
        "A": {
            "correct": False,
            "en": "[Concept]: Blood plasma is an aqueous fluid matrix (>90% water) transporting soluble nutrients, ions, urea, hormones, and hydrogencarbonate. [Comparison]: Oxygen has extremely low solubility in aqueous liquids (<1.5% physically dissolved in plasma); bulk oxygen transport requires specialized red blood cells. [Confusion Trap]: Students conflate 'blood as an entire tissue transports substances' with 'liquid plasma', incorrectly assuming plasma carries all biological materials equally.",
            "cn": "【涉及知识点】血浆（Plasma）是占全血约55%的淡黄色水性液体基质（90%以上为水），专职运输可溶性营养物、尿素、激素及碳酸氢根。【异同辨析】氧气在水中的溶解度极低（血浆中物理溶解的氧气不足1.5%），全身组织巨大的耗氧需求绝不可能依靠血浆运载，必须依赖红细胞内高浓度的血红蛋白结合运输。【混淆陷阱】容易将“血液整体具有运输功能”与“液体血浆基质”混为一谈，误以为血浆能统包体内所有分子的转运。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Platelets (thrombocytes) are membrane-bound cellular fragments derived from bone marrow megakaryocytes that initiate blood clotting. [Comparison]: Platelets release clotting factors and aggregate to form haemostatic plugs; they contain no respiratory pigments and do not participate in gas transport. [Confusion Trap]: Confusing the distinct cellular components of blood and mistaking clotting fragments for respiratory carriers.",
            "cn": "【涉及知识点】血小板（Platelets）是骨髓成熟巨核细胞脱落形成的无核胞质碎片，专职参与止血与血液凝固级联反应。【异同辨析】血小板的生理使命是黏附受损胶原、释放凝血因子并构筑初级血小板血栓；其胞内无血红蛋白，完全不具备气体运载功能。【混淆陷阱】对血液各种有形成分的劳动分工发生记忆混淆，误将止血胞质碎片当成呼吸载体。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Red blood cells (erythrocytes) are biconcave, anucleate discs specifically packed with iron-rich haemoglobin for respiratory gas transport. [Comparison]: Haemoglobin binds reversibly with oxygen in high-PO2 alveolar capillaries to form oxyhaemoglobin, transporting >98.5% of the body's oxygen to metabolizing tissues. [Key Criteria]: Perfectly aligns with the official Cambridge syllabus definition for oxygen transport.",
            "cn": "【涉及知识点】红细胞（Red blood cells）呈双凹圆盘状、无细胞核与细胞器，胞内高度充盈含铁四聚体蛋白质——血红蛋白（Haemoglobin）。【异同辨析】在高氧分压的肺泡毛细血管网中，血红蛋白迅速与氧气紧密结合为亮红色的氧合血红蛋白；流经低氧的外周组织时解离释放游离氧，承担体内98.5%以上的氧气运载使命。【核心考点】准确契合剑桥大纲中红细胞作为专职运氧细胞的核心定义。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: White blood cells (leucocytes, including phagocytes and lymphocytes) are nucleated defensive cells of the immune system. [Comparison]: Leucocytes defend the body against invading pathogens via phagocytosis and antibody production; they lack haemoglobin and do not transport respiratory gases. [Confusion Trap]: Assuming that because white blood cells are large, complete, and active cells, they must perform general transport functions.",
            "cn": "【涉及知识点】白细胞（White blood cells）是机体免疫系统的核心防御细胞，包含吞噬细胞（Phagocytes）和淋巴细胞（Lymphocytes）。【异同辨析】白细胞通过变形运动吞噬病原体或合成特异性抗体构筑防线；其内部不含血红蛋白，完全不参与呼吸气体的扩散与运输。【混淆陷阱】误以为白细胞体型大且拥有完整细胞核与细胞器，就能够统管体内物质的常规运输。"
        }
    },

    "Rev_SecA_Q02": {
        "A": {
            "correct": True,
            "en": "[Concept]: Blood plasma is the straw-coloured, pale-yellow liquid extracellular matrix comprising roughly 55% of total blood volume. [Comparison]: Plasma holds all suspended cellular elements (RBCs, WBCs, platelets) and dissolves vital solutes (glucose, amino acids, mineral ions, urea, hormones, plasma proteins). [Key Criteria]: Precise histological identification matching standard Cambridge textbook figures.",
            "cn": "【涉及知识点】血浆（Plasma）是全血经抗凝离心后位于上层的淡黄色清亮液体，约占人体总血容量的55%。【异同辨析】血浆为血细胞提供悬浮液体环境，并溶解转运葡萄糖、氨基酸、无机盐、尿素、激素以及白蛋白、纤维蛋白原等血浆蛋白。【核心考点】完全符合剑桥教材对血液液体成分（淡黄色基质）的基础解剖学命名。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Serum is the amber fluid that separates out when blood coagulates in vitro, representing plasma depleted of fibrinogen and clotting factors. [Comparison]: Plasma is the normal circulating liquid phase in living vessels with intact fibrinogen; serum is an artificial post-clotting derivative lacking clotting proteins. [Confusion Trap]: In common parlance, 'serum' and 'plasma' are often used synonymously, causing students to overlook that serum is plasma minus clotting factors.",
            "cn": "【涉及知识点】血清（Serum）是全血凝固析出血块后表面渗出的清亮液体，即“去除了纤维蛋白原及凝血因子”的血浆衍生液。【异同辨析】在活体血管中自然流动的血液液体部分是血浆（含可溶性纤维蛋白原）；血清是体外凝血反应后的副产物，不属于正常血管内循环的原生液体。【混淆陷阱】日常口语常将“血清”与“血浆”混用，导致忽略了血清缺少关键凝血蛋白这一本质区别。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Lymph is excess tissue fluid (interstitial fluid) collected into blind-ended lymphatic capillaries and returned to the subclavian veins. [Comparison]: Lymph flows in the lymphatic system rather than blood vessels, has lower protein concentration than plasma, and contains no red blood cells. [Confusion Trap]: Both are yellowish extracellular fluids, but lymph is located in the lymphatic vessels after draining from interstitial spaces, not the liquid portion of whole blood.",
            "cn": "【涉及知识点】淋巴液（Lymph）是由毛细血管渗出的组织液经毛细淋巴管盲端重吸收形成的液体，最终汇入锁骨下静脉。【异同辨析】淋巴液在独立的淋巴管道系统中流动，其蛋白质含量远低于血浆且不含红细胞；血浆则是封闭心血管系统内直接循环的液体。【混淆陷阱】两者均为淡黄色透明液体，容易因外观相似而混淆其所在的不同解剖系统与蛋白质浓度等级。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Cytoplasm is the gelatinous, aqueous intracellular matrix contained within the plasma membrane of individual cells, housing organelles. [Comparison]: Cytoplasm is strictly intracellular (inside living cells), whereas blood plasma is extracellular matrix circulating outside cells in the lumen of blood vessels. [Confusion Trap]: Etymological and phonological similarity (both sharing '-plasm') leads students to confuse internal cellular fluid with external circulating fluid.",
            "cn": "【涉及知识点】细胞质（Cytoplasm）是存在于单个活细胞质膜内部的胶状基质，容纳细胞器并发生各项胞内生化反应。【异同辨析】细胞质严格属于“细胞内液（Intracellular fluid）”，而血浆是心血管腔内包围着血细胞的“细胞外液（Extracellular fluid）”。【混淆陷阱】词尾形似（均含有-plasm词根），容易让学生在英文词汇辨析时将胞内胶体与血管外液混淆。"
        }
    },

    "Rev_SecA_Q03": {
        "A": {
            "correct": False,
            "en": "[Concept]: Fibrinogen is a large, soluble plasma glycoprotein synthesized by hepatocytes, circulating dissolved in blood plasma. [Comparison]: Fibrinogen is cleaved by thrombin into insoluble fibrin during haemostasis; it does not bind respiratory gases and is located in plasma, not inside red blood cells. [Confusion Trap]: Remembering fibrinogen as a prominent blood protein, but confusing clotting functions with oxygen carriage.",
            "cn": "【涉及知识点】纤维蛋白原（Fibrinogen）是由肝细胞合成并分泌到血浆中的大分子可溶性糖蛋白，分子量约340 kDa。【异同辨析】纤维蛋白原在凝血级联末期被凝血酶催化裂解为不溶性纤维蛋白网以封堵伤口；其游离于血浆中，无含铁血红素基团，不具备结合氧气的能力。【混淆陷阱】记住了纤维蛋白原是血液中的重要蛋白质，但张冠李戴将其功能与红细胞内的运氧蛋白混淆。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Haemoglobin is an intracellular, tetrameric globular protein containing four iron-bearing haem prosthetic groups packaged inside erythrocytes. [Comparison]: Each haemoglobin molecule binds reversibly up to four O2 molecules in the pulmonary capillaries to form oxyhaemoglobin, dissociating to release oxygen in respiring tissues. [Key Criteria]: The definitive textbook oxygen-binding respiratory pigment required by the Cambridge curriculum.",
            "cn": "【涉及知识点】血红蛋白（Haemoglobin）是红细胞特有的四聚体球蛋白，由四条多肽链和四个含二价铁离子（Fe²⁺）的血红素辅基构成。【异同辨析】在肺部高氧分压下，Fe²⁺与氧分子迅速可逆结合形成鲜红色的氧合血红蛋白；在耗氧组织处解离释放氧气。二者结合完全可逆且高度灵敏。【核心考点】精准契合剑桥大纲中关于红细胞内含铁运氧呼吸色素的经典定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: An antibody (immunoglobulin) is a Y-shaped glycoprotein secreted by plasma cells (differentiated B-lymphocytes) into blood and lymph. [Comparison]: Antibodies bind specifically to complementary antigens on foreign pathogens to neutralize toxins or opsonize microbes; they do not bind oxygen and circulate in plasma, not inside red cells. [Confusion Trap]: Conflating protective immune proteins in plasma with respiratory transport proteins inside red blood cells.",
            "cn": "【涉及知识点】抗体（Antibody/Immunoglobulin）是浆细胞（活化的B淋巴细胞）分泌的Y形特异性糖蛋白，广泛分布于血浆与组织液中。【异同辨析】抗体通过其可变区精准识别并结合病原体表面的外来抗原分子以行使免疫防御；其不含血红素，无运氧活性，且绝不封装于红细胞内。【混淆陷阱】把体液免疫中的防御性蛋白（抗体）与气体代谢中的转运蛋白（血红蛋白）发生知识域串线。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Insulin is a peptide hormone produced and secreted by beta cells of the pancreatic islets of Langerhans into the blood. [Comparison]: Insulin binds to cell-surface insulin receptors to promote cellular glucose uptake and glycogenesis; it is an endocrine signaling molecule circulating in plasma, not an oxygen carrier in RBCs. [Confusion Trap]: Both are vital circulating globular proteins, but insulin controls carbohydrate homeostasis rather than gas transport.",
            "cn": "【涉及知识点】胰岛素（Insulin）是胰腺胰岛β细胞合成并分泌入血的由51个氨基酸组成的双链小分子多肽激素。【异同辨析】胰岛素作为化学信使与靶细胞膜受体结合，加速葡萄糖摄取与糖原合成以降低血糖；它在血浆中微量运行，不具备气体运载结构与功能。【混淆陷阱】二者皆为血液中的关键蛋白质分子，容易将调节血糖的内分泌激素与红细胞内的气体转运载体混淆。"
        }
    },

    "Rev_SecA_Q04": {
        "A": {
            "correct": False,
            "en": "[Concept]: Diffusion is the net movement of particles from a region of higher concentration to lower concentration down a concentration gradient as a result of random motion. [Comparison]: Diffusion is a purely passive, non-specific physical process requiring no cellular ATP or membrane deformation; phagocytosis is an active, endocytic cellular process. [Confusion Trap]: Confusing passive membrane transport phenomena with active cellular immune mechanisms.",
            "cn": "【涉及知识点】扩散作用（Diffusion）是微粒由于无规则热运动，顺浓度梯度从高浓度区域向低浓度区域发生的净移动。【异同辨析】扩散是完全被动、不消耗ATP分子的纯物理过程；而白细胞吞噬病原体依赖细胞骨架剧烈形变、胞膜凹陷及溶酶体融合，属于高耗能的胞吞作用。【混淆陷阱】容易将分子层面的被动跨膜扩散与细胞层面的主动免疫吞噬机制相混淆。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Phagocytosis is the specialized form of endocytosis in which phagocytic white blood cells (e.g. neutrophils, macrophages) engulf large particulate matter or pathogens. [Comparison]: The cell extends pseudopodia around the microbe, encloses it in a phagosome, and fuses with lysosomes containing hydrolytic enzymes to digest and destroy it. [Key Criteria]: Flawless alignment with the standard biological definition of cellular pathogen ingestion.",
            "cn": "【涉及知识点】吞噬作用（Phagocytosis）是机体非特异性免疫的核心机制，专由吞噬细胞（如中性粒细胞、巨噬细胞）执行。【异同辨析】吞噬细胞伸出伪足包裹外来微生物，将其封闭于吞噬小泡（Phagosome）中，继而与溶酶体融合，利用溶菌酶与蛋白水解酶彻底消解病原体。【核心考点】完美对应剑桥科学考纲中关于白细胞通过吞噬作用吞食并消化病原体的标准考查定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Filtration is a physical process where fluids and small solutes pass through a porous barrier under mechanical hydrostatic pressure, retaining larger particles. [Comparison]: Filtration is driven by pressure differences (such as glomerular ultrafiltration in the nephron) rather than cellular recognition, pseudopod extension, and enzymatic digestion. [Confusion Trap]: Conflating organ-level mechanical filtering (like in lymph nodes or renal glomeruli) with cellular-level active ingestion.",
            "cn": "【涉及知识点】滤过作用（Filtration）是在流体静压力差驱动下，水和小分子溶质被迫穿过微孔过滤屏障而大颗粒被截留的物理分离过程。【异同辨析】滤过作用依赖物理机械压力（如肾小球毛细血管高压超滤），不涉及细胞主动伸出伪足包被或溶酶体酶学水解；白细胞杀菌是主动胞吞而非压力滤过。【混淆陷阱】将器官层面宏观的“滤除杂质”（如淋巴结或肾小球滤过）与微观细胞的主动免疫“吞噬消化”混为一谈。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Reabsorption is the recovery of filtered water, essential ions, and nutrients (glucose, amino acids) from tubule lumen back into peritubular capillaries in the kidneys. [Comparison]: Reabsorption is a renal physiological transport process aimed at conserving valuable metabolic substrates; it does not destroy foreign pathogens. [Confusion Trap]: Selecting an unrelated physiological uptake process simply because it involves transport into a cell or tissue.",
            "cn": "【涉及知识点】重吸收作用（Reabsorption）是泌尿系统中肾小管和集合管上皮细胞将原尿中的水分、葡萄糖、无机盐等拉回周围毛细血管的生理过程。【异同辨析】重吸收的目的是回收对人体有益的营养成分以维持水盐稳态；其作用对象是营养分子而非病原体，与免疫杀菌毫无交集。【混淆陷阱】随意套用生理学中的吸收类词汇，未能将其定位于泌尿系统的回收功能。"
        }
    },

    "Rev_SecA_Q05": {
        "A": {
            "correct": False,
            "en": "[Concept]: Platelets are cell fragments that initiate blood clotting by sticking to damaged vessels and releasing clotting factors. [Comparison]: Platelets trigger the reaction and form a temporary platelet plug, but they are not the chemical product formed from fibrinogen; fibrinogen polymerizes into protein fibres, not cells. [Confusion Trap]: Confusing the cellular trigger (platelets) with the insoluble protein meshwork (fibrin) that results from the biochemical cascade.",
            "cn": "【涉及知识点】血小板（Platelets）是参与初期止血的细胞碎片，在血管内皮受损时发生黏附、聚集并释放凝血因子。【异同辨析】血小板是启动凝血级联反应的“细胞扳机”并构成初级血栓；可溶性的纤维蛋白原是经酶解交联形成“蛋白质纤维网”，绝不可能转化为血细胞或碎片。【混淆陷阱】血小板与纤维蛋白网共同构成终极血凝块，学生极易将细胞层面的触发者与分子层面的产物相混淆。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Haemoglobin is the intracellular oxygen-binding protein packaged inside red blood cells. [Comparison]: Haemoglobin is synthesized during erythrocyte maturation and plays zero role in blood clotting; red cells are only passively trapped inside the fibrin mesh. [Confusion Trap]: Observing that blood clots appear dark red and incorrectly guessing that the red pigment itself is the structural protein of the mesh.",
            "cn": "【涉及知识点】血红蛋白（Haemoglobin）是严格包裹在红细胞胞质内部的含铁四聚体呼吸色素，专司结合与运输氧气。【异同辨析】血红蛋白由骨髓幼稚红细胞合成，完全不具备纤维交联凝胶化活性；红细胞只是被动被纤维网截留以增加血块机械强度。【混淆陷阱】肉眼观察到的血痂呈暗红色，学生容易误以为形成网状骨架的物质就是使血液呈现红色的血红蛋白。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Fibrin is an insoluble, fibrous protein formed during the final step of blood coagulation when thrombin cleaves soluble plasma fibrinogen. [Comparison]: Fibrin monomers polymerize into long, tough strands that cross-link into a meshwork, physically trapping red blood cells and platelets to form a stable blood clot. [Key Criteria]: Precise match for the central enzymatic step of blood coagulation taught in Cambridge G8 Science.",
            "cn": "【涉及知识点】纤维蛋白（Fibrin）是凝血酶（Thrombin）催化水解血浆中可溶性纤维蛋白原后形成的不溶性高分子纤维状蛋白质。【异同辨析】可溶性纤维蛋白原失去末端电荷多肽后迅速自组装聚合为坚韧交织的纤维蛋白三维立体网，阻截过往血细胞形成牢固血栓，封堵血管破损口。【核心考点】完全符合剑桥考纲中关于凝血酶促使纤维蛋白原转化为不溶性纤维蛋白纤维网的核心机制。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Antibodies are Y-shaped immunoglobulins produced by plasma cells (lymphocytes) to specifically target microbial antigens. [Comparison]: Antibodies neutralize bacterial toxins or bind antigens for immune clearance; they do not assemble into insoluble structural matrices to stop haemorrhage. [Confusion Trap]: Conflating different types of protective blood proteins (immune antibodies vs haemostatic fibrin).",
            "cn": "【涉及知识点】抗体（Antibodies）是由浆细胞合成的特异性免疫球蛋白，具备高度专一的抗原结合臂（Fab段）。【异同辨析】抗体行使的是针对病原体的特异性中和与调理吞噬功能；它们不具备机械骨架聚合性质，无法交织成网以物理封堵出血创口。【混淆陷阱】两者同属血浆中的重要防御性蛋白质，学生容易在概念检索时把免疫中和蛋白与机械止血蛋白相混淆。"
        }
    },

    "Rev_SecA_Q06": {
        "A": {
            "correct": False,
            "en": "[Concept]: Antigens are molecular markers (typically foreign surface glycoproteins or polysaccharides) present on the exterior of pathogens. [Comparison]: Antigens are recognized by the immune system as non-self; lymphocytes do NOT produce antigens to attack pathogens, but rather synthesize antibodies against them. [Confusion Trap]: Classic linguistic confusion between the foreign target ('antigen') and the host defensive molecule ('antibody').",
            "cn": "【涉及知识点】抗原（Antigens）通常是位于病原体外表面、能诱导机体产生特异性免疫应答的外来大分子（如外膜糖蛋白、细菌多糖等）。【异同辨析】抗原是病原体携带的“外来异物标识”；淋巴细胞合成的是用来结合并攻击抗原的“抗体”，绝对不会自己生产抗原去反击病原体。【混淆陷阱】典型的概念方向性倒置：严重混淆了被攻击的靶标分子（抗原）与免疫细胞制造的攻击武器（抗体）。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Lymphocytes (specifically B-lymphocytes / plasma cells) synthesize and secrete antibodies (immunoglobulins). [Comparison]: Each antibody possesses a unique antigen-binding site complementary in shape to a specific antigen on the invading pathogen, agglutinating or neutralizing them. [Key Criteria]: Precise curriculum statement defining adaptive humoral immunity.",
            "cn": "【涉及知识点】淋巴细胞（Lymphocytes，特别是B淋巴细胞分化形成的浆细胞）是体液免疫中合成与分泌抗体的专属细胞。【异同辨析】每种抗体分子的可变区空间构象与特定病原体表面的抗原决定簇高度互补（锁钥机制），能特异性结合抗原，促成凝集、中和毒素或引导吞噬。【核心考点】完全契合剑桥大纲中淋巴细胞通过合成抗原特异性抗体来抵御病原体感染的核心结论。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Fibrin is an insoluble fibrous protein produced in the blood coagulation cascade to seal wound breaches. [Comparison]: Fibrin generation is triggered by platelets and clotting enzymes (thrombin), not synthesized by lymphocytes as an antigen-specific immune response. [Confusion Trap]: Misunderstanding the verb 'trap'—thinking that because lymphocytes fight pathogens, they must physically net them with fibrin.",
            "cn": "【涉及知识点】纤维蛋白（Fibrin）是凝血酶作用于血浆纤维蛋白原后形成的不溶性网状蛋白，属于循环系统的机械止血产物。【异同辨析】纤维蛋白网由凝血级联系统催化生成，专用于创口处截留血细胞形成血栓；它绝不是淋巴细胞分泌的分子，不具备抗原识别专一性。【混淆陷阱】对“捕获/拦截”一词发生歧义理解，误以为淋巴细胞也是通过结出纤维蛋白网来网捕细菌。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Haemoglobin is the intracellular oxygen-carrying metalloprotein housed inside erythrocytes. [Comparison]: Haemoglobin functions purely in respiratory gas exchange; it possesses no immune targeting domains and is neither synthesized nor used by lymphocytes. [Confusion Trap]: Indiscriminately selecting any well-known blood protein name regardless of its physiological function.",
            "cn": "【涉及知识点】血红蛋白（Haemoglobin）是红细胞特有的含铁球蛋白，执行氧气和部分二氧化碳的装载与转运。【异同辨析】血红蛋白完全不具备抗菌或免疫调理活性，且仅由骨髓造血系红细胞系合成，淋巴细胞绝不生产或利用血红蛋白消灭病原体。【混淆陷阱】在多选干扰项中盲目套用熟悉的血液蛋白质专有名词，脱离了免疫学的具体情境。"
        }
    },

    "Rev_SecA_Q07": {
        "A": {
            "correct": False,
            "en": "[Concept]: Glucose is a polar, hydrophilic monosaccharide nutrient absorbed from the small intestine. [Comparison]: Glucose dissolves freely in the aqueous phase of blood plasma (maintaining normal concentrations of 4.0–7.8 mmol/L); it does not bind to intracellular proteins inside RBCs. [Confusion Trap]: Knowing glucose is transported in blood, but failing to distinguish water-soluble solutes in plasma from non-polar gases requiring intracellular pigments.",
            "cn": "【涉及知识点】葡萄糖（Glucose）是极性高、水溶性优良的六碳单糖，是全身细胞有氧呼吸最重要的能量底物。【异同辨析】葡萄糖分子极易溶解在以水为主体的血浆液体基质中自由运输（正常空腹浓度维持在4.0–7.8 mmol/L）；它完全不需要借助红细胞内的载体蛋白绑定。【混淆陷阱】只记住了葡萄糖随血液周流全身，却未能区分高水溶性溶质（溶解于血浆）与难溶气体（需红细胞载体）的运载载体差异。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Urea is a small, highly water-soluble nitrogenous metabolic waste product formed in the liver by deamination of amino acids. [Comparison]: Urea dissolves completely in aqueous blood plasma to be carried from the liver to the kidneys for ultrafiltration; it has zero affinity for haemoglobin. [Confusion Trap]: Incorrectly assuming that because urea is a waste product, it must be sequestered or bound inside red blood cells.",
            "cn": "【涉及知识点】尿素（Urea）是肝脏通过鸟氨酸循环将多余氨基酸脱下的有毒氨基合成的含氮代谢终产物，极易溶于水。【异同辨析】尿素在血浆中直接以溶解状态循环运送至肾小球进行滤过排出；其对红细胞内血红蛋白毫无亲和力，绝不由红细胞结合运输。【混淆陷阱】误以为代谢产生的毒性废物必须由专门的血细胞“封装隔离”运送，忽略了尿素直接溶于血浆运输的常识。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Hormones are endocrine chemical messengers, ranging from peptide hormones (e.g. insulin) to steroid hormones (e.g. testosterone). [Comparison]: Peptide hormones dissolve in plasma, while lipid-soluble steroids travel bound to soluble plasma proteins (albumin/globulins); none are carried inside red blood cells. [Confusion Trap]: Students know some hormones bind to carrier proteins, but confuse extracellular plasma transport proteins with intracellular haemoglobin inside red blood cells.",
            "cn": "【涉及知识点】激素（Hormones）是内分泌腺分泌的微量化学信使，涵盖多肽/蛋白类激素以及固醇类激素。【异同辨析】多肽类激素直接溶解在血浆中，脂溶性固醇类激素结合在血浆白蛋白或特异性球蛋白表面运行；两者均游离于细胞外液，绝不进入红细胞内部结合运输。【混淆陷阱】部分学生知道脂溶性激素需与载体蛋白结合，但混淆了“血浆载体蛋白（如白蛋白）”与“红细胞内血红蛋白”。"
        },
        "D": {
            "correct": True,
            "en": "[Concept]: Oxygen is a non-polar gas with extremely poor solubility in aqueous solutions (~0.3 mL per 100 mL of plasma). [Comparison]: Over 98.5% of oxygen is transported chemically bound to haemoglobin inside red blood cells, which drastically boosts blood's oxygen-carrying capacity seventy-fold. [Key Criteria]: Perfectly fulfills the prompt's criterion of being carried bound to a protein inside red blood cells.",
            "cn": "【涉及知识点】氧气（Oxygen）是非极性双原子分子，在以水为溶剂的血浆中物理溶解度极微（每100 mL血浆仅能溶解约0.3 mL氧）。【异同辨析】人体98.5%以上的氧气必须钻入红细胞内部，与高浓度的血红蛋白结合成氧合血红蛋白，使全血运氧能力提升近70倍；这与溶解在血浆中的葡萄糖、尿素形成鲜明对比。【核心考点】完全符合题干“在红细胞内部与特定蛋白质结合、而非直接溶解于血浆中”的唯一判据。"
        }
    },

    "Rev_SecA_Q08": {
        "A": {
            "correct": False,
            "en": "[Concept]: Bronchioles are narrow, muscular conduits (<1 mm diameter) branching off from secondary/tertiary bronchi within lung tissue, lacking cartilage rings. [Comparison]: Bronchioles are distal intrapulmonary passages leading directly to alveolar ducts; the trachea does not branch into bronchioles, but into primary bronchi first. [Confusion Trap]: Confusing the first-order primary branches (bronchi) with downstream microscopic branches (bronchioles) due to lexical similarities.",
            "cn": "【涉及知识点】细支气管（Bronchioles）是支气管进入肺叶深部后反复分支形成的管径小于1 mm的微细呼吸管道，管壁无软骨环支撑。【异同辨析】细支气管是支气管树末梢深入肺泡前的过度管道；气管并不直接分出细支气管，而是先在隆凸处分为左、右两根粗大的主支气管。【混淆陷阱】因词根形似（Bronchus 与 Bronchiole），混淆了第一级粗大主干（支气管）与深部微观末梢分支（细支气管）。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Alveoli (singular: alveolus) are microscopic, cup-shaped terminal air sacs surrounded by capillary networks where external gas exchange occurs. [Comparison]: Alveoli are microscopic functional gas-exchange units, not large conducting airways; they are located at the terminus of respiratory bronchioles, miles away from the tracheal bifurcation. [Confusion Trap]: Jumping straight to the final functional destination of inhaled air instead of naming the immediate intermediate conducting tube branching from the trachea.",
            "cn": "【涉及知识点】肺泡（Alveoli）是支气管树最末梢囊泡状微观结构，外缠致密毛细血管网，是肺部执行气体交换的核心功能单元。【异同辨析】肺泡是微观的囊状气体交换场所（单层上皮，直径仅0.2 mm），根本不是宏观的导气管道；气管绝不可能直接分支形成肺泡。【混淆陷阱】直觉式地跳跃到空气吸入的最终目的地（肺泡），而忽略了题干询问的是从气管分叉直接引向两肺的宏观管道。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: The bronchus (plural: bronchi) is the primary cartilaginous airway branching from the inferior end of the trachea into each lung. [Comparison]: The trachea bifurcates at the carina into the right and left primary bronchi, which enter the hilum of each respective lung to deliver incoming air. [Key Criteria]: Flawless anatomical match for the primary bifurcation of the mammalian trachea.",
            "cn": "【涉及知识点】支气管（Bronchus，复数形式为 Bronchi）是气管在胸腔内分为左、右两支的主干导气管，分别进入左肺和右肺。【异同辨析】气管（Trachea）下端隆凸处直接分为左主支气管与右主支气管，管壁同样具备C形软骨环以防塌陷，是将吸入气体分流引导至双侧肺脏的必经枢纽。【核心考点】完美对应剑桥教材中对呼吸道宏观解剖路径“气管（Trachea）→ 支气管（Bronchi）→ 肺（Lungs）”的标准界定。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The larynx (voice box) is a cartilaginous structure housing the vocal cords, positioned superior to the trachea in the anterior neck. [Comparison]: The larynx sits upstream of the trachea (air flows pharynx -> larynx -> trachea -> bronchi); it does not branch from the trachea, but rather leads down into it. [Confusion Trap]: Chronological and spatial reversal of the respiratory tract, placing the upstream voice box downstream of the windpipe.",
            "cn": "【涉及知识点】喉（Larynx/Voice box）是位于颈前正中部、连接咽部与气管上端的软骨性器官，内含声带。【异同辨析】喉位于气管的“上方（上游）”，是吸入空气进入气管之前的门户（空气路径：咽 → 喉 → 气管 → 支气管）；喉绝不从气管分出。【混淆陷阱】对上呼吸道与下呼吸道的解剖空间顺序发生记忆颠倒，误把位于气管上游的发声器官当成了气管下游的分支。"
        }
    },

    "Rev_SecA_Q09": {
        "A": {
            "correct": False,
            "en": "[Concept]: Label A points to the nasal cavity (conchae), which functions in the upper respiratory tract to filter dust, warm, and humidify incoming air. [Comparison]: The trachea (windpipe) is the conducting airway situated in the neck and upper chest inferior to the larynx, whereas label A is located inside the head/nasal region. [Confusion Trap]: Students often reflexively pick the uppermost label 'A' at the top of the diagram without tracing its leader line into the nasal cavity.",
            "cn": "【涉及知识点】标号A的指引线明确指向头面部的鼻腔（Nasal cavity），其核心生理功能是对吸入的冷空气进行黏膜过滤除尘、加湿与毛细血管加温。【异同辨析】气管（Trachea）是位于颈部喉部下方、纵贯进入胸腔的垂直软骨主干导管，而标号A深居头部鼻腔内；二者解剖系统与位置截然不同。【混淆陷阱】容易产生“盲目首选思维”，误以为最上方的第一个字母A一定代表气管，而未仔细顺着指引线观察其指向的是鼻腔。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: The trachea (windpipe) is the primary midline cartilaginous airway descending from the larynx into the thoracic cavity. [Mechanism]: In Figure 1, label B points directly to the central, non-branched vertical tube supported by C-shaped cartilage rings, located immediately inferior to the larynx and superior to the primary bronchi. [Key Criteria]: Precise visual identification of structure B as the trachea in Figure 1.",
            "cn": "【涉及知识点】气管（Trachea/Windpipe）是连接喉部与支气管的中央垂直主干导气管道，管壁具有特征性C形透明软骨环以维持气道长久通畅。【异同辨析】在图1解剖图谱中，标号B的指引线精准指向喉部正下方、进入胸腔且未分叉的单一中央大风管（气管）。【核心考点】准确契合剑桥大纲与教材图1图注中对气管（标号B）的解剖结构识别。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Label C points to the primary bronchus (plural: bronchi), the first-order division of the airway branching off the trachea into each lung hilum. [Comparison]: The bronchus is downstream of the tracheal bifurcation (carina); B is the unbranched trachea, whereas C represents the lateral branched bronchi entering the lung lobes. [Confusion Trap]: Confusing the single vertical parent trunk (B, trachea) with its lateral first-order branches (C, bronchi).",
            "cn": "【涉及知识点】标号C指向的是主支气管（Bronchus），即气管下端在隆凸处左右分叉后斜向进入单侧肺门的第一级主干分支管道。【异同辨析】气管（B）是未分叉的单一中央主干；而C已经处于分叉之后、分别导入左肺或右肺的侧支管道，属于气管的下游分支。【混淆陷阱】未能精确分辨气管主干（B）与主支气管（C）在分支节点前后的空间解剖关系。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Label D points to the intrapulmonary bronchioles, the fine tree-like arborizations branching extensively throughout the lung parenchyma towards alveoli. [Comparison]: Bronchioles are distal, narrower conducting passages lacking cartilage rings, located deeply within pulmonary lobes, far downstream from the central trachea (B). [Confusion Trap]: Confusing the deep intrapulmonary arborization (D) with the main external conducting windpipe (B).",
            "cn": "【涉及知识点】标号D指向的是肺实质内的细支气管树（Bronchioles），即支气管深入肺组织内部后进一步呈树枝状反复细分的小气道。【异同辨析】细支气管位于肺叶实质深层内部，管径纤细且无软骨环，远比位于上胸部中央粗大的气管主干（B）更靠末梢。【混淆陷阱】把肺实质内部深层分布的微细分支树（细支气管）与中央大风管（气管）发生图位混淆。"
        }
    },

    "Rev_SecA_Q10": {
        "A": {
            "correct": False,
            "en": "[Concept]: Inhaled air filtration is performed by mechanical trapping by nasal hairs and the mucociliary escalator (ciliated epithelial cells and goblet cells) lining the upper respiratory tract. [Comparison]: The diaphragm is a skeletal muscle lying beneath the lungs; it has zero direct contact with inspired air and possesses no cilia or mucus to filter particulates. [Confusion Trap]: Conflating the mechanical muscular pump that drives airflow with the protective conditioning tissues that line the airways.",
            "cn": "【涉及知识点】吸入空气的机械过滤与除尘功能是由鼻毛以及鼻腔、气管上皮表面的纤毛上皮细胞与黏液毯（纤毛电梯系统）共同完成的。【异同辨析】膈肌是位于胸腔底部的纯骨骼肌肉薄板，其与吸入的气流完全不接触，既无纤毛也无黏液腺，根本不参与空气过滤。【混淆陷阱】把为肺通气提供物理动力的“肌肉泵”（膈肌）与呼吸道黏膜上皮的“空气净化防御功能”混为一谈。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Mucus secretion is carried out by specialized epithelial goblet cells and submucosal glands embedded within the respiratory mucosa. [Comparison]: The diaphragm is composed strictly of somatic striated muscle fibres and connective tissue; it contains no glandular or epithelial tissue and secretes no mucus. [Confusion Trap]: Assigning mucosal glandular secretions to an external respiratory skeletal muscle.",
            "cn": "【涉及知识点】黏液分泌完全依赖分布于气道黏膜层的杯状细胞（Goblet cells）和黏膜下腺体，用以黏附空气中的灰尘与细菌。【异同辨析】膈肌是受躯体运动神经支配的横纹肌组织，胞内富含肌原纤维以执行收缩做功，绝无任何外分泌上皮腺体，绝不分泌黏液。【混淆陷阱】将上呼吸道黏膜上皮细胞的生化保护分泌功能，张冠李戴转移到负责呼吸力学的骨骼肌上。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: During active inhalation, the diaphragm contracts and pulls its dome downwards into a flattened shape. [Comparison]: This downward movement increases the vertical dimension and overall volume of the thoracic cavity, dropping intrapulmonary pressure below atmospheric pressure to suck air in. [Key Criteria]: The foundational mechanism of negative-pressure ventilation required by Cambridge curricula.",
            "cn": "【涉及知识点】在吸气（Inhalation）过程中，膈肌肌纤维在膈神经电冲动驱动下发生主动收缩，穹窿部向下移动并扁平化。【异同辨析】膈肌收缩下移直接扩大了胸腔的上下径（垂直容积），导致胸腔内压力下降并低于外界大气压，外界空气在负压抽吸作用下顺利涌入肺泡。【核心考点】精准契合剑桥大纲中关于吸气时“膈肌收缩变平、胸腔容积增大、胸内压下降”的标准力学机制。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Warming and humidifying incoming air to core body temperature (37°C) is mediated by extensive capillary beds in the vascularized nasal mucosa. [Comparison]: The diaphragm does not interface with the airstream; air warming occurs in the nasal cavity and upper airways long before air reaches the alveolar space. [Confusion Trap]: Misattributing nasal thermoregulatory adaptations to the muscular diaphragm at the base of the chest.",
            "cn": "【涉及知识点】将吸入空气加温加湿至37°C的核心场所是鼻腔，其黏膜固有层内密集交织着极其丰富的浅表毛细血管网。【异同辨析】外界冷空气刚进入鼻腔时便通过热传导被加温；膈肌深居腹胸交界处，空气从不流经膈肌，膈肌无法对其传导热量。【混淆陷阱】把鼻腔丰富的血管网行使的空气热力学加温作用，错误附会给胸腹交界处的膈肌。"
        }
    },

    "Rev_SecA_Q11": {
        "A": {
            "correct": False,
            "en": "[Concept]: A decrease in thoracic cavity volume occurs during exhalation, when the diaphragm relaxes (springing back into a dome) and external intercostal muscles relax (ribs move down and in). [Comparison]: During inhalation, active muscle contraction expands the chest in all dimensions; volume must increase, not decrease, to lower internal pressure. [Confusion Trap]: Inverting the mechanical phases of ventilation or confusing changes in volume with changes in pressure (volume increases while pressure decreases).",
            "cn": "【涉及知识点】胸腔容积减小发生在呼气（Exhalation）阶段，此时膈肌舒张恢复圆顶隆起，肋间外肌舒张使肋骨向下向内回缩。【异同辨析】吸气时骨骼肌的主动收缩是为了扩充胸廓三维空间；根据玻意耳定律，容积必须增大才能促使内部压力降低形成进气压差。选“减小”属于完全倒置。【混淆陷阱】呼吸力学方向性混乱；或者将“胸腔容积（增大）”与“胸内压（减小）”的变化趋势发生颠倒。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: During inhalation, the simultaneous contraction and flattening of the diaphragm and contraction of external intercostals (lifting the ribcage upwards and outwards) expands thoracic volume. [Comparison]: This expansion increases thoracic volume, which reduces alveolar pressure below atmospheric pressure to establish the pressure gradient driving air into the lungs. [Key Criteria]: The central physical principle of mammalian negative-pressure breathing.",
            "cn": "【涉及知识点】吸气过程中，膈肌收缩变平扩大胸腔垂直径，同时肋间外肌收缩提升肋骨并向外展开，扩大胸腔前后径与左右径。【异同辨析】两组肌肉的协同收缩显著增加了胸腔的总体积；容积增大必然导致胸腔内压低于外界大气压，迫使新鲜空气充盈肺泡。【核心考点】完美符合剑桥教学大纲中吸气时胸腔容积增大（Volume increases）的基本生理力学定律。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The thoracic cage is dynamic and compliant, consisting of moveable articulated ribs, costal cartilages, and flexible muscular partitions. [Comparison]: If thoracic volume remained constant, no pressure difference could be established, and air would not enter or leave the lungs (ventilation would cease entirely). [Confusion Trap]: Mistaking the bony skeletal thorax for a rigid, unyielding box that cannot alter its internal volume.",
            "cn": "【涉及知识点】胸廓是由胸椎、肋骨、肋软骨和胸骨构成的弹性活动骨架，具有优异的形变柔顺度以执行周期性换气。【异同辨析】若胸腔容积保持恒定不变，就无法形成任何气体流动所需的压力差，肺通气将瞬间停止导致窒息；容积恒定在生理学上是不可能的。【混淆陷阱】误以为骨骼构成的胸腔如同坚硬的刚性密闭木箱，忽略了肋软骨的活动度与呼吸肌的驱动力。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Respiration is strictly regulated by the respiratory rhythmicity center in the medulla oblongata and pons, firing rhythmic, cyclical motor impulses. [Comparison]: Thoracic volume follows a highly predictable, periodic oscillation corresponding to inspiration and expiration phases, never fluctuating randomly. [Confusion Trap]: Believing physiological biological systems lack precise neurological pacing and regulation.",
            "cn": "【涉及知识点】人体的呼吸运动受脑桥和延髓呼吸中枢的节律性神经冲动严格调控，呈现出高度精密的周期性节律。【异同辨析】吸气与呼气交替进行，胸腔容积的变化呈现平滑可预测的正弦曲线式周期振荡，绝对不是无规则、不可控的随机波动。【混淆陷阱】缺乏对自主神经系统调控节律的认知，误以为呼吸运动如同杂乱无章的布朗运动。"
        }
    },

    "Rev_SecA_Q12": {
        "A": {
            "correct": False,
            "en": "[Concept]: Fick's First Law states that the rate of diffusion is inversely proportional to membrane thickness and directly proportional to surface area and solubility. [Comparison]: Thick walls would drastically lengthen diffusion distance, small surface area would severely bottleneck total gas flux, and a dry lining would prevent gases from dissolving before crossing cell membranes. [Confusion Trap]: Selecting the complete opposite of every single structural adaptation required for efficient diffusion.",
            "cn": "【涉及知识点】菲克扩散定律（Fick's Law）明确指出：气体扩散速率与表面积呈正比，与扩散距离（厚度）呈反比，且气体必须溶于液体才能穿膜。【异同辨析】极厚的壁会使扩散距离急剧成倍增加，极小的表面积无法支撑代谢需氧量，干燥的内壁使氧气无法溶解穿过磷脂双分子层。这是低效的灾难性组合。【混淆陷阱】全盘逆转了适应性进化的方向，把每一个有利于气体交换的结构特征都选成了完全相反的阻碍特征。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Alveoli possess four quintessential evolutionary adaptations for gas exchange: single-cell-thick walls (<1 µm barrier), vast aggregate surface area (~70 m²), moisture film for gas dissolution, and extensive capillaries to maintain concentration gradients. [Comparison]: All four features simultaneously maximize diffusion rate by minimizing diffusion distance, maximizing exchange area, enabling molecular transition, and preserving steep gradients. [Key Criteria]: Flawless alignment with the standard Cambridge textbook gas exchange criteria.",
            "cn": "【涉及知识点】肺泡具备四大高度进化的气体交换结构特征：单层扁平上皮超薄壁、巨大的总表面积（约70平方米）、湿润内膜薄液层以及极度丰富的毛细血管网。【异同辨析】极薄管壁极大缩短了扩散距离，巨大面积提供了海量交换位点，水分薄膜确保氧气先溶解再弥散穿膜，密集血流不断带走氧气以维持陡峭的浓度差。四者协同达到极致效率。【核心考点】完整无瑕地涵盖了剑桥官方考纲所规定的“肺泡高效气体交换四大结构特征”标准答案。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Continuous capillary blood flow is essential to transport oxygen away and bring carbon dioxide in, maintaining steep partial pressure gradients across the alveolar wall. [Comparison]: Without a blood supply, oxygen in the alveolar air would rapidly equilibrate with the stagnant fluid, the concentration gradient would vanish, and net gas exchange would halt entirely. [Confusion Trap]: Partial feature matching where the mention of 'large surface area' blinds students to fatal flaws like thick walls and absent blood flow.",
            "cn": "【涉及知识点】血液持续不断的流动是维持肺泡与血液之间陡峭分压浓度差（Partial pressure gradient）的绝对前提。【异同辨析】若没有毛细血管血流供应，局部滞留的氧气迅速达到平衡，浓度梯度瞬间消失，气体交换彻底瘫痪；且厚壁更是阻碍穿透。【混淆陷阱】选项中混入了一个正确词汇（“巨大表面积”），制造了诱人陷阱，学生容易匆忙看上一半便忽视了后面致命的“无血液供应”。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Efficient gas exchange requires maximizing total surface area and providing a thin aqueous film for gases to dissolve prior to passive diffusion. [Comparison]: While thin walls are correct, a small surface area would provide insufficient gas transfer capacity for an endothermic human, and a dry surface would prevent oxygen molecules from dissolving and crossing the hydrophilic heads of cell membranes. [Confusion Trap]: Recognizing one correct adaptation ('thin walls') but overlooking the fatal shortcomings of small area and dryness.",
            "cn": "【涉及知识点】气体在穿过肺泡上皮细胞与毛细血管内皮细胞的磷脂双分子层时，分子必须首先溶解在极薄的表面液体层中。【异同辨析】虽然该项提到了“薄壁”，但“表面积狭小”无法满足人体巨大的基础代谢需氧量，而“干燥表面”导致氧分子无法完成水化溶解并扩散穿膜。【混淆陷阱】只看到部分正确的字眼（薄壁），而忽视了必须同时满足“湿润表面”与“巨大面积”这一协同必要条件。"
        }
    },

    "Rev_SecA_Q13": {
        "A": {
            "correct": False,
            "en": "[Concept]: Active transport is the carrier-protein-mediated movement of substances across cell membranes against a concentration gradient, requiring metabolic energy in the form of ATP. [Comparison]: Respiratory gases (O2 and CO2) are small, non-polar molecules that move strictly down partial pressure gradients without requiring ATP or membrane pumps; respiration uses passive diffusion, not active transport. [Confusion Trap]: Assuming that because gas exchange is crucial, fast, and vital to survival, the body must 'actively' burn energy to pump the gases.",
            "cn": "【涉及知识点】主动运输（Active transport）指借助膜载体蛋白逆浓度梯度跨膜转运微粒的过程，必须直接水解消耗细胞代谢能量（ATP）。【异同辨析】氧气和二氧化碳是非极性小分子，依靠分子热运动顺分压差自由穿透细胞膜双分子层，完全不消耗任何ATP，也无载体蛋白介导，绝非主动运输。【混淆陷阱】学生潜意识中认为气体交换对生命至关重要且极其高效，便误以为机体必须“主动消耗能量”去泵送气体。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Gas exchange across the alveolar-capillary membrane occurs entirely by passive net diffusion down partial pressure concentration gradients. [Comparison]: O2 moves from high partial pressure in alveolar air to lower partial pressure in deoxygenated blood; CO2 moves in reverse, driven purely by thermal kinetic energy without consuming cellular ATP. [Key Criteria]: The cornerstone biological physical mechanism of external respiration in Cambridge G8 Science.",
            "cn": "【涉及知识点】肺泡与毛细血管之间的气体交换纯粹依靠被动扩散作用（Diffusion），遵循物理学分压差扩散定律。【异同辨析】吸入的肺泡气中氧分压高于肺动脉端毛细血管血液，氧分子自发顺浓度差弥散入血；血液中二氧化碳分压高于肺泡气，自发顺浓度差向肺泡腔弥散排出，全程零能耗。【核心考点】精准契合剑桥大纲中关于肺部气体交换遵循顺浓度梯度被动物理扩散（Diffusion）的核心考点。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Osmosis is strictly defined as the net movement of water molecules from a region of higher water potential to lower water potential across a partially permeable membrane. [Comparison]: Osmosis refers exclusively to the solvent water; it does not describe the movement of gas molecules like O2 or CO2. [Confusion Trap]: Misusing 'osmosis' as a generic catch-all term for any passive transport process across biological membranes.",
            "cn": "【涉及知识点】渗透作用（Osmosis）在生物学中有严格的排他性定义：专指“水分子”顺水势差跨越半透膜的净移动过程。【异同辨析】渗透作用唯一适用的对象是溶剂水分子，绝不能用来描述气体分子（如氧气或二氧化碳）的移动。气体跨膜只能称作单纯扩散。【混淆陷阱】概念范畴泛化；学生容易将渗透作用当成一切跨膜被动过程的代名词，混淆了溶剂水与溶质气体的术语界限。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: High-pressure filtration (ultrafiltration) is the mechanical bulk movement of liquid and small solutes through a filter barrier driven by hydrostatic blood pressure, occurring in renal glomeruli. [Comparison]: Alveolar capillaries maintain low hydrostatic pressure to prevent fluid exudation into air sacs (pulmonary edema); gases move across membranes by individual molecular diffusion, not hydraulic bulk flow. [Confusion Trap]: Conflating renal hemodynamic filtration mechanisms with pulmonary alveolar gas transfer.",
            "cn": "【涉及知识点】高压滤过（High-pressure filtration/超滤）是指在强流体静压差驱动下，液体及微小溶质被强行挤过滤过膜孔径的流体动力学过程。【异同辨析】超滤作用发生在肾小球以产生原尿；而肺毛细血管必须维持较低的流体静压以防体液渗漏入肺泡（肺水肿），气体移动靠的是分子的自由弥散而非水压挤压。【混淆陷阱】把泌尿系统的肾小球血流动力学超滤机制，张冠李戴转移到呼吸系统肺泡膜的气体交换过程中。"
        }
    },

    "Rev_SecA_Q14": {
        "A": {
            "correct": False,
            "en": "[Concept]: Oxygen is consumed by metabolizing body cells during aerobic cellular respiration to generate ATP, making incoming venous blood low in oxygen. [Comparison]: Because alveolar air has a higher PO2 than pulmonary blood, oxygen diffuses INTO the blood from the alveoli, which is the exact opposite of the direction stated in the question. [Confusion Trap]: Directional reversal; confusing which respiratory gas enters the bloodstream versus which gas is eliminated.",
            "cn": "【涉及知识点】氧气（Oxygen）是组织细胞线粒体进行有氧呼吸合成ATP必需的原料气体，体循环消耗后使回心静脉血呈现低氧状态。【异同辨析】由于肺泡内氧分压显著高于毛细血管血液，氧气自发从肺泡“扩散进入血液”，方向与题干询问的“从血液扩散进入肺泡”完全相反。【混淆陷阱】生理方向性思维混乱；未能审清题干中气体流动的起点（血液）与终点（肺泡），将吸收的气体与排出的气体搞反。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Atmospheric nitrogen gas (N2) is chemically inert in the human body, comprising roughly 78% of both inhaled and exhaled air. [Comparison]: Because human tissues do not produce or consume nitrogen gas, its partial pressure in blood is in equilibrium with alveolar air; there is no net concentration gradient driving diffusion out of the blood. [Confusion Trap]: Students know nitrogen is the most abundant gas in breath, but confuse its passive, unchanged presence with active net excretion from blood.",
            "cn": "【涉及知识点】大气中的氮气（Nitrogen）在常温常压下属于化学惰性气体，占吸入和呼出空气体积的约78%。【异同辨析】人体组织细胞既不消耗氮气也不生成氮气，血液与肺泡气中的氮分压处于均等动态平衡状态，根本不存在顺梯度的净扩散过程。【混淆陷阱】学生知道呼出气体中氮气占比最高，容易误以为呼出的氮气也是机体代谢产生后从血液扩散排出的废物。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Carbon dioxide (CO2) is the primary gaseous metabolic waste product generated in mitochondria by the decarboxylation reactions of cellular respiration. [Comparison]: Pulmonary capillary blood arrives rich in CO2, establishing a higher PCO2 in blood than in alveolar air; CO2 readily diffuses down its gradient into the alveoli to be exhaled. [Key Criteria]: Exactly matches the biological definition of pulmonary gaseous waste excretion.",
            "cn": "【涉及知识点】二氧化碳（Carbon dioxide）是全身细胞线粒体进行有氧呼吸分解有机物碳骨架时产生的气态代谢终产物。【异同辨析】流经肺泡的静脉血中二氧化碳分压显著高于肺泡腔内气体分压，二氧化碳顺浓度差快速穿透毛细血管壁和肺泡壁，弥散进入肺泡腔准备呼出体外。【核心考点】准确切合剑桥大纲中关于细胞代谢废物二氧化碳从血液排入肺泡腔随呼气排出的核心结论。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Elemental hydrogen gas (H2) is not produced during mammalian cellular respiration. [Comparison]: Biochemical hydrogen atoms from glucose catabolism are transferred to coenzymes (NADH/FADH2) and combined with oxygen to yield water (H2O); free gaseous hydrogen does not circulate in blood or diffuse into alveoli. [Confusion Trap]: Confusing hydrogen ions (protons, H+) involved in ATP synthesis with molecular hydrogen gas (H2).",
            "cn": "【涉及知识点】人体哺乳动物的细胞呼吸代谢过程中，绝对不会产生游离的氢气单质气体（H2）。【异同辨析】细胞分解葡萄糖脱下的氢是以氢离子（H⁺）和高能电子形式传递给辅酶，最终在线粒体内膜与氧气结合生成水（H2O）；血液中根本没有需要排出的游离氢气分子。【混淆陷阱】将生化呼吸链中的氢离子/还原当量（[H]）与自然界的气态单质氢分子（H2）混为一谈。"
        }
    },

    "Rev_SecA_Q15": {
        "A": {
            "correct": False,
            "en": "[Concept]: Oxygen is a respiratory substrate tested chemically by relighting a glowing splint; it does not react with calcium hydroxide solution (limewater). [Comparison]: Furthermore, exhaled air contains LESS oxygen (~16%) than fresh ambient air (~21%), because oxygen has been extracted by tissues for cellular respiration. [Confusion Trap]: Mistaking limewater for a general gas reagent and forgetting that exhaled air has a lower, not higher, oxygen content.",
            "cn": "【涉及知识点】氧气（Oxygen）的化学检验特征是能够使带火星的木条复燃，其与澄清石灰水中的氢氧化钙不发生任何化学沉淀反应。【异同辨析】呼出气体中的氧气含量（约16%）显著低于吸入的新鲜空气（约21%），因为部分氧已被组织细胞呼吸消耗。题干强调“浓度更高”且“使石灰水浑浊”，氧气双重不符。【混淆陷阱】实验检测试剂记忆混乱；误以为澄清石灰水是通用的呼吸气体检测试剂，且忽视了呼出气氧浓度下降的事实。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Nitrogen gas is unreactive under biological conditions and does not form precipitates with alkaline solutions like limewater. [Comparison]: The percentage of nitrogen in exhaled air (~78%) is virtually identical to that in fresh air, because it is neither produced nor utilized by human cells. [Confusion Trap]: Assuming that because nitrogen is the most abundant gas in breath, it must cause the chemical precipitation in limewater.",
            "cn": "【涉及知识点】氮气在常温下分子结构具有极高键能，化学性质极不活泼，通入氢氧化钙溶液中完全不发生反应。【异同辨析】呼出气与吸入气中氮气浓度保持恒定（均约为78%），既没有浓度升高，也不可能与澄清石灰水反应产生白色浑浊。【混淆陷阱】把气体体积分数的“绝对数量最大”（氮气占78%）错误推论为引起化学试剂明显显色沉淀反应的诱因。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Limewater is a saturated aqueous solution of calcium hydroxide (Ca(OH)2), which serves as the diagnostic chemical test for carbon dioxide gas. [Comparison]: CO2 reacts with Ca(OH)2 to produce insoluble calcium carbonate (CaCO3), forming a milky-white cloudy suspension. Exhaled air contains ~4% CO2, roughly a hundred times higher than fresh air (~0.04%). [Key Criteria]: Classic school science laboratory indicator reaction for pulmonary CO2 excretion.",
            "cn": "【涉及知识点】澄清石灰水是氢氧化钙（Ca(OH)2）的饱和澄清溶液，是中学科学中检验二氧化碳气体的标准特效试剂。【异同辨析】呼出气中的二氧化碳浓度（约4%）是环境新鲜空气（约0.04%）的近100倍；CO2与石灰水反应生成难溶的碳酸钙（CaCO3）白色微细沉淀，使溶液呈现特征性乳白色浑浊。【核心考点】完全符合剑桥考纲中关于利用澄清石灰水变浑浊验证呼出气体中二氧化碳浓度显著升高的经典实验。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Haemoglobin is an intracellular globular protein permanently restricted inside red blood cells within blood vessels. [Comparison]: Under healthy conditions, haemoglobin never escapes blood capillaries or crosses into alveolar air; exhaling haemoglobin would mean severe, fatal pulmonary haemorrhage. [Confusion Trap]: Associating 'haemoglobin' broadly with respiration, but committing a gross anatomical absurdity by putting an intracellular blood protein into exhaled breath.",
            "cn": "【涉及知识点】血红蛋白（Haemoglobin）是严格包裹在血管内红细胞内部的高分子四聚体蛋白质，分子量达64 kDa。【异同辨析】正常人生理状态下，大分子蛋白质绝不可能穿透肺泡毛细血管屏障进入肺泡腔并随气体呼出（若呼出血红蛋白属于致死性肺出血咯血）。【混淆陷阱】在联想思维中机械套用“与呼吸相关的名词”，脱离了气体物理常识，把血管内的细胞内蛋白质当成呼出的气体成分。"
        }
    },

    "Rev_SecA_Q16": {
        "A": {
            "correct": False,
            "en": "[Concept]: The liver is the body's primary metabolic organ that deaminates surplus amino acids into urea and detoxifies poisons, secreting them into blood. [Comparison]: The liver manufactures urea, but it does NOT filter circulating blood to extract it as urine; blood-borne urea must travel to the kidneys to be filtered out into urine. [Confusion Trap]: Confusing the biochemical site of urea SYNTHESIS (liver) with the anatomical site of blood FILTRATION and urine FORMATION (kidneys).",
            "cn": "【涉及知识点】肝脏（Liver）是人体的化工厂，负责将过剩氨基酸脱氨基转化为毒性较低的尿素，并将毒素灭活后排入血液循环。【异同辨析】肝脏是尿素的“合成车间”而非“排泄器官”；肝脏本身没有毛细血管滤过膜和尿液排泄通道，真正滤过血液并生成尿液的器官是肾脏。【混淆陷阱】严重混淆了代谢废物尿素的“生化制造场所（肝脏）”与血液废物的“机械滤过排泄器官（肾脏）”。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: The kidneys are paired retroperitoneal organs receiving ~20% of resting cardiac output via the renal arteries to purify blood. [Comparison]: Each kidney contains around one million functional nephrons that execute ultrafiltration and selective reabsorption to remove metabolic waste (urea, excess salts, water) as urine. [Key Criteria]: Foundational organ-level definition of the human excretory system.",
            "cn": "【涉及知识点】肾脏（Kidneys）是人体主要的泌尿排泄器官，每分钟接受心输出量的约五分之一，负责滤过全血并调控内环境稳态。【异同辨析】肾脏内含有数百万个微观功能单元——肾单位（Nephrons），通过肾小球的高压超滤和肾小管的选择性重吸收，精准清除血液中的尿素与多余无机盐，生成终尿。【核心考点】准确契合剑桥大纲中关于肾脏是滤过血液产生尿液的核心排泄器官的解剖学定位。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The urinary bladder is a hollow, distensible muscular sac located in the pelvic cavity lined with transitional epithelium. [Comparison]: The bladder functions solely as a temporary storage reservoir for already-formed urine delivered by the ureters; it possesses no nephrons and cannot filter blood. [Confusion Trap]: Confusing urine storage and micturition (bladder) with blood filtration and urine production (kidneys).",
            "cn": "【涉及知识点】膀胱（Urinary bladder）是位于骨盆腔内的肌性囊状器官，内壁由可拉伸的移形上皮和逼尿肌构成。【异同辨析】膀胱仅行使“暂时储存终尿”的蓄水池功能，待充盈到一定体积时触发排尿反射；其内部没有任何肾单位结构，根本无法滤过血液制造尿液。【混淆陷阱】把尿液排泄系统下游的“储存容器（膀胱）”与上游负责高科技血液净化的“生产工厂（肾脏）”相混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The pancreas is a dual organ: an exocrine gland producing pancreatic digestive juice and an endocrine gland producing insulin and glucagon. [Comparison]: The pancreas regulates luminal digestion and blood glucose homeostasis; it does not receive blood for filtration and does not produce urine. [Confusion Trap]: Conflating abdominal glands involved in homeostasis with urinary organs.",
            "cn": "【涉及知识点】胰腺（Pancreas）是兼具外分泌与内分泌功能的双重器官，外分泌部分泌胰消化酶，内分泌部（胰岛）分泌胰岛素与胰高血糖素。【异同辨析】胰腺专职参与食物水解消化与全身血糖稳态调控，其解剖与生理功能完全独立于泌尿系统，不参与任何血液滤过或尿液生成。【混淆陷阱】对腹腔各内脏器官的功能定位模糊，在排泄题干下随意盲选熟悉的内脏腺体名称。"
        }
    },

    "Rev_SecA_Q17": {
        "A": {
            "correct": False,
            "en": "[Concept]: The urethra is the single terminal muscular tube leading from the bladder neck to the exterior of the body for urination. [Comparison]: The ureters carry urine from kidneys to bladder (paired conduits); the urethra carries urine from bladder to the external environment (single conduit). [Confusion Trap]: Severe lexical and spelling confusion between 'ureter' (输尿管) and 'urethra' (尿道) due to phonetic similarity.",
            "cn": "【涉及知识点】尿道（Urethra）是起始于膀胱颈、将终尿排出体外的单根肌性管道。【异同辨析】输尿管（Ureter）是左右成对的管道，连接“肾脏到膀胱”；而尿道（Urethra）是单独一根管道，连接“膀胱到外界”。二者上下游拓扑关系完全不同。【混淆陷阱】英语医学术语高频混淆点：由于 Ureter 与 Urethra 词根极度相似，学生极易混淆“输尿管”与“尿道”。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: The ureters are paired muscular tubes (one from each kidney) that convey urine from the renal pelvis to the urinary bladder. [Comparison]: Urine is propelled downwards through the ureters via rhythmic waves of smooth muscle peristalsis to fill the bladder. [Key Criteria]: Precise anatomical pathway for urine transport within the urinary system.",
            "cn": "【涉及知识点】输尿管（Ureter）是连接肾盂与膀胱的左右成对的细长肌性管道，全长约25–30 cm。【异同辨析】肾脏形成的终尿汇入肾盂后，由输尿管平滑肌节律性蠕动波驱动，由上至下单向输送并注入膀胱蓄存。这是连接肾脏与膀胱的唯一通道。【核心考点】精准对应剑桥考纲中关于终尿从肾脏运往膀胱的专属解剖管道——输尿管（Ureter）的标准考查。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The renal artery is a major high-pressure systemic blood vessel branching off the abdominal aorta to supply the kidney. [Comparison]: The renal artery carries oxygenated, unfiltered blood INTO the kidney; it transports blood, not urine, and runs aorta -> kidney, not kidney -> bladder. [Confusion Trap]: Confusing vascular blood supply (artery) with excretory urinary ductwork (ureter).",
            "cn": "【涉及知识点】肾动脉（Renal artery）是直接从腹主动脉分出的粗大血管分支，为肾实质提供高压含氧血液以供超滤。【异同辨析】肾动脉内流动的是“待滤过的动脉血”而非尿液，其走向是从“腹主动脉通往肾脏”，绝不通往膀胱。【混淆陷阱】概念范畴混淆；把循环系统供应血液的血管（肾动脉）与泌尿系统输送尿液的管道（输尿管）相混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The renal vein drains filtered, deoxygenated blood from the kidney and returns it to the inferior vena cava. [Comparison]: The renal vein transports purified blood back toward the heart; it contains blood rather than urine and does not connect to the bladder. [Confusion Trap]: Confusing the return blood pathway with the excretory urine conduit.",
            "cn": "【涉及知识点】肾静脉（Renal vein）是收集经肾单位净化、脱氧后的血液并注入下腔静脉返回心脏的主干静脉血管。【异同辨析】肾静脉运输的是“净化后的静脉血”并流向心脏，完全不参与尿液的引流，更不与骨盆底部的膀胱相通。【混淆陷阱】对肾脏进出液体的管道性质缺乏区分，混淆了血流回路（静脉）与排泄回路（输尿管）。"
        }
    },

    "Rev_SecA_Q18": {
        "A": {
            "correct": False,
            "en": "[Concept]: Carbon dioxide is generated in all cell mitochondria during cellular respiration via the link reaction and Krebs cycle. [Comparison]: CO2 results from the decarboxylation and complete oxidation of carbon skeletons from all fuels (carbs, fats, proteins), not specifically from nitrogenous amino acid deamination. [Confusion Trap]: Knowing carbon dioxide is a primary metabolic waste product, but failing to link nitrogen-containing amino acid breakdown specifically to urea.",
            "cn": "【涉及知识点】二氧化碳（Carbon dioxide）是机体所有活细胞在线粒体内通过有氧呼吸（三羧酸循环等）完全氧化碳骨架生成的呼吸废气。【异同辨析】CO2是由所有有机营养物（糖类、脂质、氨基酸）的碳链氧化脱羧产生的通用碳质废物，而非特异性源自肝脏对过剩氨基酸含氮基团的分解转化。【混淆陷阱】只记住了CO2是体内主要废物，却忽视了题干专门限定的“过剩氨基酸在肝脏中的特征性含氮分解产物”。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Glucose is a high-energy hexose monosaccharide that serves as the body's primary respiratory substrate for cellular energy. [Comparison]: Glucose is a valuable nutrient, not a toxic metabolic waste product; amino acid deamination removes nitrogen precisely so that the remaining carbon skeleton can be metabolized or converted. [Confusion Trap]: Confusing nutrient substrates with toxic excreted wastes.",
            "cn": "【涉及知识点】葡萄糖（Glucose）是富含高能化学键的六碳单糖，是机体最核心的能量供给底物和血液循环营养成分。【异同辨析】葡萄糖是宝贵的营养物质，绝不是机体排泄的毒性代谢废物；肝脏脱氨基的初衷正是排除含氮毒性并保留碳骨架转为能量。【混淆陷阱】思维缺乏逻辑界定；将维持生命运转的宝贵营养分子与必须被机体清除的毒性代谢废物倒置混淆。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Urea is the major nitrogenous excretory compound synthesized in the liver via the ornithine (urea) cycle. [Comparison]: When dietary amino acids exceed protein synthesis requirements, hepatocytes strip the amine group (-NH2) by deamination, converting toxic ammonia (NH3) into safer, water-soluble urea for excretion. [Key Criteria]: The standard Cambridge syllabus mechanism for hepatic nitrogenous excretion.",
            "cn": "【涉及知识点】尿素（Urea）是哺乳动物最主要的含氮代谢排泄物，由肝脏通过鸟氨酸循环合成并释放入血。【异同辨析】当人体摄入过量蛋白质时，体内无法储存氨基酸；肝细胞将过剩氨基酸进行脱氨基作用（Deamination），剥离出的剧毒游离氨迅速与二氧化碳结合为低毒溶于水的尿素。【核心考点】精准契合剑桥大纲中关于肝脏分解过剩氨基酸生成尿素（Urea）的专属代谢机制考查。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Glycogen is an insoluble, branched polysaccharide synthesized from glucose molecules and stored in hepatocytes and skeletal myocytes. [Comparison]: Glycogen is a safe, non-toxic polymeric storage form of carbohydrates, not a metabolic waste product generated from amino acid breakdown. [Confusion Trap]: Conflating the liver's role in macromolecular nutrient storage (glycogen) with its role in nitrogenous waste processing (urea).",
            "cn": "【涉及知识点】糖原（Glycogen）是由成千上万个葡萄糖分子聚合而成的多糖储能大分子，主要储存于肝脏和骨骼肌中。【异同辨析】糖原是机体极其重要的储备能源，在血糖低时可迅速水解回葡萄糖，绝不是被丢弃的代谢废物，也不含有氨基酸的氨基部分。【混淆陷阱】把肝脏合成的“营养储存大分子（糖原）”与肝脏解毒合成的“排泄废物分子（尿素）”相混淆。"
        }
    },

    "Rev_SecA_Q19": {
        "A": {
            "correct": False,
            "en": "[Concept]: Excretion is the removal from the body of toxic metabolic waste products produced by chemical reactions inside living cells (e.g. urea, CO2). [Comparison]: Metabolic waste comes from chemical cellular reactions; egestion involves unabsorbed, undigested dietary matter that traversed the gut lumen without ever crossing cell membranes. [Confusion Trap]: The single most notorious syllabus confusion in IGCSE Biology: confusing excretion (排泄, metabolic waste) with egestion (排遗, undigested gut residue).",
            "cn": "【涉及知识点】排泄（Excretion）在生物学中具有极其严密的定义：专指机体排出由细胞内生物化学代谢产生的毒性终产物（如二氧化碳、尿素等）。【异同辨析】代谢废物必须是细胞内生化反应的产物；而排遗针对的是从未被消化吸收、从未穿透肠壁上皮细胞进入体液的食物残渣。二者生理学本质完全不同。【混淆陷阱】整个剑桥生理学最经典的必考混淆陷阱：把细胞层面的“代谢排泄（Excretion）”与消化道末端的“食物排遗（Egestion）”混淆。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Egestion (defaecation) is strictly defined in biology as the expulsion of undigested, unabsorbed food material from the alimentary canal through the anus as faeces. [Comparison]: Because dietary fibre (cellulose) and unabsorbed bulk never entered the internal body cells or cellular metabolism, their discharge is classified as egestion, distinct from metabolic excretion. [Key Criteria]: The textbook-perfect Cambridge definition of egestion.",
            "cn": "【涉及知识点】排遗（Egestion）在剑桥官方大纲中严格界定为：未被消化或吸收的食物残渣（如植物纤维素）以粪便形式通过肛门排出体外。【异同辨析】食物残渣在消化道管腔内穿行，在解剖学拓扑结构上消化道管腔与外界环境相通；这部分残渣从未参与过人体细胞内的生化代谢，因而只能称作排遗。【核心考点】完全契合剑桥大纲中对排遗（Egestion）即“排出未消化的食物残渣”的唯一定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Regulating water balance and removing excess water is osmoregulation, executed primarily by the kidneys (urine) and skin (sweating). [Comparison]: Egestion involves the voiding of solid, unabsorbed dietary bulk via the anus, not selective fluid and electrolyte homeostasis. [Confusion Trap]: Assuming that because watery stools occur during diarrhoea, egestion is defined as removing excess water.",
            "cn": "【涉及知识点】调节体内多余水分和维持体液平衡属于渗透压调节（Osmoregulation），主要由肾脏排水和皮肤出汗完成。【异同辨析】排遗的实质是排出固态不可消化的膳食纤维和残渣；大肠的主要功能反而是尽量重吸收水分以防脱水，排遗绝非为了“专门排除多余水分”。【混淆陷阱】以腹泻等病理状态下的水样便为依据，产生局部片面联想，把排遗误解为排水稳态机制。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The elimination of carbon dioxide gas via exhalation from the lungs is pulmonary gaseous excretion. [Comparison]: Carbon dioxide is a cellular metabolic waste product discharged by the respiratory tract, having zero connection to the digestive alimentary canal or egestion. [Confusion Trap]: Lumping all physiological removal processes under one term without respecting the distinction between the digestive canal and the respiratory system.",
            "cn": "【涉及知识点】肺部呼出二氧化碳是呼吸系统执行的气态代谢产物排泄（Pulmonary excretion）。【异同辨析】二氧化碳来自组织细胞有氧呼吸，由呼吸道排出；它与消化道中食物残渣的物理排空毫无重叠。选此项属于跨器官系统的大概念错误。【混淆陷阱】把所有带有“排出体外”字眼的生理过程不加甄别地归纳，忽略了消化管与呼吸道的根本区别。"
        }
    },

    "Rev_SecA_Q20": {
        "A": {
            "correct": False,
            "en": "[Concept]: The renal tubule (proximal tubule, loop of Henle, distal tubule) carries out selective reabsorption of vital solutes and tubular secretion. [Comparison]: The renal tubule functions DOWNSTREAM after filtration has already occurred, recovering valuable glucose, amino acids, and water; it does not carry out the initial high-pressure filtration. [Confusion Trap]: Confusing the downstream site of nutrient recovery (renal tubule) with the upstream capillary filter (glomerulus).",
            "cn": "【涉及知识点】肾小管（Renal tubule，包括近曲小管、髓袢和远曲小管）专职对肾小囊中的原尿进行选择性重吸收与分泌。【异同辨析】肾小管位于滤过环节的“下游”；它负责将原尿中的全部葡萄糖、氨基酸及大部分水分拉回血液，本身不执行原尿生成的高压超滤操作。【混淆陷阱】未能厘清尿液生成的两步法时空顺序，将下游的“重吸收加工车间（肾小管）”与上游的“初级高压压滤机（肾小球）”混淆。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: The collecting duct receives processed filtrate from multiple distal convoluted tubules and executes final variable water reabsorption under the control of ADH. [Comparison]: The collecting duct is the terminal segment of the nephron system conveying concentrated urine to the renal pelvis; it concentrates urine rather than generating the initial filtrate. [Confusion Trap]: Confusing the final conduit that concentrates urine with the initial vascular knot that performs ultrafiltration.",
            "cn": "【涉及知识点】集合管（Collecting duct）汇集来自多个肾单位的终末小管液，并在抗利尿激素（ADH）精细调控下完成最后的水分重吸收以浓缩尿液。【异同辨析】集合管属于肾单位管道系统的终末汇流段，终尿由此滴入肾盏和肾盂；它完全不具备高压毛细血管网的初级滤过功能。【混淆陷阱】对肾单位各区段解剖定位模糊，将最后的尿液汇流管道当成了最前端的滤过起始点。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: The glomerulus is a dense, high-pressure knot of branching capillaries encapsulated within Bowman's capsule at the head of each nephron. [Comparison]: Because the afferent arteriole is wider than the efferent arteriole, high hydrostatic pressure forces water and small dissolved solutes through the basement membrane into Bowman's capsule (ultrafiltration). [Key Criteria]: Precise alignment with Cambridge curriculum terminology for ultrafiltration.",
            "cn": "【涉及知识点】肾小球（Glomerulus）是位于肾小囊（Bowman's capsule）凹陷内的球状毛细血管丛，连接入球小动脉与出球小动脉。【异同辨析】由于入球小动脉管径明显粗于出球小动脉，毛细血管丛内形成了极高的流体静水压，迫使水、葡萄糖、尿素等微小分子穿过滤过膜涌入肾小囊腔，完成初级高压超滤（Ultrafiltration）。【核心考点】准确契合剑桥考纲中关于肾小球（毛细血管球）是执行高压超滤起始结构的经典定义。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The ureter is a macroscopic, gross anatomical muscular duct transporting finished urine from the renal pelvis to the urinary bladder. [Comparison]: The ureter is an external conducting organ that transports bulk urine; it contains no microscopic nephrons, no filtration membranes, and performs zero blood filtration. [Confusion Trap]: Confusing macroscopic gross organ plumbing conduits with microscopic functional nephron units.",
            "cn": "【涉及知识点】输尿管（Ureter）是属于器官层面的宏观肌性输尿管道，直径数毫米，长达数十厘米。【异同辨析】输尿管是终尿形成的终极排泄管道，内部根本没有毛细血管滤过膜或肾单位微观结构，完全不参与血液成分的滤过。【混淆陷阱】发生严重的宏观解剖器官与微观细胞结构尺度错乱，把运送尿液的外部大管子误当成微观滤过结构。"
        }
    }
}
