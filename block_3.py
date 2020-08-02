import telebot

import command_name

name = 'Прогнозируемый доход и убыток'.upper()

description = name


# Кнопки блоков уровня block_3
buttons = telebot.types.InlineKeyboardMarkup()

data_show_key_name = 'Отображение введенных данных'
data_entry_key_name = 'Ввод новых данных'
data_correct_key_name = 'Корректировка данных'
data_delete_key_name = 'Удаление данных'

data_show_key_callback = 'block_3_data_show'
data_entry_key_callback = 'block_3_data_entry'
data_correct_key_callback = 'block_3_data_correct'
data_delete_key_callback = 'block_3_data_delete'

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
    '\n\nПоказать прогнозируемый_доход все'
    '\n\nПоказать прогнозируемый_убыток дата<вчера' 
    '\n\nПоказать прогн.доход величина>=200'
    '\n\nПоказать прогн.убыток id=2'
)

data_entry_description = (
    'Шаблон ввода данных:'
    f'\n\nОперация Раздел Наименование Дата_начала_поступления Дата_окончания_поступления Периодичность_поступления Величина Валюта'
    '\n\nПримеры ввода:'    
    f'\n\nдобавить прогнозируемый_доход Зарплата 01.01.15 бессрочно ежемесячно 120000 руб'
    f'\n\nДобавить прогнозируемый_убыток Подписка_YouTube 24/11/2019 бессрочно месяц=1 199 рубл'
    f'\n\nдобавить прогн.убыток ВыплатаПоКредиту сегодня 25.03.2021 неделя=6 15000 рублей'
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