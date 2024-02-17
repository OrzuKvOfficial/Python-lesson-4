import telebot

# Botni tokeni
TOKEN = 'Botning tokenini shu yerga yozing'

# Botni quramiz
bot = telebot.TeleBot("6421682986:AAEwiMVGiUIMjXgBro5oXoCrfgAkUmN_uyU")

# /start buyrug'iga javob berish
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu Alaykum!")

# Botni ishga tushurish
bot.polling()
