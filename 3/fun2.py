# funkcje zwracające wynik
def dodaj(a, b):
    return a + b  # zwróc wynik do miejsca skąd zostałeś wywołany


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(10, 10))
print(odejmij())
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(c=9, b=9))
print(odejmij(9, 12) + dodaj(7, 65))  # 69

print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=5, cena=1000))
# 1230.0
# 1080.0
# 1050.0
zm = oblicz_vat(1000)
print(zm)  # 1230.0 float

if zm == 1230:
    print("Działa")  # Działa
