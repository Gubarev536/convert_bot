import requests
import json
from config import keys, API_KEY


class APIException(Exception):
    pass

class CryptoConverter():
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
       
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest'
            f'?access_key={API_KEY}'
            f'&base={quote_ticker}'
            f'&symbols={base_ticker}')
        # print(r.content)
        total_base = json.loads(r.content)['rates'][keys[base]]
        # print(total_base)

        return total_base