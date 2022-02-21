import telebot
from telebot.util import async_dec

@async_dec()
def iphone(message):
    print('Тут может быть функция любой сложности')
       
bot.polling()
