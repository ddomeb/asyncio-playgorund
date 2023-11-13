import asyncio

from contextlib import asynccontextmanager
from time import sleep

def download_webpage(url):
    # blocking and time consuming code
    print('downloading page')
    sleep(2)
    print('downloaded page')
    return url

def update_stats(url):
    # blocking and time consuming code
    print('processing data')
    sleep(2)
    print('processed data')

@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, download_webpage, url)
    yield data
    await loop.run_in_executor(None, update_stats, url)

async def main():
    async with web_page('google.com') as data:
        print(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
    loop.close()
