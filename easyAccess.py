import requests

def say(value):
    print(value)

def math(value):
    print(value)

def joke():
    response = requests.get("https://pixel-api-production.up.railway.app/fun/joke")
    joke = response.json()["joke"]
    print(joke)
