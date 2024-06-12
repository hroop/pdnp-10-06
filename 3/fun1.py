# funkcje - wydzielony fragment kodu, mozna go wykonac wielokrotnie
# deklaracja funkcji musi nastąpic wcześniej niz jej wywołanie
# w miejscu deklaracji funkcja nic nie wykonuje

a = 8
b = 9


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)  # argumenty z globalnego zakresu


def dodaj2(a, b):  # funkcja z dwoma parametrami, obowiązkowe do przekazania
    print(a + b)


def odejmij(a, b, c=0):  # a,b - obowiązkowe, c - domyslny
    print(a - b - c)


# uzycie funkcji
dodaj()  # 17
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(7, 56)  # 63
odejmij(1, 2)
odejmij(1, 2, 3)  # argumenty pozycyjne
odejmij(b=9, c=8, a=10)  # argumenty przekazane po nazwie
odejmij(5, c=10, b=7)
# odejmij(a=5, b=10, 7)  # SyntaxError: positional argument follows keyword argument
print(dodaj())  # None
print(dodaj() + dodaj2(5, 6))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
