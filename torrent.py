import os

import asyncio

import pyrogram

from pyrogram import Client, filters

@pyrogram.Client.on_message(filters.document)

async def torrent(bot, update):

  await bot.send_message(

    chat_id=update.chat.id,

    text="/leech",

    reply_to_message_id=update.message_id

  )
