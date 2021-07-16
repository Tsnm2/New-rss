import feedparser
from sql import db
from time import sleep
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler

from bot import app, FEED_URLS, LOG_CHANNEL, INTERVAL, MAX_INSTANCES

for feed_url in FEED_URLS:
    if db.get_link(feed_url) == None:
        db.update_link(feed_url, "*")

def create_feed_checker(feed_url):
    def check_feed():
        FEED = feedparser.parse(feed_url)
        entry = FEED.entries[0]
        enid = entry.id
        if entry.id != db.get_link(feed_url).link:
                       # ↓ Edit this message as your needs.
            if "eztv.re" in enid:   
                message = f"{entry.torrent_magneturi}"
            elif "yts.mx" in enid:
                message = f"{entry.links[1]['href']}"
            else:
                message = f"{entry.link}"
            try:
                msg = app.send_message(LOG_CHANNEL, message)
                msg.reply_text("/leech@jarvisleechbot")
                db.update_link(feed_url, entry.id)
                
            except FloodWait as e:
                print(f"FloodWait: {e.x} seconds")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"Checked RSS FEED: {entry.id}")
    return check_feed


scheduler = BackgroundScheduler()
for feed_url in FEED_URLS:
    feed_checker = create_feed_checker(feed_url)
    scheduler.add_job(feed_checker, "interval", seconds=INTERVAL, max_instances=MAX_INSTANCES)
scheduler.start()
