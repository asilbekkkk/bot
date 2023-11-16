import telebot
with open('./ol.jpeg', 'rb') as photo:
    bot.send_photo(message.from_user.id, photo)
        