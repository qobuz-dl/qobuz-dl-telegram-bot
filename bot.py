import logging
from HelperFunc.readableTime import ReadableTime
from config import Config
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name='antispambot',
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=343,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        LOGGER.info(f"started with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        if Config.OWNER_ID != 0:
            try:
                await self.send_message(
                    text= "🇹🇷 Bot Restarted",
                    chat_id=Config.OWNER_ID)
            except Exception as t:
                LOGGER.error(str(t))

    async def stop(self, *args):
        if Config.OWNER_ID != 0:
            texto = f"\n\n🇹🇷 Bot Restarted: {ReadableTime(time.time() - Config.botStartTime)}"
            try:
                await self.send_message(text= texto,chat_id=Config.OWNER_ID)
            except Exception as t:
                LOGGER.warning(str(t))
        await super().stop()
        LOGGER.info(msg="App Stopped.")
        exit()

app = Bot()
app.run()
