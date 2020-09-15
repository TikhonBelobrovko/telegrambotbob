import telebot
import random
from text import hello_list, bye_list, what_you_can_request, speak_guid, How_are_you_request_list, \
    What_are_you_doing_list, Question_list, Update, News_list

bot = telebot.TeleBot('1398287849:AAFO3qMjXYycrHNXzxH3LjAfKZZnk7bCSvs')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'я Боб.  Я рад с Тобой познакомится!  Напиши мне  "Что ты умеешь?" ,  что бы узнать что я умею!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text in hello_list:
        sti = open('C:\Inf\Sticker\hello_sticker.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)

    elif message.text in bye_list:
        sti = open('C:\Inf\Sticker\good_bye_sticker.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)

    elif message.text == 'Что ты умеешь?':
        bot.send_message(message.chat.id, what_you_can_request)

    elif message.text == 'Как с тобой общаться?':
        bot.send_message(message.chat.id, speak_guid)

    elif message.text in Question_list:
        bot.send_message(message.chat.id, random.choice(How_are_you_request_list))

    elif message.text == 'Что делаешь?':
        bot.send_message(message.chat.id, random.choice(What_are_you_doing_list))
    elif message.text == 'Версия':
        bot.send_message(message.chat.id, Update)
    elif message.text == 'Что нового?':
        bot.send_message(message.chat.id, random.choice(News_list))
    elif message.text == 'Ты веселый':
        sti = open('C:\Inf\Sticker\Тывеселый.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == 'Ты крутой':
        sti = open('C:\Inf\Sticker\Тыкрутой.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == 'Ты грустный':
        sti = open('C:\Inf\Sticker\Тыгрустный.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == 'Скинь свою фотку':
        pic = 'https://lumiere-a.akamaihd.net/v1/images/c2-b5-main_b2481990.jpeg?region=0%2C0%2C1560%2C878&width=768'
        bot.send_photo(message.chat.id, pic)


bot.polling(none_stop=True, interval=0)