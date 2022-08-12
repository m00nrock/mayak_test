from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

input_file = KeyboardButton('Загрузить файл')
cancel = KeyboardButton('Отмена')


file = ReplyKeyboardMarkup(resize_keyboard=True).add(input_file)
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel)
