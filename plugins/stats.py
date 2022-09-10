from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
import logging
import time
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.folderSize import get_size
from HelperFunc.messageFunc import sendMessage
from HelperFunc.readableTime import ReadableTime
from psutil import disk_usage, cpu_percent, swap_memory, cpu_count, virtual_memory, net_io_counters
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
from config import Config


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        n += 1
    return f"{str(round(size, 2))} {Dic_powerN[n]}B"

@Client.on_message(filters.command("status"))
def stats(bot, message:Message):
    if not AuthUserCheck(message): return
    currentTime = ReadableTime(time.time() - Config.botStartTime)
    total, used, free, disk= disk_usage('/')
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(net_io_counters().bytes_sent)
    recv = humanbytes(net_io_counters().bytes_recv)
    cpuUsage = cpu_percent(interval=0.5)
    p_core = cpu_count(logical=False)
    t_core = cpu_count(logical=True)
    swap = swap_memory()
    swap_p = swap.percent
    swap_t = humanbytes(swap.total)
    swap_u = humanbytes(swap.used)
    swap_f = humanbytes(swap.free)
    memory = virtual_memory()
    mem_p = memory.percent
    mem_t = humanbytes(memory.total)
    mem_a = humanbytes(memory.available)
    mem_u = humanbytes(memory.used)
    stats = f'<b>Bot Uptime:</b> {currentTime}\n'\
        f'<b>Disk:</b> {total} | <b>Used:</b> {used} | <b>Free:</b> {free}\n' \
        f'<b>Memory:</b> {mem_t} | <b>Used:</b> {mem_u} | <b>Free:</b> {mem_a}\n' \
        f'<b>Cores:</b> {t_core} | <b>Physical:</b> {p_core} | <b>Logical:</b> {t_core - p_core}\n' \
        f'<b>SWAP:</b> {swap_t} | <b>Used:</b> {swap_u}% | <b>Free:</b> {swap_f}\n'\
        f'<b>DISK:</b> {disk}% | <b>RAM:</b> {mem_p}% | <b>CPU:</b> {cpuUsage}% | | <b>SWAP:</b> {swap_p}%\n' \
        f'<b>Total Upload:</b> {sent}\n' \
        f'<b>Total Download:</b> {recv}\n\n' \
        "🔻 Currently Downloaded Music: " + humanbytes(get_size("qobuzdown"))
    a = sendMessage(message, stats)
    time.sleep(30)
    a.delete()
    message.delete()
