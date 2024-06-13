# klasa - szablon, przepis, stempel
# obiekt - odcisk stempla
# obiekt - instancja klasy

# definicja klasy
class Human:
    """
    Klasa human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print("Nazywam się", self.imie)


cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001919E7E1BE0>
print(cz1.__doc__)  # Klasa human opisująca człowieka w pythonie
print(cz1.imie)
cz1.imie = 'Ania'
cz1.wiek = 27
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Ania
# 27
# k
cz2 = Human()
cz2.imie = 'Radek'
cz2.wiek = 34
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Radek
# 34
# m
cz1.powitanie()
cz2.powitanie()
# Nazywam się Ania
# Nazywam się Radek
