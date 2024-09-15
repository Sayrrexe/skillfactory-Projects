class APIException(BaseException):
    pass

class CommandExeption(APIException):
    def __str__(self):
        return "Неверный формат команды"

class MoneyExeption(APIException):
    def __str__(self):
        return "Введенная валюта отсутствует в списке возможных"

class EqualExeption(APIException):
    def __str__(self):
        return "Наименования валют одинаковые. Перевод не требуется"

class ValueExeption(APIException):
    def __str__(self):
        return "Неверная величина валюты"

