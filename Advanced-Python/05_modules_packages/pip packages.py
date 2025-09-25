import requests

url = "https://official-joke-api.appspot.com/random_joke"
res = requests.get(url)
joke = res.json()
print(f"{joke['setup']} 🤔")
print(f"{joke['punchline']} 😂")


