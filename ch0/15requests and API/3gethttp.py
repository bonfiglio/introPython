import requests

response = requests.get('https://www.jagex.com/careers')
print(response.status_code)
if response.status_code != 200:
    raise Exception("ERROR: GET request unsuccessful.")
print(response.content)
