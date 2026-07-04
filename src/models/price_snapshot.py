import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base


class PriceSnapshot(Base):
    __tablename__ = "price_snapshots"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trade_type: Mapped[str] = mapped_column(String(10), index=True)  # BUY o SELL
    fiat_unit: Mapped[str] = mapped_column(String(10), default="VES")
    crypto_unit: Mapped[str] = mapped_column(String(10), default="USDT")
    price: Mapped[float] = mapped_column(Float)
    min_amount: Mapped[float | None] = mapped_column(Float, nullable=True)
    max_amount: Mapped[float | None] = mapped_column(Float, nullable=True)
    trader_name: Mapped[str] = mapped_column(String(100))
    trader_nickname: Mapped[str | None] = mapped_column(String(100), nullable=True)
    payment_method: Mapped[str] = mapped_column(String(100))
    orders_count: Mapped[int] = mapped_column(Integer, default=0)
    completion_rate: Mapped[float | None] = mapped_column(Float, nullable=True)
    adv_no: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), index=True
    )
