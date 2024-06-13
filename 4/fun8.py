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
    pass
