# AGENTS.md — Master Context & Rules

*Este archivo es la fuente de verdad. La IA lo lee al inicio y lo actualiza al final de cada sesión.*

## Project Identity

- **Name**: {{nombre_del_proyecto}}
- **Stack**: React Native (Expo) + TypeScript (strict)
- **API**: WhatsApp Cloud API (Meta)
- **Purpose**: {{descripción_del_proyecto}}
- **Pattern**: Feature-based architecture

## Critical Rules (Never violate)

1. **Every change must be validated** — run `npx tsc --noEmit` and `npx eslint .` after every modification.
2. **No file over 300 lines.** Split if exceeded.
3. **Tests for every business logic file.** No exceptions.
4. **No new files without justification** — prefer extending existing ones.
5. **Commits must be atomic** — one logical change per commit. Use conventional commits (`feat:`, `fix:`, `chore:`, `refactor:`).
6. **Update AGENTS.md, ARCHITECTURE.md and PLAN.md after every session** — keep them in sync with reality.
7. **Never flatten the structure** — all code lives in `src/features/<feature>/` by domain.

## Architecture Decision Records

*(AI updates this as decisions are made)*

| Decision | Chosen Option | Rationale |
|---|---|---|
| State management | | |
| Local database | | |
| Navigation | | |
| HTTP client | | |
| Auth strategy | | |

## Current Tech Stack

| Layer | Choice | Status |
|---|---|---|
| Framework | React Native (Expo) | Pending |
| Language | TypeScript (strict) | Pending |
| State | _to be decided_ | Pending |
| Local DB | _to be decided_ | Pending |
| Testing | _to be decided_ | Pending |

## Session Log

*AI appends here after each session: date, what was done, current state, next steps.*

---

## Last Session

- **Date**: {{fecha}}
- **Done**: {{qué se hizo}}
- **Next**: {{qué sigue}}
- **Blockers**: {{problemas}}
