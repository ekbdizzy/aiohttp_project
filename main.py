from aiohttp import web
from settings import Settings

from database.database import create_tables
from database.models import User, Permission

settings = Settings()


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def main():
    await create_tables()

    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started at http://localhost:8080")
    return runner


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
