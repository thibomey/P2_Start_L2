# Gebruik de bored api om een JSON-bestand in te lezen: https://www.boredapi.com/api/activity
# De response als json interpreteren kan zo: data = response.json()
import requests

personen = input ("Hoeveel personen? ")

response = requests.get(f'http://bored.api.lewagon.com/api/activity?participants={personen}')
tekst = response.text

if response.status_code == 200:
    print(tekst)
else:
    print(f"Joke not found. Foutcode{response.status_code}")

data = response.json()