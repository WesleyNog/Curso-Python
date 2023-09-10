import requests

URL = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(URL).json()
print(response)