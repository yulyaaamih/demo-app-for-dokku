from src.services.redis_service import get_redis


async def register_visit(endpoint: str):
    conn = await get_redis()

    return await conn.incr(endpoint)


async def get_visits(endpoint: str):
    conn = await get_redis()
    value = await conn.get(endpoint)

    return int(value) if value is not None else 0
