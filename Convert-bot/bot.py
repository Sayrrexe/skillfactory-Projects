import myexceptions
import telebot
from requestprovider import RequestProvider

# Класс бота
class MoneyBot:
    # Конструктор
    def __init__(self, token, money_names):
        self.money_names = money_names
        self.bot = telebot.TeleBot(token)

        # Функции созданы для возможности обращения к боту в поле класса
        @self.bot.message_handler(commands=['start', 'help'])
        def _help_reply(message):
            self.help_reply(message)

        @self.bot.message_handler(commands=['values'])
        def _values_reply(message):
            self.values_reply(message)

        @self.bot.message_handler()
        def _command_reply(message):
            self.command_reply(message)

    # Запуск бота
    def start(self):
        print("bot started")
        self.bot.polling(none_stop=True)

    # Отправка приветственного сообщения
    def help_reply(self, message):
        text = "MoneyInformer выполняет расчет цены на заданное количество валюты.\n" \
               "Для получения списка возможных валют введите /values.\n\n" \
               "Для выполнения расчета введите команду в следующем формате:" \
               " <имя валюты, цену которой он хочет узнать>" \
               " <имя валюты, в которой надо узнать цену первой валюты>" \
               " <количество первой валюты>\n\n" \
               "Пример:\n" \
               "евро доллар 100\n\n" \
               "Для повторного вывода инструкции введите /start или /help"
        self.bot.reply_to(message, text)

    # Отправка списка валют
    def values_reply(self, message):
        text = "\n".join(self.money_names.keys())
        self.bot.reply_to(message, text)

    # Отправка ответа по курсу валют
    def command_reply(self, message):
        result = ""
        try:
            command = self.parse_message(message.text)
            result = str(RequestProvider.get_price(command[0], command[1], command[2]))
        except myexceptions.CommandExeption as e1:
            result = e1
        except myexceptions.MoneyExeption as e2:
            result = e2
        except myexceptions.ValueExeption as e3:
            result = e3
        except myexceptions.EqualExeption as e4:
            result = e4

        self.bot.reply_to(message, result)

    # Парсинг сообщения пользователя с проверкой ошибок ввода
    def parse_message(self, text):
        result = []
        tmp = text.split(' ')
        if len(tmp) == 3:
            base = tmp[0].lower()
            quote = tmp[1].lower()
            if base in self.money_names.keys() and quote in self.money_names.keys():
                if str(tmp[2]).isdigit() and int(tmp[2]) >= 0:
                    amount = int(tmp[2])
                    if base != quote:
                        result.append(self.money_names[base])
                        result.append(self.money_names[quote])
                        result.append(amount)
                    else:
                        raise myexceptions.EqualExeption
                else:
                    raise myexceptions.ValueExeption
            else:
                raise myexceptions.MoneyExeption
        else:
            raise myexceptions.CommandExeption

        return result
