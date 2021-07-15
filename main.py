import os
from pyrogram import Client
from config import Config

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )

    app = Client(":memory:", bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,)

    app.run()
