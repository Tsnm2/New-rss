import os
from pyrogram import client
from config import Config

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )

    app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

    app.run()
