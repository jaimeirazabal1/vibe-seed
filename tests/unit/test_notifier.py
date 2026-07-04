import pytest

from src.modules.notifier.telegram import format_opportunity, format_summary
from src.modules.analyzer.models import BestPrice, Opportunity


@pytest.fixture
def sample_opportunity():
    return Opportunity(
        buy_price=42.00,
        sell_price=46.50,
        spread=4.50,
        spread_percent=10.71,
        best_buy=BestPrice(
            trade_type="BUY", price=42.00, trader="Comprador1",
            payment_method="Banco Venezuela", min_amount=1000.0,
            max_amount=50000.0, completion_rate=0.99,
        ),
        best_sell=BestPrice(
            trade_type="SELL", price=46.50, trader="Vendedor1",
            payment_method="Banco Venezuela", min_amount=2000.0,
            max_amount=30000.0, completion_rate=0.97,
        ),
        payment_method="Banco Venezuela",
    )


def test_format_opportunity_contains_spread(sample_opportunity):
    msg = format_opportunity(sample_opportunity)
    assert "10.71%" in msg
    assert "42.00" in msg
    assert "46.50" in msg
