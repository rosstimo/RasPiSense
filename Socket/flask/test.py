import requests

BASE = "http://127.0.0.1:5000/"
thing='stuff'
response = requests.get(BASE + "helloworld/Tim")
print(response.json())
response = requests.post(BASE + "helloworld/" + thing)
