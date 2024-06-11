import random

# generowanie liczb pseudolosowych

print(random)
# <module 'random' from 'C:\\Users\\cscomarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>

print(random.randint(1, 100))  # int 1, 100
print(random.randrange(1, 100))  # int 1 do 99
print(random.randrange(7))  # int 0..6
print(random.random())  # 0.7737474880682195 float 0 do 0.999999
print(random.random() * 10)  # float 3.9668286657612803 0 do 9.999999

lista = [6, 12, 34, 56, 67, 89, 120]
print(random.choice(lista))  # 6

lista_kule = list(range(1, 50))  # range() od 1 do 49
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [32, 15, 43, 49, 15, 43] losowanie z powtórzeniami
print(random.sample(lista_kule, 6))  # [33, 45, 46, 11, 3, 31]
print(random.sample(lista_kule, k=6))  # [28, 13, 46, 34, 3, 1]
