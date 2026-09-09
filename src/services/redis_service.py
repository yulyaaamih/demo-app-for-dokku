import redis.asyncio as redis

from src.config import settings

redis_conn = None


async def get_redis():
    global redis_conn

    if redis_conn is None:
        redis_conn = redis.Redis.from_url(settings.redis_url, decode_responses=True)

    return redis_conn


async def close_redis():
    global redis_conn

    if redis_conn is not None:
        await redis_conn.aclose()
        redis_conn = None
