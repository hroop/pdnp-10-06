# funkcja obliczjąca srednią
def liczby(name=None, *cyfry):
    print(cyfry)  # (1, 2, 3, 4, 5, 6)
    count = len(cyfry)
    suma = 0
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


liczby("Radek", 1, 2, 3, 4, 5, 6)
liczby("Tomek")
liczby("Magda", 5, 6, 5, 6, 5)
liczby("Franek", 2, 3, 3, 3, 2)
