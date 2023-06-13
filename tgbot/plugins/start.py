from .. import bot,openai_key
from telethon import events
import asyncio
import openai

openai.my_api_key = openai_key

@bot.on(events.NewMessage(incoming= True, pattern ="/help"))
async def start(event):
  await event.reply("You can translate text in diff languages using /tr command like,"
 "[ /tr <language code> text ], like"+
 "[ /tr hi How are you ]"+
 "And if you need to download audio use /yta "+
  "and for video use /ytv and followed by the link of it, like "+
 "[ /yta <link> ]"+
 "use /lancode command to get the language code of the desired language"+
 "[/lancode English]"+
 "for some extra queries use command /extra.")
  
  
  
@bot.on(events.NewMessage(incoming= True, pattern ="/start"))
async def start(event):
  a = await event.reply("Hello! This is Windy bot")
  await asyncio.sleep(2)
  await a.edit("Hello! This is Windy bot,"+
  "this bot can help you with language translation and audio/video download of any YouTube video using its link,"+
  "for further information, you can use   /help command.")
  
  
@bot.on(events.NewMessage(incoming= True, pattern ="/extra"))
async def start(event):
  await event.reply("If you search for something unrelated or unavailable content, it will not give any output and in some cases it may shkw some error, so please check your content before givig it to Windy.")
    