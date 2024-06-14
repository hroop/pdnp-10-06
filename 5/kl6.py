from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkoscia", self.szybkosc)

    @abstractmethod  # oznaczylismy metode jako abstrakcyjną
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("Kierr kier kir")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# Po oznaczeniu klasy jako abstrakcyjna nie możemy tworzyc obiektu klasy Ptak
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkoscia 45
# or1.wydaj_odglos()
#
# kur1 = Ptak("Kura domowa", 0)
# kur1.latam()
# kur1.wydaj_odglos()
# Tu Orzeł Lecę z szybkoscia 45
# Tu Kura domowa Lecę z szybkoscia 0
kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
kur2.wydaj_odglos()
kur2.dziobanie()

or2 = Orzel("Orzeł Bielik", 50)
or2.latam()
or2.wydaj_odglos()
or2.polowanie()
# Tu Orzeł Bielik Lecę z szybkoscia 50
# Kierr kier kir
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa1 = Sowa("Sowa", 25)
