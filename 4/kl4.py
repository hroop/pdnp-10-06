# dziedziczenie
# przejęcie cech innej klasy
# nadpisanie, modyfikowac, rozszerzenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor:", self.kolor)


class Samochod(Pojazd):
    """
    Klasa samochód
    """

    def __init__(self, kolor, marka=None):
        super().__init__(kolor)  # musimy wywołac konstruktor klasy wyzszej
        self.marka = marka

    def info(self):
        super().info()  # możemy wywołac metode klasy wyższej
        print(f'Marka {self.marka}')


poj = Pojazd("Czerwony")
poj.info()
# Kolor: Czerwony

sam = Samochod("Zielony")
sam.info()
# Kolor: Czerwony
# Kolor: Zielony
# Marka None
sam2 = Samochod("Biały", 'Lambo')

# polimorfizm - mozliwosć wykorzystania obiektów różnych klas za pomocą cech wspólnych
lista = [poj, sam, sam2]
for i in lista:
    print(i, i.info())

# <__main__.Pojazd object at 0x0000022A5DFD6300> None
# Kolor: Zielony
# Marka None
# <__main__.Samochod object at 0x0000022A5DFD63C0> None
# Kolor: Biały
# Marka Lambo
# <__main__.Samochod object at 0x0000022A5DFD6450> None
