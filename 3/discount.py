from datetime import date, datetime, timedelta

today = date.today()
print("Data:", today)  # Data: 2024-06-12

time = datetime.now()
print('Czas:', time)  # Czas: 2024-06-12 12:13:56.079080
print(type(time))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro:", tomorrow)  # Jutro: 2024-06-13

print(time.time())  # 12:17:21.404271
print(today.day)  # 12

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 12/06/2024

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 12:20

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 50},
    {'sku': 3, 'exp_date': tomorrow, 'price': 250},
    {'sku': 4, 'exp_date': today, 'price': 80.0},
    {'sku': 5, 'exp_date': today, 'price': 100.0},
    {'sku': 6, 'exp_date': today, 'price': 100.0},
    {'sku': 7, 'exp_date': tomorrow, 'price': 100.0},
    {'sku': 8, 'exp_date': today, 'price': 100.0},
]

for p in products:
    # print(p)  # {'sku': 1, 'exp_date': datetime.date(2024, 6, 12), 'price': 100}
    # print(p['sku'])
    if p['exp_date'] != today:
        print('cena nie ulega zmianie')
        continue
    p['price'] *= 0.8
    print(f"""Price for sku{p['sku']} 
is now {p['price']}""")
# Price for sku1
# is now 80.0
# Price for sku2
# is now 40.0
# Price for sku4
# is now 64.0
# Price for sku5
# is now 80.0
# Price for sku6
# is now 80.0
# Price for sku8
# is now 80.0
# Price for sku6
# is now 80.0
# cena nie ulega zmianie
# Price for sku8
# is now 80.0