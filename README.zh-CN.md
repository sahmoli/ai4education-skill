# AI4Education Skill

**[English](README.md) | [简体中文](README.zh-CN.md)** · **[在线主页（中文）](https://juanli.me/ai4education/) · [English Portal](https://juanli.me/ai4education/en/) · [Agent 接入页](https://juanli.me/ai4education/agent/)**

[![Live Site](https://img.shields.io/badge/在线访问-juanli.me%2Fai4education-94501F)](https://juanli.me/ai4education/)
[![Languages](https://img.shields.io/badge/多语言-简体中文_%7C_English-2F6F6A)](https://juanli.me/ai4education/)
[![Schema](https://img.shields.io/badge/接口规范-ai4education.public.v2-6B5B4F)](https://juanli.me/ai4education/manifest.json)
[![License: MIT](https://img.shields.io/badge/开源许可-MIT-3A2E27)](LICENSE)

一个面向 Agent 的中英双语、来源可追溯 **AI 与教育（AI in Education）** 公开阅读札记接口。

本仓库开放的是 [Juan Li · AI4Education](https://juanli.me/ai4education/) 的**公开阅读层**：涵盖大学、中小学与家庭教育场景的 AI 教学、学习与评价研究札记，每条记录均保留中英文标题、摘要、**证据边界说明（`limits`）**、**实际读取范围（`sources[].scope`）**、原始发布日期精度以及原始出处链接。

---

## 1. 安装与读取

把下面这句话交给支持 Skills 的 Agent（Claude Code、Cursor、Codex、Grok Bot 等）：

> 请从 https://github.com/sahmoli/ai4education-skill 安装 AI4Education Skill（或读取 https://juanli.me/ai4education/agent/SKILL.md），并按说明读取公开接口。

或者直接将 `ai4education/` 目录复制到你的 Agent 使用的 skills 目录中。

---

## 2. 能做什么

- 用**中文或英文**检索 AI 与教育领域的实证研究、课堂实验、政策报告与学者反思
- 按**主题**（`teaching` 教学、`learning` 学习、`assessment` 评价、`theory` 理论、`policy` 政策、`tools` 工具）或**学段**（`higher` 高校、`k12` 中小学、`family` 家庭）过滤
- 严格区分**全量收录（`items.json`）**、**编辑精选（`picks.json`）**与**每日阅读（`daily.json`）**
- 保留每条文献的**证据边界**与**原始日期精度**（绝不把期号或转载日期伪造为原始发表日）

零第三方依赖的 Python 查询示例：

```bash
python3 ai4education/scripts/query_ai4education.py --lang zh --topic teaching --limit 5
```

---

## 3. 公开只读接口（无需 API Key）

- **Manifest（`v4`）**：`https://juanli.me/ai4education/manifest.json`
- **LLMs.txt**：`https://juanli.me/ai4education/llms.txt`
- **全量条目 JSON（`v2`）**：`https://juanli.me/ai4education/api/v2/items.json`
- **编辑精选 JSON（`v2`）**：`https://juanli.me/ai4education/api/v2/picks.json`
- **每日阅读 JSON（`v2`）**：`https://juanli.me/ai4education/api/v2/daily.json`
- **主题与实体 JSON（`v2`）**：`https://juanli.me/ai4education/api/v2/topics.json` · `https://juanli.me/ai4education/api/v2/entities.json`
- **RSS 订阅**：
  - 每日阅读：`https://juanli.me/ai4education/feed/daily.zh.xml` · `https://juanli.me/ai4education/feed/daily.en.xml`
  - 编辑精选：`https://juanli.me/ai4education/feed/selected.zh.xml` · `https://juanli.me/ai4education/feed/selected.en.xml`
  - 全量条目：`https://juanli.me/ai4education/feed.zh.xml` · `https://juanli.me/ai4education/feed.en.xml`

---

## 4. 开源许可与李娟（Juan Li）相关项目

Skill 代码与文档采用 [MIT License](LICENSE)。所链接的原始资料仍遵循各自权利人的条款。

- **[Juan Li · 个人学术主页](https://juanli.me/zh/)** —— 西交利物浦大学（XJTLU）保护生物学与空间生态学研究。
- **[Juan Li · AI4Science](https://juanli.me/ai4science/zh/)**（[`sahmoli/ai4science-skill`](https://github.com/sahmoli/ai4science-skill)）—— AI 如何进入各门科学：每日精选、双语导读，每条均回到原始来源。
- **[Juan Li · Seeing Ecology（看见生态）](https://juanli.me/seeing-ecology/)**（[`sahmoli/seeing-ecology`](https://github.com/sahmoli/seeing-ecology)）—— 生态学与保护生物学经典概念的中英双语视觉与交互拆解。
