# pętle - mozliwosć wykonania wielokrotnie tego samego kodu
# for - pętla iteracyjna
import random

for i in range(5):  # 0..4
    print(i)

for i in range(5):
    pass  # nic ie rób

for _ in range(10):
    pass
    print(_)
print("-----")
for i in range(20):  # 0..19
    print(i, i * 2)

lista_kule = list(range(1, 50))
lista_wylosowane = []
for i in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [20, 15, 18, 38, 40, 3]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wylosowane:
    if c > 10:
        print('Większe od 10', c)
    print(c)

for i in range(0, 20, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # od 10 do 2 co druga w dół
    print(i)

for i in range(-10, 0):
    print(i)
lista2 = [1, 2, 3, 1, 5, 6, 7, 2, 3, 5]

for c in lista2:
    if c == 3:
        c += 1  # c = c + 1
        print(c)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', 'Tomek', 'Zenek', 'Ania']
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# wyswietlic z listy elementy w postaci 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca numer i elemnt z kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
a, b = (3, 'Ania')
print("index=", a, "element=", b)  # index= 3 element= Ania
for i, p in enumerate(imiona):
    print(i, p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

# ludzie = ['Radek', 'Arek', 'Tomek', 'Ania']
ludzie = ['Radek', 'Arek', 'Tomek', 'Ania', 'krzysztof']  # IndexError: list index out of range
wiek = [40, 34, 23, 30]

# wypisac w postaci Radek 40
# dla róznych długosci listy będzie bład
# IndexError: list index out of range
# for i in range(len(ludzie)):  # range(4) -> for i in range(4)
#     print(ludzie[i], wiek[i])
#
# for p in ludzie:
#     print(p, wiek[ludzie.index(p)])

# zip() - łączenie kolekcji
for i in zip(ludzie, wiek):
    print(i)  # ('Ania', 30)

for p, w in zip(ludzie, wiek):
    print(p, w)  # Tomek 23

# wyswietlic w postaci 0 Radek 30
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (0, ('Radek', 40))

a, b = (0, ('Radek', 40))
print(a)
print(b)  # ('Radek', 40)
c, d = b
print(c, d)  # Radek 40
(a, (c, d)) = (0, ('Radek', 40))
print(a, c, d)  # 0 Radek 40
a, (c, d) = (0, ('Radek', 40))
print(a, c, d)  # 0 Radek 40

for i, (p, w) in enumerate(zip(ludzie, wiek)):
    print(i, p, w)
# 0 Radek 40
# 1 Arek 34
# 2 Tomek 23
# 3 Ania 30
