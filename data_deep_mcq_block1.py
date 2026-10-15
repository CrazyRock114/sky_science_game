# -*- coding: utf-8 -*-
"""
data_deep_mcq_block1.py
Deep, concept-grounded distractor analyses for:
- Lesson 24 Housekeeping Exam: Q1 to Q10 (10 MCQs)
- Lesson 30 Housekeeping Exam: Q1 to Q10 (10 MCQs)

Each option contains:
- correct: bool
- en: [Concept] ... [Comparison] ... [Confusion Trap] ...
- cn: 【涉及知识点】... 【异同辨析】... 【混淆陷阱】...
"""

BLOCK1_DISTRACTORS = {
    # ==================== LESSON 24 HOUSEKEEPING EXAM (Q1 - Q10) ====================
    "L24_Review_MCQ_1": {
        "A": {
            "correct": False,
            "en": "[Concept]: Plasma is the liquid extracellular matrix (>90% water) transporting polar, water-soluble molecules. [Comparison]: Urea dissolves freely in aqueous plasma, whereas oxygen is virtually insoluble in water (<1.5% dissolved). Oxygen requires red blood cells packed with haemoglobin. [Confusion Trap]: Students often attribute all transport duties to plasma, forgetting that poorly soluble gases require dedicated intracellular carriers.",
            "cn": "【涉及知识点】血浆（Plasma）是占血液约55%的液体基质（90%以上为水），专职运输极性、高水溶性小分子。【异同辨析】尿素极易溶于水，作为溶解溶质在血浆中运至肾脏；而氧气在水中溶解度极低（<1.5%在血浆中物理溶解），必须依靠红细胞内的血红蛋白结合运输。二者运输介质与生化机制截然不同。【混淆陷阱】容易将“血液整体运输”与“血浆液体基质”混为一谈，误以为血浆运输一切体内物质。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Red blood cells (erythrocytes) are biconcave, anucleate discs packed with haemoglobin for respiratory gas transport. [Comparison]: Haemoglobin binds reversibly with oxygen in high-PO2 pulmonary alveoli (forming oxyhaemoglobin) and releases it in respiring tissues. [Key Criteria]: Perfect match with Cambridge syllabus definition for oxygen transport.",
            "cn": "【涉及知识点】红细胞（Red blood cells）呈双凹圆盘状、成熟后无核，胞内充满高浓度的含铁血红蛋白（Haemoglobin）。【异同辨析】在肺泡高氧分压环境下，血红蛋白与氧气结合为氧合血红蛋白；在全身组织低氧分压处解离释放氧气，是全身氧气运输的绝对主体（>98.5%）。【核心考点】完全符合剑桥教学大纲中红细胞作为专职运氧细胞的核心定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Blood clotting involves platelet activation and the conversion of soluble fibrinogen into an insoluble fibrin mesh. [Comparison]: Forming a fibrin net is a local haemostatic seal, not gas transport. Red blood cells only get passively trapped in the net to strengthen the plug. [Confusion Trap]: Conflating the components of a finished clot (which traps red cells) with the cells responsible for oxygen transport.",
            "cn": "【涉及知识点】血液凝固（Clotting）是由血小板激活引发的酶级联反应，将血浆纤维蛋白原转变为不溶性纤维蛋白网。【异同辨析】构建纤维蛋白网是为了封堵创口止血，与氧气运输毫无关联；红细胞只是被动被纤维网截留以加固血栓，不负责催化或主动生成纤维。【混淆陷阱】容易把血栓结构中“含有被捕获的红细胞”误解为“红细胞的功能是构建纤维网”。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Engulfing and digesting invading microbes is phagocytosis, carried out by specialized white blood cells (phagocytes). [Comparison]: Phagocytosis is an active, ATP-consuming endocytic immune defence. Red blood cells lack organelles, lysosomes, and motility, dedicating 100% of internal volume to haemoglobin. [Confusion Trap]: Confusing the distinct roles of the two main cellular lineages in blood (erythrocytes vs leucocytes).",
            "cn": "【涉及知识点】吞噬并消化病原体属于非特异性免疫吞噬作用（Phagocytosis），是由白细胞中的吞噬细胞（Phagocytes）执行的。【异同辨析】吞噬作用依赖伪足伸缩与溶酶体酶消化，属于耗能免疫防线；红细胞无细胞核、无溶酶体，无法执行吞噬，全胞空间专用于容纳血红蛋白运氧。【混淆陷阱】将血液两大主要细胞系的功能张冠李戴，混淆了红细胞（运氧）与白细胞（免疫）。"
        }
    },

    "L24_Review_MCQ_2": {
        "A": {
            "correct": False,
            "en": "[Concept]: Plasma provides the fluid suspension and circulates inactive soluble fibrinogen, but cannot initiate clotting. [Comparison]: Plasma cannot adhere to damaged collagen or secrete clotting factor cascades. Clotting initiation requires platelet receptor adhesion to exposed vessel collagen. [Confusion Trap]: Students confuse the raw substrate (plasma fibrinogen) with the initiating trigger (platelet activation).",
            "cn": "【涉及知识点】血浆（Plasma）提供液体介质并运输可溶性的非活性纤维蛋白原前体，但不具备创伤感知能力。【异同辨析】血浆自身无法特异性识别破损血管壁暴露的胶原纤维，不能主动释放启动因子；血小板才是感知损伤并分泌凝血激酶的触发者。【混淆陷阱】容易把凝血的“原料来源”（血浆中的纤维蛋白原）与凝血的“触发开关”（血小板激活）混淆。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: White blood cells (neutrophils, lymphocytes) defend against microbial infection via phagocytosis and antibody production. [Comparison]: Leucocytes fight pathogens in tissues; they do not trigger the coagulation cascade upon physical vessel cuts. [Confusion Trap]: Assuming that because white blood cells are part of the 'protective' system, they must also protect against blood loss.",
            "cn": "【涉及知识点】白细胞（White blood cells）是机体免疫卫士，通过吞噬作用或抗体中和作用杀灭侵入的微生物。【异同辨析】白细胞应对的是生物病原体入侵，不负责物理性血管破裂后的止血凝栓。启动止血级联的是血小板而非白细胞。【混淆陷阱】误以为白细胞作为“防御细胞”也承担防止血液流失的止血任务，混淆了免疫防御与机械止血。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Red blood cells transport respiratory gases (O2 and CO2) and lack granules or clotting enzymes. [Comparison]: In a clot, red blood cells are passive bystanders trapped in the fibrin mesh, providing bulk to the plug rather than biochemical initiation. [Confusion Trap]: Observing red color in a scab and incorrectly inferring that red blood cells created the clot.",
            "cn": "【涉及知识点】红细胞（Red blood cells）专职运送呼吸气体，胞内不含有任何凝血酶原激活物或分泌颗粒。【异同辨析】在形成的血栓中，红细胞只是被纤维网网罗拦截的被动填充物（增加血栓体积与密闭性），绝不释放凝血因子启动凝血。【混淆陷阱】直观看到血痂是红色的，便误以为是红细胞“启动”了血液凝固。"
        },
        "D": {
            "correct": True,
            "en": "[Concept]: Platelets (thrombocytes) are specialized cell fragments containing dense alpha-granules and clotting factors. [Comparison]: Upon vessel injury, platelets adhere to subendothelial collagen, change shape, aggregate into a platelet plug, and release clotting factors that activate prothrombin into thrombin. [Key Criteria]: Flawless alignment with the syllabus description of clotting initiation.",
            "cn": "【涉及知识点】血小板（Platelets）是骨髓成熟巨核细胞裂解产生的无核胞质碎片，胞内储有丰富的凝血活性物质。【异同辨析】当血管内皮破损暴露出底层胶原纤维时，血小板迅速黏附变性，聚集形成血小板止血栓，并释放凝血因子激活凝血酶级联，使可溶纤维蛋白原变成不溶纤维网。【核心考点】准确契合剑桥大纲中血小板启动止血与凝血的核心生理机制。"
        }
    },

    "L24_Review_MCQ_3": {
        "A": {
            "correct": True,
            "en": "[Concept]: Blood plasma is an aqueous transport solution containing dissolved nutrients (glucose, amino acids), excretory wastes (urea), dissolved gases (HCO3-), and endocrine hormones. [Comparison]: Plasma transports all water-soluble metabolic products throughout the body. [Key Criteria]: Fully matches Cambridge textbook Table B7.02.",
            "cn": "【涉及知识点】血浆（Plasma）是含水率高达90%以上的循环介质，是全身水溶性营养素、代谢废物及化学信使的主要运输载体。【异同辨析】血浆通过水分子溶剂化作用稳定溶解葡萄糖、氨基酸、尿素、碳酸氢根离子及激素分子，运送至各组织或排泄器官。【核心考点】完美契合剑桥教材对血浆运输可溶性物质（尿素、激素、二氧化碳等）的官方考点要求。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Oxygen is a non-polar gas with extremely poor solubility in water (Henry's law constant limits physical solution to <0.3 mL O2 / 100 mL blood). [Comparison]: Plasma carries <1.5% of total blood oxygen; >98.5% is chemically bound inside red blood cells to haemoglobin. [Confusion Trap]: Confusing the carrier of carbon dioxide (mostly in plasma as HCO3-) with the carrier of oxygen (strictly in red blood cells).",
            "cn": "【涉及知识点】氧气（Oxygen）是非极性双原子气体，在水中的物理溶解度极低（100毫升血浆常温常压仅溶解约0.3毫升氧）。【异同辨析】血浆仅能以游离分子形式运载不到1.5%的氧，绝大多数（>98.5%）的氧气依靠红细胞内的血红蛋白结合运输。相反，二氧化碳主要在血浆中以碳酸氢根形式运送。【混淆陷阱】容易把二氧化碳的运输方式（大部分在血浆中）与氧气的运输方式（绝大部分在红细胞内）相互混淆。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Fibrin is an insoluble filamentous protein polymer formed only at localized sites of vascular injury. [Comparison]: Soluble fibrinogen circulates in plasma, but insoluble fibrin threads do not circulate freely; systemic circulating fibrin would cause fatal thrombosis (stroke/infarction). [Confusion Trap]: Confusing the soluble precursor (fibrinogen) with the insoluble active mesh (fibrin).",
            "cn": "【涉及知识点】纤维蛋白（Fibrin）是不溶性的固态蛋白质纤维网，仅在局部血管损伤破裂处临时聚合并沉积。【异同辨析】血浆正常循环运输的是可溶性前体纤维蛋白原（Fibrinogen），不溶性的纤维蛋白网绝不作为循环溶质在血液中流转，否则将引发致命的广泛血栓与血管栓塞。【混淆陷阱】混淆了可溶性的循环前体蛋白（纤维蛋白原）与不溶性的局部终产物（纤维蛋白网）。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Haemoglobin is an intracellular tetrameric protein strictly compartmentalized inside red blood cells. [Comparison]: Free haemoglobin does not circulate in normal plasma; if released (haemolysis), it precipitates, blocks renal tubules, and causes acute kidney injury. [Confusion Trap]: Students know haemoglobin is in blood, but mistakenly assume it floats freely in plasma liquid.",
            "cn": "【涉及知识点】血红蛋白（Haemoglobin）是专职包裹在红细胞细胞质内部的四聚体呼吸色素蛋白。【异同辨析】正常生理状态下，血浆中几乎没有游离血红蛋白；游离血红蛋白属于血管内溶血的病理表现，会阻塞肾小球滤过孔并造成严重肾毒性损伤。【混淆陷阱】考生知道血液中富含血红蛋白，但容易错误假设血红蛋白是“直接游离溶解在血浆液体中”。"
        }
    },

    "L24_Review_MCQ_4": {
        "A": {
            "correct": False,
            "en": "[Concept]: Egestion is the expulsion of undigested, unabsorbed food residue through the anus as faeces in the digestive system. [Comparison]: Egestion involves materials that never entered body cells or crossed epithelial membranes. Phagocytosis is an intracellular immune mechanism engulfing living pathogens inside tissues. [Confusion Trap]: Both involve passing or moving bulk matter, but egestion is an alimentary disposal, not cellular engulfment.",
            "cn": "【涉及知识点】排遗（Egestion）指消化系统末端将未被消化或吸收的食物残渣（粪便）经肛门排出体外的过程。【异同辨析】排遗物实质上从未穿透上皮细胞进入人体内环境；而吞噬作用是体内的免疫细胞（如吞噬细胞）通过变形运动主动摄取并消灭组织中的活体病原微生物。【混淆陷阱】两个词都有“排除/排出”的宏观印象，但排遗是消化道残渣排出，吞噬是白细胞内部杀菌。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Excretion is the removal of toxic metabolic waste products produced by intracellular chemical reactions (e.g. urea, CO2, sweat). [Comparison]: Excretion removes chemical by-products of metabolism out of the organism. Phagocytosis is an internal cellular defence destroying invading microbes. [Confusion Trap]: Conflating cellular destruction of foreign invaders with metabolic waste removal.",
            "cn": "【涉及知识点】排泄（Excretion）特指机体将细胞内部新陈代谢过程中产生的化学毒性终产物（如尿素、二氧化碳等）排出体外的生理过程。【异同辨析】排泄清除的是自身细胞代谢产生的“小分子分子垃圾”；而吞噬作用是免疫防卫，消灭的是外源入侵的“外来活体病原细胞”。【混淆陷阱】混淆了“细胞生物防卫（吞噬）”与“代谢化学废物清除（排泄）”的本质界限。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Phagocytosis is a specialized form of endocytosis by phagocytic white blood cells (macrophages, neutrophils). [Comparison]: The phagocyte extends pseudopodia around the pathogen, encloses it in a phagosome vesicle, and fuses it with lysosomes containing hydrolytic lysozymes to digest it completely. [Key Criteria]: Exact syllabus definition for pathogen engulfment by white blood cells.",
            "cn": "【涉及知识点】吞噬作用（Phagocytosis）是吞噬细胞（如巨噬细胞、中性粒细胞）特有的内吞性免疫防卫机制。【异同辨析】吞噬细胞伸出伪足将病原体完全包裹，形成吞噬体并与胞内溶酶体融合，利用水解酶将其彻底消化分解为无害小分子。【核心考点】完全对应剑桥教材中白细胞包围、摄入并胞内酶解病原体的权威标准术语。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Assimilation is the uptake and chemical incorporation of absorbed nutrient molecules (e.g. amino acids, glucose) into cell structures. [Comparison]: Assimilation uses digested nutrients to build cellular components (e.g. protein synthesis). Phagocytosis captures foreign invaders to destroy them. [Confusion Trap]: Confusing the cellular uptake of nutrients for growth with cellular engulfment of pathogens for defence.",
            "cn": "【涉及知识点】同化作用（Assimilation）指细胞吸收血液运送来的小分子可溶性养分，并将其转化为自身原生质结构或储能分子的过程。【异同辨析】同化作用是“利用营养建设自身细胞”，属于营养代谢过程；吞噬作用是“吞入外来病原体并将其摧毁”，属于免疫防御动作。【混淆陷阱】两者都包含“物质进入细胞内部”，但同化作用是吸收养料自用，吞噬作用是捕获杀灭敌对病原体。"
        }
    },

    "L24_Review_MCQ_5": {
        "A": {
            "correct": False,
            "en": "[Concept]: Urea is a small, highly water-soluble nitrogenous metabolic waste product synthesized by the liver during amino acid deamination. [Comparison]: Urea is excreted dissolved in urine and sweat; it has zero structural or clotting properties. Fibrin is an insoluble fibrous protein net. [Confusion Trap]: Random chemical substance confusion; urea is a waste solute, not a structural blood mesh.",
            "cn": "【涉及知识点】尿素（Urea）是肝脏对多余氨基酸脱氨基产生的低分子量含氮代谢终产物，具有极高的水溶性。【异同辨析】尿素随血液运送至肾脏溶解排泄，不具备任何机械交联或结构成网特性；而构成血栓骨架的是长链纤维状不溶性蛋白质（纤维蛋白）。【混淆陷阱】名词辨识模糊，将水溶性的排泄废物（尿素）与伤口处不溶性的机械网状蛋白（纤维蛋白）混淆。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Fibrin is an insoluble, fibrous structural protein polymer. [Comparison]: During coagulation, the active enzyme thrombin cleaves soluble fibrinogen, polymerization forms long insoluble fibrin strands that weave a sticky 3D mesh across the wound, trapping blood cells and platelets to form a stable red clot. [Key Criteria]: Direct match for the insoluble mesh trapping blood cells.",
            "cn": "【涉及知识点】纤维蛋白（Fibrin）是由血浆可溶性纤维蛋白原在凝血酶催化下裂解聚合而成的不溶性纤维状大分子蛋白质。【异同辨析】纤维蛋白单体相互交织聚合成坚韧的三维立体纤维网，机械性地截留红细胞与血小板，形成不可溶的凝块封死伤口并防止进一步失血与病原体入侵。【核心考点】精准对应教材中“网罗血细胞形成血栓的不溶性纤维网”的考点定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Haemoglobin is an intracellular globular transport protein containing four haem iron groups packaged inside red blood cells. [Comparison]: Haemoglobin carries oxygen in solution inside cells; it is a soluble globular protein, not an insoluble fibrous structural mesh. [Confusion Trap]: Confusing the red pigment found inside trapped cells with the structural mesh that traps them.",
            "cn": "【涉及知识点】血红蛋白（Haemoglobin）是严格储存在红细胞内部的含铁四聚体球状运输蛋白。【异同辨析】血红蛋白是球状水溶性蛋白，专职可逆结合氧气，不能在创口交联成结构纤维网；纤维蛋白则是不溶性的纤维状硬蛋白。【混淆陷阱】因为血栓是红色的，学生容易把被捕获细胞内部的红色色素（血红蛋白）与网罗细胞的支架蛋白（纤维蛋白）搞混。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Blood plasma is the liquid extracellular fluid matrix of blood, consisting of water and suspended proteins. [Comparison]: Plasma is the liquid carrier medium, not an insoluble solid mesh. Fibrin precipitates *out of* plasma during clotting. [Confusion Trap]: Confusing the surrounding fluid with the solid mesh that forms within it.",
            "cn": "【涉及知识点】血浆（Plasma）是占全血体积55%的流动性液体基质，本身绝非固体网络。【异同辨析】血浆为血细胞与凝血因子提供流动的液体悬浮环境；纤维蛋白网是在凝血酶催化下从血浆中析出并交联的不溶性固态网状纤维。【混淆陷阱】容易把宏观的液体环境（血浆）与在其中析出交联的微观固体网状物（纤维蛋白）混淆。"
        }
    },

    "L24_Review_MCQ_6": {
        "A": {
            "correct": True,
            "en": "[Concept]: The trachea (windpipe) is the primary cartilaginous airway running from the larynx down the midline of the thorax. [Comparison]: At its inferior end (carina), the trachea bifurcates into the left and right primary bronchi. It is reinforced with C-shaped hyaline cartilage rings to keep the airway permanently open. [Key Criteria]: Matches anatomical pathway connecting throat/larynx to bronchi.",
            "cn": "【涉及知识点】气管（Trachea/Windpipe）是位于颈部正中及胸腔上部、由16-20个C形透明软骨环支撑的气道主干。【异同辨析】气管向上通过喉部（Larynx）连接咽喉，向下在胸骨角水平分为左、右主支气管（Bronchi），是气体出入肺部的唯一必经主通道。【核心考点】完美对应教材中“连接咽喉部与左右支气管的主气道”的解剖学位置与结构特性。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: The ureter is a muscular excretory duct connecting the renal pelvis of each kidney to the urinary bladder. [Comparison]: The ureter transports urine in the excretory system, located retroperitoneally in the abdomen and pelvis, completely unrelated to the respiratory trachea. [Confusion Trap]: Morphological confusion between two Latin-derived tubular terms starting with 'U' vs respiratory airways.",
            "cn": "【涉及知识点】输尿管（Ureter）是属于泌尿排泄系统的成对肌性细长管道，起于肾盂，止于膀胱。【异同辨析】输尿管位于腹膜后间隙及盆腔内，专职依靠蠕动波将尿液从肾脏泵入膀胱，与呼吸道气管（Trachea）属于完全不同的器官系统。【混淆陷阱】解剖学名词混淆，将泌尿系统的输尿管（Ureter）误记为呼吸系统的管道。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The oesophagus (gullet) is a collapsible muscular tube connecting the pharynx to the stomach in the digestive system. [Comparison]: The oesophagus lies posterior to the trachea and conducts food boluses by peristalsis. It contains no cartilage rings and does not connect to bronchi. [Confusion Trap]: The trachea and oesophagus run parallel in the neck; students mix up the airway (trachea) with the food pipe (oesophagus).",
            "cn": "【涉及知识点】食道（Oesophagus/Gullet）属于消化系统，是连接咽部与胃底的平滑肌肌性消化管道。【异同辨析】食道紧贴气管后方下行，管壁无软骨环支撑，平时呈塌陷状态，依靠蠕动波向胃输送食团；而气管位于食道前方，由软骨支撑永不闭合，通向支气管。【混淆陷阱】两者在颈部前后平行排列，学生最常把“气管（Trachea）”与“食管（Oesophagus）”的解剖位置与连通目标混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The urethra is the terminal excretory duct running from the urinary bladder to the exterior of the body. [Comparison]: The urethra drains finished urine during micturition (and semen in males), situated at the base of the pelvis, completely distinct from thoracic airways. [Confusion Trap]: Phonic and spelling confusion between 'urethra', 'ureter', and 'trachea'.",
            "cn": "【涉及知识点】尿道（Urethra）是泌尿系统的最末端排泄通道，起自膀胱底部的内口，开口于体表。【异同辨析】尿道位于盆腔最下方，负责将膀胱中暂存的尿液排出体外（男性还兼任排精），与胸腔内的呼吸主干气道毫无关联。【混淆陷阱】容易把英文形似的三大管道名词 Urethra（尿道）、Ureter（输尿管）和 Trachea（气管）在拼写和功能上混淆。"
        }
    },

    "L24_Review_MCQ_7": {
        "A": {
            "correct": False,
            "en": "[Concept]: Fick's Law of Diffusion dictates that rate of gas diffusion is inversely proportional to membrane thickness (Diffusion distance). [Comparison]: Thick muscular walls would drastically lengthen diffusion distance, creating an insurmountable diffusion barrier that would suffocate the organism. Alveolar walls are extremely thin (one cell thick, ~0.1-0.5 µm). [Confusion Trap]: Assuming that a 'robust' or 'muscular' organ design is always better, ignoring the physics of gas diffusion.",
            "cn": "【涉及知识点】菲克扩散定律（Fick's Law）表明：气体分子扩散速率与扩散距离（膜厚度）成严格反比。【异同辨析】厚实多肌的管壁会极大增加氧气穿透的阻力与时间延迟，彻底扼杀气体的迅速扩散；肺泡壁特化为单层扁平上皮细胞（厚度仅0.1微米级），旨在最大化缩短弥散距离。【混淆陷阱】直觉上误以为器官“壁厚结实、有肌肉”就更好，忽略了气体交换器官的首要适应性必须是“极度菲薄”。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Alveoli provide an immense exchange surface area (~70-100 m² in an adult, equivalent to half a tennis court) packed into ~300-500 million microscopic sacs. [Comparison]: A small surface area would severely throttle the volume of oxygen entering blood per second. High surface area is essential to meet human metabolic demands. [Confusion Trap]: Confusing the tiny microscopic size of an individual alveolus with the collective total surface area of all alveoli combined.",
            "cn": "【涉及知识点】人体双肺约有3亿至5亿个肺泡，其总内表面积高达70-100平方米（相当于半个网球场大小）。【异同辨析】表面积越广阔，每秒能同时扩散透过的氧气分子总数就越多；狭小的表面积根本无法满足温血恒温动物庞大的耗氧代谢。【混淆陷阱】学生把单个肺泡微观尺寸的“微小（Small）”错误等同于全部肺泡集合后的“总表面积狭小（Small surface area）”。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Alveoli are evolutionarily optimized for rapid passive diffusion: their walls are one single squamous epithelial cell thick, lined with a thin moisture film, and surrounded by dense capillary networks. [Comparison]: Single-cell walls minimize diffusion distance (<1 µm), while continuous blood flow maintains a steep partial pressure gradient (high PO2 in alveoli, low PO2 in deoxygenated capillary blood). [Key Criteria]: Exact match for Cambridge syllabus gas exchange adaptations.",
            "cn": "【涉及知识点】肺泡是气体交换的终极微观功能单位，其结构适应性表现为：壁薄（仅一层扁平上皮细胞）、面大（总面积近百平米）、湿润（利于气体溶解）、血流密集。【异同辨析】单层细胞使氧气与二氧化碳的扩散距离缩短至1微米以内；密布的毛细血管网不断运来低氧缺氧血并带走氧合血，时刻维持陡峭的气体浓度梯度差。【核心考点】教科书关于肺泡适应气体交换特征（薄壁、大面积、密布毛细血管）的标准满分答案。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Oxygen gas cannot diffuse across dry cellular membranes; it must first dissolve into an aqueous phase before crossing lipid bilayers. [Comparison]: Alveoli are lined with a microscopic film of aqueous pulmonary fluid containing surfactant. Completely dry alveoli would prevent oxygen dissolution and cause membrane desiccation and collapse. [Confusion Trap]: Students mistakenly think 'dry' avoids drowning, not realizing that gases must dissolve in fluid to cross cell membranes.",
            "cn": "【涉及知识点】气体分子无法直接穿透干燥的固态蛋白质脂质膜，必须先在液相中物理溶解，才能顺浓度梯度穿透细胞膜。【异同辨析】肺泡内壁覆盖着极薄的液体水分薄膜（含肺表面活性物质），使吸入的氧气先在此溶解再穿膜扩散；完全干燥的表面会导致气体无法溶解穿透，且上皮细胞会脱水坏死。【混淆陷阱】常识性误以为肺里“越干燥越好”，不知道生物体所有气体交换界面（肺泡、鳃、皮肤）都必须保持湿润。"
        }
    },

    "L24_Review_MCQ_8": {
        "A": {
            "correct": False,
            "en": "[Concept]: Emulsification is the physical breakdown of large lipid droplets into tiny emulsion droplets by bile salts in the duodenum. [Comparison]: Emulsification occurs in the digestive tract to increase surface area for lipase; it involves mechanical detergent action on fats, not gas movement across alveolar membranes. [Confusion Trap]: Category error mixing up chemical digestion of dietary lipids with alveolar respiration.",
            "cn": "【涉及知识点】乳化作用（Emulsification）指十二指肠内胆汁酸盐将大脂肪颗粒物理分散为微小乳滴的过程。【异同辨析】乳化作用发生在消化道腔内，目的是为胰脂肪酶提供更大的作用表面积，属于物理性消化；与肺泡膜两侧氧气和二氧化碳的跨膜交换毫无关联。【混淆陷阱】概念范畴混淆，将消化系统对脂肪的机械分散（乳化）错误挪用到呼吸系统气体交换上。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Gas exchange in the lungs is governed strictly by passive physical diffusion down partial pressure concentration gradients. [Comparison]: Alveolar air has high PO2 (~104 mmHg) and low PCO2 (~40 mmHg), whereas deoxygenated capillary blood has low PO2 (~40 mmHg) and high PCO2 (~45 mmHg). Oxygen spontaneously diffuses from alveoli into blood without cellular energy expenditure. [Key Criteria]: Textbook mechanism for all biological gas exchange.",
            "cn": "【涉及知识点】扩散作用（Diffusion）是指粒子顺浓度梯度（或气体分压差）从高浓度区域向低浓度区域进行的净随机物理移动。【异同辨析】吸入的肺泡气中氧气分压显著高于进入肺毛细血管的脱氧静脉血，氧气分子顺分压梯度自发穿过肺泡壁和毛细血管壁弥散进入血液，全程不消耗细胞ATP。【核心考点】完全契合教材考点：人体肺部所有的气体交换机制纯粹依赖被动物理扩散（Diffusion）。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Ingestion is the mechanical act of taking food and drink into the body through the oral cavity (mouth). [Comparison]: Ingestion is the entry phase of the digestive system. Gas exchange in the lungs moves respiratory molecules into the blood across internal epithelia. [Confusion Trap]: Confusing the entry of food through the mouth with the microscopic diffusion of oxygen in the lungs.",
            "cn": "【涉及知识点】摄食（Ingestion）特指动物通过口腔将食物与液体送入体内消化道的行为动作。【异同辨析】摄食是消化系统的第一步（进食），发生在口腔；而肺泡中的气体交换发生在深部呼吸道末端的微观细胞界面，通过扩散使气体进入循环系统。【混淆陷阱】字面混淆，误以为氧气“进入人体”都可以泛称为摄食（Ingestion）。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Egestion is the discharge of undigested, unabsorbed solid food residue from the alimentary canal via the anus as faeces. [Comparison]: Egestion removes bulk digestive waste from the bowel. Pulmonary gas exchange moves oxygen into blood and carbon dioxide out of blood. [Confusion Trap]: Random process confusion between lower bowel defaecation and respiratory alveolar gas exchange.",
            "cn": "【涉及知识点】排遗（Egestion）指未被消化的植物纤维及食物残渣以粪便形式从直肠和肛门排出体外。【异同辨析】排遗是肠道固体废弃物的机械排出；而肺部气体交换是呼吸系统通过极薄细胞层进行的分子级气体吸收与交换。【混淆陷阱】消化道末端排便（排遗）与肺部吸收氧气（扩散）风马牛不相及，属于纯粹的干扰项辨识错误。"
        }
    },

    "L24_Review_MCQ_9": {
        "A": {
            "correct": False,
            "en": "[Concept]: The liver synthesizes urea (from toxic ammonia via deamination) and secretes bile into the gall bladder for lipid emulsification. [Comparison]: While the liver *creates* urea, it cannot filter blood to form urine; it dumps urea into blood circulation. The kidneys must physically filter that blood to excrete the urea as urine. [Confusion Trap]: Conflating the chemical factory that synthesizes urea (liver) with the mechanical filter that excretes it (kidneys).",
            "cn": "【涉及知识点】肝脏（Liver）是人体化工厂，负责将多余氨基酸脱氨基转化为无毒的尿素，并分泌胆汁储存在胆囊中。【异同辨析】肝脏仅仅是尿素的“制造者”，制造后直接释放入血液循环，本身不具备过滤血液制造尿液的能力；肾脏才是将血液中尿素滤出并生成尿液的“排泄过滤器”。【混淆陷阱】最经典的考点陷阱！学生极易混淆：合成尿素的是肝脏（Liver），而滤过血液生成尿液的是肾脏（Kidneys）。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: The paired kidneys are the primary organs of the urinary excretory system, containing ~1 million nephrons each. [Comparison]: Renal arteries branch directly from the aorta, delivering high-pressure blood to glomeruli where ultrafiltration forces water, urea, and small solutes into Bowman's capsule, forming urine after selective tubular reabsorption. [Key Criteria]: Exact syllabus definition of the blood-filtering, urine-producing organ.",
            "cn": "【涉及知识点】肾脏（Kidneys）是泌尿系统的核心排泄器官，每侧肾脏包含约100万个微观功能单位——肾单位（Nephrons）。【异同辨析】肾动脉引入全身五分之一的高压心输出血流，在肾小球处进行超滤过，将代谢废物（尿素、尿酸、多余无机盐）及水分滤入肾小管，经选择性重吸收后形成终尿。【核心考点】完美契合剑桥大纲中专职“滤过血液代谢废物并生成尿液”的器官定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The urinary bladder is a distensible muscular storage reservoir, and the urethra is the exit conduit to the outside. [Comparison]: Neither the bladder nor the urethra contains nephrons or blood-filtering capillary beds. They merely store and evacuate urine already produced upstream by the kidneys. [Confusion Trap]: Confusing the collection/evacuation plumbing (bladder/urethra) with the active filtration organ (kidneys).",
            "cn": "【涉及知识点】膀胱（Urinary bladder）是平滑肌构成的可膨胀储尿囊袋，尿道（Urethra）是引流终尿排出体外的管道。【异同辨析】膀胱与尿道完全没有肾单位或滤过毛细血管球，不具备任何血液净化与尿液生成功能，它们仅作为下游管道负责尿液的“暂存”与“排放”。【混淆陷阱】容易把泌尿系统的下游储尿排尿管道（膀胱与尿道）误当成生成尿液的源头滤过器官（肾脏）。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The pancreas secretes digestive enzymes (pancreatic juice) and endocrine hormones (insulin, glucagon). The spleen filters aging erythrocytes and coordinates immune surveillance. [Comparison]: Neither organ connects to the urinary tract or produces urine. [Confusion Trap]: Miscellaneous abdominal organ confusion.",
            "cn": "【涉及知识点】胰腺（Pancreas）兼具外分泌（胰消化酶）与内分泌（胰岛素调血糖）功能；脾脏（Spleen）是淋巴免疫器官，负责破坏老化红细胞。【异同辨析】胰腺和脾脏均不属于泌尿系统，完全不参与尿素排泄和尿液生成。【混淆陷阱】同属腹腔内脏器官，但在生理功能上与排泄系统互不重叠，属于干扰项辨析。"
        }
    },

    "L24_Review_MCQ_10": {
        "A": {
            "correct": False,
            "en": "[Concept]: Excretion is the removal of toxic waste substances produced by metabolic chemical reactions inside body cells (e.g. urea, CO2, sweat). [Comparison]: Excretion removes molecules created inside cells that crossed cell membranes. Egestion expels food materials that remained inside the gut cavity and were never absorbed. [Confusion Trap]: The classic Cambridge distinction between excretion (metabolic waste) and egestion (undigested food).",
            "cn": "【涉及知识点】排泄（Excretion）特指清除机体细胞内部生化新陈代谢反应所产生的毒性化学废物（如尿素、二氧化碳等）。【异同辨析】排泄物来源于细胞内部代谢产物，必须跨膜进入血液循环再排出；而排遗物（粪便）本质上从未穿透肠壁上皮细胞进入人体内环境，只是沿着消化管道直通排出。【混淆陷阱】剑桥IGCSE最经典的混淆考点！很多学生常把“排便（排遗 Egestion）”错误归为“排泄（Excretion）”。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Digestion is the chemical and mechanical breakdown of large insoluble food polymers into small soluble monomer molecules for absorption. [Comparison]: Digestion breaks food down inside the stomach/intestine; egestion is the subsequent voiding of the leftovers that could not be digested. [Confusion Trap]: Conflating the breakdown process (digestion) with the expulsion of unabsorbed remnants (egestion).",
            "cn": "【涉及知识点】消化（Digestion）指机体通过机械研磨与消化酶水解，将大分子不溶性食物分解为可吸收的小分子可溶性养分的过程。【异同辨析】消化是食物在胃肠道内的分解利用过程；而排遗是消化管将“无法被消化分解”的残渣废弃物（如植物纤维素）排出体外。【混淆陷阱】混淆了对食物的分解利用过程（消化）与对不可消化残渣的排出过程（排遗）。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Egestion is the passing out of dietary material that has not been digested or absorbed through the digestive tract, as faeces via the anus. [Comparison]: Cellulose fibres, dead intestinal bacteria, and bile pigments pass straight through the alimentary canal lumen without entering metabolic pathways. [Key Criteria]: Exact verbatim syllabus definition for egestion.",
            "cn": "【涉及知识点】排遗（Egestion）在剑桥教学大纲中被严格且专一定义为：未被消化或吸收的食物残渣（如粗纤维）以粪便形式通过肛门排出体外。【异同辨析】这些物质从口腔进入，沿消化道腔一路通过，从未穿透细胞膜参与细胞内的生化代谢反应，故绝对属于排遗而非排泄。【核心考点】完美契合剑桥大纲中对排遗（Egestion）的精准官方定义。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Cellular respiration is the chemical oxidation of glucose inside mitochondria to generate ATP energy, producing CO2 and H2O. [Comparison]: Respiration is an energy-releasing metabolic reaction occurring in every living cell. Egestion is a gross physical bowel evacuation. [Confusion Trap]: Confusing cellular respiration with digestive waste elimination.",
            "cn": "【涉及知识点】细胞呼吸（Cellular respiration）是细胞在线粒体中氧化分解葡萄糖等有机物，释放能量合成ATP的生物化学过程。【异同辨析】呼吸作用是微观细胞内部的能量释放代谢；而排遗是宏观消化道末端排出固体残渣的物理排便动作，两者分属完全不同的生理学维度。【混淆陷阱】术语辨识混淆，将细胞供能的生化反应（呼吸作用）与消化道排废（排遗）搞混。"
        }
    },

    # ==================== LESSON 30 HOUSEKEEPING EXAM (Q1 - Q10) ====================
    "L30_Review_MCQ_1": {
        "A": {
            "correct": True,
            "en": "[Concept]: Sweat is an aqueous secretory excretion produced by eccrine sweat glands in the dermis of the skin. [Comparison]: Sweat consists predominantly of water (>99% for evaporative heat loss during thermoregulation) along with dissolved sodium chloride (mineral salt) and trace metabolic urea. [Key Criteria]: Matches Cambridge syllabus description of skin excretory output.",
            "cn": "【涉及知识点】汗液（Sweat）由真皮层中的外泌汗腺分泌，是人体兼顾体温调节与辅助排泄的液体分泌物。【异同辨析】汗液主要成分是水（>99%，通过皮肤表面蒸发带走潜热以实现降温），并伴随排出过量的无机盐（氯化钠）以及微量的细胞代谢废物尿素。【核心考点】完全符合剑桥教材中皮肤作为排泄器官所排出的三大成分：水、无机盐、尿素。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Oxygen is a vital respiratory substrate actively delivered to cells by blood for aerobic respiration in mitochondria. [Comparison]: Oxygen is never excreted as waste; cells constantly consume it to produce ATP. Carbon dioxide is the metabolic gas excreted, and it is eliminated by the lungs, not the skin. [Confusion Trap]: Confusing a consumed metabolic input (oxygen) with an excreted waste product.",
            "cn": "【涉及知识点】氧气（Oxygen）是细胞进行有氧呼吸不可或缺的能量代谢底物与电子受体。【异同辨析】人体对氧气唯恐不足，细胞无时无刻不在消耗氧气，绝不可能把氧气当作代谢废物随汗腺排出；汗液排泄的是代谢终产物与水盐。【混淆陷阱】把细胞呼吸必需的消耗性原料（氧气）与机体需要清除的废物相混淆。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Glucose and lipids (fats) are high-energy macronutrients vital for cellular fuel and membrane integrity. [Comparison]: The body strictly conserves glucose and lipids through renal tubular reabsorption. Excreting glucose or fats in sweat would cause severe nutrient wasting and indicates pathology. [Confusion Trap]: Confusing valuable retained nutrients with excreted metabolic wastes.",
            "cn": "【涉及知识点】葡萄糖和脂肪是机体极为宝贵的储能物质和结构原料，肾脏与消化道会全力进行重吸收与储存。【异同辨析】人体具有极其严密的营养物质回收机制，正常情况下汗液中绝对不含有葡萄糖与脂肪；排汗排泄的是无机物和有害小分子废物。【混淆陷阱】把机体精心保留的高能量养分（糖类、脂类）与主动排泄的水盐废物混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Carbon dioxide is a volatile respiratory gas excreted almost entirely (>99%) via pulmonary alveolar exhalation in the lungs. [Comparison]: Sweat is an aqueous fluid and does not serve as a gaseous route for carbon dioxide excretion. [Confusion Trap]: Knowing carbon dioxide is a waste product, but confusing the excretory organ responsible (lungs vs skin).",
            "cn": "【涉及知识点】二氧化碳（Carbon dioxide）是有氧呼吸脱羧反应产生的挥发性气体代谢产物。【异同辨析】人体99%以上的二氧化碳都是通过肺部呼吸运动呼出体外；汗腺排出的是液态水相中的溶质（尿素与无机盐），不承担二氧化碳排泄。【混淆陷阱】知道二氧化碳是代谢废物，但搞错了排泄器官的分工（二氧化碳归肺管，尿素水盐归肾脏与汗腺管）。"
        }
    },

    "L30_Review_MCQ_2": {
        "A": {
            "correct": False,
            "en": "[Concept]: The ureter is a macro-anatomical muscular tube conducting finished urine from the renal pelvis to the urinary bladder. [Comparison]: The ureter is merely a passive transit conduit with thick smooth muscle walls; it contains no filtration barrier or capillary glomeruli. Ultrafiltration occurs inside microscopic nephrons in the renal cortex. [Confusion Trap]: Confusing gross anatomical conduits with microscopic nephron filtration structures.",
            "cn": "【涉及知识点】输尿管（Ureter）是连接肾盂与膀胱的宏观肌性输送管道，管壁由平滑肌构成。【异同辨析】输尿管仅依靠蠕动节律单向输送已经形成的终尿，管壁极厚且没有毛细血管滤过膜，不具备超滤过功能；超滤过发生在肾皮质内的微观肾单位深处。【混淆陷阱】把输送终尿的宏观管道（输尿管）与肾脏微观功能滤过结构（肾小球）相混淆。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: The urinary bladder is a hollow muscular organ lined with transitional epithelium designed to temporarily store urine. [Comparison]: The bladder has no nephrons, no filtration membranes, and no blood-filtering capabilities. It simply holds urine until micturition. [Confusion Trap]: Assuming that because urine collects in the bladder, the bladder must be where urine is filtered from blood.",
            "cn": "【涉及知识点】膀胱（Urinary bladder）是由逼尿肌和平滑肌构成的具有弹性的肌性储尿器官。【异同辨析】膀胱的主要功能是安全暂存由输尿管注入的尿液，其内膜不与血液发生滤过交换，完全不具备从血液中滤过杂质的能力。【混淆陷阱】因为尿液在膀胱中聚集，学生常常凭生活直觉误以为“尿液是在膀胱中滤出形成的”。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: The glomerulus is a specialized knot of high-pressure fenestrated capillaries nestled inside Bowman's capsule in the renal cortex. [Comparison]: The afferent arteriole is wider than the efferent arteriole, generating high hydrostatic pressure (~50 mmHg) that forces water, glucose, urea, and ions across the basement membrane into Bowman's capsule (ultrafiltration), retaining blood cells and large proteins. [Key Criteria]: Exact syllabus definition of the ultrafiltration site in the nephron.",
            "cn": "【涉及知识点】肾小球（Glomerulus）是位于肾小囊（Bowman's capsule）凹腔内的微动脉分支形成的毛细血管球。【异同辨析】入球微动脉管径粗于出球微动脉，从而在肾小球内形成极高的流体静水压，迫使水、葡萄糖、氨基酸、尿素及无机盐滤过基底膜进入肾小囊腔（称为超滤作用），而血细胞和大分子蛋白质被阻截在血管内。【核心考点】教科书中关于肾单位内发生超滤过（Ultrafiltration）专属部位的标准答案。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The renal tubule (proximal tubule, loop of Henle, distal tubule) is the coiled tubular segment downstream of Bowman's capsule. [Comparison]: The renal tubule carries out selective reabsorption (pumping 100% of glucose and ~99% of water back into blood) and tubular secretion, occurring AFTER ultrafiltration has already happened in the glomerulus. [Confusion Trap]: Confusing the first stage of urine formation (filtration in glomerulus) with the second stage (reabsorption in tubules).",
            "cn": "【涉及知识点】肾小管（Renal tubule，包括近曲小管、髓袢和远曲小管）是紧接肾小囊之后的盘曲细管。【异同辨析】肾小管专职执行选择性重吸收（Selective reabsorption，将原尿中100%的葡萄糖及绝大部分水盐主动拉回血液）和分泌，这发生在超滤过完成“之后”的下游环节，其本身不执行初级超滤过。【混淆陷阱】混淆了尿液生成的两大先后阶段：第一步超滤过（肾小球）与第二步选择性重吸收（肾小管）。"
        }
    },

    "L30_Review_MCQ_3": {
        "A": {
            "correct": False,
            "en": "[Concept]: An electrical impulse traveling along a neurone is an action potential, belonging to the nervous system. [Comparison]: Nerve impulses are electrical ion fluxes across axonal membranes acting in milliseconds along hard-wired nerves. Hormones are blood-borne chemical molecules secreted by endocrine glands with slower, broader, longer-lasting effects. [Confusion Trap]: Confusing the two communication systems of the human body (electrical nervous vs chemical endocrine).",
            "cn": "【涉及知识点】沿神经纤维传导的电信号是动作电位或神经冲动（Nerve impulse），属于神经系统调节。【异同辨析】神经冲动依赖膜电位离子流动，传导速度极快（毫秒级），通过专用神经线路点对点传导；而激素是内分泌腺分泌的纯化学物质，随血液漫游，起效慢但作用范围广、持续持久。【混淆陷阱】将人体两大信息调控系统（电信号传导的神经系统 vs 化学分子运输的内分泌系统）混同。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: A hormone is a chemical messenger produced by an endocrine gland, secreted directly into blood, and transported to alter the metabolic activity of specific target organs/cells possessing complementary receptors. [Comparison]: Chemical nature, gland origin, blood transport, and target organ receptor action form the complete definition. [Key Criteria]: Verbatim Cambridge textbook definition.",
            "cn": "【涉及知识点】激素（Hormone）是由无导管的内分泌腺体（Endocrine glands）合成并直接分泌入血液的化学信使（Chemical messenger）。【异同辨析】激素借由血液循环流经全身，但仅与表面带有特异性受体的靶器官（Target organs）结合，精准诱发细胞代谢、生长或分化状态的改变。【核心考点】完全符合剑桥教学大纲中对激素（化学物质、腺体产生、血液运输、改变靶器官）的标准定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: White blood cells (leucocytes) are living, motile cellular units of the immune system that engulf pathogens or synthesize antibodies. [Comparison]: White blood cells are living complete cells with nuclei, organelles, and amoeboid movement. Hormones are non-living chemical molecules (peptides, steroids, amines) secreted by cells. [Confusion Trap]: Confusing cellular immune components with molecular endocrine messengers.",
            "cn": "【涉及知识点】白细胞（White blood cells）是血液中有核的活性免疫防卫细胞（如淋巴细胞、单核细胞等）。【异同辨析】白细胞是具有完整细胞核与细胞器、能自主变形运动的活体细胞；而激素是内分泌细胞制造并释放的化学分子（蛋白质类或类固醇类），并非活体细胞本身。【混淆陷阱】把活的免疫防御细胞（白细胞）与细胞分泌的无生命化学调节分子（激素）搞混。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Digestive enzymes are biological protein catalysts produced by exocrine glands (salivary, gastric, pancreatic) and secreted via ducts into the gut lumen. [Comparison]: Digestive enzymes break chemical bonds of food locally in the digestive cavity and are never transported in blood to control target organs. Hormones are endocrine messengers circulating systemically. [Confusion Trap]: Confusing exocrine secretions into body cavities with endocrine secretions into the bloodstream.",
            "cn": "【涉及知识点】消化酶（Digestive enzymes）是外分泌腺（唾液腺、胃腺、胰腺外分泌部）合成并经导管排入消化管腔的生物催化剂。【异同辨析】消化酶的作用场所是消化道腔内（属于体外环境延伸），功能是催化水解食物大分子，绝不经血液循环传递信息；激素则是无导管内分泌，进入血液循环调节靶器官代谢。【混淆陷阱】混淆了外分泌产物（催化食物水解的消化酶）与内分泌产物（全身信息调控的激素）。"
        }
    },

    "L30_Review_MCQ_4": {
        "A": {
            "correct": False,
            "en": "[Concept]: The nervous system consists of the brain, spinal cord, and peripheral nerves transmitting bioelectrical action potentials along axons. [Comparison]: Nerves do not contain fluid flow channels to transport hormones; hormones are chemical solutes carried in bulk fluid flow inside cardiovascular blood vessels. [Confusion Trap]: Assuming that regulatory signals (hormones) travel through the 'signal network' of nerves.",
            "cn": "【涉及知识点】神经系统由脑、脊髓和周围神经构成，专门利用轴突细胞膜上的离子流动传递生物电信号。【异同辨析】神经纤维是实体的神经元轴突束，内部不存在流体管道以输送化学溶液；激素是溶解在血浆液体中的化学分子，必须依靠循环系统的血液宏观流动运输。【混淆陷阱】学生潜意识中认为“所有调控信号都由神经线路传输”，误以为激素也是沿着神经走的。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: The digestive tract (alimentary canal) is a hollow tube for ingesting, digesting, and absorbing nutrients. [Comparison]: The gut lumen contains food chyme, digestive enzymes, and acid/bile that would rapidly destroy peptide hormones (e.g. insulin). Hormones are strictly excluded from the gut lumen and circulate internally in blood. [Confusion Trap]: Confusing the internal circulatory system with the external hollow digestive canal.",
            "cn": "【涉及知识点】消化道（Digestive tract）是消化吸收食物的连续肌肉管道，腔内含有高浓度的蛋白水解酶与强酸强碱。【异同辨析】蛋白质类激素（如胰岛素）若进入消化道腔内，会被胃蛋白酶与胰蛋白酶瞬间水解破坏失效；内分泌腺分泌的激素直接进入组织间隙并渗入毛细血管，由血液运送。【混淆陷阱】混淆了体内真正的内环境（循环系统）与贯通体外的内腔道（消化道）。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Endocrine glands are ductless glands embedded within extensive capillary networks. [Comparison]: Hormones diffuse directly across the thin endothelial walls of surrounding capillaries into blood plasma. Bulk blood flow rapidly distributes them systemically throughout the cardiovascular network to reach distant target tissues. [Key Criteria]: Perfect match with textbook description of hormone transport.",
            "cn": "【涉及知识点】内分泌腺（Endocrine glands）结构上无排泄导管（Ductless），腺实质细胞周围交织着极其密集的毛细血管网。【异同辨析】合成的激素分子直接穿透毛细血管内皮细胞进入血浆，搭乘心血管系统的血液循环快车迅速扩散并流经全身，与远端靶器官受体特异性结合。【核心考点】教科书关于激素长距离运输载体（血液循环系统 Bloodstream）的标准答案。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Lymphatic lacteals are specialized lymphatic capillaries inside intestinal villi dedicated to absorbing dietary fats (chylomicrons). [Comparison]: Lacteals drain dietary lipids into the thoracic duct. Endocrine glands secrete directly into surrounding blood capillaries, not lymphatic lacteals. [Confusion Trap]: Confusing the absorption pathway for dietary lipids (lacteals) with the transport pathway for systemic hormones (blood).",
            "cn": "【涉及知识点】淋巴乳糜管（Lacteals）是专职分布在小肠绒毛中央的盲端毛细淋巴管，负责吸收消化后的长链脂肪。【异同辨析】乳糜管专职引流乳糜微粒（脂肪），最后汇入胸导管；全身各处的内分泌腺体内富含的是微血管网，激素直接分泌入血液，不通过淋巴乳糜管运输。【混淆陷阱】把吸收脂肪的微观淋巴管道（乳糜管）与运输全身内分泌激素的血液循环系统相混淆。"
        }
    },

    "L30_Review_MCQ_5": {
        "A": {
            "correct": False,
            "en": "[Concept]: The pancreas is an elongated retroperitoneal glandular organ located in the epigastric region below and behind the stomach. [Comparison]: The pancreas secretes insulin and glucagon and is positioned transversely across the posterior abdominal wall, not capping the kidneys. [Confusion Trap]: Knowing the pancreas is an endocrine organ in the abdomen, but mixing up its anatomical coordinates with the adrenal glands.",
            "cn": "【涉及知识点】胰腺（Pancreas）是位于腹上区及左季肋区、紧贴胃后下方的狭长横卧实质性腺体。【异同辨析】胰腺头部被十二指肠环抱，尾部达脾门，负责分泌胰岛素和胰液；而位于两侧肾脏上方的腺体是成对的肾上腺。【混淆陷阱】知道胰腺是腹腔内的内分泌器官，但把胰腺的横卧解剖位置与附着在肾顶部的肾上腺相混淆。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: The ovaries are paired female gonads situated in the ovarian fossa on the lateral pelvic wall, connected to the uterus by ovarian ligaments. [Comparison]: The ovaries are deep in the pelvic cavity, producing oestrogen and ova, completely separated from the high retroperitoneal abdominal kidneys. [Confusion Trap]: Conflating pelvic female reproductive glands with abdominal stress glands.",
            "cn": "【涉及知识点】卵巢（Ovaries）是女性盆腔内的成对生殖腺，位于子宫两侧输卵管下方。【异同辨析】卵巢处于盆腔腹膜皱襞内，负责排卵和产生雌孕激素；肾脏及附着其上的肾上腺位于背部腹膜后间隙，相隔甚远。【混淆陷阱】解剖区域混同，把盆腔深部的生殖腺（卵巢）与上腹部腹膜后的肾上腺搞混。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The testes are paired male reproductive gonads suspended outside the abdominopelvic cavity within the scrotum for temperature regulation. [Comparison]: The testes produce sperm and testosterone at ~34-35°C outside the body wall, geographically distant from the abdominal kidneys. [Confusion Trap]: Gross anatomical confusion between male external gonads and internal abdominal endocrine glands.",
            "cn": "【涉及知识点】睾丸（Testes）是男性外生殖腺，悬垂于体腔外部的阴囊内以维持低于体温约2-3℃的精子发生环境。【异同辨析】睾丸处于体表阴囊，分泌睾酮和精子；而肾上腺深埋于腹膜后腹腔最顶端，二者解剖空间相差极大。【混淆陷阱】解剖学常识混淆，将体外的男性生殖腺（睾丸）与体内深部的肾上腺相混同。"
        },
        "D": {
            "correct": True,
            "en": "[Concept]: The adrenal glands (suprarenal glands) are paired triangular/crescent-shaped endocrine organs perched like caps atop the superior poles of both kidneys. [Comparison]: Derived from Latin *ad* (near) + *renes* (kidneys), the adrenal cortex and medulla produce corticosteroid hormones and adrenaline. [Key Criteria]: Anatomical definition of the endocrine glands sitting on top of the kidneys.",
            "cn": "【涉及知识点】肾上腺（Adrenal glands/Suprarenal glands）是位于左右两侧肾脏顶端上方的成对扁平三角形/月牙形内分泌器官。【异同辨析】其拉丁文词根 Ad-（附着、邻近）+ Renal（肾脏）直观标明了其依附在肾脏顶极的解剖关系；由外层的皮质和内层的髓质（分泌肾上腺素）构成。【核心考点】准确契合剑桥教材中关于“坐落于双肾顶部的内分泌腺（肾上腺）”的解剖学考点。"
        }
    },

    "L30_Review_MCQ_6": {
        "A": {
            "correct": False,
            "en": "[Concept]: Adrenaline is the primary emergency hormone of the sympathetic nervous system, accelerating cardiac nodal pacing and inotropy. [Comparison]: Decreasing heart rate would reduce tissue perfusion, starving skeletal muscles of oxygen and causing collapse during an attack. Adrenaline drastically *increases* heart rate and cardiac output. [Confusion Trap]: Inversion trap; attributing an inhibitory/calming parasympathetic effect to an excitatory emergency hormone.",
            "cn": "【涉及知识点】肾上腺素（Adrenaline）是交感神经系统主导的急性应激激素，直接激动心脏窦房结β1受体。【异同辨析】若减慢心率会直接导致心输出量暴跌，使奔跑逃命的骨骼肌缺血缺氧瘫痪；肾上腺素的作用恰恰是强烈且迅速地“加快心率”并增强心肌收缩力。【混淆陷阱】生理方向完全倒置的送分陷阱！把应激兴奋作用错误反转为抑制减慢效应。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Adrenaline triggers hepatic and muscle glycogenolysis, breaking stored glycogen into free glucose. [Comparison]: Reducing blood glucose would cause hypoglycaemic muscle weakness and syncope during a crisis. Adrenaline surges blood glucose to guarantee continuous fuel for brain and muscles. [Confusion Trap]: Reversing the metabolic energy-mobilizing effect of adrenaline.",
            "cn": "【涉及知识点】肾上腺素激活肝脏与骨骼肌中的糖原磷酸化酶，迅速将储存的肝糖原分解为游离葡萄糖释放入血。【异同辨析】危机时刻若降低血糖会导致骨骼肌与大脑能量耗竭而昏厥；肾上腺素与胰岛素对抗，其核心效应是显著“升高血糖”以提供随时可用的燃料。【混淆陷阱】将应激供能（升高血糖）与降糖稳态混为一谈，因果倒置。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Adrenaline orchestrates the classic 'fight or flight' response evolved for acute survival in response to danger or stress. [Comparison]: It increases heart rate and stroke volume, dilates bronchioles (increasing alveolar ventilation), mobilizes blood glucose, and diverts blood flow away from the gut towards skeletal muscles. [Key Criteria]: Perfect match with Cambridge syllabus description of adrenaline action.",
            "cn": "【涉及知识点】肾上腺素是机体应对生死危机演化出的核心激素，全权启动急性“战斗或逃跑”（Fight or flight）应激反应。【异同辨析】通过加速心跳、扩张支气管平滑肌（增加通气量）、分解糖原升高血糖，并收缩内脏血管将大量血液优先分流至骨骼肌，为战斗或逃命做好最大体能储备。【核心考点】完美契合教材中关于肾上腺素激发战斗或逃跑反应、加快心率、扩张气道的核心考点描述。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Adrenaline stimulates reticular activating systems in the brainstem, driving intense cortical arousal, vigilance, and pupillary dilation. [Comparison]: Inducing sleep would result in immediate death if attacked by a predator. Adrenaline actively suppresses sedation and ensures maximal vigilance. [Confusion Trap]: Complete biological contradiction; adrenaline stimulates wakefulness, never sleep.",
            "cn": "【涉及知识点】肾上腺素激动中枢脑干网状上行激动系统，使大脑皮层进入高度觉醒与极度警觉状态，并散大瞳孔。【异同辨析】在面对天敌或危机时若诱导睡眠将瞬间致命；肾上腺素绝对是消除困倦、强力兴奋神经中枢的觉醒激素，绝非催眠剂。【混淆陷阱】荒谬的生理功能反向干扰项，把高度觉醒状态与抑制催眠状态相对立。"
        }
    },

    "L30_Review_MCQ_7": {
        "A": {
            "correct": False,
            "en": "[Concept]: Testosterone is the principal androgen steroid hormone secreted by testicular Leydig cells. [Comparison]: Testosterone coordinates spermatogenesis, voice deepening, and anabolic protein synthesis in muscles; it has zero direct acute role in lowering postprandial blood glucose. [Confusion Trap]: Confusing reproductive developmental steroid hormones with pancreatic metabolic peptide hormones.",
            "cn": "【涉及知识点】睾酮（Testosterone）是由男性睾丸间质细胞大量合成并分泌的类固醇雄性激素。【异同辨析】睾酮负责驱动男性第二性征成熟、促进骨骼肌蛋白同化生长及维持精子发生，与餐后急性降低血糖的代谢机制毫无直接关联。【混淆陷阱】把长期的生殖发育类固醇激素（睾酮）与餐后短期的糖代谢调节多肽激素（胰岛素）相混淆。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Oestrogen is the primary female ovarian steroid hormone governing the follicular phase of the menstrual cycle and secondary sex traits. [Comparison]: Oestrogen repairs and thickens the endometrium; it does not control acute postprandial glucose uptake into liver and muscle cells. [Confusion Trap]: Conflating female reproductive cycle hormones with pancreatic glucose regulators.",
            "cn": "【涉及知识点】雌激素（Oestrogen）是由卵巢卵泡分泌的类固醇性激素，主导女性第二性征发育及月经周期。【异同辨析】雌激素的作用靶器官主要是子宫内膜（刺激细胞分裂修复增厚）及乳腺，完全不具备降低饱餐后血液中葡萄糖浓度的能力。【混淆陷阱】将女性生殖内分泌周期激素（雌激素）与普遍存在的血糖调节激素相混同。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Adrenaline is the emergency hormone produced by the adrenal medulla during stress, exercise, or hypoglycemia. [Comparison]: Adrenaline *elevates* blood glucose by stimulating glycogenolysis (breaking glycogen into glucose) to fuel muscles; it acts in direct opposition to insulin and does not lower glucose after a meal. [Confusion Trap]: Directional inversion trap; adrenaline raises blood glucose during fight-or-flight, whereas insulin lowers it after feeding.",
            "cn": "【涉及知识点】肾上腺素（Adrenaline）是肾上腺髓质在应激、恐慌或剧烈运动时释放的升糖激素。【异同辨析】肾上腺素的作用是刺激肝脏分解糖原以“升高血糖”，为机体应急供能，其作用与胰岛素完全相反；在饱餐后血糖本就偏高时，绝不需要肾上腺素来降糖。【混淆陷阱】生理调控方向彻底混淆，将应激升糖激素（肾上腺素）误当成餐后降糖激素（胰岛素）。"
        },
        "D": {
            "correct": True,
            "en": "[Concept]: Insulin is a peptide hormone synthesized and secreted by the beta cells of the Islets of Langerhans in the pancreas. [Comparison]: Following a carbohydrate-rich meal, rising blood glucose triggers insulin release. Insulin stimulates liver and skeletal muscle cells to take up glucose and polymerize it into storage glycogen (glycogenesis), restoring normal blood glucose levels (~5 mmol/L). [Key Criteria]: Verbatim match for Cambridge textbook negative feedback blood glucose regulation.",
            "cn": "【涉及知识点】胰岛素（Insulin）是由胰腺内部的胰岛β细胞直接合成并释放入血的降血糖多肽激素。【异同辨析】饱餐后消化吸收的葡萄糖使血糖浓度迅速攀升，胰岛β细胞受刺激分泌胰岛素；胰岛素促使全身组织摄取葡萄糖，并激活肝脏与骨骼肌合成不溶性糖原储存，使血糖回落至正常稳态范围。【核心考点】完全符合剑桥教材中关于胰岛素负反馈调节降低血糖的权威核心定义。"
        }
    },

    "L30_Review_MCQ_8": {
        "A": {
            "correct": False,
            "en": "[Concept]: The adrenal glands consist of an outer cortex (corticosteroids) and an inner medulla (adrenaline and noradrenaline). [Comparison]: Adrenal medulla produces adrenaline which raises blood glucose. Adrenal cells do not synthesize insulin; insulin is manufactured exclusively by pancreatic beta cells. [Confusion Trap]: Conflating the stress glands (adrenals) with the digestive/metabolic gland (pancreas).",
            "cn": "【涉及知识点】肾上腺（Adrenal glands）由外层的皮质（分泌皮质醇与醛固酮）和内层的髓质（分泌肾上腺素）构成。【异同辨析】肾上腺分泌的肾上腺素功能是升高血糖；肾上腺内根本不含有胰岛β细胞，绝不合成或分泌胰岛素。【混淆陷阱】把肾上腺（应激与水盐调节）与胰腺（血糖稳态调节）两处完全不同的内分泌腺体相混淆。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: The pancreas contains microscopic endocrine clusters called the Islets of Langerhans scattered throughout its exocrine acinar tissue. [Comparison]: Beta cells within the islets synthesize, package, and secrete insulin into pancreatic venules whenever blood glucose rises above baseline. [Key Criteria]: Flawless match for the gland producing insulin.",
            "cn": "【涉及知识点】胰腺（Pancreas）是兼具外分泌与内分泌功能的复合腺体，其内分泌部分由散布在腺泡间的数十万个胰岛（Islets of Langerhans）构成。【异同辨析】胰岛中的β细胞具有精密的葡萄糖感受器，能根据血糖浓度高低动态合成并释放胰岛素直接入血，是体内唯一能够分泌胰岛素的专属组织。【核心考点】教科书中关于分泌胰岛素的腺体（胰腺 Pancreas）的标准考点答案。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The thyroid gland is a butterfly-shaped endocrine organ located in the anterior neck overlying the trachea. [Comparison]: The thyroid synthesizes iodinated thyroxine (T4/T3) which governs basal metabolic rate and cellular oxygen consumption throughout the body; it does not produce insulin. [Confusion Trap]: Confusing the metabolic rate regulator (thyroid) with the glucose storage regulator (pancreas).",
            "cn": "【涉及知识点】甲状腺（Thyroid gland）是位于颈前部、喉和气管两侧的蝴蝶状内分泌腺体。【异同辨析】甲状腺利用碘合成甲状腺激素（Thyroxine），作用是调节全身细胞的基础代谢率、耗氧量和骨骼智力发育，绝不生产胰岛素。【混淆陷阱】只模糊记得甲状腺与“代谢”有关，误把基础能量代谢调节腺（甲状腺）当成了降血糖腺（胰腺）。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The pituitary gland (hypophysis) is a pea-sized master endocrine gland situated at the base of the brain in the sella turcica. [Comparison]: The pituitary secretes trophic hormones (growth hormone, TSH, ACTH, FSH, LH, and ADH), controlling other glands. It does not synthesize insulin; blood glucose regulation bypasses the pituitary and acts directly on the pancreas. [Confusion Trap]: Over-applying the 'master gland' concept, incorrectly assuming the pituitary produces every single hormone in the body.",
            "cn": "【涉及知识点】脑垂体（Pituitary gland）位于颅底蝶鞍内，是人体内分泌系统的“总指挥部”。【异同辨析】脑垂体分泌生长激素、抗利尿激素以及调控下游甲状腺、性腺的促激素，但它绝对不生产胰岛素；血糖稳态的调控是血液中葡萄糖直接刺激胰岛β细胞，不经过垂体中转。【混淆陷阱】过度迷信垂体是“主腺（Master gland）”，便误以为体内所有重要激素（包括胰岛素）都是脑垂体生产的。"
        }
    },

    "L30_Review_MCQ_9": {
        "A": {
            "correct": False,
            "en": "[Concept]: Oestrogen is the primary female ovarian steroid hormone. [Comparison]: Oestrogen stimulates female secondary sexual traits during puberty (e.g. breast development, widening of the pelvis, deposition of subcutaneous adipose tissue). Testosterone drives male traits. [Confusion Trap]: Gender hormone reversal; assigning the female sex hormone to male developmental changes.",
            "cn": "【涉及知识点】雌激素（Oestrogen）是主要由女性卵巢发育卵泡合成分泌的类固醇激素。【异同辨析】雌激素专职促进女孩在青春期的第二性征发育（如乳房增大、骨盆增宽、皮下脂肪沉积及初潮来潮）；驱动男孩出现男性特征的则是睾酮。【混淆陷阱】性别主导激素完全颠倒，把女性特征主导激素（雌激素）张冠李戴到男性特征发育上。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Insulin is a peptide metabolic hormone produced by pancreatic beta cells. [Comparison]: Insulin controls cellular glucose uptake and blood sugar levels; it has zero direct morphogenic action on pubertal sex differentiation or secondary sexual traits. [Confusion Trap]: Category error confusing non-sexual metabolic hormones with pubertal steroid androgens.",
            "cn": "【涉及知识点】胰岛素（Insulin）是由胰腺内分泌部胰岛β细胞分泌的调节糖代谢的多肽激素。【异同辨析】胰岛素全身细胞都需要，专职维持餐后血糖平衡，与青春期男性喉结突出、变声、长胡须等性别体态分化发育毫无关系。【混淆陷阱】概念范畴脱节，将普遍的非性别糖代谢激素（胰岛素）与青春期雄性激素搞混。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Testosterone is the potent androgenic steroid hormone secreted in massive quantities by the interstitial Leydig cells of the testes during puberty. [Comparison]: It binds intracellular androgen receptors, stimulating facial/body hair growth, larynx enlargement and vocal cord thickening (voice deepening), and rapid acceleration of skeletal muscle protein synthesis. [Key Criteria]: Verbatim match for male secondary sexual characteristic regulation.",
            "cn": "【涉及知识点】睾酮（Testosterone）是主要由男性睾丸间质细胞合成并大量释放入血的雄性类固醇激素。【异同辨析】进入青春期后在垂体促性腺激素刺激下，睾酮水平成倍激增，特异性刺激男性喉头软骨增大、声带变宽增厚（声调低沉变声）、长出胡须及体毛、加速骨骼肌蛋白质合成使体格强健。【核心考点】教科书中关于驱动男性第二性征发育的主导激素（睾酮 Testosterone）的标准答案。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Adrenaline is an amino acid-derived hormone secreted by the adrenal medulla during acute fight-or-flight emergencies. [Comparison]: Adrenaline operates on a timescale of seconds to minutes to survive acute danger (increasing heart rate and ventilation); it has no developmental role in pubertal secondary sex traits. [Confusion Trap]: Confusing acute emergency survival hormones with chronic pubertal developmental hormones.",
            "cn": "【涉及知识点】肾上腺素（Adrenaline）是由肾上腺髓质在遭遇突发危险或剧烈应激时瞬间激增分泌的激素。【异同辨析】肾上腺素的作用时间在数秒到数分钟之间，负责应急战斗逃跑（加快心率、扩张支气管）；它绝不参与长达数年的青春期身体形态学渐进发育。【混淆陷阱】将面对危机时的急性应急激素（肾上腺素）与调控长达数年发育周期的性激素（睾酮）相混淆。"
        }
    },

    "L30_Review_MCQ_10": {
        "A": {
            "correct": True,
            "en": "[Concept]: Adolescence (encompassing puberty) is the defined developmental transitional stage between childhood and adulthood. [Comparison]: Characterized by rapid physical growth, maturation of the gonads (gametogenesis), emergence of secondary sexual traits, and psychological/emotional maturation leading to reproductive maturity. [Key Criteria]: Perfect match with Cambridge textbook Chapter 5 definition.",
            "cn": "【涉及知识点】青春期（Adolescence / Puberty）是人体由儿童向成年过渡的特有生命发育黄金阶段。【异同辨析】此阶段伴随下丘脑-垂体-性腺轴的觉醒，生殖器官快速成熟具备生殖能力，出现男女第二性征，体格经历生长突增，并伴随神经心理的深刻成熟。【核心考点】完全符合剑桥教材第5章中关于青春期“由儿童向成年人过渡、达到生殖成熟的发展时期”的权威定义。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Assimilation is the biochemical uptake and incorporation of digested nutrient molecules (glucose, amino acids) into cell structures. [Comparison]: Assimilation is a metabolic process occurring inside individual cells at all ages throughout life; it is not a human developmental life-stage. [Confusion Trap]: Category error confusing cellular nutrient incorporation with organismal pubertal maturation.",
            "cn": "【涉及知识点】同化作用（Assimilation）指细胞吸收血液运送来的小分子营养物并将其合成构建自身细胞结构物质的生化代谢过程。【异同辨析】同化作用是人在一生中任何年龄阶段无时无刻不在进行的微观细胞级生化反应；而青春期是一个宏观的人体生理与形态学发育生命阶段。【混淆陷阱】概念范畴错误，把细胞吸收营养合成自身的代谢名词（同化作用）错误当成了人体的发育阶段。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Homeostasis is the physiological maintenance of a relatively constant internal environment (e.g. constant core body temperature, blood pH, blood glucose, water potential). [Comparison]: Homeostasis operates continuously across all life stages to preserve cellular stability, not a specific developmental transition period. [Confusion Trap]: Confusing a continuous regulatory physiological state (homeostasis) with a transitional developmental stage (adolescence).",
            "cn": "【涉及知识点】稳态（Homeostasis）指机体神经-体液调节网络维持内环境理化特性（如体温37℃、血浆pH 7.4、血糖稳态）动态平衡的机制。【异同辨析】稳态是维持生命存在不可或缺的稳恒状态调节，存在于人生的每一秒钟；它绝对不是指代从儿童到成人的转变发育阶段。【混淆陷阱】把维持体内理化环境稳定的生理学机制名词（稳态）与人生的特定发育时期（青春期）相混同。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Egestion is the voiding of undigested and unabsorbed food residues through the anus as faeces in the digestive system. [Comparison]: Egestion is a gastrointestinal disposal function, bearing zero relationship to pubertal reproductive maturation or human life stages. [Confusion Trap]: Completely arbitrary anatomical distraction; bowel defaecation has nothing to do with pubertal adolescence.",
            "cn": "【涉及知识点】排遗（Egestion）是消化系统的最末端生理过程，指不可消化的食物残渣以粪便形式排出体外。【异同辨析】排遗是肠道排便功能；而青春期是全身生殖系统与第二性征成熟的黄金过渡时期，二者毫无共同点。【混淆陷阱】最基本的生理学术语辨识错误，将排便动作（排遗）与青春发育期混为一谈。"
        }
    }
}
