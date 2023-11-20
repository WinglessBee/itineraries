import os

import requests
from cachetools import cached, TTLCache

from itineraries.models import CurrencyOptions

cache: TTLCache = TTLCache(maxsize=100, ttl=3600)

EXCHANGE_API = "https://openexchangerates.org/api/latest.json?app_id={app_id}"


def get_amount_in_euros(amount: int, currency: CurrencyOptions) -> int:
    if currency == CurrencyOptions.EUR:
        return amount

    return CurrencyConvertor.convert_currency(amount, currency, CurrencyOptions.EUR)


class CurrencyConvertor:
    app_id = os.getenv("CONVERTOR_APP_ID")

    @classmethod
    def convert_currency(cls, amount, from_currency, to_currency):
        conversion_rate = _get_conversion_rate(cls.app_id, from_currency, to_currency)
        return conversion_rate * amount


@cached(cache)
def _get_conversion_rate(app_id, from_currency, to_currency):
    response = requests.get(EXCHANGE_API.format(app_id=app_id))
    data = response.json()

    return data["rates"][to_currency] / data["rates"][from_currency]
