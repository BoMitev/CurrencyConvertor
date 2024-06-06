import json

BOLD = '\033[1m'
ORANGE = '\033[33m'
RESET = '\033[0m'


def load_config() -> json:
    """
    Load config.json file
    """
    with open("config.json") as config_file:
        return json.load(config_file)


def save_conversion(conversion: dict) -> None:
    """
    Saving conversation
    If the file doesn't yet exist, a new one gets created.
    """
    try:
        with open("conversions.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(conversion)
    with open("conversions.json", 'w') as file:
        json.dump(data, file, indent=4)