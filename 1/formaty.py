user = 'Tomek'  # str
wiek = 39  # int
wersja = 3.900001  # float - liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 123456789123  # int
print(type(liczba))  # <class 'int'>

print('Witaj %s masz teraz %d lat' % (user, wiek))  # Witaj Tomek masz teraz 39 lat
# W tym przypadku typy są sprawdzane
# print('Witaj %d masz teraz %s lat' % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit

print("witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, 'wiek': wiek})
print("witaj %(user)s, masz teraz %(age)d lat." % {'user': user, 'age': wiek})
# Witaj Tomek masz teraz 39 lat
# witaj Tomek, masz teraz 39 lat.
# witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")
print("Witaj {}, masz teraz {} lat.".format(user, wiek))

print('Używamy wersji Pythona %i' % 3)  # Używamy wersji Pythona 3
print('Używamy wersji Pythona %f' % 3.9)  # Używamy wersji Pythona 3.900000
print('Używamy wersji Pythona %.1f' % 3.9)  # Używamy wersji Pythona 3.9
print('Używamy wersji Pythona %.2f' % 3.9)  # Używamy wersji Pythona 3.90
print('Używamy wersji Pythona %.0f' % 3.9)  # Używamy wersji Pythona 4
# zaokrągla przy wyświetlaniu
print('Używamy wersji Pythona %.f' % 3.9)  # Używamy wersji Pythona 4
x = 3.14
print('Zero miejsc po przecinku %.f' % x)  # Zero miejsc po przecinku 3

print("X sie nie zmieniło", x)  # X sie nie zmieniło 3.14

y = round(x)
print("y=", y)
print("x=", x)
# y= 3
# x= 3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.900001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 123456789123
print('Nasza duża liczba {:,}'.format(liczba))  # Nasza duża liczba 123,456,789,123
print('Nasza duża liczba {:,}'.format(liczba).replace(",", "."))  # Nasza duża liczba 123.456.789.123
print('Nasza duża liczba {:,}'.format(liczba).replace(",", " "))  # Nasza duża liczba 123 456 789 123

print(f"Nasza duża liczba {liczba:,}")
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))

liczba_2 = 123_456_789_123
print(liczba_2)  # 123456789123
print(type(liczba_2))  # <class 'int'>
print(f"Nasza duża liczba {liczba_2:,}".replace(",", " "))
# Nasza duża liczba 123 456 789 123
