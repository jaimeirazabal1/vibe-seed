from sqlalchemy import select

from src.core.database import async_session
from src.models.price_snapshot import PriceSnapshot
from src.modules.analyzer.models import BestPrice, Opportunity


async def get_best_prices(limit: int = 5) -> tuple[list[BestPrice], list[BestPrice]]:
    async with async_session() as session:
        buy = await _top_prices(session, "BUY", limit)
        sell = await _top_prices(session, "SELL", limit)
    return buy, sell


async def find_opportunities(min_spread: float = 0.5) -> list[Opportunity]:
    buy_best, sell_best = await get_best_prices(10)
    opportunities = []

    for buy in buy_best:
        for sell in sell_best:
            if buy.payment_method != sell.payment_method:
                continue
            spread = sell.price - buy.price
            spread_pct = (spread / buy.price) * 100 if buy.price else 0
            if spread_pct >= min_spread:
                opportunities.append(Opportunity(
                    buy_price=buy.price,
                    sell_price=sell.price,
                    spread=round(spread, 2),
                    spread_percent=round(spread_pct, 2),
                    best_buy=buy,
                    best_sell=sell,
                    payment_method=buy.payment_method,
                ))
    return sorted(opportunities, key=lambda o: o.spread_percent, reverse=True)


async def _top_prices(session, trade_type: str, limit: int) -> list[BestPrice]:
    latest = (
        await session.execute(
            select(PriceSnapshot.created_at)
            .where(PriceSnapshot.trade_type == trade_type)
            .order_by(PriceSnapshot.created_at.desc())
            .limit(1)
        )
    ).scalar_one_or_none()

    if not latest:
        return []

    order = PriceSnapshot.price.asc() if trade_type == "BUY" else PriceSnapshot.price.desc()
    result = await session.execute(
        select(PriceSnapshot)
        .where(PriceSnapshot.trade_type == trade_type, PriceSnapshot.created_at == latest)
        .order_by(order)
        .limit(limit)
    )
    rows = result.scalars().all()

    return [
        BestPrice(
            trade_type=r.trade_type,
            price=r.price,
            trader=r.trader_name,
            payment_method=r.payment_method,
            min_amount=r.min_amount,
            max_amount=r.max_amount,
            completion_rate=r.completion_rate,
        )
        for r in rows
    ]
