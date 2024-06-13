class Human:
    """
    Klasa Human definiująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    def wypisz_wiek(self):
        print("Mam", self.wiek, 'lat')

    def wypisz_wzrost(self):
        print("Mam", self.wzrost, "cm wzrostu")

    def wypisz_plec(self):
        print("Jestem", self.plec)

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print('Ruszyałam w drogę')


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human('Ania', 27, 165)
print(cz1.plec)
print(cz1.wiek)
print(cz1.wzrost)
cz1.powitanie()
# k
# 27
# 165
# Nazywam się Ania
cz1.wypisz_wzrost()
cz1.wypisz_plec()
cz1.wypisz_wiek()
# Nazywam się Ania
# Mam 165 cm wzrostu
# Jestem k
# Mam 27 lat
cz2 = Human("Radek", 45, 190, "m")
cz2.wypisz_wzrost()  # Mam 190 cm wzrostu

lista = [cz1, cz2]
for i in lista:
    i.powitanie()
    i.ruszaj()

# Ruszyałam w drogę
# Ruszyłem w drogę
# Nazywam się Ania
# Ruszyałam w drogę
# Nazywam się Radek
# Ruszyłem w drogę
