from telethon import TelegramClient
import logging
import time 

openai_key=""

api_id = ""
api_hash = ""
bot_token = ""

bot  =TelegramClient("Windy", api_id, api_hash).start(bot_token=bot_token)
