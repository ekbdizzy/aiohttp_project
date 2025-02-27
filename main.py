from importlib import reload

from aiohttp import web
import logging
import asyncio

from settings import Settings
from database.database import create_tables
from database.models import User, Permission

settings = Settings()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("main")

app = web.Application()


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


# Add routes
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)


# Startup event
async def on_startup(app):
    await create_tables()
    logger.info("Server started!")


app.on_startup.append(on_startup)

# For direct execution
if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)
