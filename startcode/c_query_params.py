# Maak een programma dat:
# - De naam van de gebruiker vraagt.
# - De naam van de gebruiker doorstuurt naar de API.
# - Een tekstje print met de naam en de voorspelde leeftijd.

import requests

naam = input ("Wat is je naam? ")

response = requests.get(f'https://api.agify.io?name={naam}')
tekst = response.text

if response.status_code == 200:
    print(tekst)
else:
    print(f"Er is iets foutgelopen. Foutcode{response.status_code}")

data = response.json()