import telebot

import command_name

name = 'Материальные ценности'.upper()

description = name

# Кнопки блоков уровня block_1
buttons = telebot.types.InlineKeyboardMarkup()

data_show_key_name = 'Отображение введенных данных'
data_entry_key_name = 'Ввод новых данных'
data_correct_key_name = 'Корректировка данных'
data_delete_key_name = 'Удаление данных'

data_show_key_callback = 'block_1_data_show'
data_entry_key_callback = 'block_1_data_entry'
data_correct_key_callback = 'block_1_data_correct'
data_delete_key_callback = 'block_1_data_delete'

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
    '\n\nПоказать материальные_ценности все'
    '\n\nПоказать мат.ценн. дата<вчера' 
    '\n\nПоказать м.ц. стоимость>=200'
    '\n\nПоказать мц id=2'
)

data_entry_description = (
    'Шаблон ввода данных:'
    f'\n\nОперация Раздел Наименование Дата_оценки Оценочная_стоимость Валюта'
    '\n\nПримеры ввода:'    
    f'\n\nДобавить материальную_ценность Наличные 25.07.2020 5000 долларов'
    f'\n\nДобавить мат.ценн. Квартира_в_Тушино 12/01/98 12000000 руб'
    f'\n\nдобавить м.ц. Машина_Reno сегодня 7000 евро'
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