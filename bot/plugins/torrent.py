from pyrogram import Client, filters

@Client.on_message(filters.document)
async def torrent(client, message):
    if message.document.mime_type == "application/x-bittorrent":
        await message.reply("/leech")
