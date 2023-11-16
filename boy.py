import telebot

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6566168187:AAFftYCiOh8IPwsUvelgtb3V-p2XnTTTiJ0')


def main_menu_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = KeyboardButton('когда родился стив джобс')
    button2 = KeyboardButton('когда начнется школа')
    button3 = KeyboardButton('зачем нужен солнце')
    button4 = KeyboardButton('кто создал бугатти')
    button5 = KeyboardButton('что быстрее звук или свет')
    button6 = KeyboardButton('число ПИ')
    button7 = KeyboardButton('почему черепахи медленные')
    button8 = KeyboardButton('что будет если засунуть руку в розетку')
    button9 = KeyboardButton('17 - 5')
    button10 = KeyboardButton('15 - 6')


    kb.add(button1, button2, button3,button4, button5, button6, button7, button8, button9, button10 )

    return kb



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'привет я QRCode)', reply_markup=main_menu_button())


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'qrcode':
        with open('./qr_code.png', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo)

   
    elif message.text.lower() == 'когда родился стив джобс':
        bot.send_message(message.from_user.id,'24 февраля 1955 г.')

    elif message.text.lower() == 'когда начнется школа':
        bot.send_message(message.from_user.id,'только 10 сентября')

    elif message.text.lower() == 'зачем нужен солнце':
        bot.send_message(message.from_user.id,'потому что полезно')

    elif message.text.lower() == 'кто создал бугатти':
        bot.send_message(message.from_user.id,'Этторе Арко Изидоро Буга́тти')


    elif message.text.lower() == 'что быстрее звук или свет':
        bot.send_message(message.from_user.id,'свет')

    elif message.text.lower() == 'число пи':
        bot.send_message(message.from_user.id,'3,14')

    elif message.text.lower() == 'почему черепахи медленные':
        bot.send_message(message.from_user.id,'у них тяжелый панцирь')

    elif message.text.lower() == 'что будет если засунуть руку в розетку':
        bot.send_message(message.from_user.id,'током ударит')

    elif message.text.lower() == '17 - 5':
        bot.send_message(message.from_user.id,'12')
    elif message.text.lower() == '15 - 6':
        bot.send_message(message.from_user.id,'9')


bot.polling()