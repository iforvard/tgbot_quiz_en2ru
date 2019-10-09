import telebot
from telebot import apihelper
import botDB
from telebot import types
import random

token = ''
bot = telebot.TeleBot(token)
# apihelper.proxy = {'https': '186.192.29.64:8080'}


questions = botDB.random_answer()
num_answer = random.randint(0, 3)
keyboard1 = types.ReplyKeyboardMarkup(True)
keyboard1.row('Играть')


r = u'\U0001F622'  # Code: 200's, 900, 901, 902, 905


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, жми играть!',
                     reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    global questions, num_answer

    if message.text.lower() == 'играть' or message.text.lower() == questions[num_answer][2]:
        questions = botDB.random_answer()
        keyboard1 = types.ReplyKeyboardMarkup()
        for i in questions:
            keyboard1.add(i[2])
        num_answer = random.randint(0, 3)
        bot.send_message(message.chat.id, f'Верный ответ!\nПереведи слово {questions[num_answer][1]}',
                         reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id, f'Ответ не верный! Попробуй еще раз')


# @bot.message_handler(content_types=['audio', 'document', 'photo', 'sticker', 'video',
#                                     'video_note', 'voice', 'location', 'contact'])
# def send_doc(message):
#     print('all')
#     print(message)

if __name__ == '__main__':
     bot.polling(none_stop=True)
