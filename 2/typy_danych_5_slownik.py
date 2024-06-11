# słownik - dane typu klucz wartosc
# {'user': 'Radek', 'wiek': 50}
# odpowiednik jsona
# klucze nie mogą się powtarzać

# pusty słownik
dictionary = dict()
print(dictionary)  # {}

dictionary1 = {}
print(dictionary1)  # {}

print(type(dictionary1))  # <class 'dict'>
print(type(dictionary))  # <class 'dict'>

print(dictionary.keys())  # dict_keys([])
print(dictionary.values())  # dict_values([])
print(dictionary.items())  # dict_items([])

dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39}
print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Tomek', 39])
print(dictionary.items())  # dict_items([('imie'#, 'Tomek'), ('wiek', 39)]# )

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

print(dictionary['imie'])  # Tomek
# print(dictionary['name'])  # KeyError: 'name'
print(dictionary.get('imie'))  # Tomek
print(dictionary.get('name', 'default'))  # default

# input() - pobiera dane np.:  z klawiatury
tekst = input("Wpisz tekst")
print(tekst)
