import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = 
    API_HASH = ""
    BOT_TOKEN = ""
    BOT_USERNAME = ""
    OWNER_ID = 
    AUTH_IDS = []
    QOBUZ_MAIL = ""
    HEROKU_APP_NAME = "xxxx" # dont touch
    HEROKU_API_KEY = "xxxx" # dont touch
    QOBUZ_PASS = ""
    QOBUZ_QUAL = 
    UPDATE_ALL = True
    LOG_CHANNEL = []
    botStartTime = time.time() # dont touch