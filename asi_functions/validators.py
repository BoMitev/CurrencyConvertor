from datetime import datetime
from iso4217 import Currency
from typing import Callable
from .system import BOLD
import re


def get_valid_input(validation_fn: Callable) -> str:
    """
    Auxiliary function for validating user input
    """
    while True:
        value = input()
        if value.upper() == "END":
            exit(0)
        if validation_fn(value):
            return value


def validate_date(date: str) -> str | None:
    """
    Date format validator
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        print(f"{BOLD}Invalid date format. Please use YYYY-MM-DD.")
        exit(0)


def validate_amount(amount: str) -> bool:
    """
    Monetary values should be constrained to two decimal places.
    """
    if bool(re.match(r'^\d+(\.\d{1,2})?$', amount)):
        return True
    print(f"{BOLD}Please enter a valid amount")
    return False


def validate_currency_code(code: str) -> bool:
    """
    Currencies must be in ISO 4217 three letter currency code format.
    """
    if code.upper() in Currency:
        return True
    print(f"{BOLD}Please enter a valid currency code")
    return False
