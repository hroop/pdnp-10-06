class Car:
    """
    Klasa opsująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        self.__predkosc = 0  # oznaczamy pole jako prywatne

    def gaz(self):
        self.__predkosc += 10

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkosć wynosi {self.__predkosc} km/h")

    def __zmien_bieg(self):
        print('zmieniam bieg')


car = Car("Tesla", 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# print(car.__predkosc)  # 50
car.licznik()  # Prędkosć wynosi 50 km/h
car.__predkosc = 0
car.licznik()
print(car.__predkosc)  # 0
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Prędkosć wynosi 0 km/h
# Prędkosć wynosi 50 km/h
# Prędkosć wynosi 50 km/h
# 0
# zmieniam bieg
# zmieniam bieg
# zmieniam bieg
# zmieniam bieg
# zmieniam bieg
# Prędkosć wynosi 0 km/h