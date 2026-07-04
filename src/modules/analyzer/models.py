from dataclasses import dataclass


@dataclass
class BestPrice:
    trade_type: str
    price: float
    trader: str
    payment_method: str
    min_amount: float | None
    max_amount: float | None
    completion_rate: float | None


@dataclass
class Opportunity:
    buy_price: float
    sell_price: float
    spread: float
    spread_percent: float
    best_buy: BestPrice
    best_sell: BestPrice
    payment_method: str
