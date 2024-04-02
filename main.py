import telebot
from telebot.types import Message
from Keyboard import mainKeyboard
from utils import save_data, load_data


file = open( 'token',mode= 'r',encoding='utf-8')
API_TOKEN = file.read()
file.close()

#Создание бота 
bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

#Добавляем обработчик
#Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])

def start_command(m: Message):
    bot.send_message(
        m.chat.id,
        'Привет, это бот финансовый помощник\n'
        'Я помогу тебе учитывать твои финансы',
        reply_markup=mainKeyboard
    )

@bot.message_handler(regexp='Как работать с ботом')
def how_to(m: Message):
    bot.reply_to(
        m,
        'Пришлите в чат с ботом сообщение в таком формате:\n'
        '+ / - сумма категория\n\n'
        'Пример\n'
        '+50000 зарплата\n'
        '-1000 ЖКХ\n'
    )

@bot.message_handler(regexp='Мои траты')
def statistics(m: Message):
    try:
        earned,spent = load_data(user_id= m.from_user.id)
    except KeyError:
        bot.send_message(
        m.chat.id,
        'Нет данных на сегодня'
    )
        return 
        
    bot.send_message(
        m.chat.id,
        '<b><n>Ваши траты за месяц</b></n>\n\n'
        f'Потрачено: {spent}\n'
        f'Заработано: {earned}'
    )


@bot.message_handler(regexp=r'^[+-]\d+ \w+$')
def transaction(m: Message):
#Распаковываем список строк в переменной
    value,category= m.text.split(maxsplit=1)
    #Операция
    operation = value[0]
    #Сумма
    amount = value[1:]

#Сохраняем айди пользователя
    user_id: int = m.from_user.ad
    

    bot.reply_to(
        m,
        f'<u><b>Данные сохранены</b></u>\n'
        f'Ваша операция: {operation}\n'
        f'Сумма операции: {amount}\n'
        f'Категория операции: {category}\n'

    )

    save_data(user_id, category,amount,operation)

restart_on_change=True
#Бесконечный цикл получения обновлений от телеграм
bot.infinity_polling()

