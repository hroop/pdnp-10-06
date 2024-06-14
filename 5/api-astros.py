# REST API
# GET, POST, PUT/PATCH, DELETE
import requests

# pip install requests
url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx przekierowania
# 4xx 404 - brak zasoby(błedny adres), 400 Bad Request bład zapytania
# 5xx błedy serwera
print(response.text)
print(type(response.text))  # <class 'str'>
response_data = response.json()
print(response_data)
print(type(response_data))  # <class 'dict'>
# wypisac klucze w głównej gałęzi
print(response_data.keys())
# dict_keys(['people', 'number', 'message'])
for k, v in response_data.items():
    print(k, "=>", v)
# people = > [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'},
#             {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'},
#             {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'},
#             {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'},
#             {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#             {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}]
# number = > 12
# message = > success

print(response_data["people"][0])  # {'craft': 'ISS', 'name': 'Oleg Kononenko'}
print(response_data["people"][0]['name'])  # Oleg Kononenko
for p in response_data['people']:
    print(p['craft'], p['name'])
# ISS Oleg Kononenko
# ISS Nikolai Chub
# ISS Tracy Caldwell Dyson
# ISS Matthew Dominick
# ISS Michael Barratt
# ISS Jeanette Epps
# ISS Alexander Grebenkin
# ISS Butch Wilmore
# ISS Sunita Williams
# Tiangong Li Guangsu
# Tiangong Li Cong
# Tiangong Ye Guangfu
