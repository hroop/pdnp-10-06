# dekoratory - przyjmuje funkcje jako argument i dodaje do niej nowwą funkcjonalnosci
# dekrator wykorzystuje mechanizm funkcji zagnieżdzonej, wewnętrznej

def dekor(func):
    def wew():
        print("Dekorujemy")
        return func()

    return wew  # zwracamy tylko adres


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@dekor
def hej():
    print('Hej')


@uppercase_decorator
def greeting():
    return "Hello World!!!"


hej()  # Hej
# po dodaniu dekoratora @dekor
# Dekorujemy
# Hej
print(greeting())
# bez dekoratora Hello World!!!
# z dekoratorem: HELLO WORLD!!!
