import requests

# opvangen = requests.get("https://catfact.ninja/fact")
# katjson = opvangen.json()

# print(katjson["fact"])

x = 0

while x < 10:
    joke_of_the_day = requests.get("https://official-joke-api.appspot.com/random_joke")
    jokejson = joke_of_the_day.json()

    print("Joke: ", jokejson["setup"])
    print("Answer: ", jokejson["punchline"])

    verz_postcodes = []
    verz_postcodes += zippjson["post code"]

    x += 1

else: print("10 jokes, namelijk:")

print(verz_jokes)





    zippo = requests.get("https://api.zippopotam.us/us/33162")
    zippjson = zippo.json()

    print("Post code: ", zippjson["post code"])
    print("Country: ", zippjson["country"])

    
