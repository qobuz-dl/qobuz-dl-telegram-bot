from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
import logging
from HelperFunc.messageFunc import sendDocument
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
from config import Config

@Client.on_message(filters.command("log"))
def log(bot, message: Message):
    if Config.OWNER_ID == 0 or message.from_user.id != Config.OWNER_ID:
        return
    sendDocument(message, "log.txt")
