from .. import bot 
from telethon import events

language_codes = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Japanese': 'ja',
    'Chinese': 'zh',
    'Arabic': 'ar',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Urdu': 'ur',
    'Korean': 'ko',
    'Turkish': 'tr',
    'Dutch': 'nl',
    'Swedish': 'sv',
    'Polish': 'pl',
    'Norwegian': 'no',
    'Danish': 'da',
    'Finnish': 'fi',
    'Czech': 'cs',
    'Greek': 'el',
    'Hungarian': 'hu',
    'Thai': 'th',
    'Indonesian': 'id',
    'Vietnamese': 'vi',
    'Malay': 'ms',
    'Romanian': 'ro',
    'Hebrew': 'he',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Croatian': 'hr',
    'Serbian': 'sr',
    'Bulgarian': 'bg',
    'Ukrainian': 'uk',
    'Lithuanian': 'lt',
    'Latvian': 'lv',
    'Estonian': 'et',
    'Albanian': 'sq',
    'Macedonian': 'mk',
    'Tagalog': 'tl',
    'Swahili': 'sw',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Punjabi': 'pa',
    'Gujarati': 'gu',
    'Burmese': 'my',
    'Khmer': 'km',
    'Lao': 'lo'
}

@bot.on(events.NewMessage(incoming=True, pattern="/lancode ?(.*)"))
async def lancode(event):
    user_input = event.text.strip().split("/lancode")[1].strip()
    if user_input in language_codes:
        language_name = user_input
        language_code = language_codes[language_name]
        reply_message = f"The language code for **{language_name}** is **{language_code}**"
    else:
        reply_message = f"Sorry, I don't have the language code for **{user_input}**. Please ensure that you have written the language name correctly."
    await event.reply(reply_message)
"""async def lancode(event):
  user_input = event.text.strip()
  language_name = user_input.split("/lancode")[1]
  language_code = language_codes.get(language_name)
  if language_code in language_codes:
    reply_message = f"The language code for **{language_name}** is **{language_code}** "
  else:
    reply_message = f"Sorry, I don't have the languuge code for language **{language_name}**  please ensure that you have written the language name correctly"
  await event.reply(reply_message)"""