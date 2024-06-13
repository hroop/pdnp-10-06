a = 10
b = 10


def dodaj():
    a = 6  # zmienne o zasiegu lokalnym tylko w tej funkcji
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # działamy na zmiennej globalnej
    a = 8  # nadpisujemy zmienna globalna a
    b = 9
    print(a + b)


def zwraca_wiele():
    return 1, 2, 3


print("Wartosć a z góry (globalne)", a)  # Wartosć a z góry (globalne) 10
dodaj()  # 13 na wartosciach lokalnych
print("Wartosć a z góry (globalne)", a)  # Wartosć a z góry (globalne) 10
dodaj2()  # 20 obliczenia na zmiennych globalnych
print("Wartosć a z góry (globalne)", a)  # Wartosć a z góry (globalne) 10
dodaj3()  # 17
print("Wartosć a z góry (globalne)", a)  # Wartosć a z góry (globalne) 8
dodaj2()  # 18
print("Wartosć a z góry (globalne)", a)  # Wartosć a z góry (globalne) 8
# ctrl shift strzałka
print(zwraca_wiele())  # (1, 2, 3)