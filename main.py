import telebot
from telebot import types
token='5859470782:AAHa6dSNk14raLckSRyLCoVvoMKuSFvPAO0'
import random

bot = telebot.TeleBot(token)

images = ['EjEW6509WWg.jpg', 'hedvvnjxmxu-edited.jpg', 'KpL5UoIJYN4.jpg', 'ZddcFJkgthY.jpg', 'S_w0Hl6jPXQ.jpg']
biar = ['b.jpg', 'maxresdefault.jpg', 'pi.jpg', 'YTH3Somui2A.jpg', 'ddf.jpg','eIhv51T9r833RcD2YKmmw.jpg', 'XShDXNuMYfI.jpg', 'fkg.jpg']
mems = ['0yTD6ywu2lU.jpg', '2639111729.jpg', '2699234329.jpg', '2701255756.jpg', 'cQMsKV6X_AVk.jpg']

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Приветик!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Начнем работать", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Приветик!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Открытка с добрым утром!')
        btn2 = types.KeyboardButton('Отсчет до дня смерти')
        btn3 = types.KeyboardButton('Цитата дня')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Что вас интересует?', reply_markup=markup) #ответ бота


    elif message.text == 'Открытка с добрым утром!':
        bot.send_message(message.from_user.id, 'Доброе утро', parse_mode='Markdown')
        bot.send_photo(message.from_user.id,open('C:/Users/admin/Desktop/picture/' + random.choice(images),'rb'))

    elif message.text == 'Отсчет до дня смерти':
        bot.send_message(message.from_user.id, 'До дня смерти осталось ', parse_mode='Markdown')
        bot.send_photo(message.from_user.id,open('C:/Users/admin/Desktop/time/' + random.choice(biar),'rb'))

    elif message.text == 'Цитата дня':
        bot.send_message(message.from_user.id, 'Ваш день', parse_mode='Markdown')
        bot.send_photo(message.from_user.id,open('C:/Users/admin/Desktop/new/' + random.choice(mems),'rb'))

        

   



if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

