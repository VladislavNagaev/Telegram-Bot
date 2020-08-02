import telebot

import block_1
import block_2
import block_3
import block_4
import block_5

name = 'Главное меню'.upper()

# Клавиатура раздела "Приветствие" (welcome)
keyboard_block_main = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard_block_main.row('/main', '/help')

# Сообщения раздела "Главный" (main)
main_message_1 = 'Выберите блок:'
main_message_2 = 'Помощь: /help'

# Кнопки данных (data) раздела "Главный" (main)
buttons_data = telebot.types.InlineKeyboardMarkup()

key_data_1_callback = 'block_main_key_1'
key_data_2_callback = 'block_main_key_2'
key_data_3_callback = 'block_main_key_3'
key_data_4_callback = 'block_main_key_4'
key_data_5_callback = 'block_main_key_5'

key_data_1 = telebot.types.InlineKeyboardButton(text=block_1.name, callback_data=key_data_1_callback)
key_data_2 = telebot.types.InlineKeyboardButton(text=block_2.name, callback_data=key_data_2_callback)
key_data_3 = telebot.types.InlineKeyboardButton(text=block_3.name, callback_data=key_data_3_callback)
key_data_4 = telebot.types.InlineKeyboardButton(text=block_4.name, callback_data=key_data_4_callback)
key_data_5 = telebot.types.InlineKeyboardButton(text=block_5.name, callback_data=key_data_5_callback)

buttons_data.add(key_data_1)
buttons_data.add(key_data_2)
buttons_data.add(key_data_3)
buttons_data.add(key_data_4)
buttons_data.add(key_data_5)