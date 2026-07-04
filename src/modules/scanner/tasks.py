from src.core.celery_app import celery_app
from src.modules.scanner.scheduler import scan_and_store


@celery_app.task
def scan_p2p_ads():
    import asyncio
    asyncio.run(scan_and_store())
