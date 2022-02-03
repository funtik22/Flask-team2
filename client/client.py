import json
import requests
response = requests.get("http://127.0.0.1:5000/")
print(response.content)
print(response.content.decode())
user = requests.content.decode()
print(user)
u = json.loads(user)
print(u["name"])
