from telethon import TelegramClient
import logging
import time 

openai_key="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"

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "5881651112:AAFGbvzUPhhuuB9forFptXMKgWuYq_wdSHk"

bot  =TelegramClient("Windy", api_id, api_hash).start(bot_token=bot_token)