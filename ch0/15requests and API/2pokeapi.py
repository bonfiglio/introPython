import requests
import json


# https://tutorialedge.net/python/python-http-requests-tutorial/
def main():
    req = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print(json_response)
    print("Pokemon Name: " + json_response['name'])
    print(f"{json_response['abilities']}")


if __name__ == '__main__':
    main()
