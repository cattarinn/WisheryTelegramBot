from aiogram import types, Dispatcher
import json
import string
from create_bot import dp

#@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('C:\\for_bots\\WisheryBotTelegram\\curse_words.json')))) != set():
        await message.reply('Curse words are not allowed.')
        await message.delete()

def register_handlers_general(dp : Dispatcher):
    dp.register_message_handler(echo_send)
