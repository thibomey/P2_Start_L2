# Print de response van deze joke api:https://official-joke-api.appspot.com/random_joke
# Kijk naar het http_request voorbeeld om te zien hoe het moet.
import requests

request = requests.get('https://official-joke-api.appspot.com/random_joke')
tekst = request.text

# Pas je code aan zodat:
# - Als de code gelijk is aan 200, de response geprint wordt.
# - Bij andere codes een foutmelding geprint wordt. (Wees creatief met je foutcodes).

if request.status_code == 200:
    print(tekst)
else:
    print(f"Joke not found. Foutcode{request.status_code}")