# krotka - tupla - kolekcja, niemutowalna
# krotka jedoelementowa - zmienna - niezmienna - stała

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>

tupla_3 = 'Radek',
print(type(tupla_3))  # <class 'tuple'>

# PEP8 zaleca przy tupli jednoelementowej używać nawiasów
tupla_4 = ("Radek",)
print(tupla_4)  # ('Radek',)

tupla_names = "Radek", 'Tomek', "Zenek", "Marek"
print(type(tupla_names))  # <class 'tuple'>

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

# tupla_liczby[2] = 0  # TypeError: 'tuple' object does not support item assignment

print(tupla_names.count("Tomek"))  # 1
print(tupla_names.index("Tomek"))  # 1

# del(tupla_names[0])  # TypeError: 'tuple' object doesn't support item deletion
del tupla_liczby  # usunięcie całe tupli
# print(tupla_liczby[0])  # NameError: name 'tupla_liczby' is not defined - nie istnieje bo została usunięta

# rozpakowanie krotki
tup = 1, 2
a, b = tup
x, y = 1, 2
print(a)  # 1
print(b)  # 2

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * - worek na pozostałe dane
print(a)  # 1
print(b)  # [2, 3]

print(len(tupla_names))  # 4
# rozpakowac do trzech zmiennych name1, name2, name3
name1, *name2, name3 = tupla_names
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek'] Marek

*name1, name2, name3 = tupla_names
print(name1, name2, name3)  # ['Radek', 'Tomek'] Zenek Marek

name1, name2, *name3 = tupla_names
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Marek']

lista = list(tupla_names)  # list() - rzutowanie na listę
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marek']
print(type(lista))  # <class 'list'>

# sortowanie krotki zwraca listę
print(sorted(tupla_names))  # ['Marek', 'Radek', 'Tomek', 'Zenek']
