import asyncio
from contextlib import suppress


async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    try:
        f.set_result('I have finished.')
    except RuntimeError as e:
        print(f'No longer allowed: {e}')
        f.cancel() 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    fut = asyncio.Task(asyncio.sleep(5))
    loop.create_task(main(fut))
    
    with suppress(asyncio.CancelledError):
        loop.run_until_complete(fut)