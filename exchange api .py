import json
from urllib.request import urlopen

from rich import print

API_KEY = "60853205d439e76d4b83925b"
BASE_CURRENCY = input("Base currency? ")
EXCHANGE_CURRENCY = input("Exchange currency? ")
EXCHANGE_RATE_API_URL = (
    f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"
)

result = urlopen(EXCHANGE_RATE_API_URL).read().decode()
data = json.loads(result)
exchange_rate = data['conversion_rates'][EXCHANGE_CURRENCY]
amount = float(input(f"How much {BASE_CURRENCY} you have: "))

print(f"In {EXCHANGE_CURRENCY} it will be: {round(amount * exchange_rate, 2)}")