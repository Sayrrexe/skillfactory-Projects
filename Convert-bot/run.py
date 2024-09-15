from config import TOKEN, VALUES
from bot import MoneyBot

# Запуск бота
bot = MoneyBot(TOKEN, VALUES)
bot.start()
