# Currency convertor

A CLI application that integrates with Fast Forex and lets the user convert currencies with exchange rates from past dates.

## Installation

Step-by-step instructions on how to get the development environment running.

```bash
git clone https://github.com/BoMitev/CurrencyConvertor.git
cd CurrencyConvertor
pip install -r requirements.txt
```

## Configuration

Create **_config.json_** file in main project directory

```python
{
  "api_key" : "YOUR_API_KEY"
}
```

## Running the Script

```python
python CurrencyConversion.py 2024-06-01
```
Use desired date as command line argument in format '_YYYY-MM-DD_'
