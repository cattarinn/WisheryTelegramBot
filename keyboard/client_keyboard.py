from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('/About')
# b2 = KeyboardButton('')
# b3 = KeyboardButton('')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1)
