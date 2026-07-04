from dataclasses import dataclass


@dataclass
class P2PAd:
    trade_type: str  # BUY o SELL
    fiat_unit: str
    crypto_unit: str
    price: float
    min_amount: float | None
    max_amount: float | None
    trader_name: str
    trader_nickname: str | None
    payment_method: str
    orders_count: int
    completion_rate: float | None
    adv_no: str
