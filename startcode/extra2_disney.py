# Bekijk de documentatie voor de Disney API: https://disneyapi.dev/docs/
# Vraag aan de API alle personages.
#
# Print alle personages als volgt:
# Naam: Abu - Oorspronkelijke film: Aladdin (film)
# Naam: Abuelita - Oorspronkelijke film: Onbekend

import requests

response = requests.get('https://api.disneyapi.dev/character')

tekst = response.text

if response.status_code == 200:
    print(tekst)
else:
    print(f"Er is iets foutgelopen. Foutcode{response.status_code}")

data = response.json()



# Zorg er voor dat je alle personages kan tonen.