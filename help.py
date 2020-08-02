import telebot

import command
import block_1
import block_2
import block_3
import block_4
import block_5


name = 'Помощь'.upper()


# Сообщения раздела "Помощь" (help)
help_message_1 = 'Будет добавлено позднее.'
help_message_2 = 'Для начала работы перейдите в раздел /main'

# Клавиатура раздела "Помощь" (help)
keyboard_main = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard_main.row('/main')



# Сообщения реакции на некорректные запросы (invalid_request)
invalid_request_message_1 = 'Некорректный запрос!'

# Клавиатура обработки некорректных запросов (invalid_request)
keyboard_invalid_request = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard_invalid_request.row('/main', '/help')




block_1_help = (
    block_1.name +
    '\n\nЗдесь можно указать:' +
    '\n1. Любые материальные ценности (квартира, машина, права на интеллектуальную собственность, утюг и т.д.).' +
    '\n2. Их остаточную стоимость на текущий момент времени или на момент их преобретения (для оценки изменения стоимости с момента покупки).' +
    '\n3. Задать (или выбрать из рекомендуемых) модель изменения остаточной стоимости.' +
    f'\n\n После указания полных данных, в разделе {block_5.name} будут доступны следующие функции:'
    '\n1. Динамика изменения остаточной стоимости.' +
    '\n2. Прогноз остаточной стоимости на заданный промежуток времени.'
)

block_2_help = (
    block_2.name +
    '\n\nЗдесь можно указать:' +
    '\n1. Любые инвестиционные активы (наличные, облигации, акции, прочие долговые бумаги).' +
    '\n2. Задать их стоимость и количество на текущий момент времени или на момент преобретения (для оценки изменения стоимости с момента покупки).' +
    '\n3. Задать (или выбрать из рекомендуемых) модель изменения стоимости активов (для большинства активов - выбрать биржу).' +
    f'\n\n После указания полных данных, в разделе {block_5.name} будут доступны следующие функции:' +
    '\n1. Динамика изменения рыночной стоимости инвестиционных активов.' +
    '\n2. Прогноз рыночной стоимости инвестиционных активов на заданный промежуток времени.'
)
# Девиденты

block_3_help = (
    block_3.name +
    '\n\nЗдесь можно указать:' +
    '\n1. Прогнозируемый гарантированный доход (заработная плата, социальные выплаты, алименты и т.д.).' +
    '\n2. Прогнозируемый гарантированный расход (выплаты по кредиту, выплаты долгов, выплаты алиментов, квартплата, подписка на стриминговый сервис и т.д.).' +
    '\n3. Задать (или выбрать из рекомендуемых) модель изменения гаранитрованного дохода и расхода.' +
    f'\n\n После указания полных данных, в разделе {block_5.name} будут доступны следующие функции:' +
    '\n1. Динамика доходов, расходов и сальдо.' +
    '\n2. Прогноз доходов, расходов и сальдо на заданный промежуток времени.'
)

block_4_help = (
    block_4.name +
    '\n\nЗдесь можно указывать:' +
    '\n1. Единоразовые затраты (анализ чека) (продукты, хоз. товары, бытовая техника, компьютерная техника, развлечения, одежда, обувь, лекарства, коммунальные услуги и т.д.)' +
    '\n2. Затраты за произвольный промежуток (день, неделя, месяц) времени с детализацией или без.' +
    '\n3. Единоразовая прибыль (премия, возврат долга, выигрыш в лотерею и т.д.)' +
    f'\n\nПосле указания полных данных, в разделе {block_5.name} будут доступны следующие функции:' +
    '\n1. Динамика доходов, расходов и сальдо.' +
    '\n2. Прогноз доходов, расходов и сальдо на заданный промежуток времени.'
)

block_5_help = (
    block_5.name +
    'ла-ла-ла'
)


q = ['Указывайте уникальные имена.']