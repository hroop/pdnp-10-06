import sys

print()  # wypisz/wydrukuj
print("Nazywam się Radek")
# ctrl d - powielenia elemntów
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# print("Nazywam sie Radek')
#   File "C:\Users\cscomarch\PycharmProjects\pdnp-10-06\pierwszy.py", line 12
#     print("Nazywam sie Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 12)
# ctrl / - komentowanie zaznaczonego kodu
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'> dane tekstowe
print("39")
print(type("39"))  # <class 'str'>
print(39)
print(type(39))  # <class 'int'> liczby całkowite
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640
# )
print("39" + "39")  # 3939 - konkatenacja - łączenie stringów
print(39 + 39)  # 78
# print(39 + "39")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# silne typowanie - sam nie zamienia typów
print(int("39") + 39)  # int() rzutowanie na int (zamiana)

print(5 * "4")  # 44444

# zmienna - pudełko na dane
# snake_case
# typowanie dynamiczne - w kadej chwili dolny typ danej możemy umieścić w zmiennej
name = "Radek"
print(type(name))  # <class 'str'>
print(name + "Kowalski")  # RadekKowalski

name = 39
print(type(name))  # <class 'int'>
print(name)
# print(name + "Kowalski") TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(name) + "Kowalski")  # 39Kowalski str() - rzutowanie na string(zamiana na tekst)
print(type(name))  # <class 'int'>

name: str = 90  # tylko podpowiedź
print(name)
print(type(name))  # <class 'int'>

age = 48
print(age)
print(type(age))
