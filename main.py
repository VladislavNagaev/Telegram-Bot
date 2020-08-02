import telebot
import os

import config
import command
import command_name
import help
import block_main
import block_1
import block_2
import block_3
import block_4
import block_5

# Запуск бота
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    """Реагирует на команду start"""

    bot.send_message(message.from_user.id, f'Добро пожаловать, {message.from_user.first_name}!')
    bot.send_message(message.from_user.id, command_name.welcome_message_2)
    bot.send_message(message.from_user.id, command_name.welcome_message_3)
    bot.send_message(message.from_user.id, command_name.welcome_message_4)
    bot.send_message(message.from_user.id, command_name.welcome_message_5, reply_markup=block_main.keyboard_block_main)

    try:

        # Сбор данных о пользователе
        status, folder_path = command.data_folder(folder_name=message.from_user.id)

        if not status == command_name.not_error:
            raise

        status = command.personal_data(folder_path=folder_path, message=message)

        if not status == command_name.not_error:
            raise

    except Exception:
        error_message = command.check_error_conditions(status=status)
        bot.send_message(message.from_user.id, error_message, reply_markup=help.keyboard_invalid_request)


@bot.message_handler(commands=['main'])
def main_command(message):
    """Реагирует на команду main"""
    bot.send_message(message.from_user.id, block_main.main_message_1, reply_markup=block_main.buttons_data)
    bot.send_message(message.from_user.id, block_main.main_message_2, reply_markup=block_main.keyboard_block_main)


@bot.message_handler(commands=['help'])
def help_command(message):
    """Реагирует на команду help"""
    bot.send_message(message.from_user.id, help.help_message_1)
    bot.send_message(message.from_user.id, help.help_message_2, reply_markup=help.keyboard_main)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """Реагирует на нажатия кнопок всех уровней"""

    # Обработчик нажатий на кнопки уровня block_main
    if call.data == block_main.key_data_1_callback:
        bot.send_message(call.message.chat.id, block_1.description, reply_markup=block_1.buttons)
    if call.data == block_main.key_data_2_callback:
        bot.send_message(call.message.chat.id, block_2.description, reply_markup=block_2.buttons)
    if call.data == block_main.key_data_3_callback:
        bot.send_message(call.message.chat.id, block_3.description, reply_markup=block_3.buttons)
    if call.data == block_main.key_data_4_callback:
        bot.send_message(call.message.chat.id, block_4.description, reply_markup=block_4.buttons)
    if call.data == block_main.key_data_5_callback:
        bot.send_message(call.message.chat.id, block_5.description, reply_markup=block_5.buttons)

    # Обработчик нажатий на кнопки уровня block_1
    if call.data == block_1.data_show_key_callback:
        bot.send_message(call.message.chat.id, block_1.data_show_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_1.data_entry_key_callback:
        bot.send_message(call.message.chat.id, block_1.data_entry_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_1.data_correct_key_callback:
        bot.send_message(call.message.chat.id, block_1.data_correct_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_1.data_delete_key_callback:
        bot.send_message(call.message.chat.id, block_1.data_delete_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    # Обработчик нажатий на кнопки уровня block_2
    if call.data == block_2.data_show_key_callback:
        bot.send_message(call.message.chat.id, block_2.data_show_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_2.data_entry_key_callback:
        bot.send_message(call.message.chat.id, block_2.data_entry_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_2.data_correct_key_callback:
        bot.send_message(call.message.chat.id, block_2.data_correct_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_2.data_delete_key_callback:
        bot.send_message(call.message.chat.id, block_2.data_delete_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    # Обработчик нажатий на кнопки уровня block_3
    if call.data == block_3.data_show_key_callback:
        bot.send_message(call.message.chat.id, block_3.data_show_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_3.data_entry_key_callback:
        bot.send_message(call.message.chat.id, block_3.data_entry_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_3.data_correct_key_callback:
        bot.send_message(call.message.chat.id, block_3.data_correct_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_3.data_delete_key_callback:
        bot.send_message(call.message.chat.id, block_3.data_delete_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    # Обработчик нажатий на кнопки уровня block_4
    if call.data == block_4.data_show_key_callback:
        bot.send_message(call.message.chat.id, block_4.data_show_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_4.data_entry_key_callback:
        bot.send_message(call.message.chat.id, block_4.data_entry_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_4.data_correct_key_callback:
        bot.send_message(call.message.chat.id, block_4.data_correct_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_4.data_delete_key_callback:
        bot.send_message(call.message.chat.id, block_4.data_delete_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    # Обработчик нажатий на кнопки уровня block_5
    if call.data == block_5.data_XX1_key_callback:
        bot.send_message(call.message.chat.id, block_5.data_XX1_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    if call.data == block_5.data_XX2_key_callback:
        bot.send_message(call.message.chat.id, block_5.data_XX2_description,
                         reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(content_types=["document"])
def entry_check(message):
    """Обрабатывает и записывает присланые чеки"""

    try:

        document_id = message.document.file_id
        file_info = bot.get_file(document_id)
        file = bot.download_file(file_info.file_path)

        # Возвращает список словарей для записи
        status, check = command.get_check(json_file=file)
        if not status == command_name.not_error:
            raise

        # Возвращает путь к папке для сохранения
        status, folder_path = command.data_folder(folder_name=message.from_user.id)
        if not status == command_name.not_error:
            raise

        # Возвращает дирректорию рабочего файла
        file_path = command.data_file(folder_path=folder_path, title=command_name.title_operating_loss)

        for data in check:

            # Возвращает свободный id позиции
            status, name_identifier = command.uniqueness_identifier(file_path=file_path)
            if not status == command_name.not_error:
                raise

            # Добавляет уникальный идентификатор к позиции
            data[command_name.feature_id] = name_identifier

            # Производит запись данных
            status = command.data_recording(data=data, file_path=file_path)
            if not status == command_name.not_error:
                raise

        bot.send_message(message.from_user.id, command_name.message_success_recording, reply_markup=help.keyboard_invalid_request)

    except Exception:
        error_message = command.check_error_conditions(status=status)
        bot.send_message(message.from_user.id, error_message, reply_markup=help.keyboard_invalid_request)


@bot.message_handler(content_types=['text'])
def request_handler(message):
    """Принимает тексстовое чообщение. Проверяет на присутствие выделенной команды.
    В случае определения запроса на команду - вызывает соответствующуйю функцию. Иначе - выдает сообщение об ошибке."""

    try:
        status, operation, title, data = command.data_parse(text=message.text)
        if not status == command_name.not_error:
            raise

        status, operation = command.define_status(operation=operation)
        if not status == command_name.not_error:
            raise

        status, title = command.define_title(title=title)
        if not status == command_name.not_error:
            raise

        # Возвращает путь к папке для сохранения
        status, folder_path = command.data_folder(folder_name=message.from_user.id)
        if not status == command_name.not_error:
            raise

        # Возвращает дирректорию рабочего файла
        file_path = command.data_file(folder_path=folder_path, title=title)

        if operation == command_name.show:

            status, display = command.show_data_constructor(file_path=file_path, data=data,
                                                            current_datetime=message.date)

            if not status == command_name.not_error:
                raise

            for i in display.index:
                data = dict(zip(list(display.columns), list(display.iloc[i].values)))

                # Преобразует данные в формат для вывода
                show_data = command.reverse_conversion(data)

                bot.send_message(message.from_user.id, show_data, reply_markup=help.keyboard_invalid_request)

        elif operation == command_name.entry:

            status, data = command.entry_data_constructor(title=title, data=data, current_datetime=message.date)

            if not status == command_name.not_error:
                raise

            # Возвращает свободный id позиции
            status, name_identifier = command.uniqueness_identifier(file_path=file_path)
            if not status == command_name.not_error:
                raise

            # Добавляет уникальный идентификатор к позиции
            data[command_name.feature_id] = name_identifier

            # Производит запись данных
            status = command.data_recording(data=data, file_path=file_path)
            if not status == command_name.not_error:
                raise

            bot.send_message(message.from_user.id, command_name.message_success_recording,
                             reply_markup=help.keyboard_invalid_request)

        elif operation == command_name.delete:
            pass

        else:
            status = command_name.error
            raise

    except Exception:
        error_message = command.check_error_conditions(status=status)
        bot.send_message(message.from_user.id, error_message, reply_markup=help.keyboard_invalid_request)


bot.polling(none_stop=True)
