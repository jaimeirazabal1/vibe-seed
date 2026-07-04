from celery import Celery

from src.core.config import settings

celery_app = Celery(
    "binance_p2p",
    broker=settings.redis_url,
    backend=settings.redis_url,
    include=["src.modules.scanner.tasks"],
)

celery_app.conf.beat_schedule = {
    "scan-p2p-every-30s": {
        "task": "src.modules.scanner.tasks.scan_p2p_ads",
        "schedule": settings.scan_interval_seconds,
    },
}
celery_app.conf.timezone = "UTC"
