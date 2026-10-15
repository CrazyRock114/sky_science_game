# -*- coding: utf-8 -*-
"""
compile_deep_distractors.py
Compiles deep distractor analyses from Blocks 1, 2, and 3:
- Block 1: L24 Housekeeping Q1-Q10, L30 Housekeeping Q1-Q10 (20 MCQs)
- Block 2: Cumulative Revision Section A Q1-Q20 (20 MCQs)
- Block 3: Cumulative Revision Section A Q21-Q40 (20 MCQs)
Total: 60 MCQs

Updates:
1. g8_science_part2_exercises_bilingual.json
2. science_exercises_data.js
3. G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md
"""

import json
import re
from data_deep_mcq_block1 import BLOCK1_DISTRACTORS
from data_deep_mcq_block2 import BLOCK2_DISTRACTORS
from data_deep_mcq_block3 import BLOCK3_DISTRACTORS

# Merge all blocks
ALL_DISTRACTORS = {}
ALL_DISTRACTORS.update(BLOCK1_DISTRACTORS)
ALL_DISTRACTORS.update(BLOCK2_DISTRACTORS)
ALL_DISTRACTORS.update(BLOCK3_DISTRACTORS)

print(f"Total merged MCQs: {len(ALL_DISTRACTORS)}")
assert len(ALL_DISTRACTORS) == 60, f"Expected 60 MCQs, got {len(ALL_DISTRACTORS)}"

# Validate each MCQ
for q_id, opts in ALL_DISTRACTORS.items():
    assert set(opts.keys()) == {"A", "B", "C", "D"}, f"{q_id} does not have A, B, C, D"
    num_correct = sum(1 for o in opts.values() if o["correct"])
    assert num_correct == 1, f"{q_id} does not have exactly 1 correct answer (found {num_correct})"
    for ltr, o in opts.items():
        assert "en" in o and len(o["en"]) > 50, f"{q_id} option {ltr} en is too short or missing"
        assert "cn" in o and len(o["cn"]) > 30, f"{q_id} option {ltr} cn is too short or missing"
        assert "不成立" not in o["cn"], f"{q_id} option {ltr} contains forbidden fallback '不成立'"

print("All 60 MCQs passed rigorous structural and content validation.")

# 1. Update g8_science_part2_exercises_bilingual.json
with open('g8_science_part2_exercises_bilingual.json', 'r', encoding='utf-8') as f:
    part2_items = json.load(f)

updated_p2_count = 0
for item in part2_items:
    if item['id'] in ALL_DISTRACTORS:
        item['options_breakdown'] = ALL_DISTRACTORS[item['id']]
        updated_p2_count += 1

print(f"Updated options_breakdown for {updated_p2_count} items in g8_science_part2_exercises_bilingual.json")
assert updated_p2_count == 60, f"Expected 60 items updated, got {updated_p2_count}"

with open('g8_science_part2_exercises_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump(part2_items, f, ensure_ascii=False, indent=2)

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

# 3. Update G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md
with open('G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

items_by_id = {it['id']: it for it in part2_items if it['id'] in ALL_DISTRACTORS}
md_updated_count = 0

for q_id, item in items_by_id.items():
    code = item['task_code']
    breakdown = item['options_breakdown']
    
    # Build replacement table
    table_lines = [
        "##### 4. 选项逐项深度辨析与考点诊断 (Option-by-Option Distractor Analysis)",
        "| 选项 | 判定 | 知识点与考点生理学深度辨析 (Bilingual Distractor Rationale) |",
        "| :---: | :---: | :--- |"
    ]
    for letter in ['A', 'B', 'C', 'D']:
        opt = breakdown[letter]
        mark = "✔️ 正确 (Correct)" if opt['correct'] else "❌ 错误 (Incorrect)"
        analysis = f"**[EN]**: {opt['en']}<br>**[CN]**: {opt['cn']}"
        table_lines.append(f"| **{letter}** | {mark} | {analysis} |")
    new_table_str = '\n'.join(table_lines) + '\n'

    # Search for this question's block in markdown
    # Heading format e.g. "#### ▶ Lesson 24 Part 1 Q1" or "#### ▶ Section A Q1"
    escaped_code = re.escape(code)
    
    # Look for existing section 4 or block up to next '---' or '#### ▶'
    # Pattern matches the task header and its body
    pattern = rf'(#### ▶ [^\n]*?{escaped_code}[^\n]*?\n)(.*?)(?=\n---|\n#### ▶|\Z)'
    match = re.search(pattern, md_content, re.DOTALL)
    if match:
        header_line = match.group(1)
        body = match.group(2)
        
        # Check if Section 4 already exists in this task block
        sec4_idx = body.find("##### 4. 选项逐项深度辨析与考点诊断")
        if sec4_idx != -1:
            # Replace existing Section 4 table
            new_body = body[:sec4_idx] + new_table_str
        else:
            # Append Section 4 table
            new_body = body.rstrip() + "\n\n" + new_table_str
        
        # Replace in md_content
        old_full_block = header_line + body
        new_full_block = header_line + new_body
        md_content = md_content.replace(old_full_block, new_full_block, 1)
        md_updated_count += 1
    else:
        print(f"Warning: could not locate task_code {code} in markdown file!")

print(f"Updated markdown distractor tables for {md_updated_count} questions in G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md")
assert md_updated_count == 60, f"Expected 60 markdown blocks updated, got {md_updated_count}"

with open('G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("All files updated and synchronized successfully!")
