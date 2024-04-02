from telebot.types import(
KeyboardButton,
ReplyKeyboardMarkup
)

#Создаем разметку главной клавиатуры
mainKeyboard = ReplyKeyboardMarkup(
    #Меняем размер кнопок под их содержание
    resize_keyboard=True
)
#Добавляем кнопку в клавиатуру
mainKeyboard.add(
    #Создаем экземпляр кнопки с текстом
    KeyboardButton('Мои траты')
)

#Добавляем кнопку в клавиатуру
mainKeyboard.add(
    #Создаем экземпляр кнопки с текстом
    KeyboardButton('Как работать с ботом')
)