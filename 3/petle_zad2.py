dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

# wyswietli klucze
for k in dictionary:
    print(k)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
    # imie
    # nazwisko

# wyswietlić wartość
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wyświetlenie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski

print("Radek", end="")
print("Tomek")  # RadekTomek tu end="\n"
print("Następny wiersz")  # w nowej linii Następny wiersz

dictionary2 = {'imie': 'Radek', 'nazwisko': 'Kowalski'}
d = {}
for k, v in dictionary2.items():
    d[v] = k
print(dictionary2)  # {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(d)  # {'Radek': 'imie', 'Kowalski': 'nazwisko'}
print({value: key for key, value in dictionary2.items()})  # {'Radek': 'imie', 'Kowalski': 'nazwisko'}
