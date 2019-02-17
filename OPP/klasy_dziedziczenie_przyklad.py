class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Cześć jestem {self.imie} {self.nazwisko}")

class Informatyk:
    def programuj(self):
        print("Programuje")

class Pracownik(Osoba,Informatyk):

    def __init__(self, imie, nazwisko, stanowisko):
        Osoba.__init__(self, imie, nazwisko)
        self.stanowisko = stanowisko

    def przedstaw_sie(self):
        super().przedstaw_sie()     # zamiast Osoba... moze byc super
        print(f"Pracuje jako: {self.stanowisko}")


osoba = Osoba("Adam", "Słodowy")
osoba.przedstaw_sie()

pracownik = Pracownik("Piotr", "Nowak", "trener")
pracownik.przedstaw_sie()
pracownik.programuj()
