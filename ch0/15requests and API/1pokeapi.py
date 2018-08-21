import requests


# pip install requests
# https://tutorialedge.net/python/python-http-requests-tutorial/
def main():
    # we define a request object that is equal to requests.get('API')
    req = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    # we then print out the http status_code that was returned on making this request
    # you should see a successfull '200' code being returned.
    print(req.status_code)
    if req.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = req.json()

    print(data)


if __name__ == '__main__':
    main()
