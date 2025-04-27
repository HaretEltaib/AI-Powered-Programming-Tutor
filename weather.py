import requests


url = f"https://official-joke-api.appspot.com/random_joke"

response = requests.get(url=url)
if response.status_code == 200:
    joke = response.json()
    print(f"{joke['setup']}")
    print(f"{joke['punchline']}")
    print(joke)
  
else:
    print("feld nto get weather data")