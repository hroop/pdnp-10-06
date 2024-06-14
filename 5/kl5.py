# pracownik - imie, nazwisko, pensja
# manager - imie, nazwisko, pensja, premia
# konstruktor
# przedstaw_sie()
# oblicz_pensje()

class Pracownik:
    lista = []

    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    """
    Klasa Manager
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5500)
pracownik.przedstaw_sie()
print(f"Pensja pracownika {pracownik.imie} {pracownik.nazwisko} wynosi: {pracownik.oblicz_pensje()}")
# Nazywam się Jan Kowalski
# Pensja pracownika Jan Kowalski wynosi: 5500

manago = Manager("Jan", "Kowalski", 5500, 10000)
manago.przedstaw_sie()
print(f"Pensja managera {manago.imie} {manago.nazwisko} wynosi: {manago.oblicz_pensje()}")
# Nazywam się Jan Kowalski
# Pensja managera Jan Kowalski wynosi: 15500
print(Pracownik.lista)
