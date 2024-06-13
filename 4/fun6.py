# funkcja obliczjąca srednią
def liczby(name=None, *cyfry):
    print(cyfry)  # (1, 2, 3, 4, 5, 6)
    count = len(cyfry)
    suma = 0
    suma_2 = sum(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except ZeroDivisionError:
        print("Dzielenie przez zero")
        print(f"Uczeń {name} nie ma ocen")
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Uczeń {name}, średnia wynosi {avg}")
    finally:
        print("Obliczone")
        print(suma_2)


liczby("Radek", 1, 2, 3, 4, 5, 6)
liczby("Tomek")
liczby("Magda", 5, 6, 5, 6, 5)
liczby("Franek", 2, 3, 3, 3, 2)
# (1, 2, 3, 4, 5, 6)
# Uczeń Radek, średnia wynosi 3.5
# Obliczone
# 21
# ()
# Dzielenie przez zero
# Uczeń Tomek nie ma ocen
# Obliczone
# 0
# (5, 6, 5, 6, 5)
# Uczeń Magda, średnia wynosi 5.4
# Obliczone
# 27
# (2, 3, 3, 3, 2)
# Uczeń Franek, średnia wynosi 2.6
# Obliczone
# 13