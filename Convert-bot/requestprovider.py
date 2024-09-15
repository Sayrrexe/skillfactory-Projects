import requests
import json

# Класс-расчетчик курса
class RequestProvider:
    def __init__(self):
        pass

    # Посчитать курс
    @staticmethod
    def get_price(base, quote, amount):
        request = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=666b44d1aa0ed125d83e5d7c44c364a4")
        result = json.loads(request.content)
        money_dict = result['rates']
        v1 = money_dict[base]
        v2 = money_dict[quote]

        # Считается кросс-курс (курс валют через третью валюту),
        # т.к. в предоставленном API в бесплатной версии нельзя менять базовую валюту (она всегда - евро)
        value = amount / (v1 / v2)
        return value
