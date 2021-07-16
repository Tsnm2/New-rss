import os
from pyrogram import Client
from config import Config

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "RSSBOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
