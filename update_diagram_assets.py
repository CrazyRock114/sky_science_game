# -*- coding: utf-8 -*-
"""
update_diagram_assets.py
Attaches high-definition extracted textbook diagrams, captions, and context descriptions
to all questions in Part 1 and Part 2 that reference figures/diagrams.
Also fixes Rev_SecA_Q09 and Rev_SecB_Q04 answer keys based on verified Figure 1.
"""

import json

# 1. Update Part 2
with open('g8_science_part2_exercises_bilingual.json', 'r', encoding='utf-8') as f:
    part2 = json.load(f)

part2_map = {it['id']: it for it in part2}

# Fix Rev_SecA_Q09
if 'Rev_SecA_Q09' in part2_map:
    q = part2_map['Rev_SecA_Q09']
    q['answer_en'] = "B) B"
    q['answer_cn'] = "B) B"
    q['rationale_en'] = "In Figure 1, structure B points directly to the trachea (the main midline windpipe descending from the larynx into the thoracic cavity). Structure A indicates the nasal cavity, C indicates the primary bronchus, and D indicates intrapulmonary bronchioles."
    q['rationale_cn'] = "在图1（Figure 1）解剖图谱中，标号B直接指向喉部下方延伸至胸腔的气管主干（Trachea/Windpipe）。标号A指向鼻腔（Nasal Cavity），C指向进入两肺的主支气管（Bronchus），D指向肺实质内的细支气管（Bronchioles）。"
    q['image_url'] = "images/fig_revision_respiratory_system.jpeg"
    q['diagram_caption_en'] = "Figure 1: The Human Respiratory System (Conducting Zone)"
    q['diagram_caption_cn'] = "图1：人体呼吸系统导气通路解剖示意图"
    q['diagram_description_en'] = "Figure 1 shows the human respiratory system: Label A points to the nasal cavity; below it are Pharynx and Larynx; Label B points to the trachea; Label C points to the bronchus; Label D points to the intrapulmonary bronchioles."
    q['diagram_description_cn'] = "图1展示人体呼吸系统导气结构：标注A指向头部鼻腔（Nasal Cavity）；下方已直接标明咽（Pharynx）与喉（Larynx）；标注B指向喉下方的气管主干（Trachea）；标注C指向通入肺门的主支气管（Bronchus）；标注D指向肺内的细支气管（Bronchioles）。"

# Fix Rev_SecB_Q04
if 'Rev_SecB_Q04' in part2_map:
    q = part2_map['Rev_SecB_Q04']
    q['image_url'] = "images/fig_revision_respiratory_system.jpeg"
    q['diagram_caption_en'] = "Figure 1: The Human Respiratory System (Conducting Zone)"
    q['diagram_caption_cn'] = "图1：人体呼吸系统导气通路解剖示意图"
    q['answer_en'] = "Mark Scheme (5 marks):\n- Structure A: Nasal cavity [1]\n- Structure B: Trachea (windpipe) [1]\n- Structure C: Bronchus (plural: bronchi) [1]\n- Structure D: Bronchiole(s) [1]\n- Function of structure D during breathing: Bronchioles conduct inhaled air deep into lung alveoli and regulate airway resistance through smooth muscle dilation/constriction. (Note: On page 142 diagram, label E indicates the diaphragm at the base of the chest, which contracts and flattens during inhalation to increase thoracic volume and draw air into the lungs.) [1]"
    q['answer_cn'] = "【官方评分标准】（满分5分）：\n- 结构A：鼻腔（Nasal cavity）[1分]\n- 结构B：气管（Trachea/Windpipe）[1分]\n- 结构C：主支气管（Bronchus）[1分]\n- 结构D：细支气管（Bronchiole）[1分]\n- 结构D在呼吸中的功能：细支气管作为导气管网将空气深入导入肺泡囊，并通过平滑肌舒缩调节气道阻力。（注：原教材第142页附图在胸底补充了标注E指向膈肌Diaphragm，吸气时膈肌收缩变平以增大胸腔容积抽吸空气。）[1分]"

# Part 2 other figures
if 'Rev_SecB_Q08' in part2_map:
    q = part2_map['Rev_SecB_Q08']
    q['image_url'] = "images/fig_revision_nephron.png"
    q['diagram_caption_en'] = "Figure 2: A Nephron (Filtration Unit of the Kidney)"
    q['diagram_caption_cn'] = "图2：肾单位（肾脏微观滤过单元）结构图"

if 'Rev_SecB_Q11' in part2_map:
    q = part2_map['Rev_SecB_Q11']
    q['image_url'] = "images/fig_revision_glucose_graph.png"
    q['diagram_caption_en'] = "Figure 3: Blood Glucose Concentration Over Time (Meal Response)"
    q['diagram_caption_cn'] = "图3：进食前后血糖浓度随时间动态变化曲线图"

if 'Rev_SecB_Q14' in part2_map:
    q = part2_map['Rev_SecB_Q14']
    q['image_url'] = "images/fig_revision_menstrual_cycle.png"
    q['diagram_caption_en'] = "Figure 4: Hormone Levels During the 28-Day Menstrual Cycle"
    q['diagram_caption_cn'] = "图4：28天月经周期中雌激素与孕激素水平动态曲线图"

if 'L21_Task_21_3' in part2_map:
    q = part2_map['L21_Task_21_3']
    q['image_url'] = "images/fig_task21_respiratory_labeling.jpeg"
    q['diagram_caption_en'] = "Figure 21.4: Major Structures of the Human Respiratory System"
    q['diagram_caption_cn'] = "图21.4：人体呼吸系统主要结构填图标注图"

if 'L22_Task_22_4' in part2_map:
    q = part2_map['L22_Task_22_4']
    q['image_url'] = "images/fig_task22_diffusion_alveolus.jpeg"
    q['diagram_caption_en'] = "Figure 22.4: Alveolus and Blood Capillary Gas Diffusion"
    q['diagram_caption_cn'] = "图22.4：肺泡与毛细血管气体交换扩散方向示意图"

if 'L23_Task_23_2' in part2_map:
    q = part2_map['L23_Task_23_2']
    q['image_url'] = "images/fig_task23_urinary_system.jpeg"
    q['diagram_caption_en'] = "Figure 23.1: The Human Urinary System"
    q['diagram_caption_cn'] = "图23.1：人体泌尿排泄系统解剖图"

if 'L25_Task_25_2' in part2_map:
    q = part2_map['L25_Task_25_2']
    q['image_url'] = "images/fig_revision_nephron.png"
    q['diagram_caption_en'] = "Figure 25.2: Nephron Anatomy (Glomerulus, Bowman's Capsule, Tubules)"
    q['diagram_caption_cn'] = "图25.2：肾单位微观解剖示意图"

if 'L27_Task_27_2' in part2_map:
    q = part2_map['L27_Task_27_2']
    q['image_url'] = "images/fig_task27_endocrine_system.jpeg"
    q['diagram_caption_en'] = "Figure 27.1: Major Endocrine Glands in the Human Body"
    q['diagram_caption_cn'] = "图27.1：人体主要内分泌腺体分布图"

if 'L28_Task_28_3' in part2_map:
    q = part2_map['L28_Task_28_3']
    q['image_url'] = "images/fig_task28_glucose_regulation.jpeg"
    q['diagram_caption_en'] = "Figure 28.1: Pancreatic Blood Glucose Homeostasis"
    q['diagram_caption_cn'] = "图28.1：胰岛素降血糖负反馈调节图"

if 'L32_Task_32_2' in part2_map:
    q = part2_map['L32_Task_32_2']
    q['image_url'] = "images/fig_task32_menstrual_cycle.jpeg"
    q['diagram_caption_en'] = "Figure 32.2: The Five Stages of the Menstrual Cycle"
    q['diagram_caption_cn'] = "图32.2：月经周期五大生理阶段示意图"

if 'L32_Task_32_3' in part2_map:
    q = part2_map['L32_Task_32_3']
    q['image_url'] = "images/fig_revision_menstrual_cycle.png"
    q['diagram_caption_en'] = "Figure 32.3: Oestrogen and Progesterone Fluctuations Graph"
    q['diagram_caption_cn'] = "图32.3：雌激素与孕激素浓度变化曲线图"

with open('g8_science_part2_exercises_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump(part2, f, ensure_ascii=False, indent=2)

print("Updated g8_science_part2_exercises_bilingual.json with diagram assets.")

# 2. Update Part 1
with open('g8_science_exercises_bilingual.json', 'r', encoding='utf-8') as f:
    part1 = json.load(f)

part1_map = {it['id']: it for it in part1}

if 'L01_Task_1_1' in part1_map:
    q = part1_map['L01_Task_1_1']
    q['image_url'] = "images/fig_autumn_1_4_food_labels_0.png"
    q['diagram_caption_en'] = "Figure 1.4: Food Packaging Nutritional Labels"
    q['diagram_caption_cn'] = "图1.4：食品包装营养成分红绿灯标签"

if 'L02_Task_2_2' in part1_map:
    q = part1_map['L02_Task_2_2']
    q['image_url'] = "images/fig_autumn_2_3_alimentary_canal.png"
    q['diagram_caption_en'] = "Figure 2.3: Human Alimentary Canal Anatomy"
    q['diagram_caption_cn'] = "图2.3：人体消化道解剖结构示意图"

if 'L04_Task_4_5' in part1_map:
    q = part1_map['L04_Task_4_5']
    q['image_url'] = "images/fig_autumn_4_2_tooth_section_1.jpeg"
    q['diagram_caption_en'] = "Figure 4.2: Longitudinal Cross-Section of a Human Tooth"
    q['diagram_caption_cn'] = "图4.2：人类牙齿纵切面解剖图"

if 'L08_Task_8_1' in part1_map:
    q = part1_map['L08_Task_8_1']
    q['image_url'] = "images/fig_autumn_8_4_ph_scale.jpeg"
    q['diagram_caption_en'] = "Figure 8.4: Universal Indicator pH Scale"
    q['diagram_caption_cn'] = "图8.4：通用酸碱指示剂 pH 比色板"

if 'L11_Task_11_1' in part1_map:
    q = part1_map['L11_Task_11_1']
    q['image_url'] = "images/fig_autumn_11_4_heart_diagram_0.png"
    q['diagram_caption_en'] = "Figure 11.4: Internal Frontal Anatomy of the Human Heart"
    q['diagram_caption_cn'] = "图11.4：人体心脏正面冠状解剖结构图"

if 'L16_Task_16_2' in part1_map:
    q = part1_map['L16_Task_16_2']
    q['image_url'] = "images/fig_autumn_16_3_body_vascular.jpeg"
    q['diagram_caption_en'] = "Figure 16.3: Double Circulatory System Vascular Plan"
    q['diagram_caption_cn'] = "图16.3：人体双循环血管网络图"

with open('g8_science_exercises_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump(part1, f, ensure_ascii=False, indent=2)

print("Updated g8_science_exercises_bilingual.json with diagram assets.")
