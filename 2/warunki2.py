# match case
# od Python 3.10

lista = []
lang = input("Podaj znany ci język programowania")

match lang.lower().replace(" ", ''):
    case "python":
        lista.append("python")
    case "java":
        lista.append("Java")
    case _:  # warunek domyslny
        print("Nie znaleziona języka programowania")

print(lista)
