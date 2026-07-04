import httpx

from src.core.config import settings
from src.modules.scanner.models import P2PAd

BINANCE_P2P_URL = f"{settings.binance_api_base}/bapi/c2c/v2/friendly/c2c/adv/search"

PAYLOAD_TEMPLATE = {
    "page": 1,
    "rows": 20,
    "payTypes": [],
    "countries": [],
    "publisherType": None,
    "classfied": "merchant",
}


async def fetch_ads(trade_type: str, fiat: str = "VES", crypto: str = "USDT") -> list[P2PAd]:
    payload = {**PAYLOAD_TEMPLATE, "tradeType": trade_type, "fiat": fiat, "asset": crypto}

    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.post(BINANCE_P2P_URL, json=payload)
        resp.raise_for_status()
        data = resp.json()

    ads = []
    for item in data.get("data", []):
        adv = item.get("adv", {})
        advertiser = item.get("advertiser", {})

        ads.append(P2PAd(
            trade_type=trade_type,
            fiat_unit=fiat,
            crypto_unit=crypto,
            price=float(adv.get("price", 0)),
            min_amount=_safe_float(adv.get("minSingleTransAmount")),
            max_amount=_safe_float(adv.get("maxSingleTransAmount")),
            trader_name=advertiser.get("nickName", ""),
            trader_nickname=advertiser.get("userNo", None),
            payment_method=adv.get("tradeMethods", [{}])[0].get("tradeMethodName", ""),
            orders_count=advertiser.get("monthOrderCount", 0),
            completion_rate=advertiser.get("monthFinishRate", None),
            adv_no=adv.get("advNo", ""),
        ))
    return ads


async def fetch_buy_ads(fiat: str = "VES", crypto: str = "USDT") -> list[P2PAd]:
    return await fetch_ads("BUY", fiat, crypto)


async def fetch_sell_ads(fiat: str = "VES", crypto: str = "USDT") -> list[P2PAd]:
    return await fetch_ads("SELL", fiat, crypto)


def _safe_float(val) -> float | None:
    if val is None:
        return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None
