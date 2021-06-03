from newsapi import NewsApiClient
import telebot


TokenBot = ''
TokenNews = ''
bot = telebot.TeleBot(TokenBot)
newsapi = NewsApiClient(TokenNews)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\n"
                                      f"Я бот, который предоставляет тебе топ 10 горячих новостей на твою тему.\n"
                                      f"Чтобы получить новости, просто введи горячее слово, по которому мне нужно будет искать.\n")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    searchword = message.text
    news = newsapi.get_top_headlines(q=f'{searchword}', qintitle=f'{searchword}', language='en')
    quantitynews = len(news['articles'])
    limitnews = 10
    count = 0


    if (quantitynews == 0):
        bot.send_message(message.from_user.id, text='Новостей нет')
    else:
        while count < quantitynews and count < limitnews:
            title =news['articles'][count]['title']
            descript = news['articles'][count]['description']
            url = news['articles'][count]['url']
            count = count + 1

            bot.send_message(message.from_user.id, text=
            f'Заголовок: {title} \n'
            f'Описание: {descript} \n'
            f'Ссылка на источник: {url} \n')


bot.polling(none_stop=True)