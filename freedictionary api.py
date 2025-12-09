import json
from urllib.request import urlopen
from rich import print

what_lang = input("Lang? ")
word = input("Word? ")

DICT_API = f"https://freedictionaryapi.com/api/v1/entries/{what_lang}/"
URL = DICT_API + word

response = urlopen(URL).read().decode()
parsed_data = json.loads(response)

senses = parsed_data["entries"][0]["senses"]

for sense in senses[:3]:
    print(sense["definition"])
    print()