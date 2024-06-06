from .system import load_config
import requests

config = load_config()                                          # Load config file
CACHE = {}                                                      # Init cache
API_KEY = config["api_key"]                                     # Get api_key
API_URL = "https://api.fastforex.io/historical"


def get_exchange_rate(base_currency: str, target_currency: str, at_date: str) -> float:
    """
    Return rate if its cached or calling APi if it's not
    """
    rate = CACHE.get(base_currency, {}).get(target_currency)
    if rate is not None:
        return rate

    return fetch_exchange_rate_from_api(base_currency, target_currency, at_date)


def fetch_exchange_rate_from_api(base_currency: str, target_currency: str, at_date: str) -> float:
    """
    Fetch exchange rate from APi at historical date
    """
    params = {
        "date": at_date,
        "from": base_currency,
        "to": target_currency,
        "api_key": API_KEY
    }
    headers = {"accept": "application/json"}

    response = requests.get(API_URL, headers=headers, params=params).json()
    rate = response["results"][target_currency]
    cache_result(base_currency, target_currency, rate)
    return rate


def cache_result(base_currency: str, target_currency: str, rate: float) -> None:
    """
    Caching results in dict()
    """
    if base_currency not in CACHE.keys():
        CACHE[base_currency] = {}
    CACHE[base_currency][target_currency] = rate
