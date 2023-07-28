from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

button1 = InlineKeyboardButton('Home', callback_data='button1')
button2 = InlineKeyboardButton('Abouot Us', callback_data='button2')
button3 = InlineKeyboardButton('Help', callback_data='button3')

markup1 = InlineKeyboardMarkup().add(button1, button2, button3)

button4 = ['left']
button5 = ['right']

markup2 = ReplyKeyboardMarkup([button4, button5])

