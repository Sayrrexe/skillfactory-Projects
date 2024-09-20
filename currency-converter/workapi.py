import requests
import json

r = requests.get(f"https://v6.exchangerate-api.com/v6/6cdd05d883cf0f66b542d8a0/pair/EUR/GBP/2")
total_base = json.loads(r.content)
print(type(total_base))
tootla = total_base['conversion_result']
print(tootla)