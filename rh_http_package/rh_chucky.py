import requests
import json

def chuck_norris_joke():
    headers = {
        'X-RapidAPI-Key': 'bb68c0589amsh03cab373e7c04e8p1cbd02jsna3214dfd4738',
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.get('https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random', headers=headers)
    data = response.json().get('value')
    print(data)
    return data


if __name__ == '__main__':
    chuck_norris_joke()
