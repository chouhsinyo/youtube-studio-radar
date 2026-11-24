# YouTube Studio Radar — 高品質影片製作框架每週追蹤

> 定期追蹤 GitHub 上最高品質 YouTube 影片製作的四大技術路線：動態視覺品質天花板、Agentic 全流程工作室、影視／電視台級後期上限、Google Flow / GenMedia 生成式影音引擎。
> 最後自動更新：`2026-11-24 15:23 UTC`（每週一自動透過 GitHub Actions 同步最新 Stars、Release 與提交動態）

## 一、動態視覺品質天花板（Video-as-Code 渲染引擎）

*取代靜態圖卡與基礎淡入淡出，達到 Vox／紀錄片等級的動態時間軸、物理緩動、資料視覺化與高質感字幕。*

| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [**remotion-dev/remotion**](https://github.com/remotion-dev/remotion) | React/TS 逐幀渲染核心 | 75,384 (`+2`) | [`v4.0.546`](https://github.com/remotion-dev/remotion/releases/tag/v4.0.546) | 2026-11-24 | Custom | 生態最完整、Studio 即時預覽，直接銜接 Youtube_Remotion<br><sub>最新提交 `0a8246f`：Merge pull request #13605 from remotion-dev/codex/preserve-sequence-duration</sub> |
| [**remotion-dev/skills**](https://github.com/remotion-dev/skills) | Remotion 官方 Agent Skills | 7,930 | - | 2026-11-23 | - | 官方維護的 AI 編寫 Remotion 最佳實踐與排版規範<br><sub>最新提交 `89c8afa`：Update template</sub> |
| [**Remocn/remocn**](https://github.com/Remocn/remocn) | shadcn 風格動效元件庫 | 1,855 | - | 2026-11-24 | MIT | 開箱即用的廣播級轉場、標題卡、背景與圖表動畫元件<br><sub>最新提交 `4cd6d12`：docs: Remotion logo animation and kinetic typography guides (#366)</sub> |
| [**haidrrrry/claude-remotion-skill**](https://github.com/haidrrrry/claude-remotion-skill) | 去 AI 廉價感動效設計規範 | 1,303 | - | 2026-08-12 | MIT | 規範 spring 緩動、錯落節奏、膠片顆粒與視覺審查規則<br><sub>最新提交 `1dcbe5e`：Show the Focus Cat example on the repo page</sub> |
| [**motion-canvas/motion-canvas**](https://github.com/motion-canvas/motion-canvas) | TS Generator 向量動畫引擎 | 20,199 | [`v3.17.2`](https://github.com/motion-canvas/motion-canvas/releases/tag/v3.17.2) | 2026-07-02 | MIT | 適合流程圖、技術解說與 3Blue1Brown 風格補間動畫<br><sub>最新提交 `7b91435`：refactor(docs): update domain (#1231)</sub> |
| [**midrender/revideo**](https://github.com/midrender/revideo) | MIT 授權伺服器渲染引擎 | 4,234 | [`v0.11.0`](https://github.com/midrender/revideo/releases) | 2026-07-15 | MIT | Motion Canvas 分支，無商業授權門檻、適合雲端大量渲染<br><sub>最新提交 `b5de67a`：docs: add RELEASING.md (#397)</sub> |
| [**ManimCommunity/manim**](https://github.com/ManimCommunity/manim) | 數學與資料圖表動畫引擎 | 42,872 | [`v0.22.1`](https://github.com/ManimCommunity/manim/releases/tag/v0.22.1) | 2026-11-23 | MIT | 高度精準的幾何、統計與模型演繹片段<br><sub>最新提交 `37056b0`：Remove import cycles between manim's modules, and test that none come back (#5156)</sub> |

## 二、Agentic 全流程影片工作室框架與 Skills

*將腳本、分鏡、查核、配音、渲染與品質審查整合成可重複的 AI Agent 工作室流程。*

| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [**OpenMontageInc/OpenMontage**](https://github.com/OpenMontageInc/OpenMontage) | 開源 Agentic 影片工作室系統 | 82,982 | - | 2026-11-16 | AGPL-3.0 | 將多條管線與渲染後端（含 Remotion）整合進 AI 編排工作室<br><sub>最新提交 `2e003e6`：docs: add updated OpenMontage Instagram link</sub> |
| [**digitalsamba/claude-code-video-toolkit**](https://github.com/digitalsamba/claude-code-video-toolkit) | Agent 影片工具箱與 MCP | 2,745 | [`v0.30.0`](https://github.com/digitalsamba/claude-code-video-toolkit/releases/tag/v0.30.0) | 2026-11-23 | MIT | 整合 Remotion、Manim、FFmpeg 與生成式模型的完整工具集<br><sub>最新提交 `b3437fc`：Merge pull request #260 from digitalsamba/feat/manim</sub> |
| [**ersinkoc/AI-Video-Factory**](https://github.com/ersinkoc/AI-Video-Factory) | 多語長片與 Shorts 工廠 | 677 | [`v0.6.15`](https://github.com/ersinkoc/AI-Video-Factory/releases/tag/v0.6.15) | 2026-11-24 | MIT | 多 Agent 分工產出長片、章節、字幕與直式 Shorts 並交 Remotion 渲染<br><sub>最新提交 `9417e48`：Release v0.6.15</sub> |
| [**AgriciDaniel/claude-youtube**](https://github.com/AgriciDaniel/claude-youtube) | YouTube 成長與留存 Skill 包 | 868 | - | 2026-04-10 | MIT | 涵蓋 Hook、留存腳本、SEO、縮圖簡報與頻道審計流程<br><sub>最新提交 `84c3fa6`：Add author section, community links, and backlinks</sub> |
| [**linyqh/NarratoAI**](https://github.com/linyqh/NarratoAI) | LLM 看片解說與剪輯工具 | 11,921 | [`v0.8.7`](https://github.com/linyqh/NarratoAI/releases/tag/v0.8.7) | 2026-10-24 | MIT | 參考其 Gemini 視覺理解結合自動切點剪輯的模式<br><sub>最新提交 `29a11b6`：更新文档</sub> |
| [**harry0703/MoneyPrinterTurbo**](https://github.com/harry0703/MoneyPrinterTurbo) | 自動化量產對照基準 | 145,401 (`+1`) | [`v1.3.11`](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.11) | 2026-11-24 | MIT | 觀察主流全自動短片管線的配音、字幕與素材整合演進<br><sub>最新提交 `dabfd3f`：fix(material): use Wan 3.0 by default (#1842)</sub> |

## 三、影視／電視台級上限（時間軸交換與專業 NLE 自動化）

*由程式自動完成 80% 粗剪、對軌、上標記，再無縫匯入 DaVinci Resolve 完成電影級調色與混音。*

| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [**AcademySoftwareFoundation/OpenTimelineIO**](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) | 影視工業標準多軌時間軸格式 | 2,115 | [`v0.18.1`](https://github.com/AcademySoftwareFoundation/OpenTimelineIO/releases) | 2026-11-23 | Apache-2.0 | DaVinci Resolve 原生匯入 .otio，銜接 Python 粗剪與專業後期<br><sub>最新提交 `f38b2cb`：Fix the version bump script to update the version headers (#2096)</sub> |
| [**samuelgursky/davinci-resolve-mcp**](https://github.com/samuelgursky/davinci-resolve-mcp) | DaVinci Resolve Studio MCP | 4,341 | [`v5.4.3`](https://github.com/samuelgursky/davinci-resolve-mcp/releases/tag/v5.4.3) | 2026-11-24 | MIT | 高星數 Resolve MCP 伺服器，讓 AI 直接操控剪輯與調色時間軸<br><sub>最新提交 `79d68de`：chore(release): bump version to 5.4.3</sub> |
| [**barckley75/resolve-claude-mcp**](https://github.com/barckley75/resolve-claude-mcp) | Resolve × Claude MCP | 401 | - | 2026-05-14 | MIT | 針對 Claude 流程最佳化的 Resolve 控制橋接<br><sub>最新提交 `9398758`：Add LICENSE; rename display name to Resolve Claude MCP</sub> |
| [**flamexnreal/davinci-resolve-ai-bridge-mcp**](https://github.com/flamexnreal/davinci-resolve-ai-bridge-mcp) | Resolve Free/Studio MCP | 66 | [`v1.14.4`](https://github.com/flamexnreal/davinci-resolve-ai-bridge-mcp/releases/tag/v1.14.4) | 2026-11-12 | MIT | 同時支援 DaVinci Resolve 免費版與 Studio 的 AI 橋接<br><sub>最新提交 `f64ccad`：docs: record Resolve Free 21.2 MCP smoke check (#11)</sub> |
| [**WheheoHu/pybmd**](https://github.com/WheheoHu/pybmd) | Resolve Python API 封裝 | 37 | [`v2026.5.0`](https://github.com/WheheoHu/pybmd/releases/tag/v2026.5.0) | 2026-11-08 | LGPL-3.0 | 現代化 Python 介面，方便將 Youtube_Maker 腳本直接連進 Resolve<br><sub>最新提交 `0d6a7a1`：Add DaVinci Resolve 21.2 API support (2026.5.0)</sub> |

## 四、Google Flow / GenMedia 生成式影音引擎與 MCP

*串接 Google Flow、Gemini Omni、Veo 3.1、Nano Banana 與 Lyria，建立可控、可快取、合規的 AI 影片／配樂素材管線。*

| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [**GoogleCloudPlatform/genmedia-creative-studio**](https://github.com/GoogleCloudPlatform/genmedia-creative-studio) | Google Cloud 官方 GenMedia 工作室與 MCP | 1,238 | [`v3.25.0`](https://github.com/GoogleCloudPlatform/genmedia-creative-studio/releases/tag/v3.25.0) | 2026-11-13 | Apache-2.0 | 內建 Veo 3.1、Gemini Omni、Nano Banana、Lyria 與 AVTool Go MCP 伺服器及官方 Agent Skills<br><sub>最新提交 `8e8c66e`：fix(deps): update all non-major dependencies (#2180)</sub> |
| [**google-gemini/gemini-skills**](https://github.com/google-gemini/gemini-skills) | Gemini API 官方 Agent Skills | 4,691 | - | 2026-11-19 | Apache-2.0 | 含 gemini-omni-flash-api、gemini-api-dev 與 gemini-api-cli，對齊最新 Interactions API 影片生成規範<br><sub>最新提交 `c4d0c62`：Merge pull request #101 from google-gemini/add-neon</sub> |
| [**googleapis/python-genai**](https://github.com/googleapis/python-genai) | Google Gen AI 官方 Python SDK | 4,087 | [`v3.6.1`](https://github.com/googleapis/python-genai/releases/tag/v3.6.1) | 2026-11-24 | Apache-2.0 | 以程式呼叫 gemini-omni-1.2-flash 影片生成、多輪對話編修與參考圖角色鎖定<br><sub>最新提交 `10f479b`：fix: stop deep-copying MCP session tools in async generate_content</sub> |
| [**ffroliva/gflow-cli**](https://github.com/ffroliva/gflow-cli) | Google Flow 社群 CLI 與 MCP（非官方） | 586 | [`v0.106.0`](https://github.com/ffroliva/gflow-cli/releases/tag/v0.106.0) | 2026-11-24 | MIT | 追蹤社群透過本機瀏覽器工作階段銜接 Flow 點數的動向（正式管線建議採官方 API 或手動入庫）<br><sub>最新提交 `4901166`：Merge pull request #1460 from LeonJoeeee/feature/thinking-level-and-4k-video</sub> |
| [**stephengpope/remotion-media-mcp**](https://github.com/stephengpope/remotion-media-mcp) | Remotion AI 媒體生成 MCP | 34 | - | 2026-02-25 | - | 參考其將生成影音直接落盤至 public/ 供 Remotion staticFile() 載入的整合模式<br><sub>最新提交 `9e153f4`：1.2.2</sub> |

## 新發現候選（每週自動雷達掃描）

### Remotion / Video-as-Code 生態新星

- [**Vincentwei1021/video-shotcraft**](https://github.com/Vincentwei1021/video-shotcraft)（★ 22,403｜更新 `2026-11-24`）：AI video skill for Claude Code & Codex — cinematic, editable product promos with Remotion: 124 shot
- [**steveseguin/vdo.ninja**](https://github.com/steveseguin/vdo.ninja)（★ 4,173｜更新 `2026-11-23`）：VDO.Ninja is a powerful tool that lets you bring remote video feeds into OBS or other studio softwar
- [**Vincentwei1021/anything2explainer**](https://github.com/Vincentwei1021/anything2explainer)（★ 3,610｜更新 `2026-11-21`）：Topic in, narrated explainer video out. A Claude Code / Codex skill that turns any topic into a blac
- [**0xsline/OpenChatCut**](https://github.com/0xsline/OpenChatCut)（★ 3,305｜更新 `2026-11-12`）：Open-source, local-first conversational AI video editor with a professional multi-track timeline, Ag

### Agentic 影片製作工作室新星

- 本週無額外新候選或受 API 速率限制。

### DaVinci Resolve / OTIO 自動化新星

- [**tmoroney/auto-subs**](https://github.com/tmoroney/auto-subs)（★ 4,608｜更新 `2026-11-22`）：On-device subtitle generation that connects directly to DaVinci Resolve, Premiere, and After Effects
- [**zelikos/davincibox**](https://github.com/zelikos/davincibox)（★ 1,046｜更新 `2026-11-09`）：Container for DaVinci Resolve installation and runtime dependencies on Linux. Mirrored to https://co
- [**alexandremendoncaalvaro/CorridorKey-Runtime**](https://github.com/alexandremendoncaalvaro/CorridorKey-Runtime)（★ 789｜更新 `2026-08-05`）：Native AI keying runtime and OFX plugin for DaVinci Resolve, built in collaboration with Corridor Di
- [**appariciojunior/video-editor-skills**](https://github.com/appariciojunior/video-editor-skills)（★ 484｜更新 `2026-10-23`）：Skills that teach Claude Code to be a first-pass video editor in DaVinci Resolve: transcript cuts, v

### Google Flow / Veo / GenMedia 生態新星

- [**maanimeisam/Google-Flow-Helper**](https://github.com/maanimeisam/Google-Flow-Helper)（★ 58｜更新 `2026-09-25`）：Unlocks Google Flow limitations by patching API responses based on remote specs.
- [**miyakejima/google-flow-mcp**](https://github.com/miyakejima/google-flow-mcp)（★ 28｜更新 `2026-10-31`）：Generate and download Google Flow videos and images from Codex, Antigravity, and any MCP agent. Live

## 與本機 `Youtube_Maker` 框架的銜接建議

1. **動態視覺品質天花板**：使用 `python shared/production/pipeline.py export-remotion videos/<project>` 匯出時間軸 JSON，交給 `Youtube_Remotion/` 進行高質感 React/TS 動畫渲染。
2. **影視／電視台級上限**：使用 `python shared/production/pipeline.py export-otio videos/<project>` 匯出 `.otio` 時間軸，一鍵匯入 DaVinci Resolve（免費版／Studio）進行電影級調色與 Fairlight 混音。
3. **Google Flow / GenMedia 生成素材管線**：先產配音定秒數，再以 `python shared/production/pipeline.py plan-flow videos/<project>` 產出 `assets_manifest.json` 與提示詞任務卡；從 Google Flow UI 下載後執行 `ingest-flow` 自動轉檔 `1080p/30fps`、`ffprobe` 品檢並入庫 `clips/` 與 `Youtube_Remotion/public/`。
4. **官方 `gemini-api` 外掛加速**：使用 `gemini-refs`（Nano Banana 2.1 風格參考圖）、`gemini-bgm`（Lyria 3.5 真實樂器紀錄片配樂）、`gemini-cutlist`（Gemini 4 直讀 YouTube 抓切點 JSON）、`gemini-qa`（圖卡排版視覺審查）與 `gemini-video`（Omni 1.2 選用補鏡），所有指令皆支援 `--dry-run`。
5. **Agentic 全流程**：根目錄已建立 `AGENTS.md`，並對齊 `remotion-dev/skills`、`OpenMontage` 與 `google-gemini/gemini-skills` 最新規範。

---
本檔案由 [`scripts/update_radar.py`](scripts/update_radar.py) 自動產生，請修改 [`watchlist.json`](watchlist.json) 來增減追蹤清單。
