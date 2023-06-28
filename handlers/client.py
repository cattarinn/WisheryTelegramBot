from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import kb_client

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hi', reply_markup=kb_client)
        await message.delete()
    except Exception as e:
        await message.reply('Any text')

async def wishery_info(message : types.Message):
    await bot.send_message(message.from_user.id, "🌟 Welcome to Wishery! 🌟\n\nI'm here to assist you in capturing and preserving your cherished wishes. Just share your wishes with me, and I'll make sure they're stored securely. You can revisit them whenever you like.")


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(wishery_info, commands=['About'])
    #dp.register_message_handler()