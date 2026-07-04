from telegram import Bot
from telegram.error import TelegramError

from src.core.config import settings
from src.modules.analyzer.models import Opportunity

_bot: Bot | None = None


def get_bot() -> Bot | None:
    global _bot
    if _bot is None and settings.telegram_bot_token:
        _bot = Bot(token=settings.telegram_bot_token)
    return _bot


def _fmt_price(v: float) -> str:
    return f"Bs.{v:,.2f}"


def format_opportunity(o: Opportunity) -> str:
    return (
        f"\u2b06 Compra: {_fmt_price(o.buy_price)} ({o.best_buy.trader})"
        f"\n\u2b07 Venta: {_fmt_price(o.sell_price)} ({o.best_sell.trader})"
        f"\n\U0001f4c8 Spread: {_fmt_price(o.spread)} ({o.spread_percent}%)"
        f"\n\U0001f3b5 Método: {o.payment_method}"
    )


def format_summary(buy: list, sell: list) -> str:
    lines = ["\U0001f4ca Mejores precios VES/USDT\n"]
    lines.append("\u2b06 Mejor compra:")
    for p in buy[:3]:
        lines.append(f"  {_fmt_price(p.price)} - {p.trader} ({p.payment_method})")
    lines.append("")
    lines.append("\u2b07 Mejor venta:")
    for p in sell[:3]:
        lines.append(f"  {_fmt_price(p.price)} - {p.trader} ({p.payment_method})")
    return "\n".join(lines)


async def send_alert(message: str, chat_id: str | None = None) -> bool:
    bot = get_bot()
    if not bot:
        return False
    try:
        await bot.send_message(chat_id=chat_id or "0", text=message)
        return True
    except TelegramError:
        return False


async def broadcast_opportunity(o: Opportunity, chat_ids: list[str]) -> None:
    msg = format_opportunity(o)
    for cid in chat_ids:
        await send_alert(msg, cid)
