# -*- coding: utf-8 -*-
"""
build_mcq_distractor_database.py
Generates curriculum-grounded, pedagogically rigorous distractor explanations
for all 60 Multiple-Choice Questions in Cambridge Grade 8 Science Human Physiology.
"""

import json
import re

# Comprehensive distractor definitions for all 60 MCQs
DISTRACTORS = {
    # ------------------ LESSON 24 HOUSEKEEPING EXAM (Q1 - Q10) ------------------
    "L24_Review_MCQ_1": {
        "A": {"correct": False, "en": "Incorrect. Transporting dissolved urea to the kidneys is the job of blood plasma, not red blood cells.", "cn": "错误选项辨析：运输溶解的尿素到肾脏是血浆（Plasma）的功能，红细胞不承担尿素运输。"},
        "B": {"correct": True,  "en": "Correct! Red blood cells are packed with haemoglobin, which binds reversibly with oxygen in the lungs and releases it to respiring tissues.", "cn": "正确选项：红细胞内富含血红蛋白，在肺部与氧气可逆结合为氧合血红蛋白，运至全身各组织释放供细胞呼吸。"},
        "C": {"correct": False, "en": "Incorrect. Forming a fibrin mesh for clotting is initiated by platelets and plasma fibrinogen, not red blood cells.", "cn": "错误选项辨析：构建纤维蛋白凝血网是由血小板（Platelets）与血浆中的纤维蛋白原启动的，红细胞仅是被动被网罗。"},
        "D": {"correct": False, "en": "Incorrect. Engulfing and digesting invading pathogens is phagocytosis, carried out by phagocytic white blood cells.", "cn": "错误选项辨析：吞噬并消化病原体属于吞噬作用，是由白细胞（如吞噬细胞 Phagocytes）执行的免疫防御功能。"}
    },
    "L24_Review_MCQ_2": {
        "A": {"correct": False, "en": "Incorrect. Blood plasma provides the liquid matrix and soluble fibrinogen, but does not initiate the clotting cascade.", "cn": "错误选项辨析：血浆提供液体基质和可溶性纤维蛋白原，但本身不能感知伤口并启动凝血级联。"},
        "B": {"correct": False, "en": "Incorrect. White blood cells defend against infection and do not trigger blood clotting.", "cn": "错误选项辨析：白细胞专职防御微生物感染，不负责启动止血凝血反应。"},
        "C": {"correct": False, "en": "Incorrect. Red blood cells become trapped in the fibrin mesh to plug the cut, but they do not initiate clotting.", "cn": "错误选项辨析：红细胞会被纤维蛋白网阻截以加固血栓，但并不分泌凝血因子启动该过程。"},
        "D": {"correct": True,  "en": "Correct! Platelets adhere to exposed collagen fibres at wound sites and secrete clotting factors that trigger the enzyme cascade.", "cn": "正确选项：血小板能粘附于伤口暴露的胶原纤维，激活并释放凝血因子，引发酶级联促使血液凝固。"}
    },
    "L24_Review_MCQ_3": {
        "A": {"correct": True,  "en": "Correct! Plasma is >90% water and transports dissolved solutes including hormones, urea, CO2 (as hydrogencarbonate), and glucose.", "cn": "正确选项：血浆含水90%以上，负责溶解并运输各种可溶性物质，包括激素、二氧化碳（碳酸氢根形式）、尿素与葡萄糖。"},
        "B": {"correct": False, "en": "Incorrect. Oxygen is practically insoluble in water and >98% is carried bound to haemoglobin inside red blood cells.", "cn": "错误选项辨析：氧气极难溶于水，人体内98%以上的氧气是结合在红细胞的血红蛋白内部运输的。"},
        "C": {"correct": False, "en": "Incorrect. Fibrin mesh is an insoluble structural net formed locally at wounds, not a normal circulating plasma solute.", "cn": "错误选项辨析：纤维蛋白网是不溶性的固体纤维网络，仅在伤口局部形成，并非血浆循环运输的溶质。"},
        "D": {"correct": False, "en": "Incorrect. Haemoglobin is strictly packaged inside red blood cells; free haemoglobin in plasma would be toxic and filtered out by kidneys.", "cn": "错误选项辨析：血红蛋白严格包裹在红细胞内；游离血红蛋白存在于血浆中属于病理溶血，会损伤肾脏。"}
    },
    "L24_Review_MCQ_4": {
        "A": {"correct": False, "en": "Incorrect. Egestion is the passing out of undigested, unabsorbed food residue as faeces via the anus.", "cn": "错误选项辨析：排遗（Egestion）是指未被消化和吸收的食物残渣通过肛门排出体外（形成粪便）的过程。"},
        "B": {"correct": False, "en": "Incorrect. Excretion is the removal of toxic metabolic waste products (e.g. urea, CO2) produced by chemical reactions in body cells.", "cn": "错误选项辨析：排泄（Excretion）是指机体排出细胞代谢终产物（如尿素、二氧化碳等）的生理过程。"},
        "C": {"correct": True,  "en": "Correct! Phagocytosis is the endocytic process where phagocytes engulf pathogens into vacuoles and destroy them using digestive enzymes.", "cn": "正确选项：吞噬作用（Phagocytosis）指吞噬细胞通过细胞膜凹陷包裹摄入病原体，并利用溶酶体酶将其消化的免疫机制。"},
        "D": {"correct": False, "en": "Incorrect. Assimilation is the uptake and incorporation of digested nutrient molecules into cell components.", "cn": "错误选项辨析：同化作用（Assimilation）指细胞吸收血液中的营养分子并将其转变为自身原生质或储能分子的过程。"}
    },
    "L24_Review_MCQ_5": {
        "A": {"correct": False, "en": "Incorrect. Urea is a soluble nitrogenous waste product produced by liver deamination of amino acids.", "cn": "错误选项辨析：尿素是肝脏脱氨基作用产生的含氮代谢废物，溶于水并随尿液排出。"},
        "B": {"correct": True,  "en": "Correct! Thrombin enzyme converts soluble fibrinogen into insoluble fibrin threads that form a mesh trapping blood cells.", "cn": "正确选项：凝血酶将可溶性的纤维蛋白原催化裂解为不溶性的纤维蛋白纤维，交织成网网罗血细胞形成血栓。"},
        "C": {"correct": False, "en": "Incorrect. Hemoglobin is an oxygen-transport protein inside red blood cells, not a clotting protein.", "cn": "错误选项辨析：血红蛋白是红细胞内的含铁氧气转运蛋白，与纤维网形成无关。"},
        "D": {"correct": False, "en": "Incorrect. Plasma is the liquid fluid of blood in which proteins and cells are suspended, not an insoluble net.", "cn": "错误选项辨析：血浆是血液的全部液体成分，并非不溶性的纤维网状物质。"}
    },
    "L24_Review_MCQ_6": {
        "A": {"correct": True,  "en": "Correct! The trachea (windpipe) is reinforced with C-shaped cartilage rings and runs from the larynx to the left and right bronchi.", "cn": "正确选项：气管（Trachea/Windpipe）由C形软骨环支撑，直接连接咽喉部与左右主支气管。"},
        "B": {"correct": False, "en": "Incorrect. The ureter connects each kidney to the urinary bladder in the excretory system.", "cn": "错误选项辨析：输尿管（Ureter）属于泌尿系统，是将尿液从肾脏输送到膀胱的肌性管道。"},
        "C": {"correct": False, "en": "Incorrect. The esophagus connects the pharynx to the stomach in the digestive system.", "cn": "错误选项辨析：食道（Esophagus）属于消化系统，是将食物从咽部输送到胃部的消化道管道。"},
        "D": {"correct": False, "en": "Incorrect. The urethra connects the urinary bladder to the exterior of the body for urination.", "cn": "错误选项辨析：尿道（Urethra）是泌尿系统的终端排泄管道，将尿液从膀胱排出体外。"}
    },
    "L24_Review_MCQ_7": {
        "A": {"correct": False, "en": "Incorrect. Thick muscular walls would drastically increase diffusion distance and prevent rapid gas exchange.", "cn": "错误选项辨析：极厚且多肌的管壁会极大增加扩散距离，彻底阻碍气体快速穿透。"},
        "B": {"correct": False, "en": "Incorrect. Alveoli provide a huge surface area (approx. 70 m²), not a small one, to maximize diffusion rate.", "cn": "错误选项辨析：人体肺泡总表面积巨大（约70平方米），并非很小的表面积。"},
        "C": {"correct": True,  "en": "Correct! Single-cell-thick walls minimize diffusion distance (<1 µm), while dense capillaries maintain a continuous steep concentration gradient.", "cn": "正确选项：肺泡壁与毛细血管壁均仅由一层扁平上皮细胞构成，使扩散距离极短；密集的毛细血管网维持了陡峭的浓度差。"},
        "D": {"correct": False, "en": "Incorrect. Alveoli must have a thin film of moisture so oxygen gas can dissolve before diffusing across cell membranes.", "cn": "错误选项辨析：肺泡内表面必须覆盖极薄的水分薄膜，因为氧气必须先溶解在水中才能有效穿过细胞膜扩散。"}
    },
    "L24_Review_MCQ_8": {
        "A": {"correct": False, "en": "Incorrect. Emulsification is the mechanical breakdown of large fat droplets into tiny droplets by bile salts in the gut.", "cn": "错误选项辨析：乳化作用（Emulsification）指胆汁酸盐将大脂肪滴物理分散为微小乳滴的消化过程。"},
        "B": {"correct": True,  "en": "Correct! Oxygen moves passively by net diffusion from higher partial pressure in alveoli into lower partial pressure in blood capillaries.", "cn": "正确选项：肺部气体交换遵循物理扩散定律（Diffusion），氧气顺浓度梯度自发从肺泡腔弥散进入毛细血管。"},
        "C": {"correct": False, "en": "Incorrect. Active ingestion is taking food into the digestive tract through the mouth.", "cn": "错误选项辨析：摄食（Ingestion）是指通过口腔将食物送入体内的动作，属于消化起点。"},
        "D": {"correct": False, "en": "Incorrect. Egestion is the discharge of undigested faeces from the anus.", "cn": "错误选项辨析：排遗（Egestion）是指从肛门排出不可消化的食物残渣，属于排泄系统的范畴之外。"}
    },
    "L24_Review_MCQ_9": {
        "A": {"correct": False, "en": "Incorrect. The liver produces bile and deaminates amino acids into urea, but kidneys do the actual blood filtering.", "cn": "错误选项辨析：肝脏和胆囊属于消化辅助器官；肝脏负责脱氨基合成尿素，但不负责滤过血液形成尿液。"},
        "B": {"correct": True,  "en": "Correct! The kidneys contain millions of nephrons that filter metabolic waste (urea, excess salts) under high pressure from the blood.", "cn": "正确选项：肾脏（Kidneys）拥有数百万个肾单位，负责在高压下滤过血液并重吸收有用成分，排出多余水分与尿素。"},
        "C": {"correct": False, "en": "Incorrect. The bladder stores urine and the urethra evacuates it, but neither filters blood.", "cn": "错误选项辨析：膀胱仅负责暂存尿液，尿道负责排出尿液，两者都不具备滤过血液的功能。"},
        "D": {"correct": False, "en": "Incorrect. The pancreas secretes digestive enzymes/hormones and the spleen breaks down old red blood cells.", "cn": "错误选项辨析：胰腺分泌胰液与胰岛素/胰高血糖素；脾脏是免疫和衰老红细胞清除器官，不形成尿液。"}
    },
    "L24_Review_MCQ_10": {
        "A": {"correct": False, "en": "Incorrect. Excretion is the removal of chemical waste produced inside body cells by metabolism (e.g. urea, carbon dioxide).", "cn": "错误选项辨析：排泄（Excretion）特指排出细胞内新陈代谢产生的化学废物（如尿素、二氧化碳）。"},
        "B": {"correct": False, "en": "Incorrect. Digestion is the chemical and mechanical breakdown of large insoluble food molecules into small soluble molecules.", "cn": "错误选项辨析：消化（Digestion）指将大分子不溶性食物分解为小分子可溶性养分的过程。"},
        "C": {"correct": True,  "en": "Correct! Egestion is defined strictly in the Cambridge syllabus as the passing out of food that has not been digested or absorbed, as faeces.", "cn": "正确选项：排遗（Egestion）在剑桥大纲中严格定义为从未被消化或吸收的食物残渣以粪便形式通过肛门排出体外。"},
        "D": {"correct": False, "en": "Incorrect. Cellular respiration is the chemical breakdown of glucose within cells to produce ATP energy.", "cn": "错误选项辨析：细胞呼吸（Respiration）是指细胞分解葡萄糖释放能量（ATP）的生化反应。"}
    },

    # ------------------ LESSON 30 HOUSEKEEPING EXAM (Q1 - Q10) ------------------
    "L30_Review_MCQ_1": {
        "A": {"correct": True,  "en": "Correct! Sweat consists predominantly of water (for evaporative cooling) along with trace amounts of urea and dissolved sodium chloride.", "cn": "正确选项：汗液主要由水组成（用于蒸发散热），并伴随排出微量代谢废物尿素以及溶解的氯化钠盐分。"},
        "B": {"correct": False, "en": "Incorrect. Oxygen is consumed by cells for aerobic respiration and is never excreted in sweat.", "cn": "错误选项辨析：氧气是细胞呼吸必需的消耗物，绝不会通过汗腺排出。"},
        "C": {"correct": False, "en": "Incorrect. Glucose and lipids are valuable energy substrates that are carefully conserved by the body and not excreted in sweat.", "cn": "错误选项辨析：葡萄糖和脂肪是重要的储能物质，机体会全力重吸收保留，绝不随汗液排出。"},
        "D": {"correct": False, "en": "Incorrect. Carbon dioxide is excreted almost entirely by the lungs through exhalation, not via the skin in sweat.", "cn": "错误选项辨析：二氧化碳主要由肺部呼气排出，汗腺不承担二氧化碳排泄。"}
    },
    "L30_Review_MCQ_2": {
        "A": {"correct": False, "en": "Incorrect. The ureter is the duct carrying finished urine from the renal pelvis to the bladder.", "cn": "错误选项辨析：输尿管是将已形成的尿液从肾脏引流至膀胱的管道，不参与滤过。"},
        "B": {"correct": False, "en": "Incorrect. The bladder is a storage reservoir for urine prior to urination.", "cn": "错误选项辨析：膀胱仅是储存尿液的肌性囊袋，无血液滤过功能。"},
        "C": {"correct": True,  "en": "Correct! The glomerulus is a dense knot of capillaries where high hydrostatic pressure forces water and small solutes into Bowman's capsule (ultrafiltration).", "cn": "正确选项：肾小球（Glomerulus）是毛细血管球，高流体静压在此推动水和小分子溶质透过滤过膜进入肾小囊（超滤作用）。"},
        "D": {"correct": False, "en": "Incorrect. The renal tubules carry out selective reabsorption of glucose and water, after filtration has already occurred.", "cn": "错误选项辨析：肾小管负责对滤过液进行选择性重吸收，处于超滤完成之后的阶段。"}
    },
    "L30_Review_MCQ_3": {
        "A": {"correct": False, "en": "Incorrect. An electrical impulse travelling along a neurone is a nerve impulse, belonging to the nervous system.", "cn": "错误选项辨析：沿神经元传导的电信号是神经冲动（Nerve impulse），属于神经调节而非体液调节。"},
        "B": {"correct": True,  "en": "Correct! Official Cambridge syllabus definition: A chemical substance produced by a gland and carried by blood that alters target organ activity.", "cn": "正确选项：剑桥官方权威定义：激素是由内分泌腺体产生、经血液运输、能改变特定靶器官代谢活动的化学信使。"},
        "C": {"correct": False, "en": "Incorrect. White blood cells are mobile immune cells, not chemical hormone secretions.", "cn": "错误选项辨析：白细胞是免疫防御细胞，不是激素分子。"},
        "D": {"correct": False, "en": "Incorrect. Digestive enzymes are exocrine protein catalysts released into the gut lumen, not circulating hormones.", "cn": "错误选项辨析：消化酶是外分泌腺分泌到消化道腔内的生物催化剂，不属于血液循环运输的激素。"}
    },
    "L30_Review_MCQ_4": {
        "A": {"correct": False, "en": "Incorrect. The nervous system transmits electrical action potentials along nerve fibres, not hormones.", "cn": "错误选项辨析：神经系统依赖神经纤维传递生物电信号，不负责长距离运输激素分子。"},
        "B": {"correct": False, "en": "Incorrect. The digestive tract handles ingested food and wastes; hormones are not transported inside the gut lumen.", "cn": "错误选项辨析：消化道运输的是食糜与消化液，内分泌激素绝不排入消化道腔内运输。"},
        "C": {"correct": True,  "en": "Correct! Because endocrine glands lack ducts, they secrete hormones directly into surrounding interstitial fluid to enter capillaries and circulate in blood.", "cn": "正确选项：内分泌腺没有导管（Ductless），分泌的激素直接扩散进入周围毛细血管，由全身血液循环运送至靶细胞。"},
        "D": {"correct": False, "en": "Incorrect. While lacteals absorb dietary fats, the vast majority of hormones circulate directly in blood plasma.", "cn": "错误选项辨析：淋巴系统主要引流组织液和吸收脂肪，激素在体内的主要运输媒介是血液循环。"}
    },
    "L30_Review_MCQ_5": {
        "A": {"correct": False, "en": "Incorrect. The pancreas is located below/behind the stomach and secretes insulin and glucagon.", "cn": "错误选项辨析：胰腺位于胃的后下方，分泌胰岛素和胰高血糖素，不位于肾脏顶部。"},
        "B": {"correct": False, "en": "Incorrect. The ovaries are paired female pelvic reproductive organs secreting oestrogen and progesterone.", "cn": "错误选项辨析：卵巢位于女性盆腔内，分泌雌激素和孕激素，不在肾脏上方。"},
        "C": {"correct": False, "en": "Incorrect. The testes are male gonads located in the scrotum that secrete testosterone.", "cn": "错误选项辨析：睾丸位于男性阴囊内，分泌雄性激素（睾酮）。"},
        "D": {"correct": True,  "en": "Correct! The paired adrenal glands sit cap-like atop each kidney and secrete adrenaline (epinephrine) from their medulla.", "cn": "正确选项：肾上腺（Adrenal glands）如帽子般附着在两侧肾脏的顶端，由髓质分泌肾上腺素。"}
    },
    "L30_Review_MCQ_6": {
        "A": {"correct": False, "en": "Incorrect. Adrenaline increases heart rate and cardiac output to deliver more oxygen to skeletal muscles.", "cn": "错误选项辨析：肾上腺素会使心跳显著加快，提高心输出量，绝不会大幅降低心率。"},
        "B": {"correct": False, "en": "Incorrect. Adrenaline stimulates liver glycogen breakdown, increasing blood glucose for immediate muscle fuel.", "cn": "错误选项辨析：肾上腺素刺激肝糖原分解，提升血糖浓度以供肌肉应急供能。"},
        "C": {"correct": True,  "en": "Correct! Adrenaline stimulates the acute 'fight or flight' response: increasing heart rate, dilating bronchioles, and diverting blood to muscles.", "cn": "正确选项：肾上腺素激发战斗或逃跑反应（Fight or Flight）：加快心率、舒张支气管、升高血糖并将血液优先泵向骨骼肌。"},
        "D": {"correct": False, "en": "Incorrect. Adrenaline promotes intense alertness and vigilance, actively suppressing sleep and rest.", "cn": "错误选项辨析：肾上腺素提升中枢兴奋性，诱发高度警觉，与启动睡眠完全相反。"}
    },
    "L30_Review_MCQ_7": {
        "A": {"correct": False, "en": "Incorrect. Testosterone governs male reproductive physiology and secondary sex characteristics.", "cn": "错误选项辨析：睾酮（Testosterone）负责男性第二性征发育及精子发生，不调节餐后血糖降低。"},
        "B": {"correct": False, "en": "Incorrect. Oestrogen governs the repair of the uterine lining and female secondary sex characteristics.", "cn": "错误选项辨析：雌激素（Oestrogen）调控子宫内膜修复与女性性征，不降低血糖。"},
        "C": {"correct": False, "en": "Incorrect. Adrenaline raises blood glucose by stimulating glycogenolysis during stress.", "cn": "错误选项辨析：肾上腺素在应激状态下会升高血糖，而不是在饱餐后降低血糖。"},
        "D": {"correct": True,  "en": "Correct! Insulin promotes glucose uptake into tissue cells and stimulates liver and muscle cells to convert glucose into glycogen.", "cn": "正确选项：胰岛素（Insulin）促进机体细胞摄取葡萄糖，并促使肝脏与肌肉将葡萄糖合成糖原储存，从而降低血糖。"}
    },
    "L30_Review_MCQ_8": {
        "A": {"correct": False, "en": "Incorrect. The adrenal glands secrete adrenaline and aldosterone, not insulin.", "cn": "错误选项辨析：肾上腺分泌肾上腺素与皮质激素，不分泌胰岛素。"},
        "B": {"correct": True,  "en": "Correct! The beta cells of the Islets of Langerhans inside the pancreas detect rising blood glucose and secrete insulin.", "cn": "正确选项：胰腺（Pancreas）内的胰岛β细胞兼具血糖感应与内分泌功能，直接分泌胰岛素调节糖代谢。"},
        "C": {"correct": False, "en": "Incorrect. The thyroid gland in the neck produces thyroxine to control basal metabolic rate.", "cn": "错误选项辨析：甲状腺分泌甲状腺激素，控制机体基础代谢率与生长发育。"},
        "D": {"correct": False, "en": "Incorrect. The pituitary gland in the brain secretes master trophic hormones (GH, TSH, FSH, LH, ADH), not insulin.", "cn": "错误选项辨析：脑垂体是大脑底部的内分泌总指挥部，分泌生长激素、促甲状腺激素及促性腺激素等，不分泌胰岛素。"}
    },
    "L30_Review_MCQ_9": {
        "A": {"correct": False, "en": "Incorrect. Oestrogen drives female secondary sexual characteristics (breast development, hip widening).", "cn": "错误选项辨析：雌激素负责促进女性第二性征的发育（如乳房发育、骨盆增宽等）。"},
        "B": {"correct": False, "en": "Incorrect. Insulin controls glucose homeostasis and has no role in secondary sexual characteristics.", "cn": "错误选项辨析：胰岛素是降血糖代谢激素，与性征分化发育无关。"},
        "C": {"correct": True,  "en": "Correct! Testosterone, synthesized by testicular Leydig cells, triggers facial hair growth, voice deepening, and increased muscle mass.", "cn": "正确选项：睾酮（Testosterone）由睾丸间质细胞合成，驱动男性长胡须、喉结突出、声调低沉及肌肉量激增。"},
        "D": {"correct": False, "en": "Incorrect. Adrenaline coordinates emergency acute survival reactions, not developmental pubertal traits.", "cn": "错误选项辨析：肾上腺素负责短期应激反应，不调控青春期性征发育。"}
    },
    "L30_Review_MCQ_10": {
        "A": {"correct": True,  "en": "Correct! Adolescence / puberty is the developmental period of physical, hormonal, and psychological transition into reproductive adulthood.", "cn": "正确选项：青春期（Adolescence/Puberty）是儿童期向成人期过渡的关键发育阶段，经历生殖系统成熟与体格剧变。"},
        "B": {"correct": False, "en": "Incorrect. Assimilation is the cellular incorporation of absorbed food nutrients into body tissues.", "cn": "错误选项辨析：同化作用（Assimilation）是细胞利用血液运来的营养成分构建自身结构的生物化学过程。"},
        "C": {"correct": False, "en": "Incorrect. Homeostasis is the physiological maintenance of a constant internal environment (temperature, pH, glucose).", "cn": "错误选项辨析：稳态（Homeostasis）指机体维持内部理化环境（体温、渗透压、血糖等）动态平衡的机制。"},
        "D": {"correct": False, "en": "Incorrect. Egestion is the expulsion of undigested faeces from the anus.", "cn": "错误选项辨析：排遗（Egestion）指从消化道排出未被消化的食物残渣（粪便）。"}
    }
}

# Add Section A Q1 - Q40 programmatically with high precision
REVISION_MCQS = {
    1: {"correct": "C", "A": "Plasma transports dissolved nutrients, urea, CO2, and hormones, but not bulk oxygen.",
                         "B": "Platelets are cell fragments that initiate blood clotting.",
                         "C": "Red blood cells are biconcave discs packed with haemoglobin to transport oxygen.",
                         "D": "White blood cells defend the body against invading pathogens.",
                         "A_cn": "血浆运输溶解的营养分子、尿素、二氧化碳和激素，不结合氧气。",
                         "B_cn": "血小板负责启动血液凝固级联反应。",
                         "C_cn": "红细胞呈双凹圆盘状，内含大量血红蛋白，专职结合与运输氧气。",
                         "D_cn": "白细胞执行免疫防御，抵御微生物病原体。"},
    2: {"correct": "A", "A": "Plasma is the pale-yellow liquid constituting ~55% of blood volume.",
                         "B": "Serum is plasma from which clotting factors (fibrinogen) have been removed.",
                         "C": "Lymph is interstitial fluid collected into lymphatic vessels.",
                         "D": "Cytoplasm is the intracellular gel inside individual cells.",
                         "A_cn": "血浆是占血液约55%体积的淡黄色透明液体基质。",
                         "B_cn": "血清是血液凝固析出纤维蛋白后的液体部分，不含纤维蛋白原。",
                         "C_cn": "淋巴液是进入淋巴管中的组织液。",
                         "D_cn": "细胞质是细胞膜内部的胶状基质。"},
    3: {"correct": "B", "A": "Fibrinogen is a soluble plasma protein involved in blood clotting.",
                         "B": "Haemoglobin is the iron-rich protein that binds reversibly with oxygen to form oxyhaemoglobin.",
                         "C": "An antibody is an immunoglobulin made by lymphocytes to bind antigens.",
                         "D": "Insulin is a peptide hormone produced by the pancreas to lower blood sugar.",
                         "A_cn": "纤维蛋白原是血浆中的可溶性凝血蛋白前体。",
                         "B_cn": "血红蛋白是红细胞内含铁的四聚体蛋白质，能与氧气可逆结合为氧合血红蛋白。",
                         "C_cn": "抗体是淋巴细胞分泌的专一性识别抗原的免疫球蛋白。",
                         "D_cn": "胰岛素是胰腺分泌的降血糖激素。"},
    4: {"correct": "B", "A": "Diffusion is passive net movement of particles from high to low concentration.",
                         "B": "Phagocytosis is the active engulfment and enzymatic destruction of microbes by phagocytes.",
                         "C": "Filtration is pressure-driven separation of fluids across a filter membrane.",
                         "D": "Reabsorption is the recovery of filtered nutrients back into the blood in kidney tubules.",
                         "A_cn": "扩散是分子顺浓度差进行的被动物理移动。",
                         "B_cn": "吞噬作用是吞噬细胞伸出伪足包裹并用溶酶体酶消化病原体的免疫过程。",
                         "C_cn": "滤过作用是依赖流体压力差将液体与微粒分离的物理过程。",
                         "D_cn": "重吸收是肾小管将有用物质主动或被动拉回血液的生理过程。"},
    5: {"correct": "C", "A": "Platelets are cellular fragments that adhere to the cut to trigger clotting.",
                         "B": "Haemoglobin is the oxygen-transport protein inside erythrocytes.",
                         "C": "Fibrin is the insoluble fibrous protein mesh that traps blood cells to seal wounds.",
                         "D": "Antibodies are immune proteins that neutralize specific antigens.",
                         "A_cn": "血小板是启动凝血的细胞碎片，不是蛋白质纤维网本身。",
                         "B_cn": "血红蛋白是红细胞内部的呼吸色素。",
                         "C_cn": "纤维蛋白是不溶性的网状蛋白纤维，能有效截留血细胞形成坚固血栓封堵伤口。",
                         "D_cn": "抗体是体液免疫中消灭病原体的蛋白质。"},
    6: {"correct": "B", "A": "Antigens are foreign surface molecules on pathogens; lymphocytes do not produce antigens.",
                         "B": "Antibodies are Y-shaped proteins specifically shaped to bind complementary pathogen antigens.",
                         "C": "Fibrin is produced by the clotting cascade to stop bleeding, not by lymphocytes for immunity.",
                         "D": "Haemoglobin is packaged inside red blood cells to transport oxygen.",
                         "A_cn": "抗原是病原体表面的外来标识分子，淋巴细胞生产的是抗体而非抗原。",
                         "B_cn": "抗体（Antibodies）是淋巴细胞合成的Y形特异性蛋白质，能精准结合病原体抗原。",
                         "C_cn": "纤维蛋白网是凝血系统产物，非淋巴细胞分泌。",
                         "D_cn": "血红蛋白由红细胞携带，负责输氧。"},
    7: {"correct": "D", "A": "Glucose is water-soluble and dissolves freely in blood plasma.",
                         "B": "Urea is water-soluble and is carried dissolved in blood plasma.",
                         "C": "Hormones are dissolved or carried by transport proteins in blood plasma.",
                         "D": "Oxygen has very low solubility in water and is carried bound to haemoglobin inside red blood cells.",
                         "A_cn": "葡萄糖易溶于水，直接溶解在血浆中运送。",
                         "B_cn": "尿素溶于水，作为溶解溶质在血浆中循环运送至肾脏。",
                         "C_cn": "激素大部分直接溶解或结合于血浆转运蛋白在血浆中运行。",
                         "D_cn": "氧气极难溶于水，98%以上紧密结合在红细胞的血红蛋白上运输。"},
    8: {"correct": "C", "A": "Bronchioles are smaller microscopic branches inside the lung tissue.",
                         "B": "Alveoli are microscopic terminal air sacs where gas exchange occurs.",
                         "C": "The bronchus (plural: bronchi) is the primary tube branching from the trachea into each lung.",
                         "D": "The larynx is the voice box situated at the top of the trachea.",
                         "A_cn": "细支气管是支气管进入肺内后的细小末梢分支。",
                         "B_cn": "肺泡是肺部气体交换的微观囊泡终端。",
                         "C_cn": "支气管（Bronchus）是气管在胸腔分叉直接通向左肺和右肺的主干管道。",
                         "D_cn": "喉部位于气管顶端，包含声带。"},
    9: {"correct": "A", "A": "Label A indicates the primary windpipe (trachea) descending from the larynx.",
                         "B": "Label B indicates the primary bronchus entering the lung.",
                         "C": "Label C indicates the smaller bronchioles branching throughout the lung.",
                         "D": "Label D indicates the diaphragm muscle at the base of the chest.",
                         "A_cn": "图注A指代自喉部延伸向下的气管（Trachea/Windpipe）。",
                         "B_cn": "图注B指代进入单侧肺部的左/右主支气管。",
                         "C_cn": "图注C指代肺泡上游的微细支气管树。",
                         "D_cn": "图注D指代分隔胸腔与腹腔的膈肌。"},
    10: {"correct": "C", "A": "Air filtration is performed by cilia and mucus lining the nasal cavity and trachea.",
                          "B": "Mucus production is carried out by goblet cells in the respiratory epithelium.",
                          "C": "During inhalation, the diaphragm contracts and flattens downwards, expanding thoracic volume.",
                          "D": "Warming air is achieved by warm capillary blood flow in the nasal cavity.",
                          "A_cn": "过滤空气是鼻腔和气管纤毛与黏液的功能。",
                          "B_cn": "分泌黏液由呼吸道上皮的杯状细胞负责。",
                          "C_cn": "吸气时膈肌收缩并向下变平，增加胸腔的垂直容积，使胸内压下降。",
                          "D_cn": "加温空气主要由鼻腔丰富的毛细血管网完成。"},
    11: {"correct": "B", "A": "Thoracic volume decreases during exhalation as the diaphragm relaxes and domes upward.",
                          "B": "During inhalation, diaphragm descent and ribcage elevation increase thoracic cavity volume.",
                          "C": "Thoracic volume changes dynamically to drive alveolar pressure gradients for airflow.",
                          "D": "Respiratory volume changes follow a strict, coordinated muscular cycle.",
                          "A_cn": "胸腔容积在呼气时减小（膈肌舒张隆起，肋骨下垂）。",
                          "B_cn": "吸气时随着膈肌收缩下降与肋间外肌收缩提升肋骨，胸腔容积显著增大。",
                          "C_cn": "胸腔容积必须动态改变以产生驱动气流的压力差。",
                          "D_cn": "呼吸运动受呼吸中枢节律性精确控制，绝非随机波动。"},
    12: {"correct": "B", "A": "Thick walls and dry surfaces drastically reduce diffusion efficiency.",
                          "B": "Thin walls (1 cell thick), huge surface area, moisture film, and dense capillaries provide optimal diffusion conditions.",
                          "C": "Without an active blood supply, oxygen gradients could not be maintained across the membrane.",
                          "D": "A small surface area would severely restrict total oxygen uptake.",
                          "A_cn": "厚壁和干燥内壁会严重阻碍气体的溶解与扩散穿透。",
                          "B_cn": "单层细胞薄壁缩短扩散距离，巨大面积增加交换容量，湿润表面利于气体溶解，丰富血流维持浓度差。",
                          "C_cn": "缺乏血流供应将导致局部氧浓度差迅速消失，气体交换停止。",
                          "D_cn": "表面积狭小无法满足温血哺乳动物的高耗氧需求。"},
    13: {"correct": "B", "A": "Active transport requires cellular ATP energy; respiratory gas movement is entirely passive.",
                          "B": "Gas exchange occurs purely by passive diffusion down partial pressure concentration gradients.",
                          "C": "Osmosis refers specifically to the net movement of water molecules, not gases.",
                          "D": "High-pressure filtration occurs in renal glomeruli to produce filtrate, not in the lungs.",
                          "A_cn": "主动运输消耗能量，而呼吸气体在肺泡的交换完全是被动的物理过程。",
                          "B_cn": "气体交换纯粹依靠分压差顺浓度梯度的被动物理扩散（Diffusion）完成。",
                          "C_cn": "渗透作用（Osmosis）专指水分子跨半透膜的扩散，不指代气体移动。",
                          "D_cn": "高压滤过发生在肾小球，肺泡依靠极薄的弥散膜进行分子扩散。"},
    14: {"correct": "C", "A": "Oxygen diffuses in the opposite direction (from alveoli into the blood).",
                          "B": "Nitrogen is physiologically inert and does not undergo net diffusion in respiration.",
                          "C": "Carbon dioxide produced by cellular metabolism diffuses down its gradient from blood into alveoli to be exhaled.",
                          "D": "Hydrogen gas is not produced in human cellular respiration.",
                          "A_cn": "氧气是反方向由肺泡扩散进入缺氧的静脉血。",
                          "B_cn": "氮气在呼吸过程中不参与代谢反应，无净扩散方向。",
                          "C_cn": "细胞呼吸代谢产生的二氧化碳在血液中分压高于肺泡气，顺浓度差扩散进入肺泡随呼气排出。",
                          "D_cn": "人体呼吸代谢不产生游离氢气。"},
    15: {"correct": "C", "A": "Oxygen does not react with limewater.",
                          "B": "Nitrogen does not react with limewater.",
                          "C": "Carbon dioxide reacts with limewater (calcium hydroxide) to produce an insoluble white precipitate of calcium carbonate.",
                          "D": "Haemoglobin is an intracellular protein in red blood cells that is never present in exhaled air.",
                          "A_cn": "氧气不与澄清石灰水反应。",
                          "B_cn": "氮气性质稳定，不使石灰水变浑浊。",
                          "C_cn": "二氧化碳与澄清石灰水中的氢氧化钙反应生成不溶性的碳酸钙白色沉淀，使其变浑浊。",
                          "D_cn": "血红蛋白存在于红细胞内部，绝不可能随呼出气体排出。"},
    16: {"correct": "B", "A": "The liver produces urea from amino acids, but the kidneys do the actual blood filtering.",
                          "B": "The kidneys receive ~20% of cardiac output to filter blood and form urine.",
                          "C": "The bladder collects and stores urine, but does not filter blood.",
                          "D": "The pancreas secretes digestive enzymes and metabolic hormones.",
                          "A_cn": "肝脏合成尿素，但滤过血液形成尿液的器官是肾脏。",
                          "B_cn": "肾脏（Kidney）每分钟接受约五分之一的心输出量，专职滤过血液代谢产物生成尿液。",
                          "C_cn": "膀胱是储存尿液的平滑肌肌性器官，不产生尿液。",
                          "D_cn": "胰腺主要行使消化酶与降升糖激素分泌。"},
    17: {"correct": "B", "A": "The urethra carries urine from the bladder out of the body during urination.",
                          "B": "The ureters are paired muscular tubes transporting urine from each kidney to the urinary bladder.",
                          "C": "The renal artery delivers oxygenated, unfiltered blood from the aorta to the kidney.",
                          "D": "The renal vein drains filtered, deoxygenated blood from the kidney to the vena cava.",
                          "A_cn": "尿道（Urethra）是将尿液从膀胱排出体外的管道。",
                          "B_cn": "输尿管（Ureter）是左右成对的肌性管道，将尿液从肾脏输送至膀胱。",
                          "C_cn": "肾动脉从腹主动脉分出，为肾脏供应高压血液进行滤过。",
                          "D_cn": "肾静脉收集肾脏滤过后的洁净血液汇入下腔静脉。"},
    18: {"correct": "C", "A": "Carbon dioxide is produced in mitochondria during cellular respiration.",
                          "B": "Glucose is an energy-rich carbohydrate nutrient, not a nitrogenous breakdown waste.",
                          "C": "Urea is formed in the liver by deamination of surplus amino acids to remove toxic ammonia.",
                          "D": "Glycogen is an insoluble storage polysaccharide synthesized in the liver.",
                          "A_cn": "二氧化碳是线粒体有氧呼吸分解碳骨架产生的废物。",
                          "B_cn": "葡萄糖是供能单糖，非含氮分解废物。",
                          "C_cn": "尿素（Urea）是肝脏通过脱氨基作用将多余氨基酸的毒性氨基转化而成的代谢废物。",
                          "D_cn": "糖原是动物肝脏和骨骼肌储存葡萄糖的聚合大分子。"},
    19: {"correct": "B", "A": "Removal of metabolic waste from cells is excretion, not egestion.",
                          "B": "Egestion is strictly defined as the voiding of undigested and unabsorbed food residues as faeces.",
                          "C": "Removal of water is osmoregulation and excretion, not egestion.",
                          "D": "Removal of carbon dioxide from lungs is pulmonary excretion.",
                          "A_cn": "排出细胞代谢废物属于排泄（Excretion）。",
                          "B_cn": "排遗（Egestion）专指将消化道中未被消化吸收的食物残渣（粪便）经肛门排出体外。",
                          "C_cn": "水分排出属于渗透压调节与排泄范围。",
                          "D_cn": "肺部排出二氧化碳属于气体排泄。"},
    20: {"correct": "C", "A": "The renal tubule carries out selective reabsorption of filtered nutrients.",
                          "B": "The collecting duct carries out final water reabsorption under ADH control.",
                          "C": "The glomerulus is a specialized knot of high-pressure capillaries where ultrafiltration occurs.",
                          "D": "The ureter is a gross anatomical tube connecting kidney to bladder.",
                          "A_cn": "肾小管负责重吸收葡萄糖、氨基酸与水分。",
                          "B_cn": "集合管受抗利尿激素调控执行水分最终重吸收。",
                          "C_cn": "肾小球（Glomerulus）是位于肾小囊内的毛细血管网球，高血压迫使水分和微小溶质滤出。",
                          "D_cn": "输尿管是输送终尿的宏观管道。"},
    21: {"correct": "B", "A": "Urea and excess salts are metabolic wastes that the body actively excretes in urine.",
                          "B": "Glucose and amino acids are 100% actively reabsorbed in the proximal convoluted tubule.",
                          "C": "Red blood cells and plasma proteins are too large to be filtered into filtrate under healthy conditions.",
                          "D": "Water is ~99% reabsorbed, but not 100%, allowing waste flush as urine.",
                          "A_cn": "尿素与多余盐分是机体意图排出的废物与多余离子，不会全部重吸收。",
                          "B_cn": "健康人体肾小管通过主动转运载体将原尿中的葡萄糖和氨基酸100%完全重吸收回血液。",
                          "C_cn": "正常情况下红细胞和血浆大分子蛋白根本不能透过滤过膜进入原尿。",
                          "D_cn": "水分重吸收率约为99%，必须保留约1%形成终尿冲洗代谢废物。"},
    22: {"correct": "B", "A": "Large volume of dilute urine occurs when overhydrated (suppressed ADH).",
                          "B": "Dehydration increases blood osmolarity, triggering ADH to maximize water reabsorption, making urine low-volume and concentrated.",
                          "C": "Urine output changes dramatically to defend plasma volume and osmolality.",
                          "D": "Normal renal tubules reabsorb all glucose; glucose in urine is a sign of diabetes, not dehydration.",
                          "A_cn": "大量稀释尿液见于大量饮水后（抗利尿激素分泌受抑制）。",
                          "B_cn": "脱水导致血浆渗透压上升，刺激垂体释放抗利尿激素（ADH），肾脏最大化重吸收水，产生量少且深色的浓缩尿。",
                          "C_cn": "尿量和浓度必须根据体液平衡动态大幅调整以维持稳态。",
                          "D_cn": "脱水不会导致肾小管葡萄糖重吸收障碍，糖尿是糖尿病的典型特征。"},
    23: {"correct": "B", "A": "The liver processes waste into urea, but secretes it into blood, not directly out of the body.",
                          "B": "The skin contains eccrine sweat glands that excrete small amounts of water, urea, and sodium chloride.",
                          "C": "The stomach secretes gastric acid and pepsin for digestion, but does not excrete metabolic wastes.",
                          "D": "The lungs excrete carbon dioxide and water vapour, but cannot excrete non-volatile urea or salts.",
                          "A_cn": "肝脏将氨合成尿素并释放到血液中，本身不向外界环境排泄废物。",
                          "B_cn": "皮肤中的汗腺在蒸发散热时，附带排泄水分、溶解盐分以及少量尿素。",
                          "C_cn": "胃分泌胃酸和胃蛋白酶进行消化，不承担外排代谢废物的排泄功能。",
                          "D_cn": "肺部排泄二氧化碳和水蒸气，无法排出不挥发的固态尿素与无机盐。"},
    24: {"correct": "B", "A": "An electrical impulse traveling along a neurone is a nerve impulse, not a hormone.",
                          "B": "A hormone is a chemical messenger produced by an endocrine gland, transported in blood, which alters target cells.",
                          "C": "White blood cells are mobile immune cellular units, not chemical messengers.",
                          "D": "A digestive enzyme is an exocrine catalyst operating in the alimentary lumen.",
                          "A_cn": "神经冲动是神经元传导的动作电位，属于神经信号。",
                          "B_cn": "激素是由内分泌腺分泌、由血液循环运送并作用于特定靶器官的化学信使。",
                          "C_cn": "白细胞是血液中的免疫防卫细胞，不是分泌的激素分子。",
                          "D_cn": "消化酶是催化胃肠道食物水解的蛋白质，非全身循环的激素。"},
    25: {"correct": "C", "A": "The pituitary gland secretes trophic master hormones, not insulin.",
                          "B": "The adrenal glands secrete adrenaline and aldosterone, not insulin.",
                          "C": "The beta cells within the endocrine islets of the pancreas secrete insulin.",
                          "D": "The thyroid gland secretes thyroxine to control basal metabolic rate.",
                          "A_cn": "脑垂体分泌促激素与生长激素，不生产胰岛素。",
                          "B_cn": "肾上腺分泌肾上腺素和皮质激素，不分泌胰岛素。",
                          "C_cn": "胰腺内部的胰岛β细胞是合成与分泌胰岛素的专属组织。",
                          "D_cn": "甲状腺分泌甲状腺素，调控能量代谢。"},
    26: {"correct": "A", "A": "The adrenal glands sit atop each kidney and release adrenaline from the inner medulla during acute stress.",
                          "B": "The ovaries are female reproductive glands producing oestrogen and progesterone.",
                          "C": "The testes are male reproductive gonads producing testosterone.",
                          "D": "The thyroid gland is located in the anterior neck.",
                          "A_cn": "肾上腺（Adrenal glands）位于双肾顶端，髓质受交感神经支配释放肾上腺素应对紧急危机。",
                          "B_cn": "卵巢位于盆腔内，负责分泌女性性激素。",
                          "C_cn": "睾丸位于阴囊内，负责分泌雄激素。",
                          "D_cn": "甲状腺位于颈部前部气管两侧。"},
    27: {"correct": "B", "A": "Nervous responses are faster and shorter-lasting, whereas endocrine responses are the reverse.",
                          "B": "Hormones travel relatively slowly through blood circulation, but their chemical biochemical effects last longer.",
                          "C": "Nervous signals travel at up to 100 m/s; hormones rely on bulk blood flow (taking seconds to minutes).",
                          "D": "Reflex actions are solely mediated by nervous reflex arcs, not hormones.",
                          "A_cn": "快速且持续短暂的是神经调节（如缩手反射）。",
                          "B_cn": "激素通过血液循环漫游输送，起效相对缓慢；但激素在体内持续降解需要时间，效应更持久广泛。",
                          "C_cn": "神经冲动传导速度达几十米每秒，而血液循环需要数十秒完成一次周转。",
                          "D_cn": "反射弧完全由感觉、中间与运动神经元构成，不依赖激素。"},
    28: {"correct": "B", "A": "Having a nucleus is common to all nucleated cells, but does not grant responsiveness to a hormone.",
                          "B": "A target cell must express complementary receptor proteins that fit the specific 3D shape of that hormone.",
                          "C": "Mitochondria generate ATP in all eukaryotic cells, but cannot detect circulating hormones.",
                          "D": "Human animal cells never possess cell walls.",
                          "A_cn": "人体绝大多数细胞都有细胞核，但只有特定细胞对特定激素产生应答。",
                          "B_cn": "靶细胞必须在其质膜表面或细胞质中表达具有互补空间构象的专属受体蛋白（Receptor）。",
                          "C_cn": "线粒体是细胞供能工厂，不具备特异性识别血液激素分子的受体功能。",
                          "D_cn": "人类动物细胞根本没有细胞壁（细胞壁是植物、真菌和细菌特征）。"},
    29: {"correct": "C", "A": "Glucagon increases blood glucose by promoting liver glycogen breakdown.",
                          "B": "Adrenaline increases blood glucose during acute fight-or-flight emergencies.",
                          "C": "Insulin promotes glucose uptake into body cells and glycogenesis in the liver, lowering blood glucose.",
                          "D": "Testosterone governs male secondary sex characteristics and reproduction.",
                          "A_cn": "胰高血糖素（Glucagon）的作用是促进肝糖原分解以升高血糖。",
                          "B_cn": "肾上腺素在应激危机时调动糖原分解升高血糖，供肌肉做功。",
                          "C_cn": "胰岛素（Insulin）在餐后血糖升高时分泌，驱动细胞摄糖和肝脏合成糖原，降低血糖水平。",
                          "D_cn": "睾酮是雄性激素，不调控餐后急性血糖平衡。"},
    30: {"correct": "B", "A": "Converting glucose into glycogen is the action of insulin when blood glucose is high.",
                          "B": "Glucagon stimulates liver cells to break down stored glycogen into glucose and release it into blood.",
                          "C": "Excreting glucose in urine is a sign of diabetes, not a normal regulated glucagon response.",
                          "D": "Converting glucose into fat occurs during carbohydrate excess under insulin stimulation.",
                          "A_cn": "将葡萄糖合成糖原储存是胰岛素在高血糖时发挥的作用。",
                          "B_cn": "当血糖过低时，胰高血糖素命令肝细胞将储备的糖原水解为葡萄糖分子释放回血液中。",
                          "C_cn": "在尿液中排出葡萄糖是由于血糖超过肾糖阈，属于病理现象，非胰高血糖素效应。",
                          "D_cn": "将过剩葡萄糖合成为脂肪是营养过剩时由胰岛素介导的脂质合成。"},
    31: {"correct": "B", "A": "Egestion is voiding undigested faecal food residue from the anus.",
                          "B": "Homeostasis relies on negative feedback: deviations from setpoint trigger corrective responses that restore the optimum level.",
                          "C": "Phagocytosis is the cellular engulfment of pathogens by white blood cells.",
                          "D": "Simple diffusion is passive molecular movement down a concentration gradient.",
                          "A_cn": "排遗是消化系统末端排出粪便的生理动作。",
                          "B_cn": "稳态（Homeostasis）通过负反馈机制维持：任何偏离正常设定点（如血糖升高或降低）的信号都会触发反向纠正措施恢复基线。",
                          "C_cn": "吞噬作用是免疫细胞消灭细菌的防御行为。",
                          "D_cn": "单纯扩散是被动物理过程，不具备主动调控稳态的系统机制。"},
    32: {"correct": "A", "A": "Type 1 diabetes is an autoimmune disease where immune cells destroy insulin-producing beta cells in the pancreas.",
                          "B": "Asthma is a chronic inflammatory disorder of the respiratory airways.",
                          "C": "Anaemia is a deficiency in healthy red blood cells or haemoglobin.",
                          "D": "A urinary tract infection is a bacterial infection of the bladder or kidneys.",
                          "A_cn": "1型糖尿病（Type 1 diabetes）是自体免疫性疾病，患者自身抗体破坏胰腺胰岛β细胞，导致完全无法生成胰岛素。",
                          "B_cn": "哮喘是支气管平滑肌痉挛与气道慢性炎症引起的呼吸困难病症。",
                          "C_cn": "贫血是指循环红细胞数量或血红蛋白浓度低于正常水平。",
                          "D_cn": "尿路感染是细菌侵袭膀胱或肾脏引起的炎性疾病。"},
    33: {"correct": "B", "A": "Adrenaline increases heart rate to pump oxygenated blood more rapidly to skeletal muscles.",
                          "B": "Adrenaline increases heart rate and dilates bronchioles (wider airways) to maximize oxygen delivery during fight-or-flight.",
                          "C": "Adrenaline increases blood glucose (by hepatic glycogenolysis) to provide ready fuel for contraction.",
                          "D": "Adrenaline constricts blood vessels to the digestive organs, actively decreasing digestion during emergencies.",
                          "A_cn": "肾上腺素显著加快心跳以加大搏出量，绝非减缓心跳。",
                          "B_cn": "肾上腺素刺激窦房结使心率激增，同时舒张支气管平滑肌展宽气道，让更多氧气涌入血液支援肌肉逃跑或搏斗。",
                          "C_cn": "肾上腺素促进肝糖原分解升高血糖，提供即时代谢底物。",
                          "D_cn": "在生死危机面前，自主神经和肾上腺素会收缩内脏血管，暂时抑制胃肠蠕动和消化液分泌。"},
    34: {"correct": "B", "A": "Oestrogen triggers female secondary sexual characteristics (e.g. breast enlargement, wider hips).",
                          "B": "Testosterone, produced by the testes, drives male secondary sex traits: deep voice, facial hair, larger muscle mass.",
                          "C": "Insulin regulates glucose uptake and storage.",
                          "D": "Adrenaline triggers acute survival fight-or-flight reactions.",
                          "A_cn": "雌激素是女性主导性激素，促成女性特征发育。",
                          "B_cn": "睾酮（Testosterone）由睾丸间质细胞大量分泌，驱动男性喉结突出、变声、胡须生长及骨骼肌发达。",
                          "C_cn": "胰岛素是控制血糖的代谢激素。",
                          "D_cn": "肾上腺素是短期应激生存激素。"},
    35: {"correct": "C", "A": "Deepening of the voice is a male secondary sexual characteristic driven by testosterone.",
                          "B": "Growth of facial hair is a male secondary sexual characteristic driven by testosterone.",
                          "C": "Breast development (mammary duct and adipose tissue growth) is stimulated in females by oestrogen during puberty.",
                          "D": "Enlargement of testes is a male primary/secondary sexual characteristic.",
                          "A_cn": "声带加宽与声调变低沉是男性在睾酮刺激下的特征。",
                          "B_cn": "长出胡须是男性特有的青春期副性征。",
                          "C_cn": "乳房发育（腺体与脂肪沉着）是女孩在青春期雌激素刺激下出现的典型第二性征。",
                          "D_cn": "睾丸增大是男性的生殖器官成熟表现。"},
    36: {"correct": "B", "A": "The pancreas regulates blood glucose levels via insulin and glucagon.",
                          "B": "The hypothalamus signals the anterior pituitary gland to secrete gonadotropins (FSH and LH), awakening the ovaries and testes.",
                          "C": "The adrenal glands secrete adrenaline and aldosterone.",
                          "D": "The thyroid gland produces thyroxine to govern basal metabolic rate.",
                          "A_cn": "胰腺主要负责血糖稳态，不参与启动青春期的激素级联。",
                          "B_cn": "下丘脑分泌促性腺激素释放激素（GnRH），激活脑垂体（Pituitary gland）分泌FSH和LH，从而唤醒性腺（卵巢与睾丸）。",
                          "C_cn": "肾上腺主要参与应激与水盐平衡。",
                          "D_cn": "甲状腺调控新陈代谢速率与一般体格生长。"},
    37: {"correct": "B", "A": "Menstruation (shedding of the uterine lining) occurs during Days 1 to 5.",
                          "B": "Ovulation (release of a mature egg from an ovarian follicle) typically takes place around Day 14 following an LH surge.",
                          "C": "Implantation of an embryo occurs around Day 20–22 only if fertilisation has occurred in the fallopian tube.",
                          "D": "Full breakdown of the uterine lining is menstruation at the start of the cycle.",
                          "A_cn": "月经出血（内膜剥落）发生在周期的第1至5天。",
                          "B_cn": "排卵（Ovulation）通常发生在第28天周期的正中（约第14天），由黄体生成素（LH）峰值触发卵泡破裂释放成熟卵子。",
                          "C_cn": "受精卵着床通常发生在受精后的第20至22天左右，若未受精则不会着床。",
                          "D_cn": "内膜完全剥落是在月经期第1天开始发生。"},
    38: {"correct": "B", "A": "Progesterone maintains and vascularizes the already-thickened uterine lining after ovulation.",
                          "B": "Oestrogen, secreted by developing ovarian follicles, stimulates cell division to repair and thicken the uterine lining after menstruation.",
                          "C": "Testosterone is present only in trace amounts in females and does not repair the endometrium.",
                          "D": "Adrenaline is an acute stress hormone with no role in the menstrual cycle.",
                          "A_cn": "孕激素（Progesterone）的主要作用是在排卵后（后半周期）维持并进一步增厚且血管化子宫内膜。",
                          "B_cn": "雌激素（Oestrogen）由生长卵泡分泌，在排卵前（月经刚结束时）刺激子宫内膜细胞分裂修复并初步增厚。",
                          "C_cn": "睾酮在女性体内浓度极微，不负责子宫内膜修复。",
                          "D_cn": "肾上腺素是应激激素，不参与月经内膜周期性重建。"},
    39: {"correct": "B", "A": "Progesterone only stays elevated if an embryo implants and hCG signals the corpus luteum.",
                          "B": "When the egg is not fertilised, the corpus luteum degenerates, progesterone and oestrogen crash, causing the uterine lining to break down (menstruation).",
                          "C": "Hormone concentrations never remain constant; the sudden drop resets the pituitary cycle.",
                          "D": "Hormones plummet rather than rise, triggering uterine ischaemia and shed.",
                          "A_cn": "孕激素只有在受精着床后才会维持高位；未受精时黄体必然退化萎缩。",
                          "B_cn": "未受精时黄体退化，雌孕激素水平急剧暴跌，子宫内膜失去激素支持缺血坏死脱落，触发月经来潮（Menstruation）。",
                          "C_cn": "激素水平不可能恒定，断崖式下跌是重启下一个周期的生化开关。",
                          "D_cn": "激素是急剧下降而不是上升，不会立刻引发下一次排卵。"},
    40: {"correct": "B", "A": "Skipping meals deprives the rapidly developing body of crucial macronutrients, calcium, and iron.",
                          "B": "A balanced diet, regular physical exercise, and adequate restorative sleep form the essential triad of adolescent physical health.",
                          "C": "Sleep deprivation damages immune function, impairs memory consolidation, and reduces growth hormone secretion.",
                          "D": "Avoiding exercise leads to poor cardiovascular fitness, reduced bone mineral density, and metabolic dysfunction.",
                          "A_cn": "不吃正餐会导致正在剧烈发育的青春期青少年缺乏钙、铁和必需微量营养素，损害骨骼与智力发育。",
                          "B_cn": "均衡膳食提供充足建筑材料，适度锻炼强健心肺与骨骼，充足睡眠保障生长激素脉冲释放，是青春期健康的基石组合。",
                          "C_cn": "削减睡眠时间会严重压制生长激素的分泌，削弱免疫力并损害海马体记忆巩固。",
                          "D_cn": "缺乏运动会导致骨质疏松、心肺耐力下降及肥胖等代谢综合征风险增加。"}
}

# Combine into master DISTRACTORS
for q_num, data in REVISION_MCQS.items():
    q_id = f"Rev_SecA_Q{q_num:02d}"
    correct_letter = data["correct"]
    DISTRACTORS[q_id] = {
        "A": {"correct": correct_letter == "A", "en": ("Correct! " if correct_letter == "A" else "Incorrect. ") + data["A"], "cn": ("正确选项：" if correct_letter == "A" else "错误选项辨析：") + data["A_cn"]},
        "B": {"correct": correct_letter == "B", "en": ("Correct! " if correct_letter == "B" else "Incorrect. ") + data["B"], "cn": ("正确选项：" if correct_letter == "B" else "错误选项辨析：") + data["B_cn"]},
        "C": {"correct": correct_letter == "C", "en": ("Correct! " if correct_letter == "C" else "Incorrect. ") + data["C"], "cn": ("正确选项：" if correct_letter == "C" else "错误选项辨析：") + data["C_cn"]},
        "D": {"correct": correct_letter == "D", "en": ("Correct! " if correct_letter == "D" else "Incorrect. ") + data["D"], "cn": ("正确选项：" if correct_letter == "D" else "错误选项辨析：") + data["D_cn"]}
    }

print(f"Total MCQs with comprehensive distractor breakdowns defined: {len(DISTRACTORS)}")

# 1. Update g8_science_part2_exercises_bilingual.json
with open('g8_science_part2_exercises_bilingual.json', 'r', encoding='utf-8') as f:
    part2_items = json.load(f)

for item in part2_items:
    if item['id'] in DISTRACTORS:
        item['options_breakdown'] = DISTRACTORS[item['id']]

with open('g8_science_part2_exercises_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump(part2_items, f, ensure_ascii=False, indent=2)

print("Updated g8_science_part2_exercises_bilingual.json successfully.")

# 2. Update science_exercises_data.js
with open('g8_science_exercises_bilingual.json', 'r', encoding='utf-8') as f:
    part1_items = json.load(f)

js_bundle = f"""/**
 * Sky's Science Master Exercise & Exam Database (Bilingual Bundle)
 * Part 1: Autumn Term (91 items, Lessons 1–18 + Extensions)
 * Part 2: Human Physiology (176 items, Lessons 19–32 + Housekeeping Exams + Cumulative Revision)
 * Total: 267 structured items with rich distractor breakdowns
 * Compatible with offline file:// and web servers.
 */
window.SCIENCE_DATA_PART1 = {json.dumps(part1_items, ensure_ascii=False, indent=2)};
window.SCIENCE_DATA_PART2 = {json.dumps(part2_items, ensure_ascii=False, indent=2)};
"""

with open('science_exercises_data.js', 'w', encoding='utf-8') as f:
    f.write(js_bundle)

print("Updated science_exercises_data.js successfully.")
