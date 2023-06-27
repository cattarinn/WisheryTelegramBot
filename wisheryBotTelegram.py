from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot is online')
    
    
''''***************CLIENT***************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Any text')
        await message.delete()
    except:
        await message.reply('Any text')

    
''''***************ADMIN***************'''


''''***************GENERAL***************'''

@dp.message_handler()
async def echo_send(message: types.Message):
    pass
    # await message.answer('Any text')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
