from datetime import datetime, timezone

from src.core.database import async_session
from src.models.price_snapshot import PriceSnapshot
from src.modules.scanner.client import fetch_buy_ads, fetch_sell_ads
from src.modules.scanner.models import P2PAd


async def scan_and_store():
    buy_ads, sell_ads = await _fetch_all_ads()
    async with async_session() as session:
        for ad in buy_ads:
            session.add(_ad_to_snapshot(ad, "BUY"))
        for ad in sell_ads:
            session.add(_ad_to_snapshot(ad, "SELL"))
        await session.commit()
    return len(buy_ads) + len(sell_ads)


async def _fetch_all_ads() -> tuple[list[P2PAd], list[P2PAd]]:
    buy_ads, sell_ads = await fetch_buy_ads(), await fetch_sell_ads()
    return buy_ads, sell_ads


def _ad_to_snapshot(ad: P2PAd, trade_type: str) -> PriceSnapshot:
    return PriceSnapshot(
        trade_type=trade_type,
        fiat_unit=ad.fiat_unit,
        crypto_unit=ad.crypto_unit,
        price=ad.price,
        min_amount=ad.min_amount,
        max_amount=ad.max_amount,
        trader_name=ad.trader_name,
        trader_nickname=ad.trader_nickname,
        payment_method=ad.payment_method,
        orders_count=ad.orders_count,
        completion_rate=ad.completion_rate,
        adv_no=ad.adv_no,
        created_at=datetime.now(timezone.utc),
    )
