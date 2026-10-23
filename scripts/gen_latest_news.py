#!/usr/bin/env python3
"""Regenerate docs/latest-news.md index from docs/news/*.md briefings.

Usage: python3 scripts/gen_latest_news.py
Keeps the front-matter, lists the most recent N briefings (default 7)
with headline bullets extracted from each briefing's ### [title](url) lines.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = ROOT / "docs" / "news"
OUT = ROOT / "docs" / "latest-news.md"
MAX_DAYS = 7
MAX_BULLETS = 10

HEADER = """---
title: "最新动态"
sidebar_position: 1
---

# 📰 最新 AI 动态

> 最后更新：{updated} ｜ 自动聚合每日新闻简报
"""


def extract_briefing(path: Path):
    text = path.read_text(encoding="utf-8")
    date_m = re.search(r"\*\*Date\*\*:\s*(\d{4}-\d{2}-\d{2})", text)
    date = date_m.group(1) if date_m else path.stem
    titles = re.findall(r"^###\s+\[([^\]]+)\]\(", text, flags=re.M)
    return date, titles


def main():
    files = sorted(NEWS_DIR.glob("*.md"), reverse=True)
    files = [f for f in files if f.name not in ("index.md",)]
    parts = [HEADER.format(updated=_now())]
    for f in files[:MAX_DAYS]:
        date, titles = extract_briefing(f)
        parts.append(f"\n## [{date} AI News 每日简报](/news/{date})\n")
        parts.append(f"\n**{date}** ｜ {len(titles)} 条动态\n")
        for t in titles[:MAX_BULLETS]:
            parts.append(f"- {t}")
        parts.append("")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"OK: wrote {OUT} ({len(files[:MAX_DAYS])} briefings indexed)")


def _now():
    from datetime import datetime, timezone, timedelta
    cst = timezone(timedelta(hours=8))
    return datetime.now(cst).strftime("%Y-%m-%d %H:%M")


if __name__ == "__main__":
    main()
