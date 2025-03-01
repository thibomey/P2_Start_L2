# Bekijk de documentatie voor de free games API: https://www.freetogame.com/api-doc
# Hoe zou je een lijst met games kunnen binnenhalen met de volgende voorwaarden?
# - PC-games
# - Gesorteerd volgens relevantie
import requests
#platform_name = input ("Welk platform? ")

#request = requests.get(f'https://www.freetogame.com/api/games?platform={platform_name}&sort-by=alphabetical')
#tekst = request.text
request = requests.get(
    url='https://www.freetogame.com/api/games',
    params={"platform": "pc","sort-by": "alphabetical" }
)
tekst = request.text

if request.status_code == 200:
    data = request.json()
    for game in data:
        title = game['title']
        if "world" in title.lower():
            print (title)
            print(game['short_description'])


else:
    print(f"Er is iets foutgelopen. Foutcode{request.status_code}")



# Bijkomende opdracht:
# Print voor alle pc-games die het woord “world” bevatten, de titel en de game_url.
# Zorg dat het niet gevoelig is aan hoofdletters.