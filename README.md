# async
python Telebot Async

Я очень долго искал на просторах интернета ответ на вопрос: *Как асинхронизировать моего бота в телеграме, который написан на библеотеке Telebot (pyTelegramBotAPI)*. Я вообще не люблю писать такие гайды и прочее, но тут я хочу действительно помочь людям, ведь этой информации нигде нет на русскоязычном пространтсве. Ближе к делу.

Я не буду рассказывать как создавать такого бота, я просто скажу что нужно добавить в вашего бота для создания асинхронизации функции.

Сверху в импорты добавляем это:

`from telebot.util import async_dec`

Перед функцией, которую мы хотим сделать асинхронной:

`@async_dec()`

Как это будет в коде:

`import telebot`

`from telebot.util import async_dec`

`@async_dec()`

`def iphone(message):`

    `print('Тут может быть функция любой сложности')`
    
    
`bot.polling()`

Для людей, которые пишут на этом замечательном языке ботов должно быть максимально все понятно. Если есть вопросы задавайте, я буду стараться на них ответить!
