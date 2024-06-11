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
print(lista_15[-5:])  # [10, 11, 12, 13, 14] pięć ostatnich elementów

# nadpisanie elemntu
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Aldona']
# lista[10] = 'Krzysztof'  # IndexError: list assignment index out of range

# wstawić element we wskazane miejsce
lista.insert(1, "Marek")
print(lista)  # ['Radek', 'Marek', 'Maciek', 'Mikołaj', 'Aldona']
lista.insert(11, "Zenek")
print(lista)  # ['Radek', 'Marek', 'Maciek', 'Mikołaj', 'Aldona', 'Zenek']

# sprawdzebnie indeksu dla danego elemntu
print(lista.index("Aldona"))  # 4
indeks = lista.index("Mikołaj")
print(indeks)  # 3

# usunięcie elemntu
lista.remove("Marek")
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Aldona', 'Zenek']
lista.append("Radek")
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Aldona', 'Zenek', 'Radek']
lista.remove('Radek')
print(lista)  # ['Maciek', 'Mikołaj', 'Aldona', 'Zenek', 'Radek']
print('Radek' in lista)  # True

# usunięcie elemntu po indeksie
indeks = lista.index("Mikołaj")
# lista.pop(indeks)
# pop() - zwraca usunięty element
print(lista.pop(indeks))  # Mikołaj
print(lista)
print(lista.pop(0))  # Maciek
print(lista.pop())  # Radek - usunie ostatni element z listy
print(lista)  # ['Aldona', 'Zenek']
lista.append("Anna")
lista.append("Tomek")
lista.append("Paulina")
print(lista)  # ['Aldona', 'Zenek', 'Anna', 'Tomek', 'Paulina']
print(lista.pop(-2))  # Tomek
print(lista)  # ['Aldona', 'Zenek', 'Anna', 'Paulina']

a = 1
b = 3
a = b
print("a=", a, "b=", b)  # a= 3 b= 3
b = 7
print("a=", a, "b=", b)  # a= 3 b= 7

lista_copy = lista.copy()  # kopia elementów listy
lista_2 = lista  # a = b to jest tylko kopiowanie adresu pamięci (referencji)
lista.clear()  # b = 7
print(lista_2)  # a []
print(lista)  # b []
print(lista_copy)  # ['Aldona', 'Zenek', 'Anna', 'Paulina']
print(id(lista_2))
print(id(lista))
print(id(lista_copy))
# 2115978056064
# 2115978056064
# 2115978376320

liczby = [54, 999, 34, 12, 22.34, 687]  # [54, 999, 34, 12, 22.34, 687]
print(liczby)
# liczby = [54, 999, 34, 12, 22.34, 687, "A"]  # [54, 999, 34, 12, 22.34, 687, 'A']
print(liczby)
print(type(liczby))  # <class 'list'>

liczby.sort()  # sortowanie
print(liczby)  # [12, 22.34, 34, 54, 687, 999]
# liczby = [54, 999, 34, 12, 22.34, 687, "A"]
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osob = ['radek', 'ola', 'agata', 'lena']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22.34, 12]

# sortowanie i odwrócenie
lista_osob.sort(reverse=True)
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']

liczby[3] = 6666
print(liczby[0:3])
print(liczby[-2])
# [999, 687, 54]
# 22.34
print(liczby[-3:])  # [6666, 22.34, 12]

liczby.remove(54)
print(liczby)  # [999, 687, 6666, 22.34, 12]

print(liczby.pop(1))  # 687
print(liczby)  # [999, 6666, 22.34, 12]
print(len(liczby))  # długość 4

print(liczby[0:4:2])  # [999, 22.34]
print(liczby[::-1])  # wyświetli w kolejności odwrotnej

tekst = "Python."
lista1 = list(tekst)  # rzutowanie na listę, rozpakowanie sekwencji
print(lista1)  # ['P', 'y', 't', 'h', 'o', 'n', '.']

lista3 = [tekst]
print(lista3)  # ['Python.']

krotka = tuple(liczby)  # tuple() rzutowanie na krotkę, tuplę
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 6666, 22.34, 12)
