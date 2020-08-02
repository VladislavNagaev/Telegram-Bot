import telebot

import command_name

name = 'Инвестиции'.upper()

description = name

# Кнопки блоков уровня block_2
buttons = telebot.types.InlineKeyboardMarkup()

data_show_key_name = 'Отображение введенных данных'
data_entry_key_name = 'Ввод новых данных'
data_correct_key_name = 'Корректировка данных'
data_delete_key_name = 'Удаление данных'

data_show_key_callback = 'block_2_data_show'
data_entry_key_callback = 'block_2_data_entry'
data_correct_key_callback = 'block_2_data_correct'
data_delete_key_callback = 'block_2_data_delete'

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
    '\n\nПоказать инвестиции все'
    '\n\nПоказать инвестиции дата<вчера' 
    '\n\nПоказать инв. стоимость>=200'
    '\n\nПоказать мц id=2'
)

data_entry_description = (
    'Шаблон ввода данных:'
    f'\n\nОперация Раздел Наименование Дата_оценки Оценочная_стоимость Валюта'
    '\n\nПримеры ввода:'    
    f'\n\nдобавить инвестиции БанковскийДепозит_ВТБ 01.12.17 800 долларов'
    f'\n\nДобавить инвестицию Банковский_вклад_Сбер 25/04/2020 1100000 рубл'
    f'\n\nдобавить инв. Акции_Facebook вчера 1900 EUR'
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