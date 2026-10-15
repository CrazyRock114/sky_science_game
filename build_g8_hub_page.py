# -*- coding: utf-8 -*-
"""
Full page builder for g8_exam_rush.html
Combines build_g8_hub_data.py with full HTML/CSS/JS frontend.
"""

import json
from build_g8_hub_data import OBJECTIVE_QUESTIONS, WRITTEN_THEORY_QUESTIONS

def build_page():
    obj_json = json.dumps(OBJECTIVE_QUESTIONS, ensure_ascii=False)
    wt_json = json.dumps(WRITTEN_THEORY_QUESTIONS, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Cambridge G8 科学考前 2 小时全真突击大厅 (10.19 考试专用)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <link rel="stylesheet" href="https://igcse.xyz/ecosystem-nav.css">
  <style>
    :root {{
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --primary-light: #eff6ff;
      --accent: #f59e0b;
      --success: #10b981;
      --success-light: #ecfdf5;
      --danger: #ef4444;
      --danger-light: #fef2f2;
      --purple: #8b5cf6;
      --bg: #0b1120;
      --card-bg: rgba(30, 41, 59, 0.88);
      --card-border: rgba(255, 255, 255, 0.1);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #0f172a 50%, #020617 100%);
      color: var(--text-main);
      font-family: var(--font-sans);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.5;
    }}

    header.rush-header {{
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid var(--card-border);
      position: relative;
      padding: 0.5rem 1rem 0.35rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }}

    .header-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      max-width: 1200px;
      margin: 0 auto;
      flex-wrap: wrap;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    .btn-back-home {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 9999px;
      padding: 0.25rem 0.65rem;
      text-decoration: none;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .btn-back-home:hover {{
      background: rgba(56, 189, 248, 0.2);
      color: #7dd3fc;
      border-color: #38bdf8;
      transform: translateX(-1px);
    }}

    .brand-title-wrap {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }}

    .brand-icon {{
      background: linear-gradient(135deg, #ef4444 0%, #f59e0b 100%);
      width: 28px;
      height: 28px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      box-shadow: 0 0 10px rgba(239, 68, 68, 0.4);
      flex-shrink: 0;
    }}

    .brand-title {{
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      color: #fff;
      margin: 0;
    }}

    .badge-emergency {{
      background: #ef4444;
      color: #fff;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 1px 7px;
      border-radius: 999px;
      animation: pulse 2s infinite;
      white-space: nowrap;
    }}

    @keyframes pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.8; transform: scale(0.96); }}
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .btn-action {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 0.32rem 0.7rem;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }}

    .btn-action:hover {{
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.25);
    }}

    .btn-action.active {{
      background: var(--primary);
      border-color: var(--primary);
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.4);
    }}

    /* Top Tabs Navigation */
    .nav-tabs {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      max-width: 1200px;
      margin: 0.4rem auto 0;
      overflow-x: auto;
      padding-bottom: 0.2rem;
      scrollbar-width: none;
      -webkit-overflow-scrolling: touch;
    }}
    .nav-tabs::-webkit-scrollbar {{ display: none; }}

    .tab-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
      padding: 0.38rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.84rem;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }}

    .tab-btn:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.25);
    }}

    .tab-btn.active {{
      color: #fff;
      background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
      border-color: rgba(96, 165, 250, 0.7);
      box-shadow: 0 0 14px rgba(59, 130, 246, 0.45);
    }}

    .tab-btn.tab-mock.active {{
      background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
      border-color: rgba(248, 113, 113, 0.8);
      box-shadow: 0 0 14px rgba(239, 68, 68, 0.45);
    }}

    .tab-btn.tab-theory.active {{
      background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
      border-color: rgba(167, 139, 250, 0.8);
      box-shadow: 0 0 14px rgba(139, 92, 246, 0.45);
    }}

    /* Main Container */
    main {{
      flex: 1;
      max-width: 1200px;
      width: 100%;
      margin: 0 auto;
      padding: 1.25rem 1rem 3rem;
    }}

    .tab-pane {{
      display: none;
    }}
    .tab-pane.active {{
      display: block;
      animation: fadeIn 0.3s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Common Card Styles */
    .glass-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.5rem;
      margin-bottom: 1.25rem;
      backdrop-filter: blur(16px);
      box-shadow: var(--shadow-lg);
    }}

    .section-title {{
      font-size: 1.25rem;
      font-weight: 800;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: #fff;
    }}

    .section-subtitle {{
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-bottom: 1.25rem;
    }}

    /* ==================== TAB 1: CONCEPT CARDS ==================== */
    .concept-accordion {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .concept-item {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      overflow: hidden;
      transition: all 0.2s ease;
    }}

    .concept-header {{
      padding: 1rem 1.25rem;
      background: rgba(30, 41, 59, 0.6);
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
    }}

    .concept-header:hover {{
      background: rgba(30, 41, 59, 0.9);
    }}

    .concept-header h3 {{
      font-size: 1.05rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .concept-body {{
      padding: 1.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      display: none;
    }}

    .concept-item.open .concept-body {{
      display: block;
    }}

    .concept-item.open .concept-header {{
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(59, 130, 246, 0.15);
    }}

    .concept-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      font-size: 0.88rem;
    }}

    .concept-table th, .concept-table td {{
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 0.65rem 0.85rem;
      text-align: left;
    }}

    .concept-table th {{
      background: rgba(59, 130, 246, 0.2);
      color: #93c5fd;
      font-weight: 700;
    }}

    .concept-table tr:nth-child(even) {{
      background: rgba(255, 255, 255, 0.02);
    }}

    .badge-pill {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 700;
      margin-right: 0.35rem;
    }}
    .pill-blue {{ background: rgba(59, 130, 246, 0.25); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); }}
    .pill-green {{ background: rgba(16, 185, 129, 0.25); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .pill-amber {{ background: rgba(245, 158, 11, 0.25); color: #fcd34d; border: 1px solid rgba(245, 158, 11, 0.4); }}
    .pill-red {{ background: rgba(239, 68, 68, 0.25); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}
    .pill-purple {{ background: rgba(139, 92, 246, 0.25); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4); }}

    .highlight-box {{
      background: rgba(15, 23, 42, 0.7);
      border-left: 4px solid var(--accent);
      padding: 0.85rem 1rem;
      border-radius: 0 10px 10px 0;
      margin: 0.85rem 0;
      font-size: 0.88rem;
    }}

    /* ==================== TAB 2: OBJECTIVE ARENA ==================== */
    .arena-toolbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }}

    .filter-pills {{
      display: flex;
      gap: 0.4rem;
      flex-wrap: wrap;
    }}

    .filter-btn {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 0.35rem 0.8rem;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .filter-btn:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.12);
    }}

    .filter-btn.active {{
      color: #fff;
      background: var(--primary);
      border-color: var(--primary);
    }}

    .stats-meter {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      font-family: var(--font-mono);
      font-size: 0.88rem;
    }}

    .timer-wrap {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      background: rgba(0, 0, 0, 0.4);
      padding: 0.35rem 0.75rem;
      border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }}

    .rush-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 1.75rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
    }}

    .q-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .q-prompt-en {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.4rem;
      line-height: 1.45;
    }}

    .q-prompt-cn {{
      font-size: 0.95rem;
      color: #94a3b8;
      margin-bottom: 1.5rem;
      line-height: 1.5;
    }}

    .options-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }}

    .opt-btn {{
      background: rgba(15, 23, 42, 0.6);
      border: 2px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 0.95rem 1.15rem;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      text-align: left;
      font-family: var(--font-sans);
      transition: all 0.2s ease;
    }}

    .opt-btn:hover:not(:disabled) {{
      background: rgba(59, 130, 246, 0.12);
      border-color: rgba(59, 130, 246, 0.5);
      transform: translateY(-2px);
    }}

    .opt-letter {{
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
      width: 28px;
      height: 28px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-family: var(--font-mono);
      flex-shrink: 0;
    }}

    .opt-text {{
      flex: 1;
    }}
    .opt-text-en {{
      font-weight: 600;
      font-size: 0.95rem;
      margin-bottom: 0.2rem;
    }}
    .opt-text-cn {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .opt-btn.correct {{
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: var(--success) !important;
      box-shadow: 0 0 15px rgba(16, 185, 129, 0.3);
    }}
    .opt-btn.correct .opt-letter {{
      background: var(--success);
      color: #0b1120;
    }}

    .opt-btn.wrong {{
      background: rgba(239, 68, 68, 0.2) !important;
      border-color: var(--danger) !important;
      box-shadow: 0 0 15px rgba(239, 68, 68, 0.3);
    }}
    .opt-btn.wrong .opt-letter {{
      background: var(--danger);
      color: #fff;
    }}

    /* Feedback Drawer */
    .feedback-box {{
      display: none;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 1.25rem;
      margin-top: 1.25rem;
      animation: fadeIn 0.3s ease;
    }}

    .fb-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.75rem;
      font-weight: 800;
      font-size: 1.05rem;
    }}

    .fb-concept {{
      background: rgba(16, 185, 129, 0.1);
      border-left: 4px solid var(--success);
      padding: 0.75rem 0.95rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 0.75rem;
      font-size: 0.88rem;
    }}

    .fb-trap {{
      background: rgba(245, 158, 11, 0.1);
      border-left: 4px solid var(--accent);
      padding: 0.75rem 0.95rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 0.75rem;
      font-size: 0.88rem;
    }}

    .fb-citation {{
      font-size: 0.75rem;
      color: var(--text-muted);
      text-align: right;
      font-family: var(--font-mono);
    }}

    .arena-actions {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 1.5rem;
      flex-wrap: wrap;
      gap: 0.75rem;
    }}

    .btn-next {{
      background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
      color: #fff;
      border: none;
      padding: 0.75rem 1.75rem;
      border-radius: 999px;
      font-weight: 800;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
      transition: all 0.2s ease;
      margin-left: auto;
    }}

    .btn-next:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }}

    /* ==================== TAB 3: WRITTEN THEORY ==================== */
    .theory-item {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-lg);
    }}

    .theory-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 0.75rem;
      margin-bottom: 0.85rem;
      flex-wrap: wrap;
    }}

    .theory-badges {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex-wrap: wrap;
    }}

    .badge-mark {{
      background: var(--purple);
      color: #fff;
      font-family: var(--font-mono);
      font-weight: 800;
      padding: 2px 9px;
      border-radius: 6px;
      font-size: 0.8rem;
    }}

    .badge-command {{
      background: rgba(245, 158, 11, 0.2);
      color: #fcd34d;
      border: 1px solid rgba(245, 158, 11, 0.4);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
    }}

    .theory-prompt-en {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.35rem;
    }}

    .theory-prompt-cn {{
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}

    .theory-textarea {{
      width: 100%;
      min-height: 110px;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 10px;
      padding: 0.85rem;
      color: #fff;
      font-family: var(--font-sans);
      font-size: 0.92rem;
      line-height: 1.5;
      resize: vertical;
      margin-bottom: 0.75rem;
      transition: border-color 0.2s ease;
    }}

    .theory-textarea:focus {{
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.3);
    }}

    .theory-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
    }}

    .btn-reveal {{
      background: rgba(139, 92, 246, 0.2);
      border: 1px solid rgba(139, 92, 246, 0.4);
      color: #c4b5fd;
      padding: 0.45rem 1rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }}

    .btn-reveal:hover {{
      background: rgba(139, 92, 246, 0.35);
      color: #fff;
    }}

    .mark-scheme-box {{
      display: none;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(139, 92, 246, 0.3);
      border-radius: 12px;
      padding: 1.25rem;
      margin-top: 1rem;
      animation: fadeIn 0.3s ease;
    }}

    .ms-point {{
      margin-bottom: 0.65rem;
      font-size: 0.88rem;
      padding-left: 1.2rem;
      position: relative;
    }}
    .ms-point::before {{
      content: "✔";
      position: absolute;
      left: 0;
      color: var(--success);
      font-weight: 800;
    }}

    .keywords-wrap {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin: 0.85rem 0;
    }}

    .kw-tag {{
      background: rgba(59, 130, 246, 0.2);
      border: 1px solid rgba(59, 130, 246, 0.4);
      color: #93c5fd;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-family: var(--font-mono);
      font-weight: 700;
    }}

    /* Self Assessment Bar */
    .self-score-bar {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-top: 1rem;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
    }}

    .score-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text-main);
      width: 38px;
      height: 34px;
      border-radius: 8px;
      font-weight: 800;
      font-family: var(--font-mono);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }}

    .score-btn:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}

    .score-btn.selected {{
      background: var(--purple);
      border-color: var(--purple);
      color: #fff;
      box-shadow: 0 0 10px rgba(139, 92, 246, 0.4);
    }}

    /* ==================== TAB 4: MOCK EXAM ==================== */
    .mock-start-box {{
      text-align: center;
      padding: 3rem 1.5rem;
    }}

    .mock-start-btn {{
      background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
      color: #fff;
      border: none;
      padding: 0.9rem 2.5rem;
      border-radius: 999px;
      font-size: 1.1rem;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(239, 68, 68, 0.4);
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      transition: all 0.2s ease;
      margin-top: 1.5rem;
    }}

    .mock-start-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(239, 68, 68, 0.6);
    }}

    .mock-timer-bar {{
      position: sticky;
      top: 60px;
      z-index: 40;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(239, 68, 68, 0.4);
      border-radius: 12px;
      padding: 0.65rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      backdrop-filter: blur(12px);
    }}

    .mock-timer-digits {{
      font-family: var(--font-mono);
      font-size: 1.3rem;
      font-weight: 800;
      color: #ef4444;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .diag-radar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin: 1.5rem 0;
    }}

    .diag-card {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 1.15rem;
    }}

    .diag-bar-track {{
      background: rgba(255, 255, 255, 0.1);
      height: 10px;
      border-radius: 999px;
      overflow: hidden;
      margin-top: 0.6rem;
    }}

    .diag-bar-fill {{
      height: 100%;
      border-radius: 999px;
      transition: width 0.6s ease;
    }}

    /* Completion View */
    .completion-card {{
      text-align: center;
      padding: 2.5rem 1.5rem;
    }}

    .cert-badge {{
      display: inline-block;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 0.4rem 1.4rem;
      border-radius: 999px;
      margin-bottom: 1rem;
    }}
    .cert-a-star {{ background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: #0f172a; box-shadow: 0 0 20px rgba(245, 158, 11, 0.4); }}
    .cert-a {{ background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); color: #fff; box-shadow: 0 0 20px rgba(59, 130, 246, 0.4); }}
    .cert-pass {{ background: linear-gradient(135deg, #10b981 0%, #047857 100%); color: #fff; box-shadow: 0 0 20px rgba(16, 185, 129, 0.4); }}
    .cert-retry {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}

    /* Confetti Canvas */
    #confetti-canvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 9999;
    }}

    @media (max-width: 768px) {{
      header.rush-header {{ padding: 0.45rem 0.65rem 0.35rem; }}
      main {{ padding: 0.75rem 0.5rem 2rem; }}
      .glass-card {{ padding: 1.15rem; }}
      .header-top {{ flex-wrap: wrap; gap: 0.4rem; }}
      .brand-title {{ font-size: 0.9rem; }}
      .brand-icon {{ width: 24px; height: 24px; font-size: 0.8rem; }}
      .btn-back-home {{ font-size: 0.72rem; padding: 0.2rem 0.5rem; }}
      .btn-action span {{ display: none; }}
      .btn-action {{ padding: 0.3rem 0.5rem; font-size: 0.75rem; }}
      .tab-btn {{ font-size: 0.78rem; padding: 0.32rem 0.65rem; }}
      .nav-tabs {{ margin-top: 0.35rem; gap: 0.3rem; }}
      .q-prompt-en {{ font-size: 1rem; }}
    }}
  </style>
</head>
<body>
  <!-- ==================== Mother-Ship Global TopBar ==================== -->
  <script src="https://igcse.xyz/ecosystem-nav.js" defer></script>
  <igcse-nav active="sky"></igcse-nav>

  <canvas id="confetti-canvas"></canvas>

  <header class="rush-header">
    <div class="header-top">
      <div class="header-left">
        <a href="index.html" class="btn-back-home" title="返回 Sky 科学岛首页">
          ← 返回 Sky 科学岛首页
        </a>
        <div class="brand-title-wrap">
          <div class="brand-icon">⚡</div>
          <h1 class="brand-title">
            G8 科学考前冲刺大厅
            <span class="badge-emergency">10.19 特训</span>
          </h1>
        </div>
      </div>

      <div class="header-actions">
        <button class="btn-action" id="btn-lang" onclick="toggleGlobalLang()">
          🌐 <span id="txt-lang">双语</span>
        </button>
        <button class="btn-action active" id="btn-sound" onclick="toggleGlobalSound()">
          🔊 <span id="txt-sound">声音</span>
        </button>
      </div>
    </div>

    <div class="nav-tabs" role="tablist">
      <button class="tab-btn active" onclick="switchMainTab('concepts')">
        📌 核心考纲速记卡
      </button>
      <button class="tab-btn" onclick="switchMainTab('objective')">
        🎯 全考点闯关 (48题)
      </button>
      <button class="tab-btn tab-theory" onclick="switchMainTab('theory')">
        📝 笔试简答大擂台 (10题)
      </button>
      <button class="tab-btn tab-mock" onclick="switchMainTab('mock')">
        ⏱️ 40分钟全真模拟卷
      </button>
    </div>
  </header>

  <main>
    <!-- ==================== TAB 1: CONCEPTS ==================== -->
    <div id="pane-concepts" class="tab-pane active">
      <div class="glass-card">
        <div class="section-title">📌 核心考纲知识卡与避坑导图 (Core Concept Cards)</div>
        <div class="section-subtitle">专为下周一二科学考试量身定制的三大专题高频考点速览。点击折叠面板快速复盘采分核心！</div>

        <div class="concept-accordion">
          <!-- Card 1: 物质跨膜运输 -->
          <div class="concept-item open">
            <div class="concept-header" onclick="toggleConcept(this)">
              <h3>🌿 专题一：物质进出细胞 (Movement in & out of Cells)</h3>
              <span>▼</span>
            </div>
            <div class="concept-body">
              <p style="font-size:0.9rem; color:#94a3b8; margin-bottom:0.75rem;">
                物质跨膜运输三大机制官方横向对比表（必背采分定义）：
              </p>
              <table class="concept-table">
                <thead>
                  <tr>
                    <th>运输机制</th>
                    <th>浓度方向</th>
                    <th>是否消耗 ATP</th>
                    <th>是否需膜/载体</th>
                    <th>经典人体与植物实例</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>扩散 (Diffusion)</strong></td>
                    <td>沿浓度梯度（高 ➔ 低）</td>
                    <td><span class="badge-pill pill-green">否 (被动)</span></td>
                    <td>否（可在任何介质自由移动）</td>
                    <td>肺泡与毛细血管间 O2 / CO2 气体交换</td>
                  </tr>
                  <tr>
                    <td><strong>渗透 (Osmosis)</strong></td>
                    <td>沿水势梯度（高水势 ➔ 低水势）</td>
                    <td><span class="badge-pill pill-green">否 (被动)</span></td>
                    <td><strong>必须穿过半透膜</strong></td>
                    <td>植物根毛吸水；红细胞吸水涨破 / 失水皱缩</td>
                  </tr>
                  <tr>
                    <td><strong>主动运输 (Active Transport)</strong></td>
                    <td><strong>逆浓度梯度（低 ➔ 高）</strong></td>
                    <td><span class="badge-pill pill-red">必须消耗 ATP</span></td>
                    <td><strong>必须依赖特异性载体蛋白</strong></td>
                    <td>肾小管 100% 重吸收葡萄糖；根毛吸收矿质离子</td>
                  </tr>
                </tbody>
              </table>

              <div class="highlight-box">
                <strong>⚠️ 官方高频陷阱：植物细胞与动物细胞在不同溶液中的表现区别</strong><br>
                1. <strong>置于纯水/低渗溶液中</strong>：<br>
                - 植物细胞：水渗入液泡，坚韧纤维素细胞壁抵抗膨胀产生膨压 ➔ <strong>膨胀坚挺 (Turgid)</strong>，支持植物直立，<strong>绝不涨破</strong>！<br>
                - 动物红细胞：没有细胞壁，吸水持续膨胀直至破裂 ➔ <strong>涨破 (Lysis / Haemolysis)</strong>！<br>
                2. <strong>置于高浓度浓盐水中</strong>：<br>
                - 植物细胞：渗透失水，液泡缩小，原生质层与细胞壁分离 ➔ <strong>质壁分离 (Plasmolysed)</strong>！<br>
                - 动物红细胞：渗透失水，细胞缩小起皱 ➔ <strong>皱缩 (Crenated)</strong>，绝对不能用质壁分离描述动物细胞！
              </div>
            </div>
          </div>

          <!-- Card 2: 泌尿系统与排泄 -->
          <div class="concept-item">
            <div class="concept-header" onclick="toggleConcept(this)">
              <h3>🩺 专题二：排泄与肾脏微观生理 (Excretion & Kidney Nephron)</h3>
              <span>▼</span>
            </div>
            <div class="concept-body">
              <table class="concept-table">
                <thead>
                  <tr>
                    <th>生理过程</th>
                    <th>科学定义</th>
                    <th>被排出的典型物质</th>
                    <th>是否参与体细胞代谢</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>排泄 (Excretion)</strong></td>
                    <td>清除细胞生物化学代谢产生的有毒副产物或过剩物质</td>
                    <td>尿素 (Urea)、二氧化碳 (CO2)、多余水分与无机盐</td>
                    <td><span class="badge-pill pill-blue">是 (来自细胞代谢)</span></td>
                  </tr>
                  <tr>
                    <td><strong>排遗 (Egestion)</strong></td>
                    <td>清除消化道未被酶分解、未被肠壁吸收的食物残渣</td>
                    <td>粪便 (Faeces / 食物粗纤维)</td>
                    <td><span class="badge-pill pill-amber">否 (从未进入体细胞)</span></td>
                  </tr>
                </tbody>
              </table>

              <div class="highlight-box">
                <strong>🔬 肾单位尿液生成两步法机制 (Nephron 2-Step Mechanism)</strong><br>
                1. <strong>肾小球高压超微滤过 (Ultrafiltration)</strong>：入球小动脉粗、出球小动脉细 ➔ 产生极高流体静水压 ➔ 挤压小分子（水、葡萄糖、氨基酸、尿素、离子）穿透基底膜进入肾小囊形成原尿；红细胞和大分子血浆蛋白（白蛋白）因孔径过大留在血液中。<br>
                2. <strong>肾小管选择性重吸收 (Selective Reabsorption)</strong>：在近曲小管处，<strong>100% 的葡萄糖和氨基酸</strong>被载体蛋白逆浓度主动重吸收回血液！约 99% 的水分通过渗透作用重吸收；尿素留在管内高度浓缩形成终尿。<br>
                3. <strong>透析机 (Dialysis Machine) 原理</strong>：血液与透析液<strong>逆流流动 (Counter-current)</strong> 维持最大浓度梯度；透析液配制正常浓度的葡萄糖与无机盐（防止有用物质丢失），但尿素浓度为零（确保尿素最大化扩散排出）。
              </div>
            </div>
          </div>

          <!-- Card 3: 血糖调节与稳态 -->
          <div class="concept-item">
            <div class="concept-header" onclick="toggleConcept(this)">
              <h3>🔄 专题三：血糖负反馈稳态与内分泌 (Blood Glucose & Homeostasis)</h3>
              <span>▼</span>
            </div>
            <div class="concept-body">
              <div class="highlight-box" style="border-left-color:var(--purple);">
                <strong>🌟 稳态与负反馈闭环图 (Negative Feedback Closed Loop)</strong><br>
                正常基准设定值：<strong>5.0 mmol/L</strong><br>
                • <strong>餐后血糖升高</strong> ➔ 胰腺 β 细胞感知并分泌【<strong>胰岛素 (Insulin)</strong>】 ➔ 促使肝脏和肌肉细胞摄取葡萄糖，并催化转化为不溶性【<strong>糖原 (Glycogen)</strong>】储存（葡萄糖 ➔ 糖原） ➔ 血糖回落正常设定值。<br>
                • <strong>饥饿/运动血糖降低</strong> ➔ 胰腺 α 细胞感知并分泌【<strong>胰高血糖素 (Glucagon)</strong>】 ➔ 促使肝脏将储备的【<strong>糖原 (Glycogen)</strong>】分解为【<strong>葡萄糖 (Glucose)</strong>】释放入血（糖原 ➔ 葡萄糖） ➔ 血糖上升回归正常设定值。
              </div>

              <p style="font-weight:700; color:#fff; margin:1rem 0 0.5rem;">三大 G 字头核心术语辨析表（千万不可拼写混淆！）：</p>
              <table class="concept-table">
                <thead>
                  <tr>
                    <th>术语</th>
                    <th>生化本质</th>
                    <th>生理功能与所在部位</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Glucose (葡萄糖)</strong></td>
                    <td>可溶性单糖 (C6H12O6)</td>
                    <td>游离于血液循环中，是细胞呼吸作用的首选直接能量原料</td>
                  </tr>
                  <tr>
                    <td><strong>Glycogen (糖原)</strong></td>
                    <td>不溶性高分子多糖</td>
                    <td>动物淀粉储备，主要储存于肝脏和骨骼肌，对细胞渗透压零干扰</td>
                  </tr>
                  <tr>
                    <td><strong>Glucagon (胰高血糖素)</strong></td>
                    <td>肽类激素化学信使</td>
                    <td>由胰腺分泌释放入血，专门发出指令催化肝糖原分解释放葡萄糖</td>
                  </tr>
                </tbody>
              </table>

              <div class="highlight-box" style="border-left-color:var(--danger);">
                <strong>🩺 糖尿病临床病理对照：1 型 vs 2 型</strong><br>
                - <strong>1 型糖尿病 (Type 1)</strong>：自身免疫系统破坏胰岛 β 细胞 ➔ 无法分泌胰岛素 ➔ 必须每日皮下注射外源性胰岛素。<br>
                - <strong>2 型糖尿病 (Type 2)</strong>：胰腺能产生胰岛素，但靶细胞膜受体不敏感发生【胰岛素抵抗】 ➔ 与高糖饮食和肥胖紧密相关 ➔ 通过健康低糖饮食、运动和口服药物改善受体敏感性。<br>
                - <strong>糖尿与肾糖阈 (Renal Threshold)</strong>：当血糖超过 10~12 mmol/L 时，超出肾小管载体蛋白最大转运能力，原尿中葡萄糖无法全部重吸收，随尿排出（糖尿）。临床可用本尼迪特试剂水浴加热检测（蓝 ➔ 砖红沉淀）。
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== TAB 2: OBJECTIVE ARENA ==================== -->
    <div id="pane-objective" class="tab-pane">
      <div class="glass-card">
        <div class="arena-toolbar">
          <div class="filter-pills">
            <button class="filter-btn active" onclick="filterObjective('all', this)">全部 48 题</button>
            <button class="filter-btn" onclick="filterObjective(1, this)">L1 物质跨膜运输 (16)</button>
            <button class="filter-btn" onclick="filterObjective(2, this)">L2 泌尿与排泄 (16)</button>
            <button class="filter-btn" onclick="filterObjective(3, this)">L3 血糖与稳态 (16)</button>
            <button class="filter-btn" id="btn-wrong-only" onclick="filterObjective('wrong', this)">🔥 错题重练本 (<span id="txt-wrong-count">0</span>)</button>
          </div>

          <div class="stats-meter">
            <div class="timer-wrap">
              <span id="obj-timer-icon">⏱️</span>
              <span id="obj-timer-sec">60s</span>
            </div>
            <div>积分: <strong id="obj-score" style="color:var(--accent);">0</strong></div>
            <div>连击: <strong id="obj-streak" style="color:var(--success);">0</strong></div>
          </div>
        </div>

        <div id="obj-arena-container">
          <div class="rush-card" id="obj-card">
            <div class="q-meta">
              <div style="display:flex;align-items:center;gap:0.4rem;">
                <span class="badge-pill pill-blue" id="obj-lvl-badge">Level 1</span>
                <span class="badge-pill pill-purple" id="obj-topic-badge">Topic</span>
              </div>
              <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted);" id="obj-counter">
                Q 1 / 48
              </div>
            </div>

            <div class="q-prompt-en" id="obj-prompt-en">Loading question...</div>
            <div class="q-prompt-cn" id="obj-prompt-cn">加载题目中...</div>

            <div class="options-grid" id="obj-options-box">
              <!-- Dynamic Options -->
            </div>

            <!-- Feedback Drawer -->
            <div class="feedback-box" id="obj-feedback-box">
              <div class="fb-header" id="obj-fb-title">解析卡片</div>
              <div class="fb-concept" id="obj-fb-concept"></div>
              <div class="fb-trap" id="obj-fb-trap"></div>
              <div class="fb-citation" id="obj-fb-citation"></div>
            </div>

            <div class="arena-actions">
              <label style="font-size:0.85rem; color:var(--text-muted); cursor:pointer; display:inline-flex; align-items:center; gap:0.35rem;">
                <input type="checkbox" id="chk-obj-autonext"> 答对 1.5 秒后自动下一题
              </label>
              <button class="btn-next" id="btn-obj-next" onclick="nextObjectiveQuestion()">下一题 ➔</button>
            </div>
          </div>

          <!-- Completion View -->
          <div class="glass-card completion-card" id="obj-completion-box" style="display:none;">
            <div style="font-size:3.5rem; margin-bottom:0.5rem;" id="cert-icon">👑</div>
            <div class="cert-badge cert-a-star" id="cert-badge">🌟 A* Master 神级学霸</div>
            <h2 style="font-size:1.6rem; font-weight:800; margin-bottom:0.5rem;" id="cert-headline">突击大练兵通关认证</h2>
            <p style="color:var(--text-muted); font-size:0.95rem; max-width:600px; margin:0 auto 1.5rem;" id="cert-desc">
              恭喜你完成了客观题突击闯关！高频生理考点与采分陷阱已完全巩固。
            </p>

            <div style="display:flex; justify-content:center; gap:2rem; margin-bottom:2rem; font-family:var(--font-mono);">
              <div>
                <div style="color:var(--text-muted); font-size:0.8rem;">正确率 (Accuracy)</div>
                <div style="font-size:1.4rem; font-weight:800; color:var(--success);" id="cert-acc">100%</div>
              </div>
              <div>
                <div style="color:var(--text-muted); font-size:0.8rem;">总积分 (Total Score)</div>
                <div style="font-size:1.4rem; font-weight:800; color:var(--accent);" id="cert-score">5200</div>
              </div>
              <div>
                <div style="color:var(--text-muted); font-size:0.8rem;">耗时 (Time Spent)</div>
                <div style="font-size:1.4rem; font-weight:800; color:#93c5fd;" id="cert-time">04:30</div>
              </div>
            </div>

            <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
              <button class="btn-action" style="padding:0.6rem 1.5rem; font-size:0.9rem;" onclick="copyObjectiveReport()">
                📋 一键复制练习战报
              </button>
              <button class="btn-next" style="margin:0;" onclick="restartObjectiveArena()">
                🔄 重新冲刺练习
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== TAB 3: WRITTEN THEORY ==================== -->
    <div id="pane-theory" class="tab-pane">
      <div class="glass-card">
        <div class="section-title">📝 笔试结构化简答与采分点大擂台 (Written Theory & Mark Scheme)</div>
        <div class="section-subtitle">完全还原 Cambridge Paper 3/4 笔试结构化大题！输入作答后点击核对官方采分点，并进行自评打分。</div>

        <div style="background:rgba(139, 92, 246, 0.15); border:1px solid rgba(139, 92, 246, 0.3); border-radius:12px; padding:0.85rem 1.25rem; margin-bottom:1.5rem; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.75rem;">
          <div>
            <strong>自评总得分：</strong>
            <span style="font-family:var(--font-mono); font-size:1.2rem; font-weight:800; color:#c4b5fd;" id="theory-total-score">0</span>
            <span style="color:var(--text-muted); font-size:0.9rem;">/ 37 分</span>
          </div>
          <div style="font-size:0.85rem; color:var(--text-muted);">
            已自评大题：<strong id="theory-evaluated-count" style="color:#fff;">0</strong> / 10 题
          </div>
        </div>

        <div id="theory-list-container">
          <!-- Dynamically populated 10 written questions -->
        </div>
      </div>
    </div>

    <!-- ==================== TAB 4: MOCK EXAM ==================== -->
    <div id="pane-mock" class="tab-pane">
      <div class="glass-card">
        <!-- Start Mock View -->
        <div id="mock-start-screen" class="mock-start-box">
          <div style="font-size:3.5rem; margin-bottom:0.75rem;">⏱️</div>
          <h2 style="font-size:1.6rem; font-weight:800; margin-bottom:0.5rem;">Cambridge G8 科学 40 分钟考场全真模拟卷</h2>
          <p style="color:var(--text-muted); max-width:640px; margin:0 auto 1.5rem; font-size:0.95rem; line-height:1.6;">
            本试卷严格遵循官方 Checkpoint / IGCSE 考卷架构，一键智能组卷：<br>
            <strong>第一部分：精选 15 道客观单选题 [15 分]</strong>（覆盖三大考纲模块）<br>
            <strong>第二部分：精选 3 道结构化笔试大题 [15 分]</strong>（物质运输、肾脏超滤、血糖负反馈各 1 大题）<br>
            全卷满分 <strong>30 分</strong>，标准考场倒计时 <strong>40 分钟</strong>。交卷后自动核分并输出三维能力雷达诊断！
          </p>

          <button class="mock-start-btn" onclick="startMockExam()">
            🚀 随机智能组卷并开始全真模考
          </button>
        </div>

        <!-- Active Mock Screen -->
        <div id="mock-active-screen" style="display:none;">
          <div class="mock-timer-bar">
            <div>
              <span class="badge-pill pill-red">EXAM IN PROGRESS</span>
              <strong style="margin-left:0.5rem;">Cambridge G8 Science Mock Exam</strong>
            </div>
            <div class="mock-timer-digits">
              <span>⏳</span>
              <span id="mock-timer-val">40:00</span>
            </div>
          </div>

          <div style="margin-bottom:2rem;">
            <h3 style="font-size:1.15rem; font-weight:800; border-bottom:2px solid rgba(255,255,255,0.1); padding-bottom:0.5rem; margin-bottom:1rem; color:#93c5fd;">
              SECTION A: Objective Multiple Choice [15 Marks] (单项选择题，每题1分)
            </h3>
            <div id="mock-secA-container">
              <!-- 15 random MCQs inserted here -->
            </div>
          </div>

          <div style="margin-bottom:2rem;">
            <h3 style="font-size:1.15rem; font-weight:800; border-bottom:2px solid rgba(255,255,255,0.1); padding-bottom:0.5rem; margin-bottom:1rem; color:#c4b5fd;">
              SECTION B: Structured Theory Questions [15 Marks] (结构化简答大题，共15分)
            </h3>
            <div id="mock-secB-container">
              <!-- 3 random Theory questions inserted here -->
            </div>
          </div>

          <div style="text-align:center; padding:1.5rem 0;">
            <button class="btn-next" style="padding:0.9rem 2.5rem; font-size:1.05rem;" onclick="submitMockExam()">
              📤 提交模拟试卷并核分诊断
            </button>
          </div>
        </div>

        <!-- Mock Results Screen -->
        <div id="mock-result-screen" style="display:none;">
          <div class="completion-card">
            <div style="font-size:3.5rem; margin-bottom:0.5rem;" id="mock-res-icon">🎯</div>
            <div class="cert-badge cert-a-star" id="mock-res-badge">🌟 A* Master 神级学霸</div>
            <h2 style="font-size:1.6rem; font-weight:800; margin-bottom:0.5rem;">模拟考成绩单与能力弱项诊断</h2>
            <p style="color:var(--text-muted); font-size:0.95rem; max-width:600px; margin:0 auto 1.5rem;" id="mock-res-desc">
              你的全真模拟考成绩已生成！对照下方三维能力雷达，针对弱项模块进行强化复习。
            </p>

            <div style="display:flex; justify-content:center; gap:2rem; margin-bottom:2rem; font-family:var(--font-mono);">
              <div>
                <div style="color:var(--text-muted); font-size:0.8rem;">总分 (Total Score)</div>
                <div style="font-size:1.6rem; font-weight:800; color:var(--accent);" id="mock-res-score">28 / 30</div>
              </div>
              <div>
                <div style="color:var(--text-muted); font-size:0.8rem;">得分率 (Percentage)</div>
                <div style="font-size:1.6rem; font-weight:800; color:var(--success);" id="mock-res-pct">93%</div>
              </div>
              <div>
                <div style="color:var(--text-muted); font-size:0.8rem;">实考用时 (Time)</div>
                <div style="font-size:1.6rem; font-weight:800; color:#93c5fd;" id="mock-res-time">24:18</div>
              </div>
            </div>

            <!-- Radar Diagnosis Bars -->
            <div class="diag-radar">
              <div class="diag-card">
                <div style="display:flex; justify-content:space-between; font-size:0.9rem;">
                  <strong>🌿 物质跨膜运输能力</strong>
                  <span id="mock-diag-t1-pct">90%</span>
                </div>
                <div class="diag-bar-track">
                  <div class="diag-bar-fill" id="mock-diag-t1-bar" style="width:90%; background:var(--primary);"></div>
                </div>
              </div>

              <div class="diag-card">
                <div style="display:flex; justify-content:space-between; font-size:0.9rem;">
                  <strong>🩺 泌尿与排泄生理能力</strong>
                  <span id="mock-diag-t2-pct">85%</span>
                </div>
                <div class="diag-bar-track">
                  <div class="diag-bar-fill" id="mock-diag-t2-bar" style="width:85%; background:var(--success);"></div>
                </div>
              </div>

              <div class="diag-card">
                <div style="display:flex; justify-content:space-between; font-size:0.9rem;">
                  <strong>🔄 血糖负反馈调节能力</strong>
                  <span id="mock-diag-t3-pct">95%</span>
                </div>
                <div class="diag-bar-track">
                  <div class="diag-bar-fill" id="mock-diag-t3-bar" style="width:95%; background:var(--purple);"></div>
                </div>
              </div>
            </div>

            <div style="display:flex; justify-content:center; gap:1rem; margin-top:2rem; flex-wrap:wrap;">
              <button class="btn-action" style="padding:0.6rem 1.5rem; font-size:0.9rem;" onclick="copyMockReport()">
                📋 一键复制全真考卷战报
              </button>
              <button class="btn-next" style="margin:0;" onclick="restartMockExam()">
                🔄 重新组卷模拟
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <script>
    // ==================== 1. DATASETS INJECTION ====================
    const RUSH_QUESTIONS = {obj_json};
    const THEORY_QUESTIONS = {wt_json};
    window.RUSH_QUESTIONS = RUSH_QUESTIONS;
    window.THEORY_QUESTIONS = THEORY_QUESTIONS;

    // ==================== 2. AUDIO SYNTHESIZER ====================
    let audioCtx = null;
    let isSoundMuted = false;

    function getAudioContext() {{
      if (!audioCtx) {{
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (AudioContextClass) audioCtx = new AudioContextClass();
      }}
      if (audioCtx && audioCtx.state === 'suspended') audioCtx.resume();
      return audioCtx;
    }}

    function playTone(freq, type = 'sine', duration = 0.15, gainVal = 0.2) {{
      if (isSoundMuted) return;
      try {{
        const ctx = getAudioContext();
        if (!ctx) return;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(gainVal, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      }} catch(e) {{}}
    }}

    function playSoundCorrect() {{
      if (isSoundMuted) return;
      setTimeout(() => playTone(523.25, 'sine', 0.2, 0.2), 0);
      setTimeout(() => playTone(659.25, 'sine', 0.25, 0.25), 80);
      setTimeout(() => playTone(783.99, 'sine', 0.35, 0.3), 160);
    }}

    function playSoundWrong() {{
      if (isSoundMuted) return;
      try {{
        const ctx = getAudioContext();
        if (!ctx) return;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(140, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(60, ctx.currentTime + 0.3);
        gain.gain.setValueAtTime(0.25, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.3);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.3);
      }} catch(e) {{}}
    }}

    function playSoundStreak() {{
      if (isSoundMuted) return;
      setTimeout(() => playTone(587.33, 'triangle', 0.12, 0.2), 0);
      setTimeout(() => playTone(739.99, 'triangle', 0.15, 0.25), 80);
      setTimeout(() => playTone(880.00, 'triangle', 0.3, 0.3), 160);
    }}

    function toggleGlobalSound() {{
      isSoundMuted = !isSoundMuted;
      const btn = document.getElementById('btn-sound');
      const txt = document.getElementById('txt-sound');
      if (isSoundMuted) {{
        btn.classList.remove('active');
        txt.textContent = '静音';
      }} else {{
        btn.classList.add('active');
        txt.textContent = '声音';
        playTone(600, 'sine', 0.1, 0.1);
      }}
    }}

    // ==================== 3. GLOBAL TAB & LANG CONTROLLERS ====================
    let globalLang = 'bilingual'; // 'bilingual' | 'en'

    function toggleGlobalLang() {{
      globalLang = globalLang === 'bilingual' ? 'en' : 'bilingual';
      const btn = document.getElementById('btn-lang');
      const txt = document.getElementById('txt-lang');
      txt.textContent = globalLang === 'bilingual' ? '🇨🇳/🇬🇧 双语' : '🇬🇧 English';
      btn.classList.toggle('active', globalLang === 'en');

      // Update question display
      renderObjectiveQuestion(false);
      renderTheoryCards();
    }}

    function switchMainTab(tabId) {{
      document.querySelectorAll('.nav-tabs .tab-btn').forEach((btn, idx) => {{
        const tabs = ['concepts', 'objective', 'theory', 'mock'];
        btn.classList.toggle('active', tabs[idx] === tabId);
      }});

      document.querySelectorAll('.tab-pane').forEach(pane => {{
        pane.classList.remove('active');
      }});
      const targetPane = document.getElementById('pane-' + tabId);
      if (targetPane) targetPane.classList.add('active');
    }}

    function toggleConcept(headerElem) {{
      const item = headerElem.closest('.concept-item');
      item.classList.toggle('open');
    }}

    // ==================== 4. TAB 2: OBJECTIVE ARENA CONTROLLER ====================
    let activeObjFilter = 'all'; // 'all', 1, 2, 3, 'wrong'
    let filteredQuestions = [...RUSH_QUESTIONS];
    let currentObjIdx = 0;
    let objScore = 0;
    let objStreak = 0;
    let objCorrectCount = 0;
    let objIsAnswered = false;
    let objWrongIds = new Set();
    let objTimerInterval = null;
    let objRemainingSec = 60;
    let objStartTime = Date.now();
    let objTotalTime = 0;

    function initObjectiveArena() {{
      applyObjectiveFilter('all');
    }}

    function filterObjective(type, btn) {{
      document.querySelectorAll('.filter-pills .filter-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      applyObjectiveFilter(type);
    }}

    function applyObjectiveFilter(type) {{
      activeObjFilter = type;
      if (type === 'all') {{
        filteredQuestions = [...RUSH_QUESTIONS];
      }} else if (typeof type === 'number') {{
        filteredQuestions = RUSH_QUESTIONS.filter(q => q.level === type);
      }} else if (type === 'wrong') {{
        filteredQuestions = RUSH_QUESTIONS.filter(q => objWrongIds.has(q.id));
        if (filteredQuestions.length === 0) {{
          alert('太棒了！错题本目前为空，没有做错的题目。');
          filterObjective('all', document.querySelector('.filter-pills .filter-btn'));
          return;
        }}
      }}
      currentObjIdx = 0;
      objScore = 0;
      objStreak = 0;
      objCorrectCount = 0;
      objStartTime = Date.now();
      document.getElementById('obj-score').textContent = objScore;
      document.getElementById('obj-streak').textContent = objStreak;
      document.getElementById('obj-card').style.display = 'block';
      document.getElementById('obj-completion-box').style.display = 'none';
      renderObjectiveQuestion();
    }}

    function renderObjectiveQuestion(resetTimer = true) {{
      if (currentObjIdx >= filteredQuestions.length) {{
        showObjectiveCompletion();
        return;
      }}

      const q = filteredQuestions[currentObjIdx];
      objIsAnswered = false;

      // Meta
      document.getElementById('obj-lvl-badge').textContent = 'Level ' + q.level;
      document.getElementById('obj-topic-badge').textContent = q.topic;
      document.getElementById('obj-counter').textContent = `Q ${{currentObjIdx + 1}} / ${{filteredQuestions.length}}`;

      // Prompts
      document.getElementById('obj-prompt-en').textContent = q.prompt_en;
      const cnElem = document.getElementById('obj-prompt-cn');
      if (globalLang === 'en') {{
        cnElem.style.display = 'none';
      }} else {{
        cnElem.style.display = 'block';
        cnElem.textContent = q.prompt_cn;
      }}

      // Options
      const optBox = document.getElementById('obj-options-box');
      optBox.innerHTML = '';
      q.options.forEach(opt => {{
        const btn = document.createElement('button');
        btn.className = 'opt-btn';
        btn.dataset.letter = opt.letter;
        btn.onclick = () => selectObjectiveAnswer(opt.letter);

        const cnDisplay = (globalLang === 'en' || !opt.text_cn) ? '' : `<div class="opt-text-cn">${{opt.text_cn}}</div>`;
        btn.innerHTML = `
          <div class="opt-letter">${{opt.letter}}</div>
          <div class="opt-text">
            <div class="opt-text-en">${{opt.text_en}}</div>
            ${{cnDisplay}}
          </div>
        `;
        optBox.appendChild(btn);
      }});

      // Hide feedback
      document.getElementById('obj-feedback-box').style.display = 'none';
      document.getElementById('btn-obj-next').style.display = 'none';

      // Timer
      if (resetTimer) {{
        startObjectiveTimer();
      }}
    }}

    function startObjectiveTimer() {{
      if (objTimerInterval) clearInterval(objTimerInterval);
      objRemainingSec = 60;
      updateObjectiveTimerUI();

      objTimerInterval = setInterval(() => {{
        objRemainingSec--;
        updateObjectiveTimerUI();
        if (objRemainingSec <= 0) {{
          clearInterval(objTimerInterval);
          handleObjectiveTimeout();
        }}
      }}, 1000);
    }}

    function updateObjectiveTimerUI() {{
      const secElem = document.getElementById('obj-timer-sec');
      secElem.textContent = `${{objRemainingSec}}s`;
      secElem.style.color = objRemainingSec <= 5 ? '#ef4444' : '#f8fafc';
    }}

    function handleObjectiveTimeout() {{
      if (objIsAnswered) return;
      selectObjectiveAnswer(null, true);
    }}

    function selectObjectiveAnswer(letter, isTimeout = false) {{
      if (objIsAnswered) return;
      objIsAnswered = true;
      if (objTimerInterval) clearInterval(objTimerInterval);

      const q = filteredQuestions[currentObjIdx];
      const isCorrect = !isTimeout && (letter === q.correct);

      // Disable buttons and mark classes
      document.querySelectorAll('#obj-options-box .opt-btn').forEach(btn => {{
        btn.disabled = true;
        if (btn.dataset.letter === q.correct) {{
          btn.classList.add('correct');
        }} else if (btn.dataset.letter === letter) {{
          btn.classList.add('wrong');
        }}
      }});

      if (isCorrect) {{
        objCorrectCount++;
        objStreak++;
        const points = 100 + (objRemainingSec * 5) + (objStreak > 1 ? objStreak * 15 : 0);
        objScore += points;
        objWrongIds.delete(q.id);
        if (objStreak >= 3) playSoundStreak(); else playSoundCorrect();
      }} else {{
        objStreak = 0;
        objWrongIds.add(q.id);
        playSoundWrong();
      }}

      document.getElementById('obj-score').textContent = objScore;
      document.getElementById('obj-streak').textContent = objStreak;
      document.getElementById('txt-wrong-count').textContent = objWrongIds.size;

      // Reveal feedback
      const fbBox = document.getElementById('obj-feedback-box');
      fbBox.style.display = 'block';
      const fbTitle = document.getElementById('obj-fb-title');
      if (isCorrect) {{
        fbTitle.textContent = `🎉 回答正确！(+${{100 + objRemainingSec * 5}} pts)`;
        fbTitle.style.color = 'var(--success)';
      }} else if (isTimeout) {{
        fbTitle.textContent = `⏰ 60秒倒计时耗尽！正确答案是: ${{q.correct}}`;
        fbTitle.style.color = 'var(--danger)';
      }} else {{
        fbTitle.textContent = `❌ 回答错误！正确答案是: ${{q.correct}}`;
        fbTitle.style.color = 'var(--danger)';
      }}

      document.getElementById('obj-fb-concept').innerHTML = `
        <strong>💡 核心考点：</strong>${{q.concept_en}}<br>
        <span style="color:#6ee7b7;font-size:0.85rem;">${{q.concept_cn}}</span>
      `;
      document.getElementById('obj-fb-trap').innerHTML = `
        <strong>⚠️ 常见陷阱辨析：</strong>${{q.trap_en}}<br>
        <span style="color:#fcd34d;font-size:0.85rem;">${{q.trap_cn}}</span>
      `;
      document.getElementById('obj-fb-citation').textContent = `出处: ${{q.citation}}`;

      document.getElementById('btn-obj-next').style.display = 'inline-flex';

      // Auto-next if enabled
      const chkAuto = document.getElementById('chk-obj-autonext');
      if (chkAuto && chkAuto.checked && isCorrect) {{
        setTimeout(() => {{
          if (objIsAnswered) nextObjectiveQuestion();
        }}, 1500);
      }}
    }}

    function nextObjectiveQuestion() {{
      currentObjIdx++;
      renderObjectiveQuestion();
    }}

    function showObjectiveCompletion() {{
      if (objTimerInterval) clearInterval(objTimerInterval);
      objTotalTime = Math.max(10, Math.floor((Date.now() - objStartTime) / 1000));
      document.getElementById('obj-card').style.display = 'none';
      const compBox = document.getElementById('obj-completion-box');
      compBox.style.display = 'block';

      const totalQ = filteredQuestions.length;
      const accPct = Math.round((objCorrectCount / totalQ) * 100);

      const mins = Math.floor(objTotalTime / 60);
      const secs = objTotalTime % 60;
      const durationStr = `${{mins < 10 ? '0' : ''}}${{mins}}:${{secs < 10 ? '0' : ''}}${{secs}}`;

      document.getElementById('cert-acc').textContent = `${{accPct}}% (${{objCorrectCount}}/${{totalQ}})`;
      document.getElementById('cert-score').textContent = objScore;
      document.getElementById('cert-time').textContent = durationStr;

      const badgeElem = document.getElementById('cert-badge');
      const descElem = document.getElementById('cert-desc');
      const iconElem = document.getElementById('cert-icon');

      if (accPct >= 90) {{
        badgeElem.className = 'cert-badge cert-a-star';
        badgeElem.textContent = '🌟 A* Master 神级学霸 (Outstanding)';
        descElem.textContent = '太震撼了！正确率高达 90% 以上，三大考纲模块高频陷阱已被完全击穿，下周考试稳操胜券！';
        iconElem.textContent = '👑';
        launchConfetti();
      }} else if (accPct >= 75) {{
        badgeElem.className = 'cert-badge cert-a';
        badgeElem.textContent = '🥇 A Grade 优秀通关 (Excellent)';
        descElem.textContent = '非常出色！成绩远超 60% 及格线，核心机制掌握扎实，建议针对做错的题目稍加复盘！';
        iconElem.textContent = '🏆';
        launchConfetti();
      }} else if (accPct >= 60) {{
        badgeElem.className = 'cert-badge cert-pass';
        badgeElem.textContent = '🥈 Pass 达标及格 (Qualified)';
        descElem.textContent = '顺利达成 60% 课堂及格线！建议对照错题卡片，重点巩固排泄超滤与血糖负反馈细节。';
        iconElem.textContent = '🎯';
        launchConfetti();
      }} else {{
        badgeElem.className = 'cert-badge cert-retry';
        badgeElem.textContent = '💪 Needs Revision 尚未及格 (Below 60%)';
        descElem.textContent = '目前正确率未达到 60% 及格线。不要气馁，建议点击下方错题本针对性逐题消灭薄弱点！';
        iconElem.textContent = '📚';
      }}
    }}

    function restartObjectiveArena() {{
      applyObjectiveFilter(activeObjFilter);
    }}

    function copyObjectiveReport() {{
      const totalQ = filteredQuestions.length;
      const accPct = Math.round((objCorrectCount / totalQ) * 100);
      const text = `🎯 Cambridge G8 科学考前客观题突击战报\n` +
                   `----------------------------------------\n` +
                   `📅 练习模块: ${{activeObjFilter === 'all' ? '全考点 48 题' : 'Level ' + activeObjFilter}}\n` +
                   `📊 答题成绩: ${{objCorrectCount}} / ${{totalQ}} 题正确 (${{accPct}}%)\n` +
                   `🏆 累积积分: ${{objScore}} pts\n` +
                   `🏅 认证评级: ${{accPct >= 60 ? '✅ 达标及格' : '⚠️ 需复练'}}\n` +
                   `🚀 冲刺平台: https://sky.igcse.xyz/g8_exam_rush.html`;
      navigator.clipboard.writeText(text).then(() => {{
        alert('📋 练习战报已复制到剪贴板！');
      }}).catch(() => {{
        alert('复制失败，请手动截屏分享。');
      }});
    }}

    // ==================== 5. TAB 3: WRITTEN THEORY ARENA ====================
    let theorySelfScores = {{}};

    function initTheoryArena() {{
      renderTheoryCards();
    }}

    function renderTheoryCards() {{
      const container = document.getElementById('theory-list-container');
      container.innerHTML = '';

      THEORY_QUESTIONS.forEach((q, idx) => {{
        const card = document.createElement('div');
        card.className = 'theory-item';
        card.id = `theory-card-${{q.id}}`;

        const savedDraft = localStorage.getItem(`draft_${{q.id}}`) || '';
        const savedScore = theorySelfScores[q.id] !== undefined ? theorySelfScores[q.id] : null;

        const cnDisplay = (globalLang === 'en') ? 'display:none;' : '';

        // Generate score buttons 0..marks
        let scoreBtnsHtml = '';
        for (let s = 0; s <= q.marks; s++) {{
          const isSel = savedScore === s ? 'selected' : '';
          scoreBtnsHtml += `<button class="score-btn ${{isSel}}" onclick="rateTheoryQuestion('${{q.id}}', ${{s}}, ${{q.marks}})">${{s}}分</button>`;
        }}

        // Mark scheme points
        let msPointsHtml = '';
        q.mark_scheme.forEach(pt => {{
          msPointsHtml += `
            <div class="ms-point">
              <strong>Point ${{pt.point}}:</strong> ${{pt.text_en}}<br>
              <span style="color:#6ee7b7;font-size:0.85rem;${{cnDisplay}}">${{pt.text_cn}}</span>
            </div>
          `;
        }});

        // Keywords
        let kwHtml = '';
        q.keywords.forEach(kw => {{
          kwHtml += `<span class="kw-tag">${{kw}}</span>`;
        }});

        card.innerHTML = `
          <div class="theory-header">
            <div class="theory-badges">
              <span class="badge-pill pill-purple">${{q.task_code}}</span>
              <span class="badge-mark">[${{q.marks}} marks]</span>
              <span class="badge-command">${{q.command_word}}</span>
              <span class="badge-pill pill-blue">${{q.topic}}</span>
            </div>
            <div style="font-size:0.82rem; color:var(--text-muted); font-family:var(--font-mono);">
              Theory Q${{idx + 1}} / ${{THEORY_QUESTIONS.length}}
            </div>
          </div>

          <div class="theory-prompt-en">${{q.prompt_en}}</div>
          <div class="theory-prompt-cn" style="${{cnDisplay}}">${{q.prompt_cn}}</div>

          <textarea class="theory-textarea" id="textarea-${{q.id}}" 
                    placeholder="Type your exam response here in English or Chinese... 键入你的英文或中文作答草稿..."
                    oninput="saveTheoryDraft('${{q.id}}', this.value)">${{savedDraft}}</textarea>

          <div class="theory-footer">
            <button class="btn-reveal" onclick="toggleTheoryMarkScheme('${{q.id}}')">
              🔍 核对官方采分点 (Reveal Mark Scheme & Keywords)
            </button>
            <div style="font-size:0.85rem; color:var(--text-muted);">
              自评得分: <strong id="lbl-score-${{q.id}}" style="color:var(--purple); font-size:1.05rem;">${{savedScore !== null ? savedScore : '-'}}</strong> / ${{q.marks}} 分
            </div>
          </div>

          <div class="mark-scheme-box" id="ms-${{q.id}}">
            <div style="font-weight:800; color:#c4b5fd; margin-bottom:0.6rem; display:flex; align-items:center; gap:0.4rem;">
              🎯 剑桥官方标准采分点 (Official Mark Scheme)
            </div>
            ${{msPointsHtml}}

            <div style="font-size:0.82rem; color:var(--text-muted); margin-top:0.75rem;">
              <strong>🔑 必须出现的官方核心采分关键词 (Keywords)：</strong>
            </div>
            <div class="keywords-wrap">
              ${{kwHtml}}
            </div>

            <div style="background:rgba(245, 158, 11, 0.1); border-left:3px solid var(--accent); padding:0.55rem 0.85rem; border-radius:0 6px 6px 0; font-size:0.82rem; color:#fde047; margin:0.75rem 0;">
              <strong>👨‍🏫 考官提示：</strong>${{q.examiner_tips}}
            </div>

            <div class="self-score-bar">
              <span style="font-size:0.85rem; font-weight:700;">对照采分点，给自己评定实际得分：</span>
              ${{scoreBtnsHtml}}
            </div>
          </div>
        `;
        container.appendChild(card);
      }});

      updateTheorySummary();
    }}

    function saveTheoryDraft(qId, val) {{
      localStorage.setItem(`draft_${{qId}}`, val);
    }}

    function toggleTheoryMarkScheme(qId) {{
      const msBox = document.getElementById(`ms-${{qId}}`);
      if (msBox.style.display === 'block') {{
        msBox.style.display = 'none';
      }} else {{
        msBox.style.display = 'block';
        playTone(700, 'sine', 0.1, 0.15);
      }}
    }}

    function rateTheoryQuestion(qId, scoreVal, maxMarks) {{
      theorySelfScores[qId] = scoreVal;
      document.getElementById(`lbl-score-${{qId}}`).textContent = scoreVal;

      // Update button visual
      const parentCard = document.getElementById(`theory-card-${{qId}}`);
      parentCard.querySelectorAll('.score-btn').forEach((btn, idx) => {{
        btn.classList.toggle('selected', idx === scoreVal);
      }});

      playTone(523 + scoreVal * 80, 'sine', 0.12, 0.2);
      updateTheorySummary();
    }}

    function updateTheorySummary() {{
      let total = 0;
      let evaluated = 0;
      THEORY_QUESTIONS.forEach(q => {{
        if (theorySelfScores[q.id] !== undefined) {{
          total += theorySelfScores[q.id];
          evaluated++;
        }}
      }});
      document.getElementById('theory-total-score').textContent = total;
      document.getElementById('theory-evaluated-count').textContent = evaluated;
    }}

    // ==================== 6. TAB 4: MOCK EXAM SIMULATOR ====================
    let mockActive = false;
    let mockTimerInterval = null;
    let mockRemainingSec = 40 * 60; // 40 minutes
    let mockSecAQuestions = [];
    let mockSecBQuestions = [];
    let mockSecAAnswers = {{}};
    let mockSecBScores = {{}};

    function startMockExam() {{
      // Select 15 random MCQs: 5 from L1, 5 from L2, 5 from L3
      const l1Pool = RUSH_QUESTIONS.filter(q => q.level === 1).sort(() => Math.random() - 0.5).slice(0, 5);
      const l2Pool = RUSH_QUESTIONS.filter(q => q.level === 2).sort(() => Math.random() - 0.5).slice(0, 5);
      const l3Pool = RUSH_QUESTIONS.filter(q => q.level === 3).sort(() => Math.random() - 0.5).slice(0, 5);
      mockSecAQuestions = [...l1Pool, ...l2Pool, ...l3Pool];

      // Select 3 Theory questions: 1 Transport, 1 Kidneys, 1 Glucose (Randomized)
      const poolTransport = THEORY_QUESTIONS.filter(q => q.topic.includes('Movement') || q.topic.includes('Cell'));
      const poolKidneys = THEORY_QUESTIONS.filter(q => q.topic.includes('Excretion') || q.topic.includes('Kidney'));
      const poolGlucose = THEORY_QUESTIONS.filter(q => q.topic.includes('Glucose') || q.topic.includes('Endocrine') || q.topic.includes('Nervous'));
      const tTransport = poolTransport[Math.floor(Math.random() * poolTransport.length)];
      const tKidneys = poolKidneys[Math.floor(Math.random() * poolKidneys.length)];
      const tGlucose = poolGlucose[Math.floor(Math.random() * poolGlucose.length)];
      mockSecBQuestions = [tTransport, tKidneys, tGlucose].filter(Boolean);

      mockSecAAnswers = {{}};
      mockSecBScores = {{}};

      // Render Section A
      const secAContainer = document.getElementById('mock-secA-container');
      secAContainer.innerHTML = '';
      mockSecAQuestions.forEach((q, idx) => {{
        const item = document.createElement('div');
        item.className = 'rush-card';
        item.style.marginBottom = '1.25rem';
        item.innerHTML = `
          <div style="font-weight:700; color:#93c5fd; font-size:0.95rem; margin-bottom:0.35rem;">
            Question ${{idx + 1}} [1 mark] &bull; ${{q.topic}}
          </div>
          <div style="font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:0.25rem;">${{q.prompt_en}}</div>
          <div style="font-size:0.88rem; color:var(--text-muted); margin-bottom:1rem;">${{q.prompt_cn}}</div>
          <div class="options-grid">
            ${{q.options.map(opt => `
              <label class="opt-btn" style="cursor:pointer;">
                <input type="radio" name="mock_mcq_${{q.id}}" value="${{opt.letter}}" onchange="selectMockSecA('${{q.id}}', '${{opt.letter}}')" style="margin-top:4px;">
                <div class="opt-text">
                  <div class="opt-text-en"><strong>${{opt.letter}}.</strong> ${{opt.text_en}}</div>
                  <div class="opt-text-cn">${{opt.text_cn}}</div>
                </div>
              </label>
            `).join('')}}
          </div>
        `;
        secAContainer.appendChild(item);
      }});

      // Render Section B
      const secBContainer = document.getElementById('mock-secB-container');
      secBContainer.innerHTML = '';
      mockSecBQuestions.forEach((q, idx) => {{
        const item = document.createElement('div');
        item.className = 'rush-card';
        item.style.marginBottom = '1.5rem';
        item.innerHTML = `
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
            <span class="badge-pill pill-purple">Theory Question ${{idx + 1}}</span>
            <span class="badge-mark">[${{q.marks}} marks]</span>
          </div>
          <div style="font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:0.25rem;">${{q.prompt_en}}</div>
          <div style="font-size:0.88rem; color:var(--text-muted); margin-bottom:0.85rem;">${{q.prompt_cn}}</div>
          <textarea class="theory-textarea" style="min-height:120px;" placeholder="Draft your answer here during exam..."></textarea>
          
          <div class="mark-scheme-box" id="mock-ms-${{q.id}}" style="display:none; margin-top:1rem;">
            <div style="font-weight:800; color:#c4b5fd; margin-bottom:0.5rem;">🎯 官方评分标准 (Mark Scheme):</div>
            ${{q.mark_scheme.map(pt => `<div class="ms-point"><strong>Point ${{pt.point}}:</strong> ${{pt.text_en}}</div>`).join('')}}
            <div class="self-score-bar">
              <span style="font-size:0.85rem; font-weight:700;">自评得分:</span>
              ${{Array.from({{length: q.marks + 1}}, (_, s) => `
                <button class="score-btn" onclick="rateMockSecB('${{q.id}}', ${{s}}, this)">${{s}}分</button>
              `).join('')}}
            </div>
          </div>
        `;
        secBContainer.appendChild(item);
      }});

      // UI Switch
      document.getElementById('mock-start-screen').style.display = 'none';
      document.getElementById('mock-active-screen').style.display = 'block';
      document.getElementById('mock-result-screen').style.display = 'none';

      // Start 40 min timer
      mockRemainingSec = 40 * 60;
      updateMockTimerUI();
      mockTimerInterval = setInterval(() => {{
        mockRemainingSec--;
        updateMockTimerUI();
        if (mockRemainingSec <= 0) {{
          clearInterval(mockTimerInterval);
          alert('⏰ 40 分钟考场时间已到，系统自动交卷！');
          submitMockExam();
        }}
      }}, 1000);

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function updateMockTimerUI() {{
      const mins = Math.floor(mockRemainingSec / 60);
      const secs = mockRemainingSec % 60;
      document.getElementById('mock-timer-val').textContent = 
        `${{mins < 10 ? '0' : ''}}${{mins}}:${{secs < 10 ? '0' : ''}}${{secs}}`;
    }}

    function selectMockSecA(qId, letter) {{
      mockSecAAnswers[qId] = letter;
    }}

    function rateMockSecB(qId, scoreVal, btn) {{
      mockSecBScores[qId] = scoreVal;
      btn.parentElement.querySelectorAll('.score-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      playTone(550 + scoreVal * 80, 'sine', 0.1, 0.2);
    }}

    function submitMockExam() {{
      if (mockTimerInterval) clearInterval(mockTimerInterval);

      // Score Section A
      let secAScore = 0;
      let secACorrect = 0;
      mockSecAQuestions.forEach(q => {{
        if (mockSecAAnswers[q.id] === q.correct) {{
          secAScore += 1;
          secACorrect++;
        }}
      }});

      // Reveal Mark Scheme for Section B so student can score
      mockSecBQuestions.forEach(q => {{
        const msBox = document.getElementById(`mock-ms-${{q.id}}`);
        if (msBox) msBox.style.display = 'block';
      }});

      // 滚动至 Section B 引导学生对照采分点打分
      const evaluatedCount = Object.keys(mockSecBScores).length;
      if (evaluatedCount < mockSecBQuestions.length) {{
        alert('📝 请对照展开的官方标准采分点，为 Section B 的 3 道笔试题完成自评打分后再查看总成绩单！');
        document.getElementById('mock-secB-container').scrollIntoView({{ behavior: 'smooth' }});
        return;
      }}

      // Calculate total Section B score
      let secBScore = 0;
      mockSecBQuestions.forEach(q => {{
        secBScore += (mockSecBScores[q.id] || 0);
      }});

      const totalScore = secAScore + secBScore;
      const totalMax = 15 + mockSecBQuestions.reduce((acc, q) => acc + q.marks, 0); // ~30
      const pct = Math.round((totalScore / totalMax) * 100);

      const elapsed = (40 * 60) - mockRemainingSec;
      const mins = Math.floor(elapsed / 60);
      const secs = elapsed % 60;
      const timeStr = `${{mins < 10 ? '0' : ''}}${{mins}}:${{secs < 10 ? '0' : ''}}${{secs}}`;

      document.getElementById('mock-active-screen').style.display = 'none';
      document.getElementById('mock-result-screen').style.display = 'block';

      document.getElementById('mock-res-score').textContent = `${{totalScore}} / ${{totalMax}}`;
      document.getElementById('mock-res-pct').textContent = `${{pct}}%`;
      document.getElementById('mock-res-time').textContent = timeStr;

      const badgeElem = document.getElementById('mock-res-badge');
      if (pct >= 90) {{
        badgeElem.className = 'cert-badge cert-a-star';
        badgeElem.textContent = '🌟 A* Master 神级学霸 (Outstanding)';
        launchConfetti();
      }} else if (pct >= 75) {{
        badgeElem.className = 'cert-badge cert-a';
        badgeElem.textContent = '🥇 A Grade 优秀通关 (Excellent)';
        launchConfetti();
      }} else if (pct >= 60) {{
        badgeElem.className = 'cert-badge cert-pass';
        badgeElem.textContent = '🥈 Pass 达标及格 (Qualified)';
        launchConfetti();
      }} else {{
        badgeElem.className = 'cert-badge cert-retry';
        badgeElem.textContent = '💪 Needs Revision 尚未及格 (Below 60%)';
      }}

      // Compute Real Module Diagnosis Accuracy from Section A
      let l1Correct = 0, l2Correct = 0, l3Correct = 0;
      mockSecAQuestions.forEach(q => {{
        const isCorr = (mockSecAAnswers[q.id] === q.correct);
        if (q.level === 1 && isCorr) l1Correct++;
        if (q.level === 2 && isCorr) l2Correct++;
        if (q.level === 3 && isCorr) l3Correct++;
      }});
      const t1Acc = Math.round((l1Correct / 5) * 100);
      const t2Acc = Math.round((l2Correct / 5) * 100);
      const t3Acc = Math.round((l3Correct / 5) * 100);
      document.getElementById('mock-diag-t1-pct').textContent = `${{t1Acc}}% (${{l1Correct}}/5)`;
      document.getElementById('mock-diag-t1-bar').style.width = `${{t1Acc}}%`;
      document.getElementById('mock-diag-t2-pct').textContent = `${{t2Acc}}% (${{l2Correct}}/5)`;
      document.getElementById('mock-diag-t2-bar').style.width = `${{t2Acc}}%`;
      document.getElementById('mock-diag-t3-pct').textContent = `${{t3Acc}}% (${{l3Correct}}/5)`;
      document.getElementById('mock-diag-t3-bar').style.width = `${{t3Acc}}%`;
    }}

    function restartMockExam() {{
      document.getElementById('mock-start-screen').style.display = 'block';
      document.getElementById('mock-active-screen').style.display = 'none';
      document.getElementById('mock-result-screen').style.display = 'none';
    }}

    function copyMockReport() {{
      const score = document.getElementById('mock-res-score').textContent;
      const pct = document.getElementById('mock-res-pct').textContent;
      const time = document.getElementById('mock-res-time').textContent;
      const badge = document.getElementById('mock-res-badge').textContent;

      const text = `🎯 Cambridge G8 科学 40 分钟全真模拟卷战报\n` +
                   `----------------------------------------\n` +
                   `🏅 认证评级: ${{badge}}\n` +
                   `📊 模拟总分: ${{score}} (${{pct}})\n` +
                   `⏱️ 实考用时: ${{time}}\n` +
                   `🌿 物质跨膜运输能力: ${{document.getElementById('mock-diag-t1-pct').textContent}}\n` +
                   `🩺 泌尿与排泄生理能力: ${{document.getElementById('mock-diag-t2-pct').textContent}}\n` +
                   `🔄 血糖负反馈稳态能力: ${{document.getElementById('mock-diag-t3-pct').textContent}}\n` +
                   `🚀 冲刺平台: https://sky.igcse.xyz/g8_exam_rush.html`;
      navigator.clipboard.writeText(text).then(() => {{
        alert('📋 模考战报已复制到剪贴板！');
      }}).catch(() => {{
        alert('复制失败，请截图分享。');
      }});
    }}

    // ==================== 7. CANVAS CONFETTI ====================
    function launchConfetti() {{
      const canvas = document.getElementById('confetti-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#f59e0b', '#3b82f6', '#10b981', '#ef4444', '#8b5cf6', '#ec4899'];
      for (let i = 0; i < 90; i++) {{
        particles.push({{
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height * 0.4,
          r: Math.random() * 6 + 3,
          d: Math.random() * 50,
          color: colors[Math.floor(Math.random() * colors.length)],
          vx: Math.random() * 4 - 2,
          vy: Math.random() * 3 + 2
        }});
      }}

      let frames = 0;
      function render() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {{
          p.x += p.vx;
          p.y += p.vy;
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.fill();
        }});
        frames++;
        if (frames < 120) requestAnimationFrame(render);
        else ctx.clearRect(0, 0, canvas.width, canvas.height);
      }}
      render();
    }}

    // ==================== 8. BOOTSTRAP ====================
    window.addEventListener('DOMContentLoaded', () => {{
      initObjectiveArena();
      initTheoryArena();
    }});
  </script>
</body>
</html>
'''
    return html_content

if __name__ == "__main__":
    content = build_page()
    with open("g8_exam_rush.html", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated g8_exam_rush.html ({len(content)} bytes)")
