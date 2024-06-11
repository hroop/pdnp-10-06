# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if

odp = True
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = 'Radek'

if odp == "Radek":  # == porównanie
    print("To jest Radek")

print(bool(odp))  # True
if odp:
    print("to jest", odp)

if odp == "Tomek":
    print("to jest Tomek")
else:  # wartosc domyslna
    print('To nie jest Tomek')

print("Dalsza cześć program")

# podatek = 0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
# print(f"Podatek wynosi {podatek * 100}%")
# print(f"Podatek wynosi {zarobki * podatek}")
# 0.2 dla dochodów 10000 do 29999

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print(f"Rabat wynosi {rabat}")

rabacik = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabacik}")

# zasymulujemy system zbierania logów
# zmienne będą przechowywać dane, które przyszłyz innego systemu
# w zaleznosci od danych, będziemy wykonywac różne zadania
# email, console, dowolny inny
# dla console: alert - komunikat
# "Stało się cos strasznego"
# email
# zapisujemy komunikaty do listy
# error, medium, dowolny inny
# dodamy własciwy opis komunikaty

alert_system = 'console'
error = 'medium'

error_message = "Stało się cos strasznego"
lista_bledow = []

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    pass  # nic nie rób
    if error == 'error':
        lista_bledow.append(error)
        print("Wystąpił bład error")
    elif error == 'medium':
        lista_bledow.append(error)
        print("Wystapiło ostrzeżenie")
    else:
        print('Inny bład')
        lista_bledow.append(error)
else:
    print("Inny system")
print(lista_bledow)

odp = input("Podaj datę Chrztu Polski").lower().replace(" ", '')
if odp == '966':
    print("Odpowiedź prawidłowa")
else:
    print("Masz to w książce na stronie 23")
