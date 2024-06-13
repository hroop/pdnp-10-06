def allparams(a, b, c=42, d=456):
    print(a, b)
    print(c, d)


allparams(1, 2)
allparams(1, 2, 5, 6)
# 1 2
# 42 456
# 1 2
# 5 6
allparams(a=4, b=6, c=7)


# 4 6
# 7 456


def allparams2(a, b, /, c=42, d=456):
    print(a, b)
    print(c, d)


# argumenty po lewej stronie / muszą byc przekazywane jako pozycyjne
allparams2(1, 2)  # TypeError: allparams2() got some positional-only arguments passed as keyword arguments: 'a, b'
allparams2(1, 2, 3)
allparams2(1, 2, 3, d=45)


def alllparam_3(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


# a i b musimy przekazac po pozycji
alllparam_3(1, 2)
alllparam_3(1, 2, 3)  # c, d 3 256
alllparam_3(1, 2, 3, 4, 5, 6)  # args (4, 5, 6)  # c, d 3 7
# d musimy przekazac po nazwie
alllparam_3(1, 2, 3, 4, 5, 6, d=7)  # args (4, 5, 6)
alllparam_3(1, 2, 3, 4, 5, 6, d=7, name='Radek')  # kwargs {'name': 'Radek'}
alllparam_3(1, 2, 3, 4, 5, 6, d=7, a=8, name='Radek')  # kwargs {'a': 8, 'name': 'Radek'}
