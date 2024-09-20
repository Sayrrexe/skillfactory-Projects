import telebot
from config import BOTAPI, keys
from extensions import ConvertionExeption, converter

bot = telebot.TeleBot(BOTAPI)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "список доступных валют: /values"
									  "\nДля Конвертации введите данные в таком порядке:\n"
									  "'Имя валюты из которой переводите''имя валюты, в которую переводите'"
									  "'количество'")

@bot.message_handler(commands=['values'])
def send_welcome(message):
	text = "Список доступных валют:"
	for key in keys.keys():
		text = "\n".join((text, key, ))
	bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=["text"])
def echo_all(message):
	try:
		check = message.text.split(" ")
		if len(check) != 3:
			raise ConvertionExeption(f"Введены некоректные данные")
		total_base = converter.convert(message.text)
	except Exception as e:
		bot.reply_to(message, f"Не удалось обработать команду\n{e}")
	else:
		quote, base, amount = message.text.split(" ")
		text = f"Цена {amount} {quote}(а): {total_base} {base}(а)"
		bot.send_message(message.chat.id, text)

bot.infinity_polling()