import requests
import json
from config import  keys, APIKEY


class converter:
    @staticmethod
    def convert(message_text):
        quote, base, amount = message_text.split(" ")
        if quote == base:
            raise ConvertionExeption(f"Нельзя использовать одинаковые валюты")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f"Валюта не распознана: {quote}")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f"валюта не распознана: {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f"Не удалось обработать количество {amount}")
        else:
            r = requests.get(f"https://v6.exchangerate-api.com/v6/{APIKEY}/pair/{quote_ticker}/"
                             f"{base_ticker}/{amount}")
            total_base = json.loads(r.content)
            tootla = total_base['conversion_result']
            return tootla


class ConvertionExeption(Exception):
    pass