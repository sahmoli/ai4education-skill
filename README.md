# AI4Education Skill

**[English](README.md) | [简体中文](README.zh-CN.md)** · **[Live Portal (EN)](https://juanli.me/ai4education/en/) · [在线主页（中文）](https://juanli.me/ai4education/) · [Agent Access](https://juanli.me/ai4education/en/agent/)**

[![Live Site](https://img.shields.io/badge/Live_Site-juanli.me%2Fai4education-94501F)](https://juanli.me/ai4education/en/)
[![Languages](https://img.shields.io/badge/Language-English_%7C_简体中文-2F6F6A)](https://juanli.me/ai4education/)
[![Schema](https://img.shields.io/badge/Schema-ai4education.public.v2-6B5B4F)](https://juanli.me/ai4education/manifest.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-3A2E27)](LICENSE)

A bilingual, source-grounded AI in Education reading index and Skill for agents.

This repository exposes the **public reading layer** of [Juan Li · AI4Education](https://juanli.me/ai4education/en/): curated reading notes across universities, K-12 schools, and family learning, with Chinese and English titles, summaries, explicit evidence boundaries (`limits`), reading scope (`sources[].scope`), and links to original sources.

---

## 1. Install

Ask a Skills-compatible agent (Claude Code, Cursor, Codex, Grok Bot, OpenCode):

> Install the AI4Education Skill from https://github.com/sahmoli/ai4education-skill (or read https://juanli.me/ai4education/agent/SKILL.md). Install the `ai4education/` directory, start a new session, and follow it to read the public interfaces.

Or copy `ai4education/SKILL.md` directly into your agent's skills folder.

---

## 2. What It Can Do

- Query recent and classic AI-in-education studies, trials, policy reports, and practitioner reflections in **English or Chinese**
- Filter by **topic** (`teaching`, `learning`, `assessment`, `theory`, `policy`, `tools`) or **educational stage** (`higher`, `k12`, `family`)
- Distinguish **editorial picks** (`picks.json`) and **daily editions** (`daily.json`) from the full catalog (`items.json`)
- Preserve strict **evidence boundaries** (e.g., whether a source is a randomized trial, observational study, institutional self-report, or opinion piece, and whether the full text or an excerpt was read)

Example CLI query (zero third-party dependencies):

```bash
python3 ai4education/scripts/query_ai4education.py --lang en --topic teaching --limit 5
```

---

## 3. Public Read-Only Interfaces (No API Key Required)

- **Manifest (`v4`)**: `https://juanli.me/ai4education/manifest.json`
- **LLMs.txt**: `https://juanli.me/ai4education/llms.txt`
- **Catalog JSON (`v2`)**: `https://juanli.me/ai4education/api/v2/items.json`
- **Editorial Picks JSON (`v2`)**: `https://juanli.me/ai4education/api/v2/picks.json`
- **Daily Editions JSON (`v2`)**: `https://juanli.me/ai4education/api/v2/daily.json`
- **Topics & Entities JSON (`v2`)**: `https://juanli.me/ai4education/api/v2/topics.json` · `https://juanli.me/ai4education/api/v2/entities.json`
- **RSS Feeds**:
  - Daily Briefs: `https://juanli.me/ai4education/feed/daily.en.xml` · `https://juanli.me/ai4education/feed/daily.zh.xml`
  - Editorial Picks: `https://juanli.me/ai4education/feed/selected.en.xml` · `https://juanli.me/ai4education/feed/selected.zh.xml`
  - Full Catalog: `https://juanli.me/ai4education/feed.en.xml` · `https://juanli.me/ai4education/feed.zh.xml`

---

## 4. License & Related Projects by Juan Li

The Skill code and documentation are available under the [MIT License](LICENSE). Linked source materials remain subject to their respective owners' terms.

- **[Juan Li · Academic Homepage](https://juanli.me/)** — Conservation biology & spatial ecology at XJTLU.
- **[Juan Li · AI4Science](https://juanli.me/ai4science/)** ([`sahmoli/ai4science-skill`](https://github.com/sahmoli/ai4science-skill)) — Bilingual, source-grounded AI for Science feed for agents.
- **[Juan Li · Seeing Ecology (看见生态)](https://juanli.me/seeing-ecology/)** ([`sahmoli/seeing-ecology`](https://github.com/sahmoli/seeing-ecology)) — Bilingual visual & interactive explainers of core concepts in ecology and conservation biology.
