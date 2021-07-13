import os

class Config(object):
  API_ID = int(os.environ.get("API_ID"))
  API_HASH = os.environ.get("API_HASH")
  FEED_URLS = list(set(i for i in os.environ.get("FEED_URLS").split("|")))
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
  INTERVAL = int(os.environ.get("INTERVAL", 10))
  MAX_INSTANCES = int(os.environ.get("MAX_INSTANCES", 3))
