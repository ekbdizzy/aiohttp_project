from aiohttp import web
import logging
import base64
from cryptography import fernet

from settings import Settings
from database.database import create_tables
from database.models import User, Permission


settings = Settings()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("main")


# Simple route handler
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)

# Add public routes
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)



# Startup event
async def on_startup(app):
    # Create database tables
    await create_tables()

    # Create default admin user
    # await create_default_admin()

    logger.info("Server started!")


app.on_startup.append(on_startup)

# For direct execution
if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)