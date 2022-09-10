import os
import shutil
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
import logging, heroku3
from HelperFunc.messageFunc import sendMessage
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
from config import Config

@Client.on_message(filters.command("reset"))
def restart(client, message: Message):
    if Config.OWNER_ID == 0 or message.from_user.id != Config.OWNER_ID: return
    cmd = message.text.split(' ', 1)
    dynoRestart = False
    dynoKill = False
    if len(cmd) == 2:
        dynoRestart = (cmd[1].lower()).startswith('d')
        dynoKill = (cmd[1].lower()).startswith('k')
    if (not Config.HEROKU_API_KEY) or (not Config.HEROKU_APP_NAME):
        LOGGER.info("If you want Heroku features, fill Config.HEROKU_APP_NAME Config.HEROKU_API_KEY vars.")
        dynoRestart = False
        dynoKill = False
    if dynoRestart:
        LOGGER.info("Dyno Restarting.")
        message.reply_text('Dyno Restarting.')
        heroku_conn = heroku3.from_key(Config.HEROKU_API_KEY)
        app = heroku_conn.app(Config.HEROKU_APP_NAME)
        app.restart()
    elif dynoKill:
        LOGGER.info("Killing Dyno. MUHAHAHA")
        message.reply_text('Killing Dyno')
        heroku_conn = heroku3.from_key(Config.HEROKU_API_KEY)
        app = heroku_conn.app(Config.HEROKU_APP_NAME)
        proclist = app.process_formation()
        for po in proclist: app.process_formation()[po.type].scale(0)
    else:
        try: shutil.rmtree("qobuzdown")
        except: pass
        os.remove("calisiyor.txt") if os.path.isfile("calisiyor.txt") else print("ok")
        toSendStr = "🇹🇷 Restarted."
        sendMessage(message, toSendStr)
