#!/usr/bin/env python3
"""Query Juan Li's public bilingual AI4Education endpoint."""

from __future__ import annotations
import argparse
import json
from urllib.request import Request, urlopen

DEFAULT_URL = "https://juanli.me/ai4education/api/v2/items.json"

def fetch(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "ai4education-skill/1.0"})
    with urlopen(req, timeout=20) as resp:
        return json.load(resp)

def main() -> None:
    parser = argparse.ArgumentParser(description="Query Juan Li · AI4Education public catalog.")
    parser.add_argument("--lang", choices=["en", "zh"], default="en")
    parser.add_argument("--topic", default="", help="Topic filter (e.g., teaching, learning, assessment, theory, policy, tools)")
    parser.add_argument("--stage", default="", help="Stage filter (e.g., higher, k12, family)")
    parser.add_argument("--q", default="", help="Keyword filter")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    data = fetch(args.url)
    items = data.get("items", [])
    q = args.q.strip().lower()
    shown = 0
    for item in items:
        if args.topic and args.topic not in (item.get("topics") or []):
            continue
        if args.stage and args.stage not in (item.get("stages") or []):
            continue
        blob = json.dumps(item, ensure_ascii=False).lower()
        if q and q not in blob:
            continue
        title = (item.get("title") or {}).get(args.lang) or ""
        summary = (item.get("summary") or {}).get(args.lang) or ""
        limit_note = (item.get("limits") or {}).get(args.lang) or ""
        src = ((item.get("sources") or [{}])[0]).get("url") or ""
        pub = item.get("publishedAt") or "date-precision-see-record"
        prefix = "en/" if args.lang == "en" else ""
        permalink = f"https://juanli.me/ai4education/{prefix}items/{item['id']}/"
        print(f"- [{pub}] {title}\n  Summary: {summary}\n  Boundary: {limit_note}\n  Source: {src}\n  Permalink: {permalink}\n")
        shown += 1
        if shown >= args.limit:
            break

if __name__ == "__main__":
    main()
