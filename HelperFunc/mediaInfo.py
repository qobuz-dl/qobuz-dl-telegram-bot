import logging
import subprocess
import json
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def get_media_info(path):
    try:
        result = subprocess.check_output(["ffprobe", "-hide_banner", "-loglevel", "error", "-print_format",
                                          "json", "-show_format", path]).decode('utf-8')
        fields = json.loads(result)['format']
    except Exception as e:
        LOGGER.info("mediainfo returned empty values.")
        return 0, None, None
    try:
        duration = round(float(fields['duration']))
    except Exception:
        duration = 0
    try:
        artist = str(fields['tags']['artist'])
    except Exception:
        artist = None
    try:
        title = str(fields['tags']['title'])
    except Exception:
        title = None
    LOGGER.info(f"ffprobe: duration: {duration} artist: {str(artist)} title: {str(title)}")
    return duration, artist, title
