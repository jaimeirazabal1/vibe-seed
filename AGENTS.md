# Vibe-Seed: AI Context & Rules

This file is the source of truth for the AI. Read it before every session.

## Project Identity

- **Name**: (auto-named by developer)
- **Stack**: React Native (Expo) + TypeScript
- **API**: WhatsApp Cloud API (Meta)
- **Purpose**: CRM SaaS with WhatsApp messaging (clon funcional de WhatsApp)
- **Pattern**: Feature-based architecture (no flat folder structure)

## Critical Rules (Never violate)

1. **Never flatten the structure.** Every feature lives in `src/features/<feature>/`. No exceptions.
2. **Tests first for business logic.** Every service/hook must have a corresponding test file.
3. **No file over 300 lines.** If a file exceeds 300 lines, split it.
4. **Every architecture decision must be documented here.** Before introducing a new dependency, add it to this file.
5. **Run `npx tsc --noEmit` and `npx eslint .` after every change.** Fix all errors before continuing.
6. **Commits must be atomic.** One logical change = one commit. Use conventional commits (`feat:`, `fix:`, `chore:`, `refactor:`).
7. **No new files without justification.** Prefer extending existing files over creating new ones.

## Architecture

```
src/
├── app/                   # Navigation config (React Navigation)
│   ├── navigation/
│   └── screens/
├── features/              # Domain modules
│   ├── chat/              # Messaging (core)
│   ├── contacts/
│   ├── conversations/
│   ├── templates/         # Message templates (CRM)
│   ├── broadcast/         # Campaigns (CRM)
│   ├── analytics/         # CRM metrics
│   └── auth/              # Meta auth
├── services/              # Global service layer
│   ├── api/               # Axios instance
│   ├── meta/              # WhatsApp Cloud API client
│   ├── websocket/         # Real-time manager
│   └── storage/           # MMKV wrapper
├── shared/                # Reusable primitives
│   ├── components/        # UI primitives
│   ├── hooks/
│   ├── utils/
│   └── types/
├── database/              # WatermelonDB models + sync
│   ├── models/
│   └── sync/
└── config/                # Environment + constants
```

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Framework | React Native (Expo) | Cross-platform, OTA updates |
| Language | TypeScript (strict) | Safety, AI guardrails |
| State | Zustand + React Query | Lightweight, testable |
| Local DB | WatermelonDB | Offline-first, relational |
| Navigation | React Navigation | Standard RN nav |
| HTTP | Axios | Interceptors for token refresh |
| Real-time | Meta Webhooks | Official API, no custom WS |
| Testing | Jest + React Native Testing Library | Standard RN testing |
| Lint | ESLint + Prettier | Consistent code |
| CI | GitHub Actions | Run tests + typecheck on PR |

## Current State

- [ ] Project scaffolded
- [ ] Meta API client configured
- [ ] Auth flow implemented
- [ ] Chat feature built
- [ ] Contacts sync working
- [ ] Templates CRUD
- [ ] Broadcast campaign system
- [ ] Analytics dashboard
- [ ] Tests for business logic

**Last session context:** (update this after every session with what was done and what's next)
