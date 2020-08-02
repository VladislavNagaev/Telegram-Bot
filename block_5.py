import telebot

import config
import command_name

name = 'Финансовая статистика'.upper()

title_1 = 'statistics_income'.lower()       # Статистика доходв
title_2 = 'statistics_expense'.lower()      # Статистика расходов
title_3 = 'statistics_balance'.lower()      # Статистика сальдо

description = name


# Кнопки блоков уровня block_5
buttons = telebot.types.InlineKeyboardMarkup()

data_XX1_key_name = 'Статистика 1'
data_XX2_key_name = 'Статистика 2'

data_XX1_key_callback = 'block_5_key_1'
data_XX2_key_callback = 'block_5_key_2'

data_XX1_key = telebot.types.InlineKeyboardButton(text=data_XX1_key_name, callback_data=data_XX1_key_callback)
data_XX2_key = telebot.types.InlineKeyboardButton(text=data_XX2_key_name, callback_data=data_XX2_key_callback)

buttons.add(data_XX1_key)
buttons.add(data_XX2_key)

data_XX1_description = (
    'test'
)

data_XX2_description = (
    'test'
)