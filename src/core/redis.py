from redis.asyncio import from_url

from src.core.config import settings

redis_client = from_url(settings.redis_url, decode_responses=True)
