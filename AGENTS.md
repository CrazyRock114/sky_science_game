# IGCSE Science 教学生态与项目矩阵说明 (Project Matrix & Context)

## 📌 项目矩阵全貌 (The Two Interlinked Projects)

用户（CrazyRock）目前拥有并交接了两个紧密联动的国际教育项目，共同构成完整的 **IGCSE Science 智能教学系统矩阵**：

### 1. 主教学系统：`IGCSE_miniMax` (核心平台)
* **本地物理路径**：`/Users/crazyrock/Antigravity/IGCSE_miniMax`
* **代码仓库**：[https://github.com/CrazyRock114/IGCSE_miniMax.git](https://github.com/CrazyRock114/IGCSE_miniMax.git)
* **线上生产地址**：[https://igcse.xyz](https://igcse.xyz)（备用镜像：`https://igcse.coze.site`）
* **定位与规模**：
  * 面向 Cambridge IGCSE 物理 (0625)、化学 (0620)、生物 (0610) 的全套互动双语教学系统。
  * **全量覆盖**：75 节课时、442 道课内测验与独立题库、944 条官方考纲条目（100% 覆盖）、140 个核心公式。
  * **核心能力**：Three.js 3D 人体解剖与 DNA 螺旋、Paper 5/6 虚拟实验与方格纸作图、Driver.js 交互式生物知识动画旅程（双循环、突触传递等）、AI 助教面板（DeepSeek/Qwen 驱动）。
  * **维护状态**：**已正式交接给 AI Agent 统一维护**，且已通过工业级 `systematic-verifier` 9 层全态穷举形式化验证。

### 2. 词汇与练习子系统：`IGCSE_science_vocab` (当前工作区)
* **本地物理路径**：`/Users/crazyrock/Antigravity/IGCSE_science_vocab`
* **代码仓库**：[https://github.com/CrazyRock114/sky_science_game](https://github.com/CrazyRock114/sky_science_game)
* **线上生产地址**：[https://sky.igcse.xyz](https://sky.igcse.xyz)
* **定位与功能**：
  * 专为 Sky G8 IGCSE 生物/科学定制的趣味词汇攻坚与习题工作站。
  * 包含 6 款单词游戏（Spelling Bee、Memory Match、Word Shooter 等）、33 个单元、180 个高频词汇、智能错题本与家长学情报告。
  * 附带 G8 Science 人体生理学 Part 2 深度习题集与知识点动画模块（`knowledge_animations/`）。

---

## 💡 AI Agent 协同与工作要求 (Universal Agent Directives)

1. **项目边界与协同认知**：
   * 当用户在此工作区提出“我们的项目”、“调研外部竞品借鉴到项目中”（如 wedulab 等）、“添加动画/实验功能”时，必须清醒意识到**主项目是 `IGCSE_miniMax` (`igcse.xyz`)**，当前子项目是 `sky.igcse.xyz`。
   * 需综合考量：
     - 微观/词汇练习维度（应用到 `sky.igcse.xyz`）
     - 宏观教学、实验模拟、交互动画维度（深度整合到主系统 `IGCSE_miniMax` / `igcse.xyz`）
2. **跨仓库联动开发**：
   * 若需修改或验证主教学系统功能，Agent 可直接操作并执行 `/Users/crazyrock/Antigravity/IGCSE_miniMax` 下的代码、脚本与测试。
   * 主系统测试命令：`pnpm test`、`pnpm run check:content`、`pnpm exec tsx scripts/verifier/index.ts`。
