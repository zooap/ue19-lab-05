import requests

# URL de l'API
url = "https://official-joke-api.appspot.com/random_joke"

# Requête GET à l'API
response = requests.get(url)

# Vérification du statut de la réponse
if response.status_code == 200:
    # Décodage de la réponse JSON
    joke = response.json()
    print(f"Voici une blague :\n{joke['setup']}\n{joke['punchline']}")
    print('test')
else:
    print(f"Erreur lors de la récupération de la blague. Statut : {response.status_code}")
