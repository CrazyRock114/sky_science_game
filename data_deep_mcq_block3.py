# -*- coding: utf-8 -*-
"""
data_deep_mcq_block3.py
Deep, concept-grounded distractor analyses for:
Cumulative Revision Exam Section A: Q21 to Q40 (20 MCQs)

Each option contains:
- correct: bool
- en: [Concept] ... [Comparison] ... [Confusion Trap/Key Criteria] ...
- cn: 【涉及知识点】... 【异同辨析】... 【混淆陷阱/核心考点】...
"""

BLOCK3_DISTRACTORS = {
    # ==================== CUMULATIVE REVISION SECTION A (Q21 - Q40) ====================
    "Rev_SecA_Q21": {
        "A": {
            "correct": False,
            "en": "[Concept]: Urea is a toxic nitrogenous waste product, and excess mineral salts are osmotically active electrolytes that must be eliminated. [Comparison]: The primary goal of excretion is to void metabolic poisons; roughly 50% of urea passively escapes while excess salts are actively dumped into urine. They are never 100% reabsorbed. [Confusion Trap]: Reversing the fundamental purpose of the excretory system by assuming wastes and excess ions are retained.",
            "cn": "【涉及知识点】尿素（Urea）是机体必须清除的含氮代谢废物，多余的无机盐离子是需要排出的电解质。【异同辨析】排泄系统的首要生理目标是排出体内毒素并维持渗透压平衡；尿素和多余盐分大部分随终尿排出体外，绝不可能被100%完全重吸收回血液。【混淆陷阱】方向性认知颠倒；误以为肾小管对原尿中的所有滤过成分都会无差别全盘回收，忘记了排泄废物是肾脏的核心职责。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Glucose and amino acids are high-value nutrient fuels and anabolic building blocks that the body cannot afford to lose. [Comparison]: Healthy proximal convoluted tubule (PCT) epithelial cells express sodium-glucose cotransporters (SGLT) and active amino acid transporters that recover 100% of filtered glucose and amino acids under normal physiological thresholds. [Key Criteria]: The standard Cambridge textbook hallmark of proximal selective reabsorption.",
            "cn": "【涉及知识点】葡萄糖和氨基酸是机体最宝贵的供能单糖与蛋白质合成基本原料，属于高价值生理营养物。【异同辨析】健康人近曲小管（PCT）上皮细胞刷状缘表达极其高效的钠-葡萄糖同向转运体与氨基酸载体，通过二级主动转运在原尿流出近曲小管前将二者100%全部重吸收回血液。【核心考点】精准契合剑桥大纲中关于正常生理状态下葡萄糖与氨基酸在肾小管被100%完全重吸收的标准定论。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Red blood cells (erythrocytes) and high-molecular-weight plasma proteins (such as albumin and globulins) are cellular and macromolecular elements of blood. [Comparison]: The three-layer glomerular filtration barrier (podocyte slit diaphragms, basement membrane, and fenestrations) completely blocks large entities; RBCs and proteins NEVER enter the glomerular filtrate in healthy individuals, so they cannot be 'reabsorbed'. [Confusion Trap]: Confusing substances that were never filtered out of the blood with substances that were filtered and subsequently reabsorbed.",
            "cn": "【涉及知识点】红细胞和高分子血浆蛋白（如白蛋白、免疫球蛋白）是血液中的细胞有形成分与胶体大分子。【异同辨析】在健康的肾小球滤过屏障（足细胞裂孔膜与基底膜）面前，红细胞和血浆蛋白由于体积过大和电荷排斥，根本不能透过滤过膜进入原尿；既然未曾滤出，就谈不上“被肾小管重吸收”。【混淆陷阱】逻辑阶段错位：把“因颗粒过大根本没有被滤过而在血液中滞留的物质”与“滤出到原尿后被主动回收的物质”混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Water is an essential solvent that is extensively recovered throughout the nephron (~99% reabsorbed overall). [Comparison]: However, water is never 100% reabsorbed because ~1% must be retained to dissolve and flush out excreted solutes (forming 1–2 L of urine per day). Furthermore, glucose and amino acids are reabsorbed alongside it, making 'water only' incorrect. [Confusion Trap]: Recognizing that massive amounts of water are reclaimed, but overlooking that ~1% must be lost to form urine and ignoring glucose/amino acid conservation.",
            "cn": "【涉及知识点】水是维持血容量与细胞外液渗透压的溶剂，在肾小管和集合管中被极高比例回收（约99%重吸收）。【异同辨析】人体绝不可能对水执行100%重吸收，必须保留约1%（每日约1.5 L）作为溶剂冲刷溶解尿素与无机盐形成终尿；此外葡萄糖和氨基酸也是100%被重吸收的，故“只有水”必然错误。【混淆陷阱】只注意到了水分被大量回收的事实，却忽略了终尿必须有水作为排泄载体，且遗漏了葡萄糖和氨基酸这两类绝对完全回收的有机营养物。"
        }
    },

    "Rev_SecA_Q22": {
        "A": {
            "correct": False,
            "en": "[Concept]: Producing a large volume of dilute (pale) urine is the physiological response to overhydration (hypotonic blood), where osmoreceptors suppress antidiuretic hormone (ADH) secretion. [Comparison]: During dehydration, sweating and water loss increase blood osmolarity; producing large amounts of dilute urine would accelerate hypovolaemic shock and lethal dehydration. [Confusion Trap]: Inverting the homeostatic response of the pituitary-renal axis, selecting the overhydration profile instead of dehydration.",
            "cn": "【涉及知识点】产生大量低渗透压的稀释尿液是机体在大量饮水（水负荷过重/低渗状态）时的生理反应，此时下丘脑抑制抗利尿激素（ADH）的释放。【异同辨析】脱水时体内严重缺水且大量排汗，血浆晶体渗透压显著升高；若此时排出大量稀释尿，会导致血容量急剧崩溃休克。机体反应恰恰相反。【混淆陷阱】对机体稳态负反馈调节发生方向性认知颠倒，误将“水过多时的排水利尿反应”套用在“脱水严重”的情境中。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Dehydration concentrates blood solutes, stimulating hypothalamic osmoreceptors to trigger ADH release from the posterior pituitary gland. [Comparison]: ADH inserts aquaporin channels into collecting duct membranes, maximizing water reabsorption back into peritubular capillaries; this conserves water for circulation, leaving urine small in volume and highly concentrated (dark amber). [Key Criteria]: Perfect illustration of negative feedback osmoregulation required by Cambridge G8.",
            "cn": "【涉及知识点】运动出汗导致脱水时，血浆渗透压升高，刺激下丘脑渗透压感受器，促使垂体后叶大量释放抗利尿激素（ADH/Vasopressin）。【异同辨析】ADH促使肾脏集合管管壁水通道蛋白开放，最大化重吸收原尿中的水分以保全循环血量；排出的尿液因此极度浓缩（呈深琥珀色）、排尿量显著减少。【核心考点】精准契合剑桥大纲中关于脱水状态下人体通过负反馈调节生成“量少且浓缩的尿液（Smaller in volume and more concentrated）”的稳态机制。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Homeostatic osmoregulation dynamically modulates renal water output in response to internal hydration shifts. [Comparison]: If urine volume and solute concentration remained rigid and static during prolonged dehydration, plasma osmolarity and blood volume would spiral out of control, resulting in organ failure. [Confusion Trap]: Assuming that biological organ systems operate as passive, inflexible plumbing machines that do not adapt to physiological stress.",
            "cn": "【涉及知识点】内环境稳态（Homeostasis）依赖于各器官根据生理状态的动态微调，肾脏是调控体液平衡最核心的效应器官。【异同辨析】若剧烈运动大量失水时尿量和浓度毫无变化，体内的水盐平衡将瞬间打破，导致严重的循环衰竭；肾脏绝不可能维持僵硬恒定的排尿量。【混淆陷阱】缺乏动态生理稳态的生物学观念，误以为器官排泄如同固定流量的自来水管道，忽视了神经体液调节的适应性。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Glucosuria (glucose in urine) occurs only when plasma glucose levels exceed the renal tubular transport maximum (~10 mmol/L), overwhelming reabsorptive capacity (classic in diabetes mellitus). [Comparison]: Dehydration concentrates normal nitrogenous solutes like urea and urobilin; it does not impair sodium-glucose transporters or cause pathological glucose spilling into urine. [Confusion Trap]: Conflating a clinical diagnostic sign of pathology (diabetic glucosuria) with an acute physiological hydration change.",
            "cn": "【涉及知识点】尿糖（Glucosuria）仅发生在血糖浓度极度超出肾糖阈（约10 mmol/L）导致近曲小管载体饱和时，是未经治疗的糖尿病的典型病理体征。【异同辨析】单纯的生理性脱水只是减少了尿中的水分溶剂，并不升高血糖，近曲小管依然将原尿中的葡萄糖100%全数重吸收回血液，健康人尿液中绝无葡萄糖。【混淆陷阱】把病理学上的典型异常尿液指标（糖尿）与正常人体在运动脱水状态下的浓缩尿现象相混淆。"
        }
    },

    "Rev_SecA_Q23": {
        "A": {
            "correct": False,
            "en": "[Concept]: The liver deaminates amino acids into urea and breaks down haemoglobin into bilirubin, discharging bile into the duodenum. [Comparison]: The liver manufactures urea and releases it into hepatic veins to circulate internally; it has no external ducts leading directly to the environment to excrete water, urea, and salts. [Confusion Trap]: Conflating the chemical site of waste creation (liver) with an excretory organ that actually discharges waste to the exterior of the body.",
            "cn": "【涉及知识点】肝脏（Liver）是处理代谢废物的中心化工厂，将有毒的氨转化为尿素并将衰老红细胞分解产物转化为胆汁色素。【异同辨析】肝脏合成的尿素直接排入下腔静脉的血液循环中，由血液运走；肝脏本身并没有向体外直接开口的排泄管道，不属于向外界环境排汗或排尿的外排器官。【混淆陷阱】严重混淆了废物的“生化合成器官（肝脏）”与向体外直接排泄物质的“外分泌排泄器官（皮肤/肾脏）”。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Eccrine sweat glands located in the dermis of the skin secrete sweat primarily for thermoregulation (evaporative cooling). [Comparison]: Sweat fluid is an ultrafiltrate of plasma composed mostly of water (>99%), but it inherently carries small quantities of dissolved sodium chloride and metabolic urea, making the skin a secondary excretory organ. [Key Criteria]: Aligns with the Cambridge definition of the skin as a supplementary excretory organ.",
            "cn": "【涉及知识点】皮肤真皮层分布着数百万个外分泌汗腺（Sweat glands），受交感神经支配分泌汗液，主要用于蒸发散热。【异同辨析】汗液本质上是毛细血管血浆的滤出衍生液，主要成分是水，但在出汗降温的同时，不可避免地伴随排出了溶解的氯化钠矿物盐以及微量的代谢废物尿素。【核心考点】准确切合剑桥大纲关于人体皮肤汗腺在体温调节的同时兼具排出部分水、无机盐与尿素的排泄考点。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The stomach is a muscular digestive organ secreting gastric juice (hydrochloric acid and pepsin) into its lumen to hydrolyse proteins. [Comparison]: Gastric secretions are internal digestive fluids that stay within the alimentary canal to break down food boluses; the stomach does not excrete metabolic urea or salts out of the body. [Confusion Trap]: Confusing luminal digestive fluid secretion with systemic excretion of metabolic waste products.",
            "cn": "【涉及知识点】胃（Stomach）是消化道膨大的肌性消化器官，分泌含胃蛋白酶原和浓盐酸的胃液以初步分解食糜中的蛋白质。【异同辨析】胃液属于消化腺的外分泌液，排入消化管腔内用于催化食物水解，绝不承担将体内代谢废物尿素和多余盐分向体外环境排泄的任务。【混淆陷阱】把消化道内部的分泌液（胃液）与机体对外排出的代谢排泄物发生概念混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The lungs excrete gaseous carbon dioxide and water vapour during the expiration phase of pulmonary ventilation. [Comparison]: The respiratory epithelium cannot excrete non-volatile, mineral solutes or nitrogenous wastes like urea and sodium chloride; the prompt explicitly requires the removal of urea and salts alongside water. [Confusion Trap]: Remembering that lungs are an excretory organ for water, but overlooking that they cannot excrete non-volatile dissolved solutes like urea and salts.",
            "cn": "【涉及知识点】肺（Lungs）是机体排泄呼吸废气的主要器官，随呼出气排出二氧化碳气体和饱和水蒸气。【异同辨析】气体排泄只能排出挥发性物质；尿素和无机盐（氯化钠）属于不挥发的高熔点固体溶质，根本不可能化为气体随肺部呼出，故肺无法满足题干中排出尿素和盐分的要求。【混淆陷阱】只注意到了“排出水分”，记起呼出气体含有水蒸气，却忽略了肺完全没有排出不挥发性尿素和无机盐的能力。"
        }
    },

    "Rev_SecA_Q24": {
        "A": {
            "correct": False,
            "en": "[Concept]: An electrical impulse (action potential) travelling along the axon of a neurone is a nerve impulse, belonging to the nervous coordination system. [Comparison]: Nerve impulses are rapid electrical depolarizations travelling along dedicated cellular wiring (axons); hormones are chemical signaling molecules transported through the liquid bloodstream. [Confusion Trap]: Confusing the two distinct bodily communication networks: the electrical nervous system versus the chemical endocrine system.",
            "cn": "【涉及知识点】神经冲动（Nerve impulse/动作电位）是沿神经元轴突质膜传导的暂态去极化生物电信号，属于神经系统。【异同辨析】神经冲动是高度特异性、沿固定神经纤维快速传递的“电信号”；而激素是由腺体分泌并借助体循环血液运输的“化学分子信使”。二者本质载体完全不同。【混淆陷阱】把人体两大信息调控系统（神经调节与激素调节）的信号形式相混淆，混淆了电信号与化学信使。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: A hormone is a regulatory chemical substance synthesized and secreted by ductless endocrine glands directly into the bloodstream. [Comparison]: Circulating in blood plasma at low concentrations, hormones travel throughout the body to alter the physiological activity of specific target cells bearing complementary receptors. [Key Criteria]: The word-for-word official Cambridge textbook definition of a hormone.",
            "cn": "【涉及知识点】激素（Hormone）是由无导管的内分泌腺（Endocrine glands）合成并直接分泌进入毛细血管血液中的化学信使。【异同辨析】激素在血浆中以极微小浓度循环周流全身，只特异性识别并结合带有互补空间受体的特定靶器官或靶细胞，从而改变其代谢活动与生理功能。【核心考点】完美契合剑桥大纲中关于激素是“由内分泌腺产生、经血液运输、改变靶器官活动的化学信使”的经典标准定义。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: A white blood cell (leucocyte) is a complete eukaryotic cellular unit providing immunological defence against pathogens. [Comparison]: Leucocytes are living cells with nuclei and organelles; hormones are acellular biochemical molecules (proteins, peptides, amines, or steroids) lacking cellular structure. [Confusion Trap]: Conflating cellular biological units with molecular biochemical messengers circulating in blood.",
            "cn": "【涉及知识点】白细胞（White blood cell）是免疫系统中有核、具有完整细胞器和运动能力的微观真核细胞生命单元。【异同辨析】白细胞是具有代谢活性的活细胞；而激素只是由腺细胞合成分泌的无细胞结构的生化化学分子（多肽或类固醇）。二者属于完全不同的物质层次。【混淆陷阱】由于二者都在血液中循环游走，学生容易在物质层级（细胞级 vs 分子级）上发生认知混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: A digestive enzyme is an exocrine protein catalyst secreted through ducts into the lumen of the alimentary canal to hydrolyse food molecules. [Comparison]: Digestive enzymes act locally in extracellular gut cavities and are not transported by blood; hormones are endocrine messengers secreted ductlessly into blood to regulate distant target organs. [Confusion Trap]: Confusing duct-directed exocrine secretions (digestive enzymes) with bloodstream-directed endocrine secretions (hormones).",
            "cn": "【涉及知识点】消化酶（Digestive enzyme）是由外分泌腺通过导管排入消化管腔的生物催化剂蛋白（如唾液淀粉酶、胃蛋白酶）。【异同辨析】消化酶局限于肠腔内水解大分子营养物，绝不进入血液循环；而激素属于内分泌，无导管直接入血以调节远端器官。二者在分泌方式与功能路径上截然相反。【混淆陷阱】把外分泌腺分泌到导管腔内的催化酶，与内分泌腺分泌到血液中的调控激素相混淆。"
        }
    },

    "Rev_SecA_Q25": {
        "A": {
            "correct": False,
            "en": "[Concept]: The pituitary gland is the 'master gland' located at the base of the brain beneath the hypothalamus, producing trophic hormones (e.g. TSH, ACTH, FSH, LH, GH, ADH). [Comparison]: The pituitary controls growth and stimulates other endocrine organs; it does not synthesize insulin, which is made exclusively by pancreatic beta cells. [Confusion Trap]: Defaulting to the prestigious 'master gland' whenever asked about any prominent hormone.",
            "cn": "【涉及知识点】脑垂体（Pituitary gland）位于下丘脑下方的垂体窝内，被称为“主内分泌腺”，分泌促甲状腺激素、促性腺激素及生长激素等。【异同辨析】垂体调控全身发育并向其他腺体下达上级指令；但它绝不分泌调节血糖的胰岛素。胰岛素的专属合成工厂位于腹部的胰腺。【混淆陷阱】因脑垂体享有“主腺体”的美誉，学生在遇到不确定的重要激素时容易盲目套用垂体作为默认选项。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: The adrenal glands are paired pyramid-shaped glands perched atop each kidney, whose medulla secretes adrenaline and cortex secretes steroid hormones. [Comparison]: Adrenal hormones mobilize the fight-or-flight response and raise blood glucose; insulin does the opposite (lowers blood glucose) and is produced in the pancreas. [Confusion Trap]: Conflating endocrine organs that regulate glucose metabolism; confusing the gland that elevates glucose in stress (adrenal) with the gland that lowers it (pancreas).",
            "cn": "【涉及知识点】肾上腺（Adrenal gland）是坐落于双肾顶端的内分泌腺体，髓质分泌肾上腺素，皮质分泌糖皮质激素和醛固酮。【异同辨析】肾上腺素和皮质醇的作用是在危机应激时迅速“升高血糖”；而胰岛素专职在餐后“降低血糖”，且由胰腺分泌，二者解剖源头不同。【混淆陷阱】知道肾上腺参与代谢调节，但将负责应激升糖的肾上腺与负责日常降糖的胰腺发生了器官错配。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: The pancreas houses millions of endocrine micro-organs called the islets of Langerhans, embedded within its exocrine acinar tissue. [Comparison]: Beta cells within these pancreatic islets monitor blood glucose levels and synthesize and secrete the peptide hormone insulin whenever blood glucose rises. [Key Criteria]: Foundational Cambridge curriculum identification of the insulin-secreting gland.",
            "cn": "【涉及知识点】胰腺（Pancreas）的实质内部散布着大量被称为“胰岛（Islets of Langerhans）”的内分泌细胞团块。【异同辨析】胰岛内部的β细胞具备直接感知高血糖浓度的葡萄糖感应机制，当餐后血糖上升时立即分泌胰岛素入血，促使外周细胞摄糖。【核心考点】精准对应剑桥教材中关于胰岛素是由胰腺（Pancreas）内分泌部合成与分泌的标志性考点。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The thyroid gland is a butterfly-shaped endocrine organ in the anterior neck draped over the trachea, producing iodine-containing thyroxine. [Comparison]: Thyroxine governs basal metabolic rate and cellular oxygen consumption across all tissues; it does not produce insulin and does not acutely manage blood glucose fluctuations. [Confusion Trap]: General confusion among the major prominent glands of the endocrine system.",
            "cn": "【涉及知识点】甲状腺（Thyroid gland）是位于颈前部、贴附在喉和气管两侧的蝴蝶状内分泌腺体，合成含碘的甲状腺素（Thyroxine）。【异同辨析】甲状腺素的核心功能是调控机体所有细胞的基础代谢率与生长发育速率；它完全不分泌胰岛素，不负责餐后急性能量底物的去向分配。【混淆陷阱】对初中阶段接触的几大核心内分泌腺名称记忆含混，在胰腺与甲状腺之间发生无根据的随机乱选。"
        }
    },

    "Rev_SecA_Q26": {
        "A": {
            "correct": True,
            "en": "[Concept]: The adrenal glands (suprarenal glands) are paired endocrine structures capping the superior pole of each kidney. [Comparison]: The inner adrenal medulla receives sympathetic preganglionic neural innervation and releases adrenaline directly into the circulation during acute stress or danger (fight-or-flight). [Key Criteria]: Exact anatomical and physiological match for adrenaline secretion.",
            "cn": "【涉及知识点】肾上腺（Adrenal glands/Suprarenal glands）是左右成对坐落在两侧肾脏上极的扁平黄色内分泌腺体。【异同辨析】肾上腺由外周皮质和中央髓质构成，其髓质受交感神经直接支配，在遭遇惊吓、危机或剧烈运动时瞬间暴发释放大量肾上腺素入血，触发战或逃反应。【核心考点】完美契合剑桥大纲中关于位于肾脏顶端并分泌应激肾上腺素的腺体——肾上腺（Adrenal glands）的标准界定。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: The ovaries are the paired female reproductive gonads located in the lateral pelvic cavity. [Comparison]: Ovaries produce female gametes (ova) and secrete oestrogen and progesterone to regulate secondary sexual traits and reproduction; they are not atop the kidneys and do not release adrenaline. [Confusion Trap]: Confusing pelvic reproductive gonads with abdominal endocrine glands responding to acute danger.",
            "cn": "【涉及知识点】卵巢（Ovaries）是女性盆腔内的成对生殖腺，位于子宫两侧，负责产生成熟卵子并分泌雌激素与孕激素。【异同辨析】卵巢主导女性生殖周期和第二性征发育，其解剖位置深在小骨盆内，根本不在肾脏上方，且绝不分泌参与紧急应激的肾上腺素。【混淆陷阱】解剖位置与生理系统双重错配；误把盆腔深部的生殖内分泌腺当成了腹后壁肾脏顶部的应急腺体。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The testes are the paired male reproductive gonads housed externally in the scrotum beneath the pelvis. [Comparison]: Testes produce spermatozoa and secrete testosterone to drive male secondary sexual characteristics; they are physically located far below the abdominal kidneys and do not produce adrenaline. [Confusion Trap]: Misattributing acute fight-or-flight hormone production to male reproductive gonads.",
            "cn": "【涉及知识点】睾丸（Testes）是男性的生殖腺，位于体外阴囊内以维持低于腹腔的核心温度，负责产生精子并分泌睾酮。【异同辨析】睾丸负责男性第二性征的维持和生殖繁衍，其解剖位置位于体表阴囊，远离腹后壁的肾脏，且不分泌肾上腺素。【混淆陷阱】对生殖腺与应急腺体的解剖定位和功能混淆，错误将男性雄性激素腺体当成应对危险的腺体。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The thyroid gland is a cervical endocrine gland positioned in the neck anterior to the upper trachea. [Comparison]: The thyroid produces thyroxine for metabolic rate control; it is located in the throat region, thousands of millimetres away from the kidneys, and does not synthesize adrenaline. [Confusion Trap]: Anatomic dislocation of neck glands to the retroperitoneal kidney region.",
            "cn": "【涉及知识点】甲状腺（Thyroid gland）是位于颈部气管前方下部的内分泌腺，合成分泌甲状腺激素调控全身能量代谢。【异同辨析】甲状腺位于颈部前下方，而肾脏深居后腹膜腔脊柱两侧，二者相隔甚远；甲状腺不位于肾脏顶端，也不分泌肾上腺素。【混淆陷阱】对人体各腺体的空间解剖图景缺乏清晰认知，把颈部的甲状腺张冠李戴转移到了腹腔肾脏上方。"
        }
    },

    "Rev_SecA_Q27": {
        "A": {
            "correct": False,
            "en": "[Concept]: Rapid onset (measured in milliseconds) and transient duration (milliseconds to seconds) are defining characteristics of nervous coordination mediated by action potentials. [Comparison]: Hormones travel via bulk convective blood flow, which is orders of magnitude slower; once delivered, hormones persist until enzymatic degradation, making endocrine responses slower and longer-lasting. [Confusion Trap]: Complete inversion of the fundamental kinetic properties of the body's two coordination systems.",
            "cn": "【涉及知识点】起效极快（毫秒级）且持续时间短暂（电信号终止即停止）是神经调节（Nervous coordination）的标志性特征。【异同辨析】沿神经纤维传导的电信号速度高达上百米每秒；而激素必须进入血液循环漫游扩散，起效显著较慢。若选“更快且更短暂”属于将二者特征完全倒置。【混淆陷阱】方向性严重搞反；把神经调节的“快而短暂”错误安插在激素调节头上，缺乏对体液运输物理速度的认知。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Endocrine responses rely on chemical messengers diffusing into capillary beds and circulating throughout the cardiovascular system to reach target receptors. [Comparison]: This circulatory transit makes hormonal responses slower to start (seconds to minutes or hours), but target cellular metabolic changes and hormone clearance take time, making their effects longer-lasting. [Key Criteria]: Core Cambridge comparative principle between nervous and endocrine control.",
            "cn": "【涉及知识点】内分泌激素调节依赖化学分子通过毛细血管进入血液循环，经体循环长途跋涉到达全身靶组织。【异同辨析】由于依赖血液流动与跨膜扩散，激素从释放到发挥效应需要数秒、数分钟甚至更久（起效较慢）；但激素在血液和细胞内降解耗时较长，引发的代谢改变可持续数小时至数天（效应持久）。【核心考点】精准对应剑桥大纲中关于激素调节相比神经调节“起效慢但作用持久（Slower to start, but longer-lasting）”的经典结论。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Evolutionary selection crafted two distinct, complementary communication modalities with divergent temporal kinetics. [Comparison]: Action potentials travel along nerve axons at velocities up to 100 m/s; blood circulation requires roughly 30–60 seconds for a single complete circuit, making identical speed and duration biologically impossible. [Confusion Trap]: Assuming biological regulatory mechanisms are identical and lack functional division of labor.",
            "cn": "【涉及知识点】人体神经系统与内分泌系统在进化上形成了高度互补的分工，具有截然不同的时间动力学特征。【异同辨析】神经元电传导速度可达100 m/s，专司即刻危机闪避；血液循环一周需30至60秒，分子解离降解需更长时间。二者速度与时效绝不可能完全一致。【混淆陷阱】对机体两大系统的分工演化缺乏理解，平铺直叙地误以为体内所有调节速度都一视同仁。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Reflex actions are rapid, involuntary motor responses governed strictly by neural reflex arcs (sensory receptor -> sensory neurone -> relay neurone -> motor neurone -> effector muscle/gland). [Comparison]: Hormones have zero involvement in simple somatic protective reflexes (e.g. knee-jerk or withdrawal reflex); they coordinate developmental, metabolic, and reproductive events over long timescales. [Confusion Trap]: Inappropriately applying the terminology of nervous reflex arcs to the endocrine system.",
            "cn": "【涉及知识点】反射弧（Reflex arc）是由感受器、传入神经、神经中枢、传出神经和效应器构成的纯神经生物通路。【异同辨析】反射活动（如缩手反射、膝跳反射）属于不假思索的快速电反应，激素完全不参与躯体反射弧的传导；激素主要统管全身生长、发育、繁殖及代谢平衡。【混淆陷阱】把神经系统专属的核心概念（反射）硬搬到内分泌系统，混淆了反射弧与激素循环靶向机制。"
        }
    },

    "Rev_SecA_Q28": {
        "A": {
            "correct": False,
            "en": "[Concept]: A cell nucleus houses chromosomes and coordinates gene transcription, being present in nearly all eukaryotic human somatic cells. [Comparison]: Almost all living human cells possess a nucleus (except mature RBCs), yet hormones only affect specific target cells; possessing a nucleus does not confer hormone sensitivity without specific receptor proteins. [Confusion Trap]: Assuming that because the nucleus controls cell activities, it is the direct sensor for all incoming blood chemicals.",
            "cn": "【涉及知识点】细胞核（Nucleus）是真核细胞储存遗传物质DNA、主导转录与细胞生命活动调控的中心细胞器。【异同辨析】人体除成熟红细胞和血小板外几乎所有体细胞均含有细胞核；但特定激素却只对极少数靶细胞起效。细胞核的存在绝不能决定激素的识别专一性。【混淆陷阱】将细胞核统管全细胞的“普遍重要性”，误当成了对外来特定激素分子的“特异性识别受体”。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Target cells are distinguished by the expression of specific receptor proteins (transmembrane or intracellular) complementary in 3D conformation to that hormone. [Comparison]: Hormones diffuse past millions of non-target cells without effect; only target cells bearing complementary receptors bind the hormone (like a lock and key) to initiate a signal transduction cascade. [Key Criteria]: The definitive molecular mechanism of endocrine specificity in the Cambridge curriculum.",
            "cn": "【涉及知识点】靶细胞之所以能响应特定激素，是因为其细胞膜表面或胞浆内表达有与该激素空间三维构象高度契合的“特异性受体蛋白（Complementary receptor）”。【异同辨析】血液中的激素与靶细胞受体的结合严格遵循“锁钥原理”；没有对应受体的细胞对游离激素视而不见，唯有具备互补受体的细胞才能启动细胞内级联反应。【核心考点】准确契合剑桥大纲中关于激素通过与靶细胞特异性受体结合（Complementary receptor）发挥调节作用的核心分子机制。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Mitochondria are double-membraned organelles responsible for aerobic cellular respiration and ATP synthesis in eukaryotic cells. [Comparison]: Mitochondria provide metabolic energy for general cell survival, but they lack the external ligand-binding receptor sites needed to recognize hormones in circulating blood. [Confusion Trap]: Confusing general cellular power generators with cell-surface regulatory recognition proteins.",
            "cn": "【涉及知识点】线粒体（Mitochondria）是真核细胞进行有氧呼吸第二、三阶段合成ATP分子的细胞器“动力工厂”。【异同辨析】人体几乎所有活细胞内部都拥有线粒体以维持基础生命能量，但线粒体深居胞质内部，不具备在质膜上识别血液中循环激素的配体结合位点。【混淆陷阱】把细胞通用的供能细胞器，与质膜上行使特异性信息感知功能的膜蛋白受体混为一谈。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: A cell wall is a rigid, cellulose- or chitin-based extracellular layer found in plants, algae, fungi, and bacteria. [Comparison]: Animal cells (including human cells) NEVER possess cell walls; selecting this option reflects a fundamental misconception of animal versus plant histology. [Confusion Trap]: Severe elementary confusion regarding the basic structural differences between animal and plant cells.",
            "cn": "【涉及知识点】细胞壁（Cell wall）是由纤维素或果胶构成的坚硬外壁保护层，只存在于植物、真菌和细菌细胞外围。【异同辨析】人类等所有动物细胞只有流动的质膜（Cell membrane），绝对不存在细胞壁；本选项在人体生理学语境下属于根本性的生物界别结构错误。【混淆陷阱】极其初级的动植物细胞结构混淆；把植物特有的支持结构当作人体细胞响应激素的必要条件。"
        }
    },

    "Rev_SecA_Q29": {
        "A": {
            "correct": False,
            "en": "[Concept]: Glucagon is a peptide hormone synthesized and secreted by alpha cells of the pancreatic islets of Langerhans. [Comparison]: Glucagon is released in response to hypoglycemia (low blood sugar) to stimulate glycogen breakdown in the liver, which INCREASES blood glucose concentration; insulin decreases it. [Confusion Trap]: Constant confusion between the two antagonistic pancreatic hormones that perform opposing regulatory tasks.",
            "cn": "【涉及知识点】胰高血糖素（Glucagon）是由胰腺胰岛α细胞合成并分泌的升高血糖的多肽激素。【异同辨析】在两餐之间空腹或饥饿导致低血糖时，胰高血糖素被激发释放，命令肝细胞水解糖原为葡萄糖释放入血以“升高血糖”；其效应与降低血糖截然相反。【混淆陷阱】剑桥高频失分点：将胰腺分泌的这一对具有拮抗效应的调节激素（降糖的胰岛素 vs 升糖的胰高血糖素）发生功能反选。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Adrenaline is an emergency catecholamine hormone secreted by the adrenal medulla during acute sympathetic activation (fight-or-flight). [Comparison]: Adrenaline stimulates glycogenolysis in hepatocytes and skeletal muscles to ELEVATE blood glucose rapidly for emergency ATP production; it never lowers postprandial blood sugar. [Confusion Trap]: Remembering that adrenaline influences glucose metabolism, but confusing its glucose-elevating emergency role with insulin's post-meal lowering role.",
            "cn": "【涉及知识点】肾上腺素（Adrenaline）是在面临突发危险或剧烈应激时由肾上腺髓质瞬间爆发释放的应急激素。【异同辨析】肾上腺素迅速调动肝脏和骨骼肌分解糖原，促使血糖迅速“飙升”，为大脑和肌肉提供充沛动力；它绝不在饱餐后分泌，更不降低血糖。【混淆陷阱】知道肾上腺素能影响糖代谢，但混淆了其在危机中“大幅升糖”的应急角色与餐后“降糖”的平稳调节角色。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Insulin is synthesized and released by pancreatic beta cells in response to elevated blood glucose levels following digestion and absorption of a meal. [Comparison]: Insulin binds to target receptors on muscle and liver cells, promoting glucose uptake, cellular respiration, and glycogenesis (conversion of glucose into insoluble glycogen), directly reducing blood glucose concentration back to the homeostatic baseline. [Key Criteria]: The canonical Cambridge definition of postprandial glucose regulation.",
            "cn": "【涉及知识点】胰岛素（Insulin）是在进食后碳水化合物被消化水解为葡萄糖并吸收入血导致血糖升高时，由胰腺胰岛β细胞分泌的降血糖激素。【异同辨析】胰岛素作为生化钥匙打开全身细胞对葡萄糖的通透大门，加速骨骼肌和脂肪细胞摄取葡萄糖，并命令肝细胞将葡萄糖脱水聚合为糖原储存，从而使血糖快速回落至正常设定点。【核心考点】完美契合剑桥大纲中关于胰岛素是在餐后促使血糖浓度下降并维持基线稳态的专属激素。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Testosterone is the principal androgenic steroid hormone secreted by the Leydig cells of the testes. [Comparison]: Testosterone orchestrates male pubertal development, secondary sexual characteristics, and spermatogenesis; it has zero direct involvement in acute postprandial glucose homeostatic control loops. [Confusion Trap]: Conflating reproductive endocrine regulators with carbohydrate metabolic hormones.",
            "cn": "【涉及知识点】睾酮（Testosterone）是由睾丸间质细胞合成的类固醇雄性激素，主要调控男性生殖系统与骨骼肌发育。【异同辨析】睾酮负责维持男性第二性征、精子发生及蛋白质同化合成，其分泌完全不受餐后急性血糖涨落的调控，不参与血糖平衡控制。【混淆陷阱】对激素分类认知模糊，在代谢平衡题目中混入了性激素干扰项。"
        }
    },

    "Rev_SecA_Q30": {
        "A": {
            "correct": False,
            "en": "[Concept]: Glycogenesis (the conversion of soluble glucose into stored insoluble glycogen) is stimulated by INSULIN when blood glucose concentration is high. [Comparison]: When blood glucose is already TOO LOW, converting more glucose into storage would deplete circulating sugar completely, causing hypoglycaemic coma or death; glucagon does the exact opposite. [Confusion Trap]: Reversing the metabolic direction of glycogenolysis versus glycogenesis.",
            "cn": "【涉及知识点】将血液中溶解的游离葡萄糖脱水缩合为不溶性糖原储存（糖原合成/Glycogenesis）是由高血糖刺激“胰岛素”介导的降糖途径。【异同辨析】在血糖过低时若还把原本匮乏的葡萄糖合成糖原锁存起来，将导致血液葡萄糖彻底耗竭，引发致命的低血糖昏迷；胰高血糖素执行的正是相反路线。【混淆陷阱】生化反应方向搞反；混淆了高血糖时的“合成糖原储能”与低血糖时的“分解糖原救急”。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: When blood glucose falls below normal (~4 mmol/L), pancreatic alpha cells secrete glucagon into the hepatic portal circulation. [Comparison]: Glucagon stimulates hepatic glycogenolysis (enzymatic breakdown of stored liver glycogen into glucose monomers) and releases free glucose into the blood to restore normoglycaemia. [Key Criteria]: The standard Cambridge mechanism for homeostatic response to hypoglycemia.",
            "cn": "【涉及知识点】当饥饿或剧烈运动使血糖浓度降至正常设定点以下时，胰腺胰岛α细胞迅速感知并分泌胰高血糖素（Glucagon）。【异同辨析】胰高血糖素特异性作用于肝脏细胞膜受体，激活糖原磷酸化酶，催化储存的肝糖原迅速水解分解为游离葡萄糖（Glycogenolysis），并释放入血提升血糖水平。【核心考点】精准对应剑桥考纲中关于低血糖时胰高血糖素促使肝脏将储存的糖原分解为葡萄糖的核心考点。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Excreting glucose in urine (glycosuria) is a pathological condition occurring in uncontrolled diabetes mellitus when blood glucose exceeds the renal threshold. [Comparison]: In hypoglycemia, glucose is dangerously scarce; the body's entire physiological machinery works to conserve every molecule of glucose, not dump it in urine. [Confusion Trap]: Conflating a clinical disease symptom with a regulated normal homeostatic hormonal response.",
            "cn": "【涉及知识点】随尿液排出葡萄糖（糖尿）是未受控糖尿病的特征，是因血糖过高超出肾小管重吸收饱和阈值而导致的被动溢出。【异同辨析】在血糖过低时，机体极其珍视每一分子葡萄糖，肾小管会竭尽全力100%全数重吸收；健康人体无论在何种激素调节下都绝不可能主动从尿中排糖。【混淆陷阱】将临床病理体征（糖尿）错误理解为机体通过激素主动执行的生理排泄调节反应。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Lipogenesis (converting excess glucose into triglyceride fat stores) occurs during prolonged nutritional carbohydrate surplus, driven by insulin. [Comparison]: During hypoglycemia, the body needs immediate free glucose in the circulation to power the brain and heart; converting precious scarce glucose into fat would worsen glucose starvation. [Confusion Trap]: Confusing high-calorie storage reactions with acute fasting mobilization pathways.",
            "cn": "【涉及知识点】将葡萄糖转化为脂肪储存（脂肪生成）发生在长期摄入过剩能量、胰岛素水平高涨的营养过剩状态。【异同辨析】当血糖已经偏低告急时，全身组织急需游离糖供能；若将葡萄糖转化为不溶性脂肪，等于雪上加霜加剧低血糖。低血糖时机体发生的是脂肪动员水解。【混淆陷阱】把能量过剩充裕时的脂质合成储存路径，与能量匮乏危机时的即时糖原水解动员路径相混淆。"
        }
    },

    "Rev_SecA_Q31": {
        "A": {
            "correct": False,
            "en": "[Concept]: Egestion is the discharge of undigested, unabsorbed solid food remnants (faeces) from the alimentary canal through the anus. [Comparison]: Egestion is an elemental digestive mechanical elimination process; it does not involve chemical sensing, hormonal release, or feedback loops to maintain blood parameters. [Confusion Trap]: Randomly selecting an unrelated physiological vocabulary term without evaluating the mechanism described.",
            "cn": "【涉及知识点】排遗（Egestion）是消化系统末端将未经消化吸收的食物纤维残渣以粪便形式排出肛门的生理过程。【异同辨析】排遗是消化道管腔的物理性残渣排出，完全不涉及内分泌感受器、激素循环或维持体内理化环境稳定的反馈机制。【混淆陷阱】生理学专有名词无意义乱填；未审题干中关于“调控血液浓度维持在狭窄区间”的内涵，盲选消化词汇。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Negative feedback is the primary homeostatic mechanism where a deviation from a set point triggers corrective actions that counteract and reverse the change. [Comparison]: When blood glucose rises, insulin lowers it; when blood glucose falls, glucagon raises it; this push-pull antagonistic antagonism maintains glucose within a narrow physiological window (~4–7 mmol/L). [Key Criteria]: The textbook paradigm of negative feedback homeostasis in Cambridge G8.",
            "cn": "【涉及知识点】负反馈（Negative feedback）是维持内环境稳态（Homeostasis）最核心的调节机制：当某一受控变量偏离正常设定点时，系统会启动与之相反的纠偏效应以恢复平衡。【异同辨析】餐后血糖升高触发胰岛素分泌促其回落，饥饿血糖降低触发胰高血糖素促其回升；这种反向调节使血糖稳固在4.0–7.8 mmol/L的极窄范围内。【核心考点】完美切合剑桥大纲中将血糖浓度的精密控制作为生物体“负反馈（负反馈稳态）”经典范例的标准表述。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Phagocytosis is the active cellular endocytosis whereby phagocytic white blood cells engulf, neutralize, and digest microorganisms. [Comparison]: Phagocytosis is an innate immune defensive action against microscopic pathogens, not a systemic feedback control loop that regulates circulating solute concentrations. [Confusion Trap]: Confusing a cellular immunological mechanism with systemic metabolic homeostasis.",
            "cn": "【涉及知识点】吞噬作用（Phagocytosis）是白细胞（巨噬细胞、中性粒细胞）伸出伪足包裹摄入细菌并依靠溶酶体酶将其杀灭的免疫活动。【异同辨析】吞噬作用属于细胞免疫防御战术，作用对象是外来生物病原体；它与人体血液中分子浓度的稳态反馈闭环调控毫无关系。【混淆陷阱】把免疫学中的细胞吞噬杀菌机制，与生理学中维持理化平衡的内分泌负反馈机制混为一谈。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Simple diffusion is the passive, unassisted movement of individual solute molecules down a concentration gradient as a result of thermal kinetic energy. [Comparison]: Simple diffusion lacks set points, receptors, control centers, and effectors; blood glucose homeostasis is an active whole-body hormonal feedback regulatory network. [Confusion Trap]: Conflating a basic physical transport process with a complex, coordinated systemic physiological control system.",
            "cn": "【涉及知识点】单纯扩散（Simple diffusion）是分子凭借自身热运动顺浓度梯度自发进行的无耗能物理跨膜或介质移动。【异同辨析】扩散只是孤立的被动物理现象，不具备任何设定点、传感器、比较器或负反馈执行机构；血糖调控是一个高度系统化、多器官联动的负反馈控制网络。【混淆陷阱】把单个分子局部的被动物理位移，与整个机体精密构建的系统级生理调控闭环相混淆。"
        }
    },

    "Rev_SecA_Q32": {
        "A": {
            "correct": True,
            "en": "[Concept]: Type 1 diabetes (insulin-dependent diabetes mellitus) is an autoimmune disorder where cytotoxic T cells destroy the insulin-producing beta cells in the pancreatic islets. [Comparison]: Because beta cells are obliterated, the pancreas produces zero endogenous insulin, leaving patients incapable of lowering blood glucose without exogenous insulin injections. [Key Criteria]: Precise pathology matching the Cambridge syllabus definition of Type 1 diabetes.",
            "cn": "【涉及知识点】1型糖尿病（Type 1 diabetes）是一种自体免疫性内分泌疾病，患者免疫系统发生紊乱，自身抗体与T细胞特异性攻击并摧毁了胰岛β细胞。【异同辨析】由于胰岛β细胞永久性坏死丧失，患者体内完全丧失了自主合成与分泌胰岛素的能力，导致餐后血糖严重蓄积失控，必须依赖外源胰岛素注射治疗。【核心考点】准确对应剑桥大纲中关于胰腺完全无法分泌胰岛素所引起的疾病即为1型糖尿病的经典考核点。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Asthma is a chronic inflammatory disorder of the respiratory conducting airways characterized by bronchial hyperresponsiveness, smooth muscle bronchospasm, and excessive mucus plugging. [Comparison]: Asthma restricts air passage in the respiratory bronchioles, producing wheezing and dyspnoea; it is completely unrelated to pancreatic histology or endocrine insulin secretion. [Confusion Trap]: Confusing a prevalent childhood respiratory illness with an endocrine metabolic disorder.",
            "cn": "【涉及知识点】哮喘（Asthma）是呼吸系统导气管道的慢性变态反应性炎症，以支气管平滑肌痉挛狭窄和黏膜水肿为特征。【异同辨析】哮喘的病变局限于肺部支气管树，导致呼吸困难与喘息；其与腹腔胰腺组织结构毫无关联，患者的胰岛素合成与分泌完全正常。【混淆陷阱】在青少年常见慢性非传染性疾病名词中随意盲选，混淆了呼吸系统疾病与内分泌代谢系统疾病。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Anaemia is a haematological condition marked by a deficiency in red blood cell count or a below-normal concentration of haemoglobin (often caused by dietary iron deficiency). [Comparison]: Anaemia causes fatigue due to impaired oxygen carriage in blood; it does not impair endocrine hormone synthesis or pancreatic beta cell function. [Confusion Trap]: Confusing blood gas transport deficiencies with endocrine gland failure.",
            "cn": "【涉及知识点】贫血（Anaemia）是循环血液中红细胞容量减少或血红蛋白浓度低于正常范围的血液系统疾病（常因缺铁导致）。【异同辨析】贫血的核心病理是机体携氧能力下降导致组织缺氧乏力；患者的胰腺功能完好无损，能正常合成并分泌胰岛素以调控血糖。【混淆陷阱】将血液成分中的携氧蛋白缺乏病症，与内分泌腺体衰竭导致的血糖调节疾病相混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: A urinary tract infection (UTI) is an acute microbial infection (typically by enteric coliform bacteria such as Escherichia coli) colonizing the urethra, bladder, or kidneys. [Comparison]: A UTI causes dysuria and urinary urgency; it is an infectious disease of the excretory plumbing, not an autoimmune endocrine failure of pancreatic islets. [Confusion Trap]: Associating diabetes with frequent urination and mistakenly jumping to a urinary infection.",
            "cn": "【涉及知识点】尿路感染（UTI）是由肠道大肠埃希菌等病原微生物逆行侵入尿道、膀胱或肾孟引发的急性化脓性感染性疾病。【异同辨析】尿路感染属于泌尿管道的外源微生物感染，表现为尿频尿急尿痛；而胰腺无法分泌胰岛素属于自身免疫破坏胰岛，二者病因与靶器官风马牛不相及。【混淆陷阱】由于糖尿病患者血糖过高也会出现多尿症状，学生容易因此产生浅层联想而误选尿路病变。"
        }
    },

    "Rev_SecA_Q33": {
        "A": {
            "correct": False,
            "en": "[Concept]: Bradycardia (slowing of the heart rate) is driven by parasympathetic nervous system stimulation via acetylcholine release from the vagus nerve during resting states. [Comparison]: Adrenaline prepares the organism for immediate physical combat or flight; slowing the heart would drop cardiac output and deprive muscles of oxygen, which would be disastrous in an emergency. [Confusion Trap]: Inverting the physiological direction of autonomic fight-or-flight cardiovascular stimulation.",
            "cn": "【涉及知识点】心率减慢（心动过缓）受副交感神经（迷走神经）末梢释放乙酰胆碱支配，发生在平静放松或睡眠休息状态。【异同辨析】肾上腺素的使命是调动一切资源应对危机搏斗；若心跳变慢将导致心输出量骤减、骨骼肌缺血缺氧，这与战或逃反应的生存逻辑完全相悖。【混淆陷阱】自主神经与应激反应方向性严重倒置；把放松状态下的心脏抑制反应错误当成了应激激素的兴奋反应。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Adrenaline acts on beta-1 adrenergic receptors in the heart to increase rate and contractility, and on beta-2 receptors in the airways to relax bronchial smooth muscle (bronchodilation). [Comparison]: An increased heart rate accelerates blood delivery, while wider airways reduce resistance to airflow, maximizing the uptake and delivery of oxygen and glucose to contracting skeletal muscles during a crisis. [Key Criteria]: The textbook classic physiological response to adrenaline.",
            "cn": "【涉及知识点】肾上腺素（Adrenaline）作为战或逃激素，特异性激动心脏β1受体使心肌收缩力增强、心率显著加快，并激动气道β2受体促使支气管平滑肌舒张。【异同辨析】心跳加快大幅提升了每分钟心输出量，气道展宽极大降低了呼吸通气阻力，二者协同作用确保海量氧气与葡萄糖在危机瞬间以最高速输送至做功的骨骼肌。【核心考点】完美切合剑桥教材中关于肾上腺素能引发“心率加快且气道展宽（An increased heart rate and wider airways）”的标准考点。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Hypoglycaemia (decreasing blood glucose) is mediated solely by the actions of insulin. [Comparison]: Adrenaline binds to hepatic and skeletal muscle adrenergic receptors to trigger rapid glycogenolysis and gluconeogenesis, which ELEVATES blood glucose; reducing blood sugar would starve fighting muscles of energy. [Confusion Trap]: Confusing the emergency glucose-mobilizing role of adrenaline with the glucose-storing action of insulin.",
            "cn": "【涉及知识点】促使血糖浓度降低是胰岛素的专属生理功能，主要通过加速葡萄糖吸收与合成糖原实现。【异同辨析】肾上腺素在应激时会强力刺激肝脏迅速将糖原水解并释放入血，导致血糖浓度急剧“升高”以为肌肉提供即时燃料，绝对不会降低血糖。【混淆陷阱】将应激状态下的急性升糖救急激素（肾上腺素），与饱餐后负责平稳降糖的代谢激素（胰岛素）相混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Digestion, peristalsis, and splanchnic blood supply are promoted by the parasympathetic division during 'rest-and-digest' periods. [Comparison]: In an acute fight-or-flight crisis, sympathetic tone and adrenaline cause splanchnic vasoconstriction, diverting blood away from the stomach and intestines to the skeletal muscles, actively suppressing digestion. [Confusion Trap]: Failing to realize the fundamental antagonism between emergency fight-or-flight survival and relaxed gastrointestinal digestion.",
            "cn": "【涉及知识点】食物的消化吸收、胃肠蠕动及消化腺分泌是由副交感神经在机体处于“休息与消化（Rest-and-digest）”状态下全力主导的。【异同辨析】面对生死存亡危机时，机体绝不可能把宝贵的血液和能量浪费在消化食物上；肾上腺素会收缩内脏血管、抑制胃肠蠕动，全力支援骨骼肌与大脑。【混淆陷阱】缺乏生理系统协调与能量再分配意识，误以为机体在应激时会把所有器官的功能都无差别地一并增强。"
        }
    },

    "Rev_SecA_Q34": {
        "A": {
            "correct": False,
            "en": "[Concept]: Oestrogen is the principal female sex steroid hormone synthesized primarily by the granulosa cells of ovarian follicles. [Comparison]: Oestrogen orchestrates female secondary sexual traits (e.g. breast development, widened hips, fat redistribution); it is not the main driver of male virilisation. [Confusion Trap]: Gender-inversion of the primary sex steroid hormones.",
            "cn": "【涉及知识点】雌激素（Oestrogen）是由卵巢卵泡颗粒细胞大量合成并分泌的具有类固醇结构的女性主导性激素。【异同辨析】雌激素负责驱动女性在青春期的第二性征发育（如乳房丰满、骨盆变宽、皮下脂肪特定分布）；它绝不是主导男性特征发育的激素。【混淆陷阱】两性关键性激素方向性对调；在考察男性特征时混淆了雌性激素与雄性激素。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Testosterone is the primary androgenic steroid hormone synthesized and secreted by the interstitial Leydig cells of the testes. [Comparison]: In response to pituitary LH during puberty, rising testosterone levels trigger male secondary sexual characteristics: deepening of the voice (laryngeal enlargement), facial/body hair growth, increased muscle and bone mass, and penile growth. [Key Criteria]: The standard Cambridge curriculum definition of male pubertal development.",
            "cn": "【涉及知识点】睾酮（Testosterone）是男性体内最强效的雄性类固醇激素，由睾丸间质细胞（Leydig cells）在垂体LH刺激下大量分泌。【异同辨析】青春期睾酮水平的暴发式激增直接促成男性第二性征的全面建立：喉结突出、声带加宽导致声音变粗沉、胡须及体毛旺盛生长、骨骼肌群大幅增厚。【核心考点】精准对应剑桥大纲中关于睾酮是主导男性第二性征发育的核心激素（Testosterone）的定论。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Insulin is a peptide hormone synthesized by pancreatic beta cells governing cellular glucose uptake and intermediary metabolism. [Comparison]: While insulin supports general cellular growth and protein synthesis, it has zero sex-specific virilising actions and does not govern male secondary sexual traits. [Confusion Trap]: Conflating a universal metabolic regulator with a sex-specific developmental steroid.",
            "cn": "【涉及知识点】胰岛素（Insulin）是由胰腺分泌的调控碳水化合物与脂质代谢的多肽激素，促进细胞摄取葡萄糖与合成蛋白质。【异同辨析】胰岛素是两性皆有且终生必需的基础代谢激素，完全不具备促进男性性征分化的雄激素活性，与青春期副性征发育无关。【混淆陷阱】对激素的功能类别认识混乱，未能区分“全身通用代谢激素”与“生殖系统专属发育激素”。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Adrenaline is an emergency catecholamine hormone released by the adrenal medulla during acute sympathetic activation. [Comparison]: Adrenaline coordinates immediate, transient fight-or-flight cardiovascular and metabolic survival responses; it plays no role in driving developmental anatomical changes during male puberty. [Confusion Trap]: Confusing acute stress survival hormones with long-term developmental steroid hormones.",
            "cn": "【涉及知识点】肾上腺素（Adrenaline）是由肾上腺髓质分泌的儿茶酚胺类激素，负责在几秒到几分钟内调控急性应激生存反应。【异同辨析】肾上腺素的作用是瞬时且可逆的，完全不参与青春期长达数年的性发育和骨骼解剖特征重构。【混淆陷阱】将危机时刻的短效应急激素，与青春期长期缓慢发挥组织塑形作用的性类固醇激素相混淆。"
        }
    },

    "Rev_SecA_Q35": {
        "A": {
            "correct": False,
            "en": "[Concept]: Marked deepening of the voice (voice drop) results from testosterone-induced hypertrophy of the thyroid cartilage (Adam's apple) and lengthening of the vocal cords. [Comparison]: This pronounced vocal change is a distinct MALE secondary sexual characteristic; while female voices mature slightly, marked deepening is a hallmark of male puberty. [Confusion Trap]: Attributing male androgen-dependent pubertal traits to females.",
            "cn": "【涉及知识点】变声与声音显著低沉是甲状软骨在雄激素刺激下急剧增大突出（形成喉结）、声带显著变长加厚所致的生理现象。【异同辨析】声音大幅度变粗沉是男性青春期极具标志性的第二性征；女性青春期虽然声调也会略微成熟，但绝不会出现男性特征性的嗓音大幅低沉。【混淆陷阱】把由高浓度睾酮驱动的男性特征，张冠李戴错当成由雌激素主导的女性第二性征。"
        },
        "B": {
            "correct": False,
            "en": "[Concept]: Growth of coarse terminal facial hair (beard and moustache) is driven by the conversion of circulating testosterone into dihydrotestosterone (DHT) in hair follicles. [Comparison]: Facial hair development is a signature MALE secondary sexual characteristic; healthy females do not develop heavy facial hair during puberty. [Confusion Trap]: Failing to differentiate male-specific androgen-mediated hair patterns from female pubertal changes.",
            "cn": "【涉及知识点】面部生长胡须是面部毛囊受高浓度雄激素（双氢睾酮）刺激，促使毳毛转化为粗硬有色终毛的过程。【异同辨析】生长胡须是极其典型的男性青春期副性征；健康女孩在青春期雌激素主导下绝不会在唇周和下颌生长浓密胡须。【混淆陷阱】对青春期两性体毛分布的特异性缺乏准确认识，混淆了男性专属的第二性征表现。"
        },
        "C": {
            "correct": True,
            "en": "[Concept]: Breast development (thelarche) is stimulated primarily by rising levels of oestrogen and progesterone produced by developing ovarian follicles. [Comparison]: Oestrogen stimulates the growth and branching of mammary duct systems and adipose deposition within the breasts, representing the quintessential female secondary sexual characteristic. [Key Criteria]: Unambiguous match for female pubertal development in the Cambridge syllabus.",
            "cn": "【涉及知识点】乳房发育（Breast development）是女孩进入青春期最早出现的标志性事件，受卵巢分泌的雌激素与孕激素协同驱动。【异同辨析】雌激素刺激乳腺导管系统增生分支，并促使胸部结缔组织与皮下脂肪特异性沉积，使胸部逐渐丰满，是女孩发育成熟的专属第二性征。【核心考点】完全契合剑桥教材中关于女孩青春期雌激素激发乳房发育（Breast development）的标准考查结论。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Enlargement of the testes is the initial physical sign of male puberty, driven by pituitary FSH and LH stimulating seminiferous tubules and testosterone production. [Comparison]: Females do not possess testes (their internal gonads are ovaries); this is exclusively an anatomical primary and secondary male reproductive developmental event. [Confusion Trap]: Gross anatomical confusion between male and female gonadal organs.",
            "cn": "【涉及知识点】睾丸增大是男孩青春期启动的最早解剖学指征，标志着曲细精管成熟以及生精功能的开启。【异同辨析】女性体内拥有的是卵巢，在解剖学上根本不存在睾丸结构；该选项是纯粹属于男性的生殖发育体征。【混淆陷阱】发生严重的生殖器官解剖学归属错误，把男性生殖腺的增大当成了女性的第二性征。"
        }
    },

    "Rev_SecA_Q36": {
        "A": {
            "correct": False,
            "en": "[Concept]: The pancreas is a dual digestive and metabolic gland secreting digestive enzymes and glucose-regulating hormones (insulin and glucagon). [Comparison]: The pancreas does not respond to hypothalamic gonadotropin-releasing hormone (GnRH) and does not release gonadotropic signals to wake up the gonads. [Confusion Trap]: Blindly picking a prominent internal abdominal organ without understanding the hypothalamic-pituitary-gonadal (HPG) axis.",
            "cn": "【涉及知识点】胰腺（Pancreas）是专注于调控食物水解和维持血糖稳态的内脏器官，受血糖浓度自身反馈调节。【异同辨析】胰腺完全不接受下丘脑关于启动青春期的生殖神经内分泌指令，也不合成任何促性腺激素，与唤醒卵巢和睾丸毫无关联。【混淆陷阱】缺乏下丘脑-垂体-性腺轴（HPG轴）的系统概念，在内脏器官名称中随意猜测。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: The anterior pituitary gland is the master endocrine coordinator positioned directly beneath the hypothalamus. [Comparison]: At the onset of puberty, the hypothalamus secretes pulses of GnRH, signaling the pituitary gland to synthesize and release the gonadotropins FSH (follicle-stimulating hormone) and LH (luteinizing hormone), which travel through the blood to activate the ovaries and testes. [Key Criteria]: The foundational neuroendocrine hierarchy for pubertal onset in Cambridge G8.",
            "cn": "【涉及知识点】脑垂体（Pituitary gland）位于下丘脑正下方，受下丘脑分泌的促性腺激素释放激素（GnRH）直接指挥。【异同辨析】青春期启动时，下丘脑发出化学脉冲信号指令脑垂体，垂体随即大量合成并释放卵泡刺激素（FSH）与黄体生成素（LH），经血液运送至性腺，从而“唤醒”卵巢和睾丸开始排卵、生精并分泌性激素。【核心考点】精准对应剑桥教材中关于下丘脑向脑垂体（Pituitary gland）发送信号以启动青春期性成熟的必考机制。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The adrenal glands perched atop the kidneys produce adrenaline (medulla) and corticosteroids/androgens (cortex). [Comparison]: While adrenal androgens contribute to pubic hair growth (adrenarche), the primary endocrine master switch signaled by the hypothalamus to awaken the gonads is the pituitary gland. [Confusion Trap]: Confusing the secondary adrenal contribution (adrenarche) with the primary neuroendocrine axis triggering puberty.",
            "cn": "【涉及知识点】肾上腺（Adrenal gland）主要负责应激反应（肾上腺素）以及水盐代谢（醛固酮）和微量肾上腺雄激素分泌。【异同辨析】虽然肾上腺雄激素参与了阴毛和腋毛的萌出，但下丘脑直接激活以促使睾丸和卵巢全面成熟的“中枢司令部”是垂体而非肾上腺。【混淆陷阱】把参与体毛生长的辅助性腺体，与接受下丘脑神经中枢直接指令的初级主控腺体（脑垂体）相混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: The thyroid gland in the neck secretes thyroxine to regulate basal metabolic rate and cellular oxygen consumption. [Comparison]: Thyroxine supports general somatic growth, but it does not produce the gonadotropins (FSH and LH) that stimulate the gonads to trigger puberty. [Confusion Trap]: Knowing that the thyroid influences overall physical growth, but confusing somatic growth with sexual maturation signals.",
            "cn": "【涉及知识点】甲状腺（Thyroid gland）合成分泌甲状腺素，专司调控身体所有细胞的能量代谢速度和神经系统发育。【异同辨析】甲状腺素维持身体正常的生长节律，但它绝不分泌激活生殖器官的促性腺激素，下丘脑不会通过甲状腺去唤醒性器官。【混淆陷阱】知道甲状腺与青少年的身体“生长”有关，但混淆了一般体格生长与特异性生殖系统性成熟（性腺激活）。"
        }
    },

    "Rev_SecA_Q37": {
        "A": {
            "correct": False,
            "en": "[Concept]: Menstruation is the shedding of the thickened endometrial lining accompanied by blood discharge via the vagina. [Comparison]: Menstruation defines the very beginning of the cycle (Days 1 to 5); Day 14 is the exact midpoint when the follicle ruptures, not when the lining sheds. [Confusion Trap]: Chronological inversion of the menstrual timeline; confusing the opening phase (menses) with the midpoint event (ovulation).",
            "cn": "【涉及知识点】月经（Menstruation）是子宫内膜功能层因激素撤退而缺血坏死、脱落并伴随出血排出体外的生理过程。【异同辨析】月经出血是整个人体月经周期“第1天开始”的标志事件（通常持续第1至5天）；第14天正值周期中点，此时内膜已重新增厚修复，绝非内膜剥落出血。【混淆陷阱】周期时间线严重颠倒；把周期的“起始点（月经期第1–5天）”与周期的“正中点（第14天）”发生时间混淆。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Ovulation is the release of a mature secondary oocyte from a mature Graafian follicle in the ovary into the fallopian tube (oviduct). [Comparison]: In an idealized 28-day menstrual cycle, a surge in luteinizing hormone (LH) triggered by peak oestrogen induces follicular rupture typically on Day 14. [Key Criteria]: The canonical Cambridge textbook milestone for Day 14 of the menstrual cycle.",
            "cn": "【涉及知识点】排卵（Ovulation）是成熟卵泡在黄体生成素（LH）分泌峰值诱导下破裂、将成熟卵子释放进入输卵管的生理事件。【异同辨析】在一个典型的28天月经周期中，前14天为卵泡期；在第14天左右，卵巢准时发生排卵，卵子随后在输卵管内等待受精。这是第14天发生的最核心标志性事件。【核心考点】完美契合剑桥考纲中关于28天月经周期第14天通常发生“排卵（Ovulation）”的标准考点。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Implantation is the process where a developing blastocyst embeds into the receptive, nutrient-rich endometrium of the uterus. [Comparison]: An egg released at ovulation (Day 14) requires fertilisation in the oviduct, followed by roughly 6–7 days of cleavage divisions as it travels to the uterus; implantation cannot occur before Days 20–22. [Confusion Trap]: Conflating the release of the unfertilised egg (ovulation on Day 14) with embryonic implantation a week later.",
            "cn": "【涉及知识点】着床（Implantation）是指受精卵在输卵管中经历卵裂发育成早期囊胚后，埋植于子宫内膜基质并建立母胎联系的过程。【异同辨析】即便在第14天排卵后卵子幸运受精，受精卵沿输卵管向子宫游走并分裂也需要耗时约6至7天；着床最早也只能在第20至22天发生，绝不可能在第14天排卵当天着床。【混淆陷阱】把排卵（卵子刚释放）与受精卵着床（需受精并经历长达一周的发育游走）这两个相隔甚远的时间节点混淆。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Complete breakdown and sloughing of the functional layer of the endometrium represents menstruation. [Comparison]: Endometrial breakdown occurs during Days 1 to 5; by Day 14, oestrogen has stimulated extensive mitotic repair and cellular proliferation, making the lining thick and vascularized, not broken down. [Confusion Trap]: Incorrectly assuming that the uterine lining collapses during ovulation rather than during menstruation.",
            "cn": "【涉及知识点】子宫内膜完全崩解剥落正是月经来潮的病理生理表现，发生于卵巢内雌、孕激素双双暴跌之时。【异同辨析】内膜崩解剥落严格局限于周期的第1至5天；从第6天到第14天，在雌激素强力滋养下子宫内膜正处于极其旺盛的增殖修复期，内膜变得饱满多血管，绝非崩解。【混淆陷阱】对子宫内膜周期性形态变化规律缺乏理解，误以为排卵期内膜也会碎裂脱落。"
        }
    },

    "Rev_SecA_Q38": {
        "A": {
            "correct": False,
            "en": "[Concept]: Progesterone is a steroid hormone synthesized and secreted by the corpus luteum (the yellow glandular body formed from the ruptured follicle). [Comparison]: Progesterone acts AFTER ovulation (Days 15–28) to MAINTAIN, vascularize, and induce glandular secretion in the already-thickened lining; oestrogen is the hormone that initially repairs and rebuilds it before ovulation. [Confusion Trap]: The single most common menstrual hormone mix-up: confusing the REPAIR/PROLIFERATION hormone (oestrogen) with the MAINTENANCE/SECRETORY hormone (progesterone).",
            "cn": "【涉及知识点】孕激素（Progesterone/黄体酮）是由排卵后卵巢残余卵泡壁细胞转化形成的黄体（Corpus luteum）分泌的固醇类激素。【异同辨析】孕激素的作用时段处于排卵后的黄体期（第15–28天），其使命是“维持”子宫内膜厚度并促使腺体分泌营养；在月经刚结束时（第6–13天）负责“增殖修复”内膜的是雌激素。【混淆陷阱】整个月经周期最经典的易错混淆点：严重混淆了排卵前负责“修建打底（增殖修复）”的雌激素与排卵后负责“巩固维持（分泌维护）”的孕激素。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Oestrogen is synthesized and secreted in increasing amounts by developing ovarian follicles during the follicular phase (Days 6–13). [Comparison]: Rising oestrogen stimulates rapid mitotic cell division and angiogenesis in the basal layer of the endometrium, restoring and thickening the uterine lining following its breakdown during menstruation. [Key Criteria]: The standard Cambridge syllabus role assigned to oestrogen in the menstrual cycle.",
            "cn": "【涉及知识点】雌激素（Oestrogen）在卵泡期（第6至13天）由卵巢内不断生长发育的优势卵泡颗粒细胞大量合成并释放入血。【异同辨析】随着雌激素浓度持续攀升，它强力刺激子宫内膜基底细胞发生旺盛的有丝分裂，使在月经期剥落殆尽的内膜得以迅速自我修复、再生并加厚，为迎接卵子做好准备。【核心考点】准确契合剑桥考纲中关于雌激素是在月经后负责“修复并增厚子宫内膜（Repairing and thickening the uterus lining）”的标准答案。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Testosterone is the principal androgenic steroid produced primarily in male testes, present only in trace concentrations in healthy females. [Comparison]: Physiological female testosterone levels do not regulate endometrial proliferation or repair; it plays no cyclical role in the menstrual cycle. [Confusion Trap]: Selecting an irrelevant androgen instead of the ovarian female hormones.",
            "cn": "【涉及知识点】睾酮（Testosterone）是男性体内的核心雄性激素，在健康女性体内仅由卵巢和肾上腺微量产生作为代谢中间体。【异同辨析】女性体内的微量睾酮绝不参与子宫内膜周期性的增殖修复与脱落，对子宫内膜组织学重构无调控作用。【混淆陷阱】在多选干扰项中选入了异性性激素，脱离了女性生殖内分泌周期调控的范畴。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Adrenaline is an emergency catecholamine secreted by the adrenal medulla during acute sympathetic stress. [Comparison]: Adrenaline controls acute circulatory and metabolic fight-or-flight adjustments; it has zero involvement in the cyclical tissue remodeling of the reproductive endometrium. [Confusion Trap]: Misattributing emergency sympathetic survival functions to long-term reproductive tissue growth.",
            "cn": "【涉及知识点】肾上腺素（Adrenaline）是在突发危险危机时调动心血管搏出和升高血糖的应激激素。【异同辨析】肾上腺素完全不作用于子宫内膜上皮，不参与任何女性月经周期的组织修复或维持。【混淆陷阱】对激素功能缺乏基本分类判断，把处理外界危险的短效激素盲目套用在内在生殖周期的组织修复上。"
        }
    },

    "Rev_SecA_Q39": {
        "A": {
            "correct": False,
            "en": "[Concept]: Sustained or rising progesterone and oestrogen levels occur ONLY if an embryo implants and secretes human chorionic gonadotropin (hCG), rescuing the corpus luteum. [Comparison]: When fertilisation does not take place, there is no embryo and no hCG; the corpus luteum degenerates, which causes hormone levels to crash, not rise. [Confusion Trap]: Confusing the hormonal profile of a successful pregnancy with the hormonal events of an unfertilised cycle.",
            "cn": "【涉及知识点】孕激素和雌激素在排卵后继续保持高位甚至进一步飙升，只发生在“成功受精并着床”的前提下（胚胎分泌hCG拯救并维系黄体）。【异同辨析】在题干明确强调“未受精”的语境下，没有任何胚胎信号支持黄体，黄体必然发生退化萎缩，导致激素断崖式下跌，绝不可能升高。【混淆陷阱】混淆了受精妊娠状态下的激素维持机制与未受精周期中的黄体退化机制，把怀孕时的特征选到了未受精情境下。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Without fertilisation, the corpus luteum degenerates into the scar-like corpus albicans by around Day 26–28 of the cycle. [Comparison]: Because the corpus luteum was the sole major source of progesterone and oestrogen, its collapse causes both hormones to plummet sharply; deprived of hormonal support, the uterine lining suffers ischaemia, breaks down, and sloughs off (menstruation). [Key Criteria]: Foundational endocrine trigger for menstruation in the Cambridge curriculum.",
            "cn": "【涉及知识点】若排出的卵子未与精子结合受精，卵巢内的黄体在第26至28天左右由于缺乏促黄体支持而发生退化，形成纤维化的白体（Corpus albicans）。【异同辨析】黄体退化直接切断了孕激素与雌激素的合成源头，二者在血液中的浓度出现断崖式暴跌；失去了激素支撑的子宫内膜小动脉发生痉挛缺血，内膜大面积坏死脱落并出血，触发新一轮月经来潮（Menstruation）。【核心考点】精准对应剑桥大纲中关于未受精时“雌孕激素急剧下跌导致子宫内膜脱落形成月经（They fall sharply, causing menstruation）”的核心机制。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: The menstrual cycle is an active, dynamic feedback loop driven by reciprocal hormone surges and crashes. [Comparison]: Hormones never remain constant; if levels remained static, the endometrium would remain indefinitely suspended, and negative feedback on the pituitary would prevent FSH secretion, permanently freezing the cycle. [Confusion Trap]: Assuming that biological homeostasis implies static inactivity rather than dynamic, cyclical resetting.",
            "cn": "【涉及知识点】月经周期是由下丘脑-垂体-卵巢轴通过精密的正负反馈驱动的周期性动态循环系统。【异同辨析】激素浓度绝不可能保持僵化恒定；若激素水平恒定，子宫内膜将处于僵死停滞状态，垂体也无法解除负反馈以重新分泌FSH，整个生殖周期将被永久锁死。【混淆陷阱】缺乏对生物反馈调控动态性的理解，误以为未受精就会使整个系统进入无变化的静态暂停模式。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Ovulation requires a specific surge in luteinizing hormone (LH) triggered by a prolonged high oestrogen plateau from a mature Graafian follicle. [Comparison]: Immediately after an unfertilised egg dies, hormone levels plummet, menstruation must occur, and a new cohort of primary follicles must undergo ~14 days of development before another ovulation is physically possible. [Confusion Trap]: Completely misunderstanding the chronobiology and follicular development timeline required for ovulation.",
            "cn": "【涉及知识点】排卵必须依赖成熟大卵泡分泌超高浓度雌激素诱发脑垂体释放黄体生成素（LH）峰值才能触发。【异同辨析】未受精时卵巢内根本没有成熟卵泡，激素是剧烈暴跌而非升高；机体必须先经历月经期排空内膜，并耗费约14天培育一批新的卵泡，绝不可能“立即引发下一次排卵”。【混淆陷阱】对卵泡发育的周期时空规律一无所知，错误以为排卵可以随时无缝衔接连续发生。"
        }
    },

    "Rev_SecA_Q40": {
        "A": {
            "correct": False,
            "en": "[Concept]: Adolescence is a developmental stage of rapid physical growth, organ enlargement, and hormonal changes requiring high energy and nutrient intake. [Comparison]: Skipping meals deprives the developing adolescent of critical macronutrients and essential micronutrients (e.g. iron for expanding blood volume, calcium for bone density), leading to nutritional deficiencies, fatigue, and impaired growth. [Confusion Trap]: The erroneous modern lifestyle assumption that cutting meals is a benign time-saving technique.",
            "cn": "【涉及知识点】青春期（Adolescence）是机体继婴儿期后的第二个生长发育高峰期，身高迅速蹿升、器官体积扩充且骨骼剧烈骨化。【异同辨析】不吃正餐会导致机体严重缺乏维持生长发育必需的宏量营养素与微量元素（如合成骨骼所急需的钙质、合成血红蛋白所需的铁质），导致代谢紊乱、易疲劳和骨量蓄积不足，严重损害健康。【混淆陷阱】误将现代快节奏生活中为了赶时间而牺牲三餐的错误生活方式，当成对健康无碍甚至有益的举措。"
        },
        "B": {
            "correct": True,
            "en": "[Concept]: Adolescent physical health is anchored by the fundamental triad of physical well-being: nutrition, physical activity, and restorative sleep. [Comparison]: A balanced diet supplies raw building materials and vitamins; regular exercise stimulates peak bone mass acquisition, muscular hypertrophy, and cardiovascular health; adequate sleep allows the nocturnal pulsatile release of growth hormone (GH) essential for tissue repair and somatic growth. [Key Criteria]: The standard Cambridge holistic health prescription for adolescents.",
            "cn": "【涉及知识点】青春期生理健康是由“均衡营养膳食、规律体育锻炼、充足优质睡眠”三大黄金基石共同构建的科学生活体系。【异同辨析】全面均衡的饮食提供了组织构建的充足基质；规律运动强健心肺功能、刺激骨骼矿化并提高肌肉质量；充足睡眠（每晚8–10小时）保障了脑垂体在深睡眠期脉冲式释放生长激素（GH），促进生长并消除疲劳。【核心考点】完美契合剑桥教材与健康考纲中关于青少年身心健康全面发展的核心准则（A balanced diet, regular exercise, and enough sleep）。"
        },
        "C": {
            "correct": False,
            "en": "[Concept]: Deep non-REM sleep is the prime physiological window during which the pituitary gland secretes growth hormone (GH) and the brain consolidates memories. [Comparison]: Chronic sleep curtailment suppresses growth hormone release, impairs immune cell proliferation, dysregulates appetite hormones, and degrades cognitive functioning, directly sabotaging both physical health and study outcomes. [Confusion Trap]: The widespread but counterproductive misconception that reducing sleep for academic work yields overall productive gains.",
            "cn": "【涉及知识点】深睡眠阶段是人体脑垂体脉冲式分泌生长激素（Growth hormone/GH）的最主要时段，同时也是海马体将短期记忆固化为长期记忆的关键生理窗口。【异同辨析】削减睡眠时间会严重压制生长激素的分泌，削弱免疫系统抗感染能力，导致注意力和记忆力严重受损，无论对体格发育还是学业表现都是灾难性的。【混淆陷阱】学生常犯的经验主义错误：误以为“牺牲睡眠换取学习时间”是一种值得提倡的健康生活选择。"
        },
        "D": {
            "correct": False,
            "en": "[Concept]: Regular mechanical loading through physical exercise is indispensable for osteoblast activation, cardiovascular conditioning, and metabolic regulation. [Comparison]: Avoiding exercise causes loss of muscle tone, lower bone mineral density (osteopenia), decreased cardiovascular endurance, and elevated risks of metabolic disorders and obesity. [Confusion Trap]: Misinterpreting physical passivity or avoidance of exertion as preserving energy.",
            "cn": "【涉及知识点】体育运动产生的机械负荷与有氧做功是刺激成骨细胞活性、积累峰值骨量（Peak bone mass）以及锻炼心肌耐力的绝对必要条件。【异同辨析】完全避免运动会导致骨矿物质流失、骨质疏松风险剧增、心肺耐力退化以及脂肪异常堆积，给心血管系统埋下巨大隐患；静止不动绝不等于“保护身体”。【混淆陷阱】把消极怠动误当成了保护体力，忽视了青春期骨骼与心肺系统对运动刺激的刚性依赖。"
        }
    }
}
