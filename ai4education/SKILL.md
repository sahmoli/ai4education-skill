---
name: ai4education-reader
description: Read the public Juan Li · AI4Education catalog and its explicit selections.
---
# AI4Education read-only consumer

Origin: https://juanli.me. All absolute URLs below are canonical, permanent URLs.
Do not fetch a Science endpoint as an Education fallback.

1. GET /ai4education/manifest.json. Assert schema ai4education.manifest.v4 and cacheNamespace ai4education-v4; follow its api/v2 URLs.
2. GET its catalog, topics, picks, entities and daily URLs using the same origin.
   Assert each response's generation equals the manifest. Reject /ai4science/ paths,
   duplicate IDs or unknown selected IDs. The complete catalog contains current public records.
3. Deduplicate by item.id. Read title/summary/body in the requested zh or en language.
   Link /ai4education/items/{id}/ or /ai4education/en/items/{id}/ for the same ID.
4. All catalog records are distinct from editorial picks. Only picks.itemIds are featured;
   their selectedAt and bilingual reason are explicit. Daily editions have their own
   selectedAt, ordered itemIds, per-item reason and recent/background role. Never
   group collectedAt into a Daily edition. Edition dates use Asia/Shanghai.
5. Preserve publishedAt (original date), collectedAt (catalog collection), selectedAt
   (editorial choice) and sources[].checkedAt/scope as separate facts. An old source
   selected today was not published today. Do not fabricate ratings or missing readings.
6. Entities use stable explicit person/institution IDs and recorded bindings. Blog,
   podcast and YouTube channels are channels, not inferred authors. Other contributors
   on a shared channel are not automatically assigned to its owner or host.
7. Read feeds.all, feeds.selected and feeds.daily from the manifest. All-note/topic
   RSS uses collection pubDate and selected RSS uses selection pubDate only when the original day is known; partial-date per-item entries omit pubDate. Daily RSS uses the edition selection pubDate.
   Daily RSS contains editions, not 115 individual collected records. Parse XML,
   compare IDs to the corresponding JSON lists, then GET the linked detail.
8. Retain type, limits and sources[].scope. An abstract/transcript/landing page is not
   a full paper or audio/video reading. Opinions and vendor statements stay attributed.
9. Refresh the complete manifest/catalog and remove withdrawn IDs from local copies.
   Absence from selected RSS is not removal from the complete catalog.
10. There are no write endpoints, account steps, credentials, payments or model calls.
    Do not transmit private conversations, student/family data or unpublished work.

This Markdown is an instruction file, not executable code or a packaged installation.
A supported agent can load its text in a fresh session; no global install is required.
Loading this file does not install a third-party skill or invoke any model.

Date precision contract (ai4education.public.v2):
- Existing v1-shaped records remain unchanged and retain exact-day publishedAt.
  Their absence of publication is the legacy day form, not a missing-date record.
- publication.schema is ai4education.publication.v2. originalPublishedAt and publishedAt
  are the same exact original day or null. Never turn a month, year or issue into a day.
- Read originalDatePrecision, originalYearMonth, originalYear and originalIssue together.
  A journal issue number does not establish a calendar month. Preserve republishedAt
  independently, including its literal timezone precision; it is not original publication.
- Unknown original days appear after dated entries, outside dated freshness groups.
  They may be explicitly chosen as background, never inferred to be recent.
- v1 URLs in manifest.legacy contain only records with an original day; an edition with
  an unrepresentable item is omitted in full. Use v2 to consume the complete catalog.
- For RSS entries without pubDate, read the explicitly labeled collection or selection
  time in description. Never infer an original date or complete reading from it.
