# kolekcja
# lista - przechowuje wiele danych, różnego typu na raz
# zachowuje kolejnosc dodawania elementów

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodawanie elemntów do listy
lista.append("Radek")
lista.append("Maciek")
lista.append("Zenek")
lista.append("Aldona")
print(lista)  # ['Radek', 'Maciek', 'Zenek', 'Aldona']
#                  0[-4]   1[-3]     2[-2]     3[-1]
print(lista[0])
# print(lista[4])  # IndexError: list index out of range
print(lista[2])
print(len(lista))  # len() długosc listy 4
print(lista[-1])
print(lista[-2])
# wypisac fragment listy - slicowanie
print(lista[0:3])  # ['Radek', 'Maciek', 'Zenek'] indeksy 0,1,2
print(lista[:3])  # ['Radek', 'Maciek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Aldona']
print(lista[:])  # ['Radek', 'Maciek', 'Zenek', 'Aldona']
print(lista[-2:0])  # []
print(lista[0:-2])  # ['Radek', 'Maciek']
print(lista[2:3])  # ['Zenek']
print(lista[2:10])  # ['Zenek', 'Aldona']
print(lista[7:10])  # []
print(lista[2:2])  # []
print(lista[0:3:2])  # ['Radek', 'Zenek'] start:stop:krok

lista_15 = list(range(15))  # range() - generuje liczby z zakresu 0..14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[-5:])  # [10, 11, 12, 13, 14] piec ostatnich elementów
