from pyrogram.types.messages_and_media.message import Message
from config import Config

def AuthUserCheck(message: Message):
    if 0 in Config.AUTH_IDS:
        return True
    elif message.from_user.id in Config.AUTH_IDS:
        return True
    elif message.chat.id in Config.AUTH_IDS:
        return True
    else:
        return False
