def connect(**opcje):  # ** dowolna ilosc argumentów nazwanych, słownikowych
    print(opcje)  # {'a': 6}
    conect_param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    conect_param['pwd'] = opcje
    print(conect_param)


connect(a=6)
connect(a=6, b=8)
connect(a=6, b=8, c=23)
connect(a=6, b=8, c=23, name="Radek")


# {'a': 6}
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 6}}
# {'a': 6, 'b': 8}
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 6, 'b': 8}}
# {'a': 6, 'b': 8, 'c': 23}
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 6, 'b': 8, 'c': 23}}
# {'a': 6, 'b': 8, 'c': 23, 'name': 'Radek'}
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 6, 'b': 8, 'c': 23, 'name': 'Radek'}}

def all_params(*args, **kwargs):
    print(args, kwargs)


all_params()
all_params(1)
all_params(1, 2, 3)
all_params(a=1, b=2, c=3)
all_params(1, b=2, c=3)
# all_params(a=1, b=2, 3)  # SyntaxError: positional argument follows keyword argument
# () {}
# (1,) {}
# (1, 2, 3) {}
# () {'a': 1, 'b': 2, 'c': 3}
# (1,) {'b': 2, 'c': 3}
