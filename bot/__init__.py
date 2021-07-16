from os import getenv
import pyrogram


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
LOG_CHANNEL = int(getenv("LOG_CHANNEL"))

INTERVAL = int(getenv("INTERVAL", 10))
MAX_INSTANCES = int(getenv("MAX_INSTANCES", 3))
FEED_URLS = list(set(getenv("FEED_URLS", "").split("|")))

plugins = dict(
    root="bot/plugins"
)

app = pyrogram.Client(
    "RSSBOT",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins
)