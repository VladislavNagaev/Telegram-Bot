import csv
import os
from datetime import datetime
from dateutil.parser import parse
import re
from dateutil.relativedelta import relativedelta
import json
from pandas import read_csv

import config
import block_1
import block_2
import block_3
import block_4
import block_5
import command_name


def data_parse(text):
    """Расшифровывает запрос. Возвращает операцию, блок ввода, данные/условия"""

    try:

        text_list = list(map(lambda x: x.strip(), text.split(' ')))
        operation = text_list[0].lower()
        title = text_list[1]
        data = text_list[2:]

        return command_name.not_error, operation, title, data

    except Exception:
        return command_name.input_error, None, None, None


def define_status(operation):
    """Определяет запрошенную операцию."""

    operation = re.sub(r'[^\w\s]', '', operation.lower())

    if operation in command_name.show_list:
        operation = command_name.show

    elif operation in command_name.entry_list:
        operation = command_name.entry

    elif operation in command_name.delete_list:
        operation = command_name.delete

    else:
        return command_name.command_error, None

    return command_name.not_error, operation


def define_title(title):
    """Определяет запрошенный раздел."""

    title = re.sub(r'[^\w\s]', '', title.lower())

    if title in command_name.title_wealth_list:
        title = command_name.title_wealth

    elif title in command_name.title_investment_list:
        title = command_name.title_investment

    elif title in command_name.title_anticipated_revenue_list:
        title = command_name.title_anticipated_revenue

    elif title in command_name.title_anticipated_loss_list:
        title = command_name.title_anticipated_loss

    elif title in command_name.title_operating_revenue_list:
        title = command_name.title_operating_revenue

    elif title in command_name.title_operating_loss_list:
        title = command_name.title_operating_loss

    elif title in command_name.title_statistics_income_list:
        title = command_name.title_statistics_income

    elif title in command_name.title_statistics_expense_list:
        title = command_name.title_statistics_expense

    elif title in command_name.title_statistics_balance_list:
        title = command_name.title_statistics_balance

    else:
        return command_name.title_error, None

    return command_name.not_error, title


def check_error_conditions(status):
    """Проверяет статус в случае ошибки. Возвращает сообщение для вывода."""

    if status == command_name.success_recording:
        message_for_print = command_name.message_success_recording

    elif status == command_name.command_error:
        message_for_print = command_name.message_command_error

    elif status == command_name.invalid_request:
        message_for_print = command_name.message_invalid_request

    elif status == command_name.input_error:
        message_for_print = command_name.message_input_error

    elif status == command_name.count_error:
        message_for_print = command_name.message_count_error

    elif status == command_name.title_error:
        message_for_print = command_name.message_title_error

    elif status == command_name.data_error:
        message_for_print = command_name.message_data_error

    elif status == command_name.query_result_error:
        message_for_print = command_name.message_query_result_error

    elif status == command_name.date_error:
        message_for_print = command_name.message_date_error

    elif status == command_name.date_inconsistency_error:
        message_for_print = command_name.message_date_inconsistency_error

    elif status == command_name.exchange_error:
        message_for_print = command_name.message_exchange_error

    elif status == command_name.value_error:
        message_for_print = command_name.message_value_error

    elif status == command_name.periodicity_error:
        message_for_print = command_name.message_periodicity_error

    elif status == command_name.write_error:
        message_for_print = command_name.message_write_error

    elif status == command_name.path_error:
        message_for_print = command_name.message_path_error

    elif status == command_name.condition_error:
        message_for_print = command_name.message_condition_error

    elif status == command_name.condition_name_error:
        message_for_print = command_name.message_condition_name_error

    elif status == command_name.condition_id_error:
        message_for_print = command_name.message_condition_id_error

    elif status == command_name.condition_date_error:
        message_for_print = command_name.message_condition_date_error

    elif status == command_name.condition_date_end_error:
        message_for_print = command_name.message_condition_date_end_error

    elif status == command_name.check_error:
        message_for_print = command_name.message_check_error

    elif status == command_name.parenthesis_count_error:
        message_for_print = command_name.message_parenthesis_count_error

    elif status == command_name.error:
        message_for_print = command_name.message_error

    else:
        message_for_print = status

    return message_for_print


def entry_data_constructor(title, data, current_datetime):
    """Обрабатывает введенное сообщение, возвоащает словарь для записи."""

    try:
        # Возвращает словарь для записи данных
        status, data = get_data(title=title, data=data)
        if not status == command_name.not_error:
            raise

        # Возвращает отформатированную дату
        if command_name.feature_date in data:
            status, date = get_datetime(date=data[command_name.feature_date], current_datetime=current_datetime)

            if not status == command_name.not_error:
                raise

            # Замена даты в словаре для записи на отформатированную
            data[command_name.feature_date] = date

        # Возвращает отформатированную дату
        if command_name.feature_date_end in data:
            status, date = get_datetime(date=data[command_name.feature_date_end], current_datetime=current_datetime)

            if not status == command_name.not_error:
                raise

            # Замена даты в словаре для записи на отформатированную
            data[command_name.feature_date_end] = date

        # Возвращает откорректированное значение валюты
        status, exchange = get_exchange(exchange=data[command_name.feature_exchange])
        if not status == command_name.not_error:
            raise

        # Замена валюты в словаре для записи на отформатированную
        data[command_name.feature_exchange] = exchange

        # Возвращает откорректированное значение суммы
        status, value = get_value(value=data[command_name.feature_value])
        if not status == command_name.not_error:
            raise

        # Замена значения суммы в словаре для записи на отформатированное
        data[command_name.feature_value] = value

        # Возвращает откорректированное значение периодичности
        if title == command_name.title_anticipated_loss or title == command_name.title_anticipated_revenue:
            status, periodicity = get_periodicity(periodicity=data[command_name.feature_periodicity])

            if not status == command_name.not_error:
                raise

            # Замена периодичности в словаре для записи на отформатированную
            data[command_name.feature_periodicity] = periodicity

            # Проверка корректности указания даты старта и даты окончания
            if not data[command_name.feature_date_end] == command_name.indefinitely_datetime:
                if not data[command_name.feature_date] < data[command_name.feature_date_end]:
                    return command_name.date_inconsistency_error, None

        return command_name.not_error, data

    except Exception:
        return status, None


def get_data(title, data):
    """Принимает раздел и данные. Возвращает словарь для записи данных"""

    if title == command_name.title_wealth:
        columns = command_name.wealth_columns

    elif title == command_name.title_investment:
        columns = command_name.investment_columns

    elif title == command_name.title_anticipated_revenue:
        columns = command_name.anticipated_revenue_columns

    elif title == command_name.title_anticipated_loss:
        columns = command_name.anticipated_loss_columns

    elif title == command_name.title_operating_revenue:
        columns = command_name.operating_revenue_columns

    elif title == command_name.title_operating_loss:
        columns = command_name.operating_loss_columns

    else:
        return command_name.error, None

    if len(columns) == len(data):
        new_data = dict(zip(columns, data))
        return command_name.not_error, new_data

    else:
        return command_name.count_error, None


def get_datetime(date, current_datetime):
    """Проверяет дату и производит форматирование. Возвращает отформатированную дату."""

    if str(date) in command_name.current_datetime_list:
        date = current_datetime
    elif str(date) in command_name.yesterday_datetime_list:
        date = int((datetime.fromtimestamp(current_datetime) - relativedelta(days=1)).timestamp())
    elif str(date) in command_name.day_before_yesterday_datetime_list:
        date = int((datetime.fromtimestamp(current_datetime) - relativedelta(days=2)).timestamp())
    elif str(date) in command_name.indefinitely_datetime_list:
        date = command_name.indefinitely_datetime
    else:
        try:
            date = int(parse(date).timestamp())
        except Exception:
            return command_name.date_error, None

    return command_name.not_error, date


def get_exchange(exchange):
    """"Валюту. Проверят соответствие валюты шаблонам. Возвращает откорректированное значение валюты."""

    exchange = re.sub(r'₽$€[^\w\s]', '', exchange.lower())

    if exchange in command_name.exchange_ruble_list:
        exchange = command_name.exchange_ruble
    elif exchange in command_name.exchange_dollar_list:
        exchange = command_name.exchange_dollar
    elif exchange in command_name.exchange_euro_list:
        exchange = command_name.exchange_euro
    else:
        return command_name.exchange_error, None

    return command_name.not_error, exchange


def get_value(value):
    """Принимает значение суммы. Проверяет соответствие значения суммы int или float.
    Возвращает откорректированное значение суммы."""

    value = re.sub(r',.[^\w\s]', '', value.lower())
    value = value.replace(',', '.')

    try:
        value = float(value)
    except Exception:
        return command_name.value_error, None

    return command_name.not_error, value


def get_periodicity(periodicity):
    """Принимает периодичность. Возвращает откорректированное значение периодичности."""

    periodicity = periodicity.split('=')

    periodicity = list(map(lambda x: re.sub(r'[^\w\s]', '', x.lower()), periodicity))

    if len(periodicity) == 1:
        time = periodicity[0]
        time_count = int(1)
    elif len(periodicity) == 2:
        try:
            time = periodicity[0]
            time_count = int(periodicity[1])
        except Exception:
            return command_name.periodicity_error, None
    else:
        return command_name.periodicity_error, None

    if time in command_name.periodicity_year_list:
        periodicity = f'years={time_count}'
    elif time in command_name.periodicity_month_list:
        periodicity = f'months={time_count}'
    elif time in command_name.periodicity_week_list:
        periodicity = f'days={7 * time_count}'
    elif time in command_name.periodicity_day_list:
        periodicity = f'days={time_count}'
    else:
        return command_name.periodicity_error, None

    return command_name.not_error, periodicity


def data_folder(folder_name):
    """Проверяет наличие рабочей папки пользователя в дирректории.
    В случае отсутствия папки - создает ее.
    Возвращает путь к данной папке."""

    folder_path = config.PATH + '\\' + str(folder_name)

    if not os.path.exists(folder_path):
        try:
            os.mkdir(folder_path)
        except Exception:
            return command_name.path_error, None

    return command_name.not_error, folder_path


def data_file(folder_path, title):
    """Принимает дирректорию рабочей папки и раздел исполняемого блока.
    Возвращает дирректорию рабочего файла"""

    if title == command_name.title_wealth:
        file_path = folder_path + '\\' + command_name.file_name_wealth

    if title == command_name.title_investment:
        file_path = folder_path + '\\' + command_name.file_name_investment

    if title == command_name.title_anticipated_revenue:
        file_path = folder_path + '\\' + command_name.file_name_anticipated_revenue

    if title == command_name.title_anticipated_loss:
        file_path = folder_path + '\\' + command_name.file_name_anticipated_loss

    if title == command_name.title_operating_revenue:
        file_path = folder_path + '\\' + command_name.file_name_operating_revenue

    if title == command_name.title_operating_loss:
        file_path = folder_path + '\\' + command_name.file_name_operating_loss

    return file_path


def personal_data(folder_path, message):
    """Проверяет наличие файла с персональными данными.
    В случае отсутствия - создает новый файл.
    Заполняет файл персональными данными."""

    file_path = folder_path + '\\' + r'personal_data.txt'

    if not os.path.exists(file_path):

        try:

            with open(file_path, 'w') as new_file:
                new_file.write(f'id:{message.from_user.id}\n')
                new_file.write(f'first_name:{message.from_user.first_name}\n')
                new_file.write(f'last_name:{message.from_user.last_name}\n')
                new_file.write(f'username:{message.from_user.username}\n')

            return command_name.not_error

        except Exception:
            return command_name.error

    else:
        return command_name.not_error


def data_recording(data, file_path):
    """Функция принимает словарь для записи и путь к файлу csv.
    Если файл отсутствует - функция создает файл.
    Далле происходит запись словаря в существующий файл"""

    try:

        if not os.path.exists(file_path):
            # create new csv
            with open(file_path, 'w', newline='', encoding='cp1251') as new_file:
                writer = csv.writer(new_file)
                writer.writerow(data.keys())
            # add new data
            with open(file_path, 'a', newline='', encoding='cp1251') as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                writer.writerow(data)

        elif os.path.exists(file_path):
            # add new data
            with open(file_path, 'a', newline='', encoding='cp1251') as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                writer.writerow(data)

        return command_name.not_error

    except Exception:
        return command_name.write_error


def get_check(json_file):
    """Принимает файл чека. Возвращает список словарей для записи."""

    try:

        data = json.loads(json_file, encoding='utf-8')

        dateTime = data['dateTime']

        check = list()
        for purchase in data['items']:
            name = f'{name_corrector(text=purchase["name"])} [{purchase["quantity"]}]'
            value = (purchase['sum'] // 100) + (purchase['sum'] % 100) / 100

            new_purchase = {'name': name,
                            'date': dateTime,
                            'value': value,
                            'exchange': 'ruble'}

            check.append(new_purchase)

        return command_name.not_error, check

    except Exception:
        return command_name.check_error, None


def name_corrector(text):
    """Проверяет позицию товара на наличие артикула. В случае наличия - удаляет."""

    string = text.strip().split(' ')

    if re.sub(r'[^\w\s]', '', string[0].lower()).isdigit():
        del string[0]

        if re.sub(r'[^\w\s]', '', string[0].lower()).isdigit():
            del string[0]

        correct_text = ' '.join(string)

        return correct_text

    return text


def uniqueness_identifier(file_path):
    """Принимает путь к файлу. Возвращает свободный id позиции."""

    if not os.path.exists(file_path):
        name_identifier = int(1)

    elif os.path.exists(file_path):
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file, delimiter=',')
                last_name_identifier = int(0)
                for row in reader:
                    if int(row[command_name.feature_id]) > last_name_identifier:
                        last_name_identifier = int(row[command_name.feature_id])
                name_identifier = last_name_identifier + int(1)

        except Exception:
            return command_name.write_error, None
    else:
        return command_name.error, None

    return command_name.not_error, name_identifier


def show_data_constructor(file_path, data, current_datetime):
    """Обрабатывает введенное сообщение, возвоащает данные для отображения."""

    try:

        status, conditions_formatted = get_conditions(conditions=data, current_datetime=current_datetime)
        if not status == command_name.not_error:
            raise

        if not os.path.exists(file_path):
            return command_name.query_result_error, None

        try:
            data = read_csv(file_path, sep=',', encoding='cp1251')

        except Exception:
            return command_name.query_result_error, None

        if data.shape[0] == 0:
            return command_name.data_error, None

        display = get_display(data=data, conditions_formatted=conditions_formatted)

        return command_name.not_error, display

    except Exception:
        return status, None


def get_conditions(conditions, current_datetime):
    """Принимает параметры отображения. Возвращает отформатированные параметры для отображения данных."""

    counter_open_parenthesis = 0
    counter_closed_parenthesis = 0

    conditions_formatted = list()

    condition_number = 0

    for condition in conditions:
        condition = condition.lower()

        condition_copy = re.sub(r'[^\w\s]', '', condition)

        if condition_copy in command_name.show_criterion_all_list:
            conditions_formatted.append(command_name.show_criterion_all)
            return command_name.not_error, conditions_formatted

        elif condition in command_name.conditions_union_list:
            set_operation = command_name.conditions_union
            conditions_formatted.append(set_operation)

        elif condition in command_name.conditions_intersection_list:
            set_operation = command_name.conditions_intersection
            conditions_formatted.append(set_operation)

        else:
            condition_number += 1

            # Создание копии объекта для дальнейшего извлечения закрывающейся скобки вконце цикла
            condition_copy = condition

            # Проверка наличия открывающейся скобки. Удаление с занесением в список.
            while not condition.find('(') == int(-1):
                condition = condition[condition.find('(') + 1:]
                conditions_formatted.append('(')
                counter_open_parenthesis += 1

            # Удаление закрывающейся скобки
            condition = condition.replace(')', '')

            try:
                sign_number = 0

                for sign in command_name.signs:
                    sign_position = condition.find(sign)

                    if not sign_position == int(-1):
                        condition_feature = condition[:sign_position]
                        condition_feature = re.sub(r'[^\w\s]', '', condition_feature.lower())
                        condition_value = condition[sign_position + len(sign):]

                        if condition_feature in command_name.show_criterion_date_list:
                            condition_feature = command_name.show_criterion_date
                            status, date = get_datetime(date=condition_value, current_datetime=current_datetime)
                            if not status == command_name.not_error:
                                raise
                            condition_value = date
                            break

                        elif condition_feature in command_name.show_criterion_date_end_list:
                            condition_feature = command_name.show_criterion_date_end
                            status, date = get_datetime(date=condition_value, current_datetime=current_datetime)
                            if not status == command_name.not_error:
                                raise
                            condition_value = date
                            break

                        elif condition_feature in command_name.show_criterion_id_list:
                            condition_feature = command_name.show_criterion_id
                            condition_value = re.sub(r'[^\w\s]', '', condition_value.lower())
                            try:
                                condition_value = int(condition_value)
                            except Exception:
                                return command_name.condition_id_error, None
                            break

                        elif condition_feature in command_name.show_criterion_name_list:
                            condition_feature = command_name.show_criterion_name
                            break

                        elif condition_feature in command_name.show_criterion_value_list:
                            condition_feature = command_name.show_criterion_value
                            status, value = get_value(value=condition_value)
                            if not status == command_name.not_error:
                                raise
                            condition_value = value
                            break

                        elif condition_feature in command_name.show_criterion_exchange_list:
                            condition_feature = command_name.show_criterion_exchange
                            status, exchange = get_exchange(exchange=condition_value)
                            if not status == command_name.not_error:
                                raise
                            condition_value = exchange
                            break

                        elif condition_feature in command_name.show_criterion_periodicity_list:
                            condition_feature = command_name.show_criterion_periodicity
                            status, periodicity = get_periodicity(periodicity=condition_value)
                            if not status == command_name.not_error:
                                raise
                            condition_value = periodicity
                            break

                        else:
                            return f'Ошибка! В условии {condition_number} не распознан признак!!', None

                    else:
                        sign_number += 1
                        if sign_number == len(command_name.signs):
                            return f'Ошибка! В условии {condition_number} не найден знак!', None

                if sign == '=':
                    sign = '=='

                condition = f'{condition_feature} {sign} {condition_value}'
                conditions_formatted.append(condition)

            except Exception:
                return status, None

            while not condition_copy.find(')') == int(-1):
                condition_copy = condition_copy[:condition_copy[::-1].find('(')]
                conditions_formatted.append(')')
                counter_closed_parenthesis += 1

    if counter_open_parenthesis != counter_closed_parenthesis:
        return command_name.parenthesis_count_error, None

    return command_name.not_error, conditions_formatted


def get_condition_index(data, condition_formatted):
    """Возвращает индексы для вывода данных"""

    if condition_formatted == command_name.show_criterion_all:

        condition_index = list(map(lambda x: True, data.index))

        return condition_index

    else:

        condition_feature = condition_formatted.split(' ')[0]

        sign = condition_formatted.split(' ')[1]

        condition_value = condition_formatted.split(' ')[2]

        if condition_feature == command_name.show_criterion_date or \
                condition_feature == command_name.show_criterion_date_end:
            condition_value = int(condition_value)

        if condition_feature == command_name.show_criterion_value:
            condition_value = float(condition_value)

        if condition_feature == command_name.show_criterion_id:
            condition_value = int(condition_value)

        if condition_feature == command_name.show_criterion_name or \
                condition_feature == command_name.show_criterion_exchange:
            condition_value = str(condition_value)

        if sign == '<=' or sign == '=<':
            condition_index = data[condition_feature] <= condition_value
        if sign == '>=' or sign == '=>':
            condition_index = data[condition_feature] >= condition_value
        if sign == '<':
              condition_index = data[condition_feature] < condition_value
        if sign == '>':
            condition_index = data[condition_feature] > condition_value
        if sign == '==':
            condition_index = data[condition_feature] == condition_value
        if sign == '!=':
            condition_index = data[condition_feature] == condition_value

        condition_index = list(condition_index.values)

    return condition_index


def get_display(data, conditions_formatted):
    """Принимает датасает Pandas.DataFrame и отформатированный список условий. Выводит данные для отображения."""

    print(conditions_formatted)

    if conditions_formatted.count(command_name.conditions_intersection) == 0 and \
            conditions_formatted.count(command_name.conditions_union) == 0 and \
            conditions_formatted.count('(') == 0 and conditions_formatted.count(')') == 0:

        condition_index = get_condition_index(data=data, condition_formatted=conditions_formatted[0])

        display = data.iloc[condition_index]

    return display


def reverse_conversion(data):
    """Принимает словарь из базы данных. Возвращает строку для вывода."""

    show_data = list()

    for key, value in zip(data.keys(), data.values()):

        if key == command_name.feature_id:
            show_data.append(f'Id={str(value)}')

        if key == command_name.feature_name:
            show_data.append(f'Наименование={str(value)}')

        if key == command_name.feature_date:
            show_data.append(f'Дата={datetime.fromtimestamp(value).strftime("%m.%d.%Y")}')

        if key == command_name.feature_date_end:

            if value == command_name.indefinitely_datetime:
                show_data.append('Срок_окончания=неопределенный')

            else:
                show_data.append(f'Срок_окончания={datetime.fromtimestamp(value).strftime("%m.%d.%Y")}')

        if key == command_name.feature_periodicity:

            periodicity = value.split('=')

            time = periodicity[0]
            time_count = int(periodicity[1])

            if time == 'days':

                if (time_count % 10) == 1:
                    show_data.append(f'Периодичность={time_count}_день')

                if (time_count % 10) in [2, 3, 4]:
                    show_data.append(f'Периодичность={time_count}_дня')

                if (time_count % 10) in [5, 6, 7, 8, 9, 0]:
                    show_data.append(f'Периодичность={time_count}_дней')

            if time == 'months':

                if (time_count % 10) == 1:
                    show_data.append(f'Периодичность={time_count}_месяц')

                if (time_count % 10) in [2, 3, 4]:
                    show_data.append(f'Периодичность={time_count}_месяца')

                if (time_count % 10) in [5, 6, 7, 8, 9, 0]:
                    show_data.append(f'Периодичность={time_count}_месяцев')

            if time == 'years':

                if (time_count % 10) == 1:
                    show_data.append(f'Периодичность={time_count}_год')

                if (time_count % 10) in [2, 3, 4]:
                    show_data.append(f'Периодичность={time_count}_года')

                if (time_count % 10) in [5, 6, 7, 8, 9, 0]:
                    show_data.append(f'Периодичность={time_count}_лет')

        if key == command_name.feature_value:
            show_data.append(f'Сумма={str(value)}')

        if key == command_name.feature_exchange:

            if value == command_name.exchange_ruble:
                show_data.append('Валюта=рубли')

            if value == command_name.exchange_dollar:
                show_data.append('Валюта=доллары')

            if value == command_name.exchange_euro:
                show_data.append('Валюта=евро')

    return ' '.join(show_data)