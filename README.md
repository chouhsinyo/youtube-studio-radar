# YouTube Studio Radar — 高品質影片製作框架每週追蹤

> 定期追蹤 GitHub 上最高品質 YouTube 影片製作的三大技術路線：動態視覺品質天花板、Agentic 全流程工作室、影視／電視台級後期上限。
> 最後自動更新：`2026-11-24 14:52 UTC`（每週一自動透過 GitHub Actions 同步最新 Stars、Release 與提交動態）

## 一、動態視覺品質天花板（Video-as-Code 渲染引擎）

*取代靜態圖卡與基礎淡入淡出，達到 Vox／紀錄片等級的動態時間軸、物理緩動、資料視覺化與高質感字幕。*

| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [**remotion-dev/remotion**](https://github.com/remotion-dev/remotion) | React/TS 逐幀渲染核心 | 75,376 | - | 2026-11-24 | Custom | 生態最完整、Studio 即時預覽，直接銜接 Youtube_Remotion |
| [**remotion-dev/skills**](https://github.com/remotion-dev/skills) | Remotion 官方 Agent Skills | 7,928 | - | 2026-11-23 | - | 官方維護的 AI 編寫 Remotion 最佳實踐與排版規範 |
| [**Remocn/remocn**](https://github.com/Remocn/remocn) | shadcn 風格動效元件庫 | 1,855 | - | 2026-11-24 | MIT | 開箱即用的廣播級轉場、標題卡、背景與圖表動畫元件 |
| [**haidrrrry/claude-remotion-skill**](https://github.com/haidrrrry/claude-remotion-skill) | 去 AI 廉價感動效設計規範 | 1,302 | - | 2026-08-12 | MIT | 規範 spring 緩動、錯落節奏、膠片顆粒與視覺審查規則 |
| [**motion-canvas/motion-canvas**](https://github.com/motion-canvas/motion-canvas) | TS Generator 向量動畫引擎 | 20,199 | - | 2026-07-02 | MIT | 適合流程圖、技術解說與 3Blue1Brown 風格補間動畫 |
| [**midrender/revideo**](https://github.com/midrender/revideo) | MIT 授權伺服器渲染引擎 | 4,234 | - | 2026-07-15 | MIT | Motion Canvas 分支，無商業授權門檻、適合雲端大量渲染 |
| [**ManimCommunity/manim**](https://github.com/ManimCommunity/manim) | 數學與資料圖表動畫引擎 | 42,871 | - | 2026-11-23 | MIT | 高度精準的幾何、統計與模型演繹片段 |

## 二、Agentic 全流程影片工作室框架與 Skills

*將腳本、分鏡、查核、配音、渲染與品質審查整合成可重複的 AI Agent 工作室流程。*

| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [**OpenMontageInc/OpenMontage**](https://github.com/OpenMontageInc/OpenMontage) | 開源 Agentic 影片工作室系統 | 82,977 | - | 2026-11-16 | AGPL-3.0 | 將多條管線與渲染後端（含 Remotion）整合進 AI 編排工作室 |
| [**digitalsamba/claude-code-video-toolkit**](https://github.com/digitalsamba/claude-code-video-toolkit) | Agent 影片工具箱與 MCP | 2,744 | - | 2026-11-23 | MIT | 整合 Remotion、Manim、FFmpeg 與生成式模型的完整工具集 |
| [**ersinkoc/AI-Video-Factory**](https://github.com/ersinkoc/AI-Video-Factory) | 多語長片與 Shorts 工廠 | 676 | - | 2026-11-24 | MIT | 多 Agent 分工產出長片、章節、字幕與直式 Shorts 並交 Remotion 渲染 |
| [**AgriciDaniel/claude-youtube**](https://github.com/AgriciDaniel/claude-youtube) | YouTube 成長與留存 Skill 包 | 867 | - | 2026-04-10 | MIT | 涵蓋 Hook、留存腳本、SEO、縮圖簡報與頻道審計流程 |
| [**linyqh/NarratoAI**](https://github.com/linyqh/NarratoAI) | LLM 看片解說與剪輯工具 | 11,921 | - | 2026-10-24 | MIT | 參考其 Gemini 視覺理解結合自動切點剪輯的模式 |
| [**harry0703/MoneyPrinterTurbo**](https://github.com/harry0703/MoneyPrinterTurbo) | 自動化量產對照基準 | 145,396 | - | 2026-11-24 | MIT | 觀察主流全自動短片管線的配音、字幕與素材整合演進 |

## 三、影視／電視台級上限（時間軸交換與專業 NLE 自動化）

*由程式自動完成 80% 粗剪、對軌、上標記，再無縫匯入 DaVinci Resolve 完成電影級調色與混音。*

| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [**AcademySoftwareFoundation/OpenTimelineIO**](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) | 影視工業標準多軌時間軸格式 | 2,115 | - | 2026-11-23 | Apache-2.0 | DaVinci Resolve 原生匯入 .otio，銜接 Python 粗剪與專業後期 |
| [**samuelgursky/davinci-resolve-mcp**](https://github.com/samuelgursky/davinci-resolve-mcp) | DaVinci Resolve Studio MCP | 4,339 | - | 2026-11-24 | MIT | 高星數 Resolve MCP 伺服器，讓 AI 直接操控剪輯與調色時間軸 |
| [**barckley75/resolve-claude-mcp**](https://github.com/barckley75/resolve-claude-mcp) | Resolve × Claude MCP | 401 | - | 2026-05-14 | MIT | 針對 Claude 流程最佳化的 Resolve 控制橋接 |
| [**flamexnreal/davinci-resolve-ai-bridge-mcp**](https://github.com/flamexnreal/davinci-resolve-ai-bridge-mcp) | Resolve Free/Studio MCP | 66 | - | 2026-11-12 | MIT | 同時支援 DaVinci Resolve 免費版與 Studio 的 AI 橋接 |
| [**WheheoHu/pybmd**](https://github.com/WheheoHu/pybmd) | Resolve Python API 封裝 | 37 | - | 2026-11-08 | LGPL-3.0 | 現代化 Python 介面，方便將 Youtube_Maker 腳本直接連進 Resolve |

## 新發現候選（每週自動雷達掃描）

### Remotion / Video-as-Code 生態新星

- [**Vincentwei1021/video-shotcraft**](https://github.com/Vincentwei1021/video-shotcraft)（★ 22,395｜更新 `2026-11-24`）：AI video skill for Claude Code & Codex — cinematic, editable product promos with Remotion: 124 shot
- [**steveseguin/vdo.ninja**](https://github.com/steveseguin/vdo.ninja)（★ 4,173｜更新 `2026-11-23`）：VDO.Ninja is a powerful tool that lets you bring remote video feeds into OBS or other studio softwar
- [**Vincentwei1021/anything2explainer**](https://github.com/Vincentwei1021/anything2explainer)（★ 3,607｜更新 `2026-11-21`）：Topic in, narrated explainer video out. A Claude Code / Codex skill that turns any topic into a blac
- [**0xsline/OpenChatCut**](https://github.com/0xsline/OpenChatCut)（★ 3,305｜更新 `2026-11-12`）：Open-source, local-first conversational AI video editor with a professional multi-track timeline, Ag

### Agentic 影片製作工作室新星

- 本週無額外新候選或受 API 速率限制。

### DaVinci Resolve / OTIO 自動化新星

- [**tmoroney/auto-subs**](https://github.com/tmoroney/auto-subs)（★ 4,608｜更新 `2026-11-22`）：On-device subtitle generation that connects directly to DaVinci Resolve, Premiere, and After Effects
- [**zelikos/davincibox**](https://github.com/zelikos/davincibox)（★ 1,046｜更新 `2026-11-09`）：Container for DaVinci Resolve installation and runtime dependencies on Linux. Mirrored to https://co
- [**alexandremendoncaalvaro/CorridorKey-Runtime**](https://github.com/alexandremendoncaalvaro/CorridorKey-Runtime)（★ 789｜更新 `2026-08-05`）：Native AI keying runtime and OFX plugin for DaVinci Resolve, built in collaboration with Corridor Di
- [**appariciojunior/video-editor-skills**](https://github.com/appariciojunior/video-editor-skills)（★ 484｜更新 `2026-10-23`）：Skills that teach Claude Code to be a first-pass video editor in DaVinci Resolve: transcript cuts, v

## 與本機 `Youtube_Maker` 框架的銜接建議

1. **動態視覺品質天花板**：使用 `python shared/production/pipeline.py export-remotion videos/<project>` 匯出時間軸 JSON，交給 `Youtube_Remotion/` 進行高質感 React/TS 動畫渲染。
2. **影視／電視台級上限**：使用 `python shared/production/pipeline.py export-otio videos/<project>` 匯出 `.otio` 時間軸，一鍵匯入 DaVinci Resolve（免費版／Studio）進行電影級調色與 Fairlight 混音。
3. **Agentic 全流程**：本機已更新 `youtube-studio-pipeline` 與 `remotion-motion-design` Skills，並對齊最新 `remotion-dev/skills` 與 `OpenMontage` 規範。

---
本檔案由 [`scripts/update_radar.py`](scripts/update_radar.py) 自動產生，請修改 [`watchlist.json`](watchlist.json) 來增減追蹤清單。
