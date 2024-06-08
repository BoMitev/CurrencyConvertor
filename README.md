> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

# Currency convertor
A CLI application that integrates with Fast Forex and lets the user convert currencies with exchange rates from past dates.

## Installation
Step-by-step instructions on how to get the development environment running.
Clone the repository
```commandline
git clone https://github.com/BoMitev/CurrencyConvertor.git
```

Navigate to your project directory
```commandline
cd ..\CurrencyConvertor
```

Create a virtual environment named .venv:
```commandline
python -m venv .venv
```

Activate the Virtual Environment:
* for Windows:
```bash
.\.venv\Scripts\activate
```
* for macOS/Linux:
```commandline
source .venv/bin/activate
```

Install requirements
```commandline
pip install -r requirements.txt
```

## Configuration
Create **_config.json_** file in main project directory

```json
{
  "api_key" : "YOUR_API_KEY"
}
```

## Running the Script
```commandline
python3 CurrencyConversion.py 2024-06-01
```
Use desired date as command line argument in format '_YYYY-MM-DD_'
