# funkcja lambda - skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, mozliwosc deklaracji w miejscu wykonaniu

def odejmij2(a, b):
    return a - b


print(odejmij2(8, 4))  # 4

odejmij = lambda a, b: a - b  # return a - b
print(odejmij(5, 2))  # 3

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
# 1230.0
# 1080.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(10))
print(wiek(11))
print(wiek(17))
print(wiek(18))
print(wiek(25))
# dziecko
# nastolatek
# nastolatek
# nastolatek
# dorosły
# dorosły

lista = [1, 2, 5, 34, 56, 100, 200, 500]
print(lista * 2)  # [1, 2, 5, 34, 56, 100, 200, 500, 1, 2, 5, 34, 56, 100, 200, 500]

lista_wynik = []
for i in lista:
    lista_wynik.append(i * 2)
print(lista_wynik)  # [2, 4, 10, 68, 112, 200, 400, 1000]
print([i * 2 for i in lista])  # [2, 4, 10, 68, 112, 200, 400, 1000]


def zmien(x):
    return x * 2


lista_wynik_funkcja = []
for i in lista:
    lista_wynik_funkcja.append(zmien(i))
print(lista_wynik_funkcja)  # [2, 4, 10, 68, 112, 200, 400, 1000]

# funkcje wyzszego rzędu
# map()  - pobiera elemt z kolekcji, wykonuje na nim zadaną funkcję
print(f"Zastosowanie map(): {list(map(zmien, lista))}")  # Zastosowanie map(): [2, 4, 10, 68, 112, 200, 400, 1000]
# Uzycie lambdy jako funkcja anonimowa, deklaracja w miejscu wykonania
print(
    f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map(): [2, 4, 10, 68, 112, 200, 400, 1000]
print(
    f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")  # Zastosowanie map(): [4, 8, 20, 136, 224, 400, 800, 2000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)

# filter() - pobiera dane, zwraca spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 50, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 200, lista))}")
# Zastosowanie filter(): [1, 2]
# Zastosowanie filter(): [56, 100, 200, 500]
# Zastosowanie filter(): [500]
# x > 3 i x < 150
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 150, lista))}")
# Zastosowanie filter(): [5, 34, 56, 100]
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 150, lista))}")
