# ARCHITECTURE.md

## Directory Structure

```
src/
├── api/                   # FastAPI routes
│   ├── routes/
│   │   ├── prices.py      # GET /api/prices, GET /api/opportunities
│   │   └── config.py      # POST /api/config (filtros, intervalos)
│   ├── middleware/
│   └── schemas/           # Pydantic models
├── core/
│   ├── config.py          # Settings from env vars
│   ├── database.py        # SQLAlchemy engine + session
│   └── redis.py           # Redis client
├── modules/
│   ├── scanner/           # Escaneo de anuncios Binance P2P
│   │   ├── client.py      # HTTP client para endpoints públicos de Binance
│   │   ├── parser.py      # Normalizar respuesta a modelo interno
│   │   └── scheduler.py   # Celery task para escaneo periódico
│   ├── analyzer/          # Detección de mejores precios
│   │   ├── spread.py      # Calcular spread compra/venta
│   │   ├── best_price.py  # Top N mejores ofertas
│   │   └── filters.py     # Filtrar por método de pago, monto, etc.
│   └── notifier/          # Alertas
│       ├── telegram.py    # Bot de Telegram
│       └── templates.py   # Mensajes formateados
├── models/                # SQLAlchemy models
│   ├── ad.py
│   ├── price_snapshot.py
│   └── user_config.py
├── services/
│   ├── binance.py         # Cliente Binance unificado
│   └── cache.py           # Cache con Redis
├── utils/
│   ├── validators.py
│   └── formatters.py
├── web/                   # Frontend (TailwindCSS + Alpine.js)
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   └── opportunities.html
│   └── static/
│       └── js/
│           └── app.js
└── main.py                # FastAPI entry point

tests/
├── unit/
├── integration/
└── fixtures/
```

## Key Decisions

| Aspect | Decision | Why |
|---|---|---|
| Backend | FastAPI | Async, auto-docs, Python |
| Frontend | Tailwind + Alpine.js (server-rendered Jinja2) | Sin necesidad de Node/SPA complejo |
| Scanning | Celery Beat cada 30-60s | Intervalo configurable |
| Cache | Redis | Evita rate limiting a Binance |
| Alerts | Telegram Bot | Notificaciones en tiempo real |
| DB | PostgreSQL | Historial de precios |
| Price data | Binance P2P public endpoint `/bapi/c2c/v2/friendly/c2c/adv/search` | Endpoint público oficial |
