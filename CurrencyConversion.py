import sys
from asi_functions import *


def main():
    date_str = validate_date(sys.argv)      # Validate date format

    while True:
        amount = float(get_valid_input(validate_amount))
        base_currency = get_valid_input(validate_currency_code).upper()
        target_currency = get_valid_input(validate_currency_code).upper()

        rate = get_exchange_rate(base_currency, target_currency, date_str)
        converted_amount = round(amount * rate, 2)
        print(f"{BOLD}{ORANGE}{amount}{RESET} {BOLD}{base_currency} is {ORANGE}{converted_amount}{RESET} {BOLD}{target_currency}")

        conversion = {
            "date": date_str,
            "amount": amount,
            "base_currency": base_currency,
            "target_currency": target_currency,
            "converted_amount": converted_amount
        }
        save_conversion(conversion)


if __name__ == "__main__":
    main()
