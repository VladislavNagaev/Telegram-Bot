# Сообщение раздела "Приветствие" (welcome)
welcome_message_1 = 'Добро пожаловать!'
welcome_message_2 = 'Данный бот предназначен для контроля за личными расходами.'
welcome_message_3 = ('Функционал предусматривает 4 независимых блока учета расходов, которые могут быть '
                     'использованы как по отдельности, так и совместно. 5-ый блок содержащий суммарную статистику.')
welcome_message_4 = 'С подробным описанием функционала можно ознакомиться  в резделе /help'
welcome_message_5 = 'Для начала работы перейдите в раздел /main'

# Наиманования файлов для сохранения
file_name_wealth = r'wealth.csv'
file_name_investment = r'investment.csv'
file_name_anticipated_revenue = r'anticipated_revenue.csv'
file_name_anticipated_loss = r'anticipated_loss.csv'
file_name_operating_revenue = r'operating_revenue.csv'
file_name_operating_loss = r'operating_loss.csv'

# Операции
show = 'show'  # Отображение введенных данных
show_list = ('show', 'показать')
entry = 'add'  # Ввод новых данных
entry_list = ('add', 'entry', 'добавить')
delete = 'delete'  # Удаление данных
delete_list = ('delete', 'del', 'удалить')

# Разделы
title_wealth = 'wealth'
title_wealth_list = ('wealth', 'материальные_ценности', 'материальная_ценность', 'материальную_ценность', 'мат_ценн',
                     'матценн', 'мц')
title_investment = 'investment'
title_investment_list = ('investment', 'invest', 'инвестиции', 'инвестицию', 'инв')
title_anticipated_revenue = 'anticipated_revenue'
title_anticipated_revenue_list = ('anticipated_revenue', 'anticipatedrevenue', 'прогнозируемый_доход',
                                  'прогнозируемыйдоход', 'прогн_доход', 'прогндоход', 'п_д', 'пд')
title_anticipated_loss = 'anticipated_loss'
title_anticipated_loss_list = ('anticipated_loss', 'anticipatedloss', 'прогнозируемый_убыток', 'прогнозируемыйубыток',
                               'прогн_убыток', 'прогнубыток', 'п_уб', 'пуб', 'п_у', 'пу')
title_operating_revenue = 'operating_revenue'
title_operating_revenue_list = ('operating_revenue', 'operatingrevenue', 'текущий_доход', 'текущийдоход',
                                'текущие_доходы', 'текущиедоходы', 'тек_доход', 'текдоход', 'тек_доходы',
                                'текдоходы' 'т_д', 'тд')
title_operating_loss = 'operating_loss'
title_operating_loss_list = ('operating_loss', 'operating_loss', 'текущий_убыток', 'текущийубыток', 'текущие_убытки',
                             'текущиеубытки', 'тек_убыток', 'текубыток', 'тек_убытки', 'текубытки', 'т_уб', 'туб',
                             'т_у', 'ту')
title_statistics_income = 'statistics_income'
title_statistics_income_list = ('statistics_income', 'statistics_income', 'статистика_доходов', 'статистикадоходов',
                                'статистика_дохода', 'статистикадохода', 'стат_доходов', 'статдоходов',
                                'стат_дохода', 'статдохода')
title_statistics_expense = 'statistics_expense'
title_statistics_expense_list = ('statistics_expense', 'statistics_expense', 'статистика_расходов',
                                 'статистикарасходов', 'статистика_расхода', 'статистикарасхода',
                                 'стат_расходов', 'статрасходов', 'стат_расхода', 'статрасхода')
title_statistics_balance = 'statistics_balance'
title_statistics_balance_list = ('statistics_balance', 'statistics_balance', 'статистика_сальдо', 'статистикасальдо',
                                 'стат_сальдо', 'статсальдо')

# Признаки данных
feature_id = 'id'
feature_name = 'name'
feature_date = 'date'
feature_value = 'value'
feature_exchange = 'exchange'
feature_date_end = 'date_end'
feature_periodicity = 'periodicity'

# Столбцы с признаками
wealth_columns = [feature_name, feature_date, feature_value, feature_exchange]
investment_columns = [feature_name, feature_date, feature_value, feature_exchange]
anticipated_revenue_columns = [feature_name, feature_date, feature_date_end, feature_periodicity, feature_value,
                               feature_exchange]
anticipated_loss_columns = [feature_name, feature_date, feature_date_end, feature_periodicity, feature_value,
                            feature_exchange]
operating_revenue_columns = [feature_name, feature_date, feature_value, feature_exchange]
operating_loss_columns = [feature_name, feature_date, feature_value, feature_exchange]

# Ошибки
error = 'error'
not_error = 'not_error'
input_error = 'input_error'
count_error = 'count_error'
command_error = 'command_error'
title_error = 'title_error'
data_error = 'data_error'
query_result_error = 'query_result_error'
date_error = 'date_error'
date_inconsistency_error = 'date_inconsistency_error'
exchange_error = 'exchange_error'
value_error = 'value_error'
periodicity_error = 'periodicity_error'
check_error = 'check_error'
write_error = 'write_error'
path_error = 'path_error'
condition_error = 'condition_error'
condition_name_error = 'condition_name_error'
condition_id_error = 'condition_id_error'
condition_date_error = 'condition_date_error'
condition_date_end_error = 'condition_date_end_error'
invalid_request = 'invalid_request_message'
parenthesis_count_error = 'parenthesis_count_error'

# Успехи
success_recording = 'success_recording'

# Сообщения об успехе
message_success_recording = 'Данные сохранены!'

# Сообщения об ошибках
message_invalid_request = 'Некорректный запрос!'
message_error = ('Неидентифицированная ошибка!'
                 '\n\nПожалуйста, сообщите о данной ошибке в поддержку!')
message_input_error = ('Некорректный ввод!'
                       '\n\nНе удалось расшифровать сообщение.'
                       '\nПроверьте соответствие вводимого сообщения шаблону!')
message_count_error = ('Некорректный ввод!'
                       '\n\nКоличество введенных параметров отличается от необходимого.'
                       '\nПроверьте соответствие вводимого сообщения шаблону!')
message_command_error = ('Некорректный ввод!'
                         '\n\nВведенная команда некорректна.'
                         '\nПроверьте соответствие вводимой команды шаблону!')
message_title_error = ('Некорректный ввод!'
                       '\n\nЗапрашиваемый раздел не найден.'
                       '\nПроверьте правильность ввода раздела!')
message_data_error = 'Соответствующих запросу данных не найдены!'
message_query_result_error = 'В выбранном разделе отсутствуют данные!'
message_date_error = ('Некорректный ввод!'
                      '\n\nВведенный формат даты некорректен.'
                      '\nПроверьте соответствие вводимого формата даты шаблону!')
message_date_inconsistency_error = ('Несогласованность даты!'
                                    '\n\nДата начала не может быть не меньше даты окончания!')
message_exchange_error = ('Некорректный ввод!'
                          '\n\nВведенная валюта некоректна или не поддерживается.'
                          '\nПроверьте соответствие вводмой валюты шаблону!')
message_value_error = ('Некорректный ввод!'
                       '\n\nВведеное значение суммы некорректно.'
                       '\nПроверьте соответствие вводмого значения суммы шаблону!')
message_periodicity_error = ('Некорректный ввод!'
                             '\n\nВведенная периодичность некорректна.'
                             '\nПроверьте соответствие вводмого значения периодичности шаблону!')
message_check_error = 'Чек некорректен!'
message_write_error = ('Ошибка записи!'
                       '\n\nЗапись данных не удалась. Файл данных занят другой операцией.'
                       '\nПопробуйте подождать выполнения предыдущих операция или обратитесь в поддержку.')
message_path_error = ('Ошибка записи!'
                      '\n\nЗапись данных не удалась. Файловая дирректория повреждена или недоступна.'
                      '\nПожалуйста, сообщите о данной ошибке в поддержку!')
message_condition_error = ('Некорректный ввод!'
                           '\n\nВведенные условия отображения данных некорректны.'
                           '\nПроверьте соответствие вводимых условий отображения данных шаблону!')
message_condition_name_error = ('Некорректный ввод!'
                                '\n\nВведенные условия отображения данных некорректны.'
                                '\nВведите конкретное наименование одной или нескольких позиций!')
message_condition_id_error = ('Некорректный ввод!'
                              '\n\nВведенные условия отображения данных некорректны.'
                              '\nВведите конкретнй идентификатор или диапазон идентификаторов!')
message_condition_date_error = ('Некорректный ввод!'
                                '\n\nВведенные условия отображения данных некорректны.'
                                '\nВведите конкретную дату или диапазон дат!')
message_condition_date_end_error = ('Некорректный ввод!'
                                    '\n\nВведенные условия отображения данных некорректны.'
                                    '\nВведите конкретную дату окончания или диапазон дат окончания!')
message_parenthesis_count_error = ('Некорректный ввод!'
                                   '\n\nКоличество введенных открытых и закрытых скобок не совпадает.'
                                   '\n\nВведите корректные условия!')

# Валюты
exchange_ruble = 'ruble'
exchange_ruble_list = ['rubles', 'ruble', 'rub', 'r', 'рублей', 'руб', 'р', 'рубль', 'рубл', 'рубли', 'рубля', '₽']
exchange_dollar = 'dollar'
exchange_dollar_list = ['dollars', 'dollar', 'doll', 'd', 'usd', 'долларов', 'доллар', 'долл', 'д', 'доллары', '$']
exchange_euro = 'euro'
exchange_euro_list = ['euros', 'euro', 'eur', 'e', 'евро', 'евр', 'е', '€']

# Периодичность
periodicity_year = 'year'
periodicity_year_list = ['years', 'year', 'y', 'annually', 'лет', 'л', 'год', 'г', 'ежегодно']
periodicity_month = 'month'
periodicity_month_list = ['months', 'month', 'm', 'monthly', 'месяц', 'месяцев', 'мес', 'м', 'ежемесячно']
periodicity_week = 'week'
periodicity_week_list = ['weeks', 'week', 'w', 'weekly', 'недель', 'неделя', 'нед', 'н', 'еженедельно']
periodicity_day = 'day'
periodicity_day_list = ['days', 'day', 'd', 'daily', 'дней', 'день', 'д', 'ежедневно']

# Даты
day_before_yesterday_datetime = 'day_before_yesterday_datetime'
day_before_yesterday_datetime_list = ['day_before_yesterday', 'before_yesterday', 'позавчера']
yesterday_datetime = 'yesterday_datetime'
yesterday_datetime_list = ['yesterday', 'вчера']
current_datetime = 'current_datetime'
current_datetime_list = ['current', 'now', 'текущий', 'текущее', 'сегодня', 'сейчас']
indefinitely_datetime = 'inf'
indefinitely_datetime_list = ['inf', 'бессрочно', 'неопределенный', 'неопределенно', 'неопр', 'неясно', 'бесконечно']

# Критерии отображения
show_criterion_all = 'all'
show_criterion_all_list = ['all', 'every', 'all_period', 'весь_период', 'весь', 'все', 'всё', 'все_данные']
show_criterion_id = 'id'
show_criterion_id_list = ['id', 'айди', 'идентификатор', 'номер', 'позиция']
show_criterion_date = 'date'
show_criterion_date_list = ['date', 'дата', 'число']
show_criterion_date_end = 'date_end'
show_criterion_date_end_list = ['date_end', 'end', 'дата_окончания', 'дата_конца', 'окончание', 'конец']
show_criterion_name = 'name'
show_criterion_name_list = ['name', 'наименование', 'имя', 'название', 'обозначение']
show_criterion_value = 'value'
show_criterion_value_list = ['value', 'val', 'сумма', 'величина', 'значение', 'стоимость']
show_criterion_exchange = 'exchange'
show_criterion_exchange_list = ['exchange', 'exch', 'валюта', 'вал']
show_criterion_periodicity = 'periodicity'
show_criterion_periodicity_list = ['periodicity', 'периодичность', 'период']

# Заменить show_criterion на Признаки данных !
# feature_id = 'id'
# feature_name = 'name'
# feature_date = 'date'
# feature_value = 'value'
# feature_exchange = 'exchange'
# feature_date_end = 'date_end'
# feature_periodicity = 'periodicity'

signs = ['<=', '=<', '>=', '=>', '<', '>', '==', '!=', '=']

conditions_union = 'or'
conditions_union_list = ['|', 'объединение', 'или', 'or']

conditions_intersection = 'and'
conditions_intersection_list = ['&', 'пересечение', 'и', 'and']