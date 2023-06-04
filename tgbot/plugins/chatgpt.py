from telethon import events
from .. import bot,openai_key
import asyncio,openai

openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern ="(?i)/ask"))

async def gpt(event):
  if event.sender_id==int(5301566463):
    await event.reply("Hello Developer")
  else:
    await event.reply("Hello User")