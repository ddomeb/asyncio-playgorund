import asyncio
from aioredis import Redis, create_redis


async def process(value):
    asyncio.wait(5)
    print(value)

async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['Americas', 'Africa', 'Europe', 'Asia']
    async for value in OneAtATime(redis, keys):
        await process(value)

class OneAtATime:
    def __init__(self, redis, keys):
        self.redis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration

        value = await Redis.get(k)
        return value

asyncio.run(main())
