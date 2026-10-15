# -*- coding: utf-8 -*-
"""
inject_markdown_diagrams.py
Injects images and diagram context into G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md
and fixes Rev_SecA_Q09 and Rev_SecB_Q04 answer keys.
"""

import re

with open('G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section A Q9
q9_old_pattern = r'(#### ▶ Section A Q9 — MCQ 9: Label of Trachea in Respiratory Diagram \(Figure 1\)\n.*?)##### 4\. 选项逐项深度辨析与考点诊断'
q9_new_block = """#### ▶ Section A Q9 — MCQ 9: Label of Trachea in Respiratory Diagram (Figure 1)
**【中文任务标题】**: 选择题9：呼吸系统示意图中代表气管的字母标注  
**【互动题型 / 游戏化组件】**: `mcq` (单选题闯关)  
**【标准依据出处】**: 《G8 Science.pdf》Chapter 3: B8.02 Gas exchange in humans (p. 36, Fig B8.01) | 《G8_Science_Human_Physiology_Part2.pdf》Revision Questions p. 134  

##### 1. 题目内容与要求 (Question Prompt)
**[EN]**:
```text
9. Look at Figure 1. Which labelled structure is the trachea?
A) A
B) B
C) C
D) D
```
**[CN]**:
9. 观察图1（Figure 1：人体呼吸系统结构示意图）。哪一个标注字母代表气管 (Trachea)？
A) A
B) B
C) C
D) D

> **【附图与图解指引 / Diagram Context】**:  
> ![Figure 1: The Human Respiratory System](images/fig_revision_respiratory_system.jpeg)  
> * **[EN Diagram Context]**: Figure 1 shows the conducting zone of the human respiratory system: Label A points to the nasal cavity (conchae); below it are Pharynx and Larynx; Label B points to the Trachea (the central vertical cartilaginous windpipe); Label C points to the Bronchus (left/right primary airway entering the lung); Label D points to the Bronchioles (intrapulmonary branching tree within the lungs).  
> * **[CN 图解说明]**: 图1显示人体呼吸系统导气通路结构：标注A指向头部鼻腔（Nasal Cavity）；下方已直接标注咽（Pharynx）与喉（Larynx）；标注B指向喉下方的气管主干（Trachea/Windpipe）；标注C指向进入肺门的主支气管（Bronchus）；标注D指向肺叶内的细支气管分支（Bronchioles）。

##### 2. 官方参考答案与评分标准 (Official Reference Answer & Mark Scheme)
**[EN]**:
```text
B) B
```
**[CN]**:
B) B

##### 3. 生理机制深度剖析与考点解析 (Scientific Rationale & Exam Marking Insights)
- **[EN Rationale]**: In Figure 1, structure B points directly to the trachea (the main midline windpipe descending from the larynx into the thoracic cavity). Structure A indicates the nasal cavity, C indicates the primary bronchus, and D indicates intrapulmonary bronchioles.
- **[CN 解析]**: 在图1（Figure 1）解剖图谱中，标号B直接指向喉部下方延伸至胸腔的气管主干（Trachea/Windpipe）。标号A指向鼻腔（Nasal Cavity），C指向进入两肺的主支气管（Bronchus），D指向肺实质内的细支气管（Bronchioles）。

"""

content = re.sub(q9_old_pattern, q9_new_block + "##### 4. 选项逐项深度辨析与考点诊断", content, flags=re.DOTALL)
print("Updated Section A Q9 in markdown.")

# 2. Update Section B Q4
q4_old_pattern = r'(#### ▶ Section B Q4 — Name Respiratory Structures A, B, C, D \(Figure 1\) \[5 marks\]\n.*?)##### 2\. 官方参考答案与评分标准'
q4_new_prompt = """#### ▶ Section B Q4 — Name Respiratory Structures A, B, C, D (Figure 1) [5 marks]
**【中文任务标题】**: 大题4：辨识呼吸系统结构A、B、C、D并阐明D的功能（5分）  
**【互动题型 / 游戏化组件】**: `cloze` (综合大题/评分细则)  
**【标准依据出处】**: 《G8 Science.pdf》Chapter 3: B8.02 Gas exchange in humans (pp. 36-39) | 《G8_Science_Human_Physiology_Part2.pdf》Revision Questions p. 142  

##### 1. 题目内容与要求 (Question Prompt)
**[EN]**:
```text
4. Using Figure 1 (shown in Section A, Question 9), name the structures labelled A, B, C, and D, and state the function of structure D during breathing. [5 marks]
```
**[CN]**:
4. 利用图1（见 Section A 第9题），写出标注结构 A、B、C 和 D 的名称，并阐明结构 D 在呼吸过程中的生理功能。[5分]

> **【附图与图解指引 / Diagram Context】**:  
> ![Figure 1: The Human Respiratory System](images/fig_revision_respiratory_system.jpeg)  
> * **[EN Diagram Context]**: Figure 1 depicts the respiratory tract: Structure A is the Nasal Cavity; Structure B is the Trachea; Structure C is the Bronchus; Structure D represents the Bronchioles. (Note: On page 142 diagram, an additional pointer E is present at the base indicating the Diaphragm).  
> * **[CN 图解说明]**: 图1展示人体呼吸系统导气通路结构：标注A为鼻腔（Nasal Cavity）；标注B为气管（Trachea）；标注C为主支气管（Bronchus）；标注D为细支气管（Bronchiole）。（原书第142页底端补充了标注E指向胸底膈肌Diaphragm）。

"""
content = re.sub(q4_old_pattern, q4_new_prompt + "##### 2. 官方参考答案与评分标准", content, flags=re.DOTALL)
print("Updated Section B Q4 prompt and image in markdown.")

# 3. Update Section B Q8 (Nephron diagram)
q8_old_pattern = r'(#### ▶ Section B Q8 — Nephron Urine Production: Ultrafiltration & Reabsorption \[5 marks\]\n.*?)##### 2\. 官方参考答案与评分标准'
q8_new_prompt = """#### ▶ Section B Q8 — Nephron Urine Production: Ultrafiltration & Reabsorption [5 marks]
**【中文任务标题】**: 大题8：肾单位尿液生成机制（超滤与选择性重吸收）（5分）  
**【互动题型 / 游戏化组件】**: `cloze` (综合大题/评分细则)  
**【标准依据出处】**: 《G8 Science.pdf》Chapter 4: B9.02 The kidneys and excretion (pp. 54-57) | 《G8_Science_Human_Physiology_Part2.pdf》Revision Questions p. 144  

##### 1. 题目内容与要求 (Question Prompt)
**[EN]**:
```text
8. Figure 2 shows a nephron (the filtration unit of the kidney). Describe how the nephron produces urine. Refer to filtration in the glomerulus and selective reabsorption in the renal tubule. [5 marks]
```
**[CN]**:
8. 图2显示了一个肾单位（肾脏的微观滤过单元）。请阐述肾单位如何生成尿液，需结合肾小球的滤过作用和肾小管的选择性重吸收作用进行说明。[5分]

> **【附图 / Figure 2】**:  
> ![Figure 2: A Nephron (Filtration Unit of the Kidney)](images/fig_revision_nephron.png)  
> * **[Diagram Context]**: Figure 2 illustrates the functional nephron unit: Afferent arteriole entering the high-pressure capillary knot (Glomerulus) inside Bowman's capsule; followed by the Proximal Convoluted Tubule, Loop of Henle, Distal Tubule, and the Collecting Duct.

"""
content = re.sub(q8_old_pattern, q8_new_prompt + "##### 2. 官方参考答案与评分标准", content, flags=re.DOTALL)
print("Updated Section B Q8 image in markdown.")

# 4. Update Section B Q11 (Blood glucose graph)
q11_old_pattern = r'(#### ▶ Section B Q11 — Blood Glucose Response after Meal & Insulin Role \(Figure 3\) \[5 marks\]\n.*?)##### 2\. 官方参考答案与评分标准'
q11_new_prompt = """#### ▶ Section B Q11 — Blood Glucose Response after Meal & Insulin Role (Figure 3) [5 marks]
**【中文任务标题】**: 大题11：餐后血糖动态曲线分析与胰岛素调节作用（5分）  
**【互动题型 / 游戏化组件】**: `cloze` (综合大题/评分细则)  
**【标准依据出处】**: 《G8 Science.pdf》Chapter 5: B10.02 Hormones & Blood Glucose (pp. 64-67) | 《G8_Science_Human_Physiology_Part2.pdf》Revision Questions p. 145  

##### 1. 题目内容与要求 (Question Prompt)
**[EN]**:
```text
11. Figure 3 shows a person's blood glucose concentration before and after eating a meal. Describe what happens to blood glucose concentration in the two hours after the meal, and explain the role of insulin in bringing the level back down to normal. [5 marks]
```
**[CN]**:
11. 图3展示了一个人在进食前后的血糖浓度变化。请描述进食后两小时内血糖浓度的变化趋势，并解释胰岛素在使血糖水平恢复正常过程中的生理作用。[5分]

> **【附图 / Figure 3】**:  
> ![Figure 3: Blood Glucose Concentration Over Time](images/fig_revision_glucose_graph.png)  
> * **[Graph Analysis]**: Time 0–1 h represents fasting baseline (~4.5 mmol/L). At 1 h, a carbohydrate-rich meal is consumed, causing blood glucose to spike sharply to a peak of ~7.8 mmol/L at hour 2. Over hours 2 to 6, insulin-driven glucose uptake and glycogen storage return glucose smoothly to normal fasting level.

"""
content = re.sub(q11_old_pattern, q11_new_prompt + "##### 2. 官方参考答案与评分标准", content, flags=re.DOTALL)
print("Updated Section B Q11 image in markdown.")

# 5. Update Section B Q14 (Menstrual cycle hormones graph)
q14_old_pattern = r'(#### ▶ Section B Q14 — Oestrogen & Progesterone Dynamics & Menstruation Trigger \(Figure 4\) \[5 marks\]\n.*?)##### 2\. 官方参考答案与评分标准'
q14_new_prompt = """#### ▶ Section B Q14 — Oestrogen & Progesterone Dynamics & Menstruation Trigger (Figure 4) [5 marks]
**【中文任务标题】**: 大题14：月经周期雌孕激素动态变化与月经来潮诱因（5分）  
**【互动题型 / 游戏化组件】**: `cloze` (综合大题/评分细则)  
**【标准依据出处】**: 《G8 Science.pdf》Chapter 5: B10.04 The Menstrual Cycle (pp. 72-75) | 《G8_Science_Human_Physiology_Part2.pdf》Revision Questions p. 147  

##### 1. 题目内容与要求 (Question Prompt)
**[EN]**:
```text
14. Figure 4 shows how the levels of oestrogen and progesterone change during the 28-day menstrual cycle. Describe how the levels of these two hormones change over the cycle, and explain what triggers menstruation to begin. [5 marks]
```
**[CN]**:
14. 图4显示了28天月经周期中雌激素和孕激素水平的变化情况。请阐述这两种激素在整个周期中的变化动态，并解释触发月经来潮的生理诱因。[5分]

> **【附图 / Figure 4】**:  
> ![Figure 4: Hormone Levels During the 28-Day Menstrual Cycle](images/fig_revision_menstrual_cycle.png)  
> * **[Graph Analysis]**: Days 1–5: Menstruation. Days 6–13: Oestrogen climbs steadily to peak around Day 13 just prior to ovulation (Day 14). After ovulation, the corpus luteum forms and progesterone surges to peak around Days 20–22. If unfertilised, the corpus luteum degenerates, causing both hormones to plummet sharply by Day 28, triggering menstruation.

"""
content = re.sub(q14_old_pattern, q14_new_prompt + "##### 2. 官方参考答案与评分标准", content, flags=re.DOTALL)
print("Updated Section B Q14 image in markdown.")

with open('G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Markdown document updated successfully with embedded images and context.")
