# while - pętla sterowana warunkiem

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 1 !!!")
    if licznik > 10:
        break
print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 2 !! !! !!")

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło. Podaj ponownie")
# print("Hasło prawidłowe")

lista = []
lista_int = []

while True:
    wej = input('Podaj liczbę')  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['6', '8', '90', '12', '11', '1']  str
# [6, 8, 90, 12, 11, 1] int
