import pytest
import httpx

from src.modules.scanner.client import fetch_ads, _safe_float


@pytest.mark.asyncio
async def test_fetch_ads_returns_list(respx_mock):
    respx_mock.post("https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search").respond(
        json={
            "data": [
                {
                    "adv": {
                        "price": "42.50",
                        "minSingleTransAmount": "1000",
                        "maxSingleTransAmount": "50000",
                        "tradeMethods": [{"tradeMethodName": "Banco de Venezuela"}],
                        "advNo": "ABC123",
                    },
                    "advertiser": {
                        "nickName": "Trader1",
                        "userNo": "USR001",
                        "monthOrderCount": 150,
                        "monthFinishRate": 0.98,
                    },
                }
            ]
        }
    )

    ads = await fetch_ads("BUY", "VES", "USDT")
    assert len(ads) == 1
    assert ads[0].price == 42.50
    assert ads[0].trade_type == "BUY"
    assert ads[0].payment_method == "Banco de Venezuela"
    assert ads[0].trader_name == "Trader1"
    assert ads[0].orders_count == 150


def test_safe_float():
    assert _safe_float("42.5") == 42.5
    assert _safe_float(None) is None
    assert _safe_float("invalid") is None
