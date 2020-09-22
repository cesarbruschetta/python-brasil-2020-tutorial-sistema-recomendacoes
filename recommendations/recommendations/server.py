import connexion
import aiohttp
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    app = connexion.AioHttpApp(__name__, port=8000)
    app._only_one_api = True
    app._api_added = False
    app.add_api("recommendations.openapi")
    aiohttp.web.run_app(app.app, port=8000, access_log=logger)
