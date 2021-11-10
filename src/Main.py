import pyttsx3
import telebot

TOKEN = '2137310516:AAEzSHLl-xGmqklgHjC5SnjJVXERsWEDcsw'
bot = telebot.TeleBot(TOKEN)  # create a new Telegram Bot object


# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, 'Welcome to Bot!!!')
    elif message.text == "/help":
        bot.send_message(message.chat.id, 'I can\'t help you')


@bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
def voice_sed(message):
    s = pyttsx3.init()
    data = message.text
    s.save_to_file(data, 'sample.ogg')
    s.runAndWait()
    audio = open('sample.ogg', 'rb')
    bot.send_voice(message.chat.id, audio)
    # bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
