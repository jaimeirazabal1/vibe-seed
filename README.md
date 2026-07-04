# binance-p2p-bot

Monitoreo de precios P2P en Binance en VES. Ve las mejores oportunidades y recibe alertas por Telegram.

## Stack

Python 3.12 / FastAPI / PostgreSQL / Redis / Celery / Telegram Bot / TailwindCSS

## Arrancar

```bash
cp .env.example .env   # editar variables
docker compose up -d
# o:
poetry install && poetry run python src/main.py
```

## Comandos del Bot de Telegram

- `/start` — Iniciar
- `/precios` — Mejores precios ahora
- `/alertar <spread>` — Alertar cuando spread supere X%
- `/metodo <nombre>` — Filtrar por método de pago
