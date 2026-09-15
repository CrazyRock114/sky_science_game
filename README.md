# Sky's Science Word Lab 🎮🧪

> Interactive word games for **Sky G8 IGCSE Biology 1v1** class.
> 6 games, 18 lessons, 127 vocabulary words. Helps Sky conquer the P0 spelling weakness.

---

## 🎯 6 Games (模式)

| Tab | 主题 | 学习维度 |
|---|---|---|
| | **Spelling Bee** 拼写闯关 | 看中文 + 释义 + 拼写提示 → 拼出英文 | 拼写 (静态) |
| | **Memory Match** 翻牌配对 | 16 张卡片中英配对 + 计时 | 视觉配对 |
| | **Word Shooter** 飞行单词 | 单词下落，输入拼写击落 + 通关 + 漏词提示 | 拼写 + 反应 (动态) |
| | **Listening** 听音辨词 | TTS 朗读 → 4 选 1 中文 | **听觉** 反射 |
| | **Anagram** 拼图重组 | 看中文 + 乱序字母，点击拼出单词 | 字母结构 |
| | **Speed Round** 极速挑战 | 60s 内尽可能多拼对单词 | **速度** + 抗压 |

---

## 📚 18 Lessons (15 教学单元 + 3 阶段复习单元)

| Lesson | 名称 | 词数 | 说明 |
|---|---|---|---|
| L01 | Balanced Diet & Micronutrients | 11 | 基础营养素与缺乏症 |
| L02 | The Alimentary Canal | 10 | 消化道结构与蠕动 |
| L03 | Accessory Organs & Digestion | 8 | 消化辅助器官与腺体 |
| L04 | Human Teeth & Mechanical Digestion | 11 | 牙齿解剖与物理消化 |
| L05 | Intro to Chemical Digestion & Bile | 6 | 化学消化与胆汁乳化 |
| L06 | Housekeeping / Review | 46 | 复习汇总 (L01~L05 合并) |
| L07 | Digestive Enzymes | 10 | 消化酶催化与底物 |
| L08 | Stomach Acid & Advanced Enzymes | 8 | 胃液酸碱度与酶环境 |
| L09 | Absorption and the Villus | 5 | 小肠绒毛与毛细吸收 |
| L10 | The Circulatory System | 10 | 循环系统与大血管 |
| L11 | Heart Anatomy & Function | 10 | 心脏解剖(心房/心室/腱索/瓣膜) |
| L12 | Housekeeping / Review | 41 | 复习汇总 (L07~L11 合并) |
| L13 | The Cardiac Cycle and Monitoring | 7 | 心动周期与仪器监测 |
| L14 | Exercise and Heart Rate | 8 | 运动耐力与心率呼吸 |
| L15 | Blood Vessels and Pressure | 9 | 血管分级与血压调控 |
| L16 | The Vascular Pathways | 10 | 体循环/肺循环主要动静脉 |
| L17 | Components of Blood | 6 | 血液成分(血浆/白细胞/血小板) |
| L18 | Housekeeping / Final Review | 42 | 总复习汇总 (L13~L17 合并) |

**总计：129 词汇条目，涵盖 15 个独立学习单元与 3 个阶段性复习单元**

---

## 🎮 核心功能

- ✅ **6 种游戏模式**：拼写 / 配对 / 反应 / 听觉 / 重组 / 速度
- ✅ **单元选择器**：顶部下拉切换 18 个单元（含 3 个智能去重阶段复习单元）
- ✅ **全平台优质音色**：排除 Albert 等怪声，优先选择 Google US English / Alex / Daniel 标准自然发音
- ✅ **iOS Safari 兼容**：右上角"开启声音"按钮 + TTS unlock + 自动 voice selection
- ✅ **通关规则** (Word Shooter)：所有词都击落 → 通关；支持别名与英美式拼写输入
- ✅ **动态卡片结算** (Memory Match)：按实际单元词数自适应配对与通关判定
- ✅ **漏词提示** (Word Shooter)：单词落到底部时屏幕中央红色大提示显示拼法
- ✅ **进度持久化**：localStorage 安全容错保存每个游戏最高分
- ✅ **响应式设计**：iPad / 手机 / 桌面自适应高对比度界面
- ✅ **血条可视化** (Word Shooter)：♥/♡ + 数字，1 命时变红警示

---

## 🚀 部署

游戏是 **self-contained 单 HTML 文件**（107 KB），无后端、无依赖。可直接部署到：

- ✅ **Vercel** （推荐 — 免费、自动部署、HTTPS）
- ✅ **GitHub Pages**
- ✅ **Cloudflare Pages**
- ✅ **任何静态服务器**（Nginx / Apache / Caddy / Python http.server）

只需把 `index.html` 部署到根目录即可。

---

## 🛠️ 技术栈

- **HTML + CSS + 原生 JavaScript**（无框架、无构建工具）
- **Web Speech API**（`speechSynthesis` 用于 TTS）
- **localStorage**（高分持久化）
- **响应式 CSS Grid + Flexbox**
- 文件大小：107 KB（自包含）

---

## 🎓 教学背景

为 **Sky（G8 IGCSE Biology 1v1）** 定制：
- **P0 短板**：英文科学词汇拼写（每节课都有）
- **学习风格**：互问互答、快节奏、联系生活、深入理解
- **教材**：5008_IG Science G8_Science_Autumn（教师版 PPT + 学生 PDF）

教师：**石头**（stone / Paul Shi）
项目：EnglishMath（线下 K12 教培辅助）

---

## 📝 License

MIT License - 教学用途