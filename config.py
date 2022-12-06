import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    OWNER_ID = int(os.environ.get('OWNER_ID', "")) # give your owner id # if given 0 shell will not works
    AUTH_IDS = [int(x) for x in os.environ.get("AUTH_IDS", "0").split()] # if open to everyone give 0
    AUTH_IDS.append(OWNER_ID)
    QOBUZ_MAIL = os.environ.get("QOBUZ_MAIL", "")
    QOBUZ_PASS = os.environ.get("QOBUZ_PASS", "")
    QOBUZ_QUAL = int(os.environ.get("QOBUZ_QUAL", 27))
    HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY', None)
    HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME', None)
    UPDATE_ALL = bool(os.environ.get("UPDATE_ALL", True))
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
    botStartTime = time.time() # dont touch
