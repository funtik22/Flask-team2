import requests
import json
response=requests.get("http://127.0.0.1:5000/user/")
print(response.content)
print(response.content.decode())
user=response.content.decode()
u = json.loads(user)
print(u)
print(u['name'])
