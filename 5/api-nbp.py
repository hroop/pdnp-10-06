import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = re.get(url)
print(response.text)
# {"table":"A","currency":"euro","code":"EUR","rates":[{"no":"115/A/NBP/2024","effectiveDate":"2024-06-14","mid":4.3581}]}
# currency, effectiveDate, mid
response_data = response.json()
currency = response_data['currency']
print("Waluta:", currency)
effective_date = response_data['rates'][0]['effectiveDate']
mid = response_data['rates'][0]['mid']
print(f"Waluta {currency}, data: {effective_date} kurs: {mid}")
# Waluta euro, data: 2024-06-14 kurs: 4.3581
