import telebot
import requests

from config import BOT_TOKEN, CURRENCY_API
from filework.work_with_users import *

bot = telebot.TeleBot(BOT_TOKEN)

data = requests.get(CURRENCY_API).json()  # Ссылка на api валют от ЦБ РФ
currencies = {"Доллар США": "USD",
              "Евро": "EUR",
              "Швейцарский франк": "CHF",
              "Фунт стерлингов": "GBP",
              "Японская йена": "JPY",
              "Китайский юань": "CNY",
              "/help": "/help"}

users = get_users_list()  # никнейм пользователя - ключ : значение - номер строки с данными о пользователе в users.txt
                          # и да, стоило бы использовать sqlite базу, но переделать я уже не успевал

# print (data)

user_requests = dict()  # user_id - ключ : значение - количество запросов пользователя



@bot.message_handler(commands=["start"], content_types=["text"])  # Стартовая функция
def start_message(message):
    cur_buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in currencies:
        cur_buttons.add(telebot.types.KeyboardButton(i))
        # print(i)
    bot.send_message(message.chat.id, f"Здравствуйте {message.from_user.first_name}, я бот валютчик. "
                                      f"Чтобы узнать все что я могу напишите /help"
                                      f" или нажмите на кнопку help", reply_markup=cur_buttons)


@bot.message_handler(commands=["help"], content_types=["text"])
def help_message(message):
    bot.send_message(message.chat.id, "Чтобы начать работать со мной, вы можете нажать на кнопку рядом с полем ввода"
                                      " и тогда вам будет доступен список популярных валют, если вы хотите узнать"
                                      " данные по другим валютам, напишите мне стандартное 3х буквенное обозначение"
                                      " валюту - Пример:\nTRY - Турецкая лира")


@bot.message_handler(content_types=["text"])
def echo_message(message):
    if (message.text.upper() == "GALEON"):  # Маленькая пасхалка :)
        bot.send_message(message.chat.id, f"1 Золотой Галеон - 1981,48 RUB")   # 1 галлеон = 1981,48 рублей;
        bot.send_message(message.chat.id, f"1 Серебрянный Сикль - 118,89 RUB")  # 1 сикль = 118,89 рублей;
        bot.send_message(message.chat.id, f"1 Бронзовый Кнат - 3,96 RUB")  # 1 кнат = 3,96 рубля;
        bot.send_message(message.chat.id,  # 1 сикль -  29 кнатов; 1 галлеон - 17 сиклей;
                         f"За дополнительной информацией\nпросьба обратиться в банк " +
                         f"[Гринготтс](harrypotter.fandom.com/ru/wiki/Гринготтс)", parse_mode="Markdown")
    if (message.text != "/help"):
        if (message.text in currencies):
            bot.send_message(message.chat.id, f"{message.text} - "
                                              f"{data['Valute'][currencies[message.text].upper()]['Value']}")
        else:
            try:
                bot.send_message(message.chat.id, f"1 {message.text} - "
                                                  f"{data['Valute'][message.text.upper()]['Value']} RUB")


            except KeyError:
                bot.send_message(message.chat.id, "Ошибка, такой валюты не существует")


bot.polling(none_stop=True)
