import time
import asyncio
import os
import threading

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye! {threading.current_thread().ident}')

def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread! {threading.current_thread().ident}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    
    loop.run_in_executor(None, blocking)
    loop.run_until_complete(task)

    pending = asyncio.all_tasks(loop=loop)
    for task in pending:
        task.cancel()

    group = asyncio.gather(*pending, return_exceptions=True)

    loop.run_until_complete(group)
    loop.close()