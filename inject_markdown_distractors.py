# -*- coding: utf-8 -*-
import json
import re

with open('g8_science_part2_exercises_bilingual.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Map id to item
items_by_id = {it['id']: it for it in items if 'options_breakdown' in it}

with open('G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# We want to insert Section 4 before the next "---" for each MCQ task
# Let's inspect where MCQs are in the markdown
count = 0
for it_id, it in items_by_id.items():
    code = it['task_code']
    # Build markdown table for options_breakdown
    breakdown = it['options_breakdown']
    table_lines = [
        "\n##### 4. 选项逐项深度辨析与考点诊断 (Option-by-Option Distractor Analysis)",
        "| 选项 | 判定 | 知识点与考点生理学深度辨析 (Bilingual Distractor Rationale) |",
        "| :---: | :---: | :--- |"
    ]
    for letter in ['A', 'B', 'C', 'D']:
        opt = breakdown[letter]
        mark = "✔️ 正确 (Correct)" if opt['correct'] else "❌ 错误 (Incorrect)"
        analysis = f"**[EN]**: {opt['en']}<br>**[CN]**: {opt['cn']}"
        table_lines.append(f"| **{letter}** | {mark} | {analysis} |")
    table_str = '\n'.join(table_lines) + '\n'

    # Search for task header
    # Pattern e.g. "▶ Lesson 24 Part 1 Q1" or "▶ Section A Q1"
    escaped_code = re.escape(code)
    pattern = rf'(#### ▶ [^\n]*?{escaped_code}[^\n]*?\n(?:(?!#### ▶|---).)*?)(?=\n---|\n#### ▶)'
    
    match = re.search(pattern, md_content, re.DOTALL)
    if match:
        matched_block = match.group(1)
        if "##### 4. 选项逐项深度辨析与考点诊断" not in matched_block:
            replacement = matched_block + table_str
            md_content = md_content.replace(matched_block, replacement, 1)
            count += 1
    else:
        print(f"Warning: could not match task_code {code} in markdown")

print(f"Successfully injected distractor tables into {count} MCQs in G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md")

with open('G8_Science_Human_Physiology_Part2_Answers_Bilingual_Complete.md', 'w', encoding='utf-8') as f:
    f.write(md_content)
