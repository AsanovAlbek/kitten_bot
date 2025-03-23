from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
get_kitten_button = types.KeyboardButton("Дай котика")
get_speaking_kitten_button = types.KeyboardButton("Дай говорящего котика")
markup.add(get_kitten_button, get_speaking_kitten_button)