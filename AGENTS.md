# AGENTS.md — AI Instructions (read this first)

## Project Identity

- **Name**: binance-p2p-bot
- **Stack**: Python 3.12+ / FastAPI / PostgreSQL / Redis / Celery / Telegram Bot / TailwindCSS + Alpine.js
- **API**: Binance P2P public endpoints
- **Purpose**: Sistema que monitorea anuncios P2P en Binance en VES, muestra los mejores precios de compra/venta, y envía alertas por Telegram para que el usuario tome decisiones manuales.
- **Pattern**: Modular monolith with background tasks

## Your Rules (never break these)

- Run `pytest` and `ruff check .` after every change. Fix all errors.
- No file over 300 lines. Split if needed.
- Tests for every business logic file.
- No new files without justification. Prefer extending existing ones.
- Commits must be atomic with conventional commit messages.
- Update AGENTS.md, ARCHITECTURE.md and PLAN.md at the end of every session.
- All secrets and API keys go in environment variables, never in code.

## Session Log

| Date | Done | Next | Blockers |
|---|---|---|---|
| 2026-07-03 | Initial scaffold, Binance P2P client, price scanner, Telegram notifier, web dashboard | Deploy preparation | None |
