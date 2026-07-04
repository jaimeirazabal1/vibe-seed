# PLAN.md — Requirements & Progress

## Requirements

Sistema para ver los mejores precios P2P en Binance en VES y recibir alertas.

1. **Scanner** — Obtener anuncios de compra y venta en VES cada N segundos
2. **Analyzer** — Calcular mejor precio de compra y venta, spread, oportunidades destacadas
3. **Notifier** — Bot de Telegram que alerta cuando hay spreads grandes o precios atractivos
4. **Dashboard web** — Tablero para ver precios en tiempo real, histórico, filtrar por método de pago

## Milestones

| # | Milestone | Status |
|---|---|---|
| 1 | Project scaffold + config | ✅ |
| 2 | Binance P2P client + scanner | ✅ |
| 3 | Analyzer + detección de mejores precios | ✅ |
| 4 | Notifier (Telegram) | ✅ |
| 5 | Dashboard web + API | ✅ |
| 6 | Docker Compose + deploy | ✅ |
| 7 | Tests | ✅ |

## Active Tasks

- [ ] Probar el proyecto localmente con Docker Compose
- [ ] Agregar autenticación al dashboard (opcional)
- [ ] Agregar más métodos de filtrado en el dashboard

## Completed

- 2026-07-03: Seed scaffold + arquitectura definida
- 2026-07-03: Scanner (client.py, scheduler.py, tasks.py, models.py)
- 2026-07-03: Analyzer (best_price.py con detección de mejores precios y oportunidades)
- 2026-07-03: Notifier (telegram.py con formato y envío de alertas)
- 2026-07-03: API + Dashboard web (FastAPI routes + TailwindCSS template)
- 2026-07-03: Docker Compose (api, worker, db, redis)
- 2026-07-03: Tests unitarios (scanner client, notifier)
