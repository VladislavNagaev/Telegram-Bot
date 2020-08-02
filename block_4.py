import telebot

import config
import command_name

name = 'Текущий доход и убыток'.upper()

description = name

# Кнопки блоков уровня block_4
buttons = telebot.types.InlineKeyboardMarkup()

data_show_key_name = 'Отображение введенных данных'
data_entry_key_name = 'Ввод новых данных'
data_correct_key_name = 'Корректировка данных'
data_delete_key_name = 'Удаление данных'

data_show_key_callback = 'block_4_data_show'
data_entry_key_callback = 'block_4_data_entry'
data_correct_key_callback = 'block_4_data_correct'
data_delete_key_callback = 'block_4_data_delete'

data_show_key = telebot.types.InlineKeyboardButton(text=data_show_key_name, callback_data=data_show_key_callback)
data_entry_key = telebot.types.InlineKeyboardButton(text=data_entry_key_name, callback_data=data_entry_key_callback)
data_correct_key = telebot.types.InlineKeyboardButton(text=data_correct_key_name, callback_data=data_correct_key_callback)
data_delete_key = telebot.types.InlineKeyboardButton(text=data_delete_key_name, callback_data=data_delete_key_callback)

buttons.add(data_show_key)
buttons.add(data_entry_key)
buttons.add(data_correct_key)
buttons.add(data_delete_key)

data_show_description = (
    'Шаблон вывода данных:'
    f'\n\nОперация Раздел Критерий_вывода Знак_сравнения Величина_критерия' 
    '\n\nПримеры ввода:'
    '\n\nПоказать текущий_доход все'
    '\n\nПоказать текущий_убыток дата<вчера' 
    '\n\nПоказать тек.доход величина>=200'
    '\n\nПоказать тек.убыток id=2'
)

data_entry_description = (
    'Шаблон ввода данных:'
    f'\n\nОперация Раздел Наименование Дата_поступления Величина Валюта'
    '\n\nПримеры ввода:'    
    f'\n\nдобавить текущий_доход Премия сегодня 500 евро'
    f'\n\nДобавить текущий_убыток ПокупкаТелевизора позавчера 1300 долл'
    f'\n\nдобавить тек.убыток чек_пятерочка 25.03.2020 1300 рублей'
)

data_delete_description = (
    'test'
)

data_download_description = (
    'test'
)

data_unload_description = (
    'test'
)