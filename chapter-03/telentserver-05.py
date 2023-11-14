# telnetdemo.py
import asyncio
from asyncio import StreamReader, StreamWriter

async def send_event(msg: str):
    # handle the massege in the server code
    await asyncio.sleep(1)

async def echo(reader: StreamReader, writer: StreamWriter):
    print('New connection.')
    try:
        while (data := await reader.readline()):
            writer.write(data.upper())
            await writer.drain()
        print('Leaving Connection.')
    except asyncio.CancelledError:
        msg = 'Connection dropped!'
        # this task will be created after the run() gathered
        # all the task after connection drop, so it will throw an error
        asyncio.create_task(send_event(msg))

async def main(host='127.0.0.1', port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()

async def main(host='127.0.0.1', port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')
