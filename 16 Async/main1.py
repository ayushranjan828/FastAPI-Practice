import time
import asyncio

async def task():
    await asyncio.sleep(4)
    return "Done Async"

print(asyncio.run(task()))