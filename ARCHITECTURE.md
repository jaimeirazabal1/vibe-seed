# ARCHITECTURE.md — Decisions & Structure

*The AI updates this as architecture decisions are made. This prevents contradictions.*

## Directory Structure

```
src/
├── app/                   # Navigation + screens
│   ├── navigation/
│   └── screens/
├── features/              # Domain modules (one per feature)
│   ├── chat/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── store/
│   ├── contacts/
│   ├── conversations/
│   ├── templates/
│   ├── broadcast/
│   ├── analytics/
│   └── auth/
├── services/              # Global services
│   ├── api/
│   ├── meta/
│   ├── websocket/
│   └── storage/
├── shared/                # Reusable primitives
│   ├── components/
│   ├── hooks/
│   ├── utils/
│   └── types/
├── database/
│   ├── models/
│   └── sync/
└── config/
```

## Key Decisions

*(AI fills these as they are made)*

| Aspect | Decision | Justification |
|---|---|---|
| State approach | | |
| Offline strategy | | |
| Real-time messaging | | |
| Auth flow | | |
| Testing framework | | |
