#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch latest GitHub metadata, releases, and rising projects for youtube-studio-radar.

Zero third-party dependencies (Python stdlib only). Uses GITHUB_TOKEN when available
(automatically provided inside GitHub Actions) for higher rate limits.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
WATCHLIST = ROOT / "watchlist.json"
STATE_FILE = ROOT / "data" / "state.json"
DIFF_FILE = ROOT / "data" / "latest_diff.md"
UPDATES_FILE = ROOT / "UPDATES.md"
README_FILE = ROOT / "README.md"

API_BASE = "https://api.github.com"


def gh_get(path_or_url: str) -> dict | list | None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token and shutil.which("gh"):
        endpoint = path_or_url.removeprefix(API_BASE)
        try:
            res = subprocess.run(
                ["gh", "api", endpoint],
                capture_output=True,
                text=True,
                timeout=20,
            )
            if res.returncode == 0 and res.stdout.strip():
                return json.loads(res.stdout)
            return None
        except Exception as e:
            print(f"WARN: gh api failed for {endpoint}: {e}", file=sys.stderr)
            return None

    url = path_or_url if path_or_url.startswith("http") else f"{API_BASE}{path_or_url}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "chouhsinyo-youtube-studio-radar",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token.strip()}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        body = e.read().decode("utf-8", "replace")[:300]
        print(f"WARN: HTTP {e.code} on {url}: {body}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"WARN: request failed for {url}: {e}", file=sys.stderr)
        return None


def fetch_repo_snapshot(slug: str, include_details: bool = True) -> dict | None:
    info = gh_get(f"/repos/{slug}")
    if not isinstance(info, dict):
        return None

    release_tag = ""
    release_date = ""
    release_url = ""
    release_name = ""
    if include_details:
        rel = gh_get(f"/repos/{slug}/releases/latest")
        if isinstance(rel, dict) and rel.get("tag_name"):
            release_tag = str(rel["tag_name"])
            release_date = str(rel.get("published_at") or "")[:10]
            release_url = str(rel.get("html_url") or "")
            release_name = str(rel.get("name") or release_tag).strip()
        else:
            tags = gh_get(f"/repos/{slug}/tags?per_page=1")
            if isinstance(tags, list) and tags:
                release_tag = str(tags[0].get("name") or "")
                release_url = f"https://github.com/{info['full_name']}/releases"

    last_commit_sha = ""
    last_commit_msg = ""
    if include_details:
        default_branch = info.get("default_branch", "main")
        commits = gh_get(f"/repos/{slug}/commits?sha={urllib.parse.quote(default_branch)}&per_page=1")
        if isinstance(commits, list) and commits:
            c0 = commits[0]
            last_commit_sha = str(c0.get("sha") or "")[:7]
            last_commit_msg = str((c0.get("commit") or {}).get("message") or "").splitlines()[0][:90]

    lic = (info.get("license") or {}).get("spdx_id") or "-"
    if lic == "NOASSERTION":
        lic = "Custom"

    return {
        "full_name": info["full_name"],
        "html_url": info["html_url"],
        "stars": int(info.get("stargazers_count") or 0),
        "forks": int(info.get("forks_count") or 0),
        "open_issues": int(info.get("open_issues_count") or 0),
        "language": info.get("language") or "-",
        "license": lic,
        "pushed_at": str(info.get("pushed_at") or "")[:10],
        "archived": bool(info.get("archived")),
        "description": (info.get("description") or "").strip(),
        "release_tag": release_tag,
        "release_name": release_name,
        "release_date": release_date,
        "release_url": release_url,
        "last_commit_sha": last_commit_sha,
        "last_commit_msg": last_commit_msg,
    }


def fetch_discovery(queries: list[dict], known_lower: set[str]) -> list[dict]:
    results: list[dict] = []
    seen = set(known_lower)
    for item in queries:
        q = urllib.parse.quote(item["query"])
        data = gh_get(f"/search/repositories?q={q}&sort=stars&order=desc&per_page=8")
        picks = []
        if isinstance(data, dict):
            for r in data.get("items", []):
                fn = r["full_name"]
                if fn.lower() in seen or r.get("archived"):
                    continue
                seen.add(fn.lower())
                picks.append(
                    {
                        "full_name": fn,
                        "html_url": r["html_url"],
                        "stars": int(r.get("stargazers_count") or 0),
                        "pushed_at": str(r.get("pushed_at") or "")[:10],
                        "description": (r.get("description") or "").strip()[:100],
                    }
                )
                if len(picks) >= 4:
                    break
        results.append({"label": item["label"], "items": picks})
    return results


def fmt_stars(n: int, delta: int | None) -> str:
    base = f"{n:,}"
    if delta is None or delta == 0:
        return base
    sign = "+" if delta > 0 else ""
    return f"{base} (`{sign}{delta:,}`)"


def esc_md(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def build_readme(cfg: dict, prev_repos: dict, curr_repos: dict, discovery: list[dict], now_str: str, highlights: list[str]) -> str:
    lines = [
        f"# {cfg['title']}",
        "",
        f"> {cfg['description']}",
        f"> 最後自動更新：`{now_str} UTC`（每週一自動透過 GitHub Actions 同步最新 Stars、Release 與提交動態）",
        "",
    ]

    if highlights:
        lines.append("## 本期重點更新")
        lines.append("")
        for h in highlights:
            lines.append(f"- {h}")
        lines.append("")

    for cat in cfg["categories"]:
        lines.append(f"## {cat['name']}")
        lines.append("")
        lines.append(f"*{cat['goal']}*")
        lines.append("")
        lines.append("| 專案 | 定位 | Stars（週變動） | 最新版本 | 最後更新 | 授權 | 最新動態 / 說明 |")
        lines.append("| --- | --- | ---: | --- | :---: | :---: | --- |")
        for entry in cat["repos"]:
            slug = entry["repo"]
            snap = curr_repos.get(slug)
            if not snap:
                lines.append(f"| [{slug}](https://github.com/{slug}) | {esc_md(entry['role'])} | - | - | - | - | ⚠️ 暫時無法取得 |")
                continue
            old = prev_repos.get(slug)
            delta = (snap["stars"] - old["stars"]) if old else None
            rel_cell = (
                f"[`{snap['release_tag']}`]({snap['release_url']})"
                if snap["release_tag"] and snap["release_url"]
                else (f"`{snap['release_tag']}`" if snap["release_tag"] else "-")
            )
            archived_tag = " `[ARCHIVED]`" if snap["archived"] else ""
            note = entry["why"]
            if snap["last_commit_msg"]:
                note = f"{entry['why']}<br><sub>最新提交 `{snap['last_commit_sha']}`：{esc_md(snap['last_commit_msg'])}</sub>"
            lines.append(
                f"| [**{snap['full_name']}**]({snap['html_url']}){archived_tag} "
                f"| {esc_md(entry['role'])} "
                f"| {fmt_stars(snap['stars'], delta)} "
                f"| {rel_cell} "
                f"| {snap['pushed_at']} "
                f"| {snap['license']} "
                f"| {note} |"
            )
        lines.append("")

    lines.append("## 新發現候選（每週自動雷達掃描）")
    lines.append("")
    for group in discovery:
        lines.append(f"### {group['label']}")
        lines.append("")
        if not group["items"]:
            lines.append("- 本週無額外新候選或受 API 速率限制。")
        else:
            for it in group["items"]:
                lines.append(
                    f"- [**{it['full_name']}**]({it['html_url']})（★ {it['stars']:,}｜更新 `{it['pushed_at']}`）：{esc_md(it['description'])}"
                )
        lines.append("")

    lines.extend(
        [
            "## 與本機 `Youtube_Maker` 框架的銜接建議",
            "",
            "1. **動態視覺品質天花板**：使用 `python shared/production/pipeline.py export-remotion videos/<project>` 匯出時間軸 JSON，交給 `Youtube_Remotion/` 進行高質感 React/TS 動畫渲染。",
            "2. **影視／電視台級上限**：使用 `python shared/production/pipeline.py export-otio videos/<project>` 匯出 `.otio` 時間軸，一鍵匯入 DaVinci Resolve（免費版／Studio）進行電影級調色與 Fairlight 混音。",
            "3. **Google Flow / GenMedia 生成素材管線**：先產配音定秒數，再以 `python shared/production/pipeline.py plan-flow videos/<project>` 產出 `assets_manifest.json` 與提示詞任務卡；從 Google Flow UI 下載後執行 `ingest-flow` 自動轉檔 `1080p/30fps`、`ffprobe` 品檢並入庫 `clips/` 與 `Youtube_Remotion/public/`。",
            "4. **Agentic 全流程**：本機已更新 `youtube-studio-pipeline` 與 `remotion-motion-design` Skills，並對齊最新 `remotion-dev/skills`、`OpenMontage` 與 `google-gemini/gemini-skills` 規範。",
            "",
            "---",
            "本檔案由 [`scripts/update_radar.py`](scripts/update_radar.py) 自動產生，請修改 [`watchlist.json`](watchlist.json) 來增減追蹤清單。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    cfg = json.loads(WATCHLIST.read_text(encoding="utf-8"))
    prev_state = json.loads(STATE_FILE.read_text(encoding="utf-8")) if STATE_FILE.is_file() else {}
    prev_repos = prev_state.get("repos", {})
    has_token = bool(os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or shutil.which("gh"))
    full_mode = has_token and ("--lite" not in sys.argv)

    curr_repos: dict[str, dict] = {}
    known_lower: set[str] = set()
    new_releases: list[str] = []
    highlights: list[str] = []

    for cat in cfg["categories"]:
        for entry in cat["repos"]:
            slug = entry["repo"]
            known_lower.add(slug.lower())
            snap = fetch_repo_snapshot(slug, include_details=full_mode)
            if snap is None:
                if slug in prev_repos:
                    curr_repos[slug] = prev_repos[slug]
                continue
            curr_repos[slug] = snap
            known_lower.add(snap["full_name"].lower())
            old = prev_repos.get(slug)
            if old:
                if snap["release_tag"] and snap["release_tag"] != old.get("release_tag"):
                    msg = (
                        f"🚀 **{snap['full_name']}** 發布新版本 "
                        f"[`{snap['release_tag']}`]({snap['release_url']})（原 `{old.get('release_tag') or '無'}`）"
                    )
                    new_releases.append(msg)
                    highlights.append(msg)
                delta = snap["stars"] - int(old.get("stars") or 0)
                if delta >= 300:
                    highlights.append(f"📈 **{snap['full_name']}** 本期星數成長 `+{delta:,}`（總計 {snap['stars']:,}）")
                if snap["archived"] and not old.get("archived"):
                    highlights.append(f"⚠️ **{snap['full_name']}** 已被作者封存（archived），建議評估替代方案。")

    discovery = fetch_discovery(cfg.get("discovery_queries", []), known_lower)
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps({"updated_at": now_str, "repos": curr_repos, "discovery": discovery}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )

    readme_text = build_readme(cfg, prev_repos, curr_repos, discovery, now_str, highlights)
    README_FILE.write_text(readme_text, encoding="utf-8")

    if new_releases:
        diff_lines = [
            f"## 偵測到新版本發布（{now_str} UTC）",
            "",
            *[f"- {m}" for m in new_releases],
            "",
            "建議檢視更新紀錄，評估是否同步更新本機 `Youtube_Maker` 框架、`Youtube_Remotion` 套件或 Skills。",
            "",
        ]
        DIFF_FILE.write_text("\n".join(diff_lines), encoding="utf-8")
        # Append to UPDATES.md log
        header = "# 歷史版本更新紀錄\n\n"
        old_log = UPDATES_FILE.read_text(encoding="utf-8") if UPDATES_FILE.is_file() else header
        body = old_log[len(header):] if old_log.startswith(header) else old_log
        UPDATES_FILE.write_text(header + "\n".join(diff_lines) + "\n" + body, encoding="utf-8")
    else:
        if DIFF_FILE.exists():
            DIFF_FILE.unlink()

    print(f"Updated {len(curr_repos)} repos, {len(new_releases)} new releases detected.")


if __name__ == "__main__":
    main()
