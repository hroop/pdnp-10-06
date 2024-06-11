# wyjatki - rzucanie, obsługa
# print(5 /0)

# Traceback (most recent call last):
#   File "C:\Users\cscomarch\PycharmProjects\pdnp-10-06\2\wyjatki.py", line 1, in <module>
#     print(5 /0)
#           ~~^~
# ZeroDivisionError: division by zero

try:
    # print(5/0)
    # print(5 / "00")
    # print("A" + 9)
    print(int("A"))
    wynik = 5 / 1
except ZeroDivisionError:
    print('Dzielenie przez zero')
except TypeError:
    print('bład typu')
except ValueError:
    print("bład wartości")
except Exception as e:
    print("wystąpił bład", e)
else:  # tylko gdy nie wystapi bład
    print("Wynik:", wynik)
finally:  # wykona sie zawsze
    print("Skończyłem")
print("Program nadal działa")
# Dzielenie przez zero
# Program nadal działa

# try - except [else - finally]
