import random
from random import randint


class Przedmiot:
    def __init__(self, nazwa, bonus):
        """

        :param nazwa: string
        :param bonus_do_ataku: int
        """
        self.nazwa = nazwa
        if isinstance(bonus, int):
            self.bonus_do_ataku = bonus
        else:
            raise ValueError("Bonus powinien być liczbą")

    def __str__(self):
        return f"{self.nazwa}, {self.bonus_do_ataku} do ataku\n"


class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.max_zdrowie = zdrowie
        self.zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        bonusy = 0
        for przedmiot in self.ekwipunek:
            bonusy += przedmiot.bonus_do_ataku
        return self._atak + bonusy
        # return self._atak += sum([e.bonus_do ataku for e in ekwipunek])

    def otrzymaj_obrazenia(self, obrazenia):
        print(f"{self.imie} oberwał za {obrazenia} obrażeń.")
        self.zdrowie -= obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, pkt_zdrowie):
        if self.zdrowie == 0:
            return False
        self.zdrowie += pkt_zdrowie
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def dodaj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)
        # self._atak += przedmiot.bonus_do_ataku

    def zabierz_przedmiot(self, przedmiot):
        self.ekwipunek.remove(przedmiot)

    def moc_ataku(self):
        return random.randint(self.atak // 2, self.atak)
        # losuje z przedziału połowa ataku do cały atak, //przy dzieleniu od razu zaokrągla do całkowitych

    def __str__(self):
        napis = f"""
Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.
EKWPIUNEK:
"""
        for przedmiot in self.ekwipunek:
            napis += str(przedmiot)
        return napis


def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20


def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymaj_obrazenia(200)
    assert postac.zdrowie == 0


def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170


def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0


def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200


def test_przedmiot():
    przedmiot = Przedmiot("Kula mocy", 10)
    assert przedmiot.nazwa == "Kula mocy"
    assert przedmiot.bonus_do_ataku == 10


def test_postac_dodaj_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 10)

    # assert len(postac.ekwipunek) == 0
    assert przedmiot not in postac.ekwipunek
    postac.dodaj_przedmiot(przedmiot)
    # assert len(postac.ekwipunek) == 1
    assert przedmiot in postac.ekwipunek


def test_postac_powiekszony_atak():
    postac = Postac("Rafał", 5, 200)
    przedmiot1 = Przedmiot("Rękawice grzmoty", 10)
    przedmiot2 = Przedmiot("Młot zagłady", 40)
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot1)
    postac.dodaj_przedmiot(przedmiot2)
    assert postac.atak == 55


def test_postac_zabierz_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 10)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 15
    postac.zabierz_przedmiot(przedmiot)
    assert postac.atak == 5
    assert przedmiot not in postac.ekwipunek


def test_postac_moc_ataku():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 10)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 15
    moc_ataku = postac.moc_ataku()
    assert (postac.atak // 2) <= moc_ataku <= postac.atak


# postac = Postac("Rafał", 5, 200)
# przedmiot1 = Przedmiot("Rękawice grzmoty", 10)
# przedmiot2 = Przedmiot("Młot zagłady", 40)
# postac.dodaj_przedmiot(przedmiot1)
# postac.dodaj_przedmiot(przedmiot2)
# print(postac.atak)
# print(postac.moc_ataku())
# print(postac.__str__())
# print(postac)


def walka(atakujacy, broniacy):
    print(f" Walka {atakujacy.imie} vs {broniacy.imie}")
    print(atakujacy)
    print(broniacy)
    print("-" * 40)

    while atakujacy.zdrowie > 0 and broniacy.zdrowie > 0:
        moc_ataku_atakujacego = atakujacy.moc_ataku()
        print(f" {atakujacy.imie} uderza {broniacy.imie} z mocą {moc_ataku_atakujacego}")
        broniacy.otrzymaj_obrazenia(moc_ataku_atakujacego)

        print("-" * 20)

        if broniacy.zdrowie > 0:
            moc_ataku_broniacego = broniacy.moc_ataku()
            print(f" {broniacy.imie} uderza {atakujacy.imie} z mocą {moc_ataku_broniacego}")
            atakujacy.otrzymaj_obrazenia(moc_ataku_broniacego)

    print("KONIEC WALKI")
    print(atakujacy)
    print(broniacy)


class Polozenie():
    def __init__(self, x, y, zasieg_x, zasieg_y):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    # porownuje wspolrzedne w tle
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def w(self):
        self.y += 1
        if self.y > self.zasieg_y:
            print("wyszedles poza plansze")
            exit()

    def s(self):
        self.y -= 1
        if self.y > self.zasieg_y:
            print("wyszedles poza plansze")
            exit()

    def a(self):
        self.x -= 1
        if self.x > self.zasieg_x:
            print("wyszedles poza plansze")
            exit()

    def d(self):
        self.x += 1
        if self.x > self.zasieg_x:
            print("wyszedles poza plansze")
            exit()

    def __str__(self):
        return f"Położenie: {self.x}, {self.y}"

    # kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
    # if kierunek == "w":
    #     gracz_y1 += 1
    # elif kierunek == "s":
    #     gracz_y1 -= 1
    # elif kierunek == 'a':
    #     gracz_x1 -= 1
    # elif kierunek == 'd':
    #     gracz_x1 += 1


polozenia_gracza = Polozenie(1, 1, 10, 10)

while True:
    print(polozenia_gracza)
    kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
    # if w to wywolaj w, ale bez pisania za kazdym razem kierunku: polozenie_gracza.kierunek()
    getattr(polozenia_gracza, kierunek)()

class Plansza:
    def __init__(self, gracz, wrog, skarb, x=10,y=10):
        self.gracz = gracz
        self.wrog = wrog
        self.skarb = skarb
        self.x = x
        self.y =y

        self. polozenie_gracza = Polozenie(randint(1,self.x), randint(1, self.y), self.x, self.y)
        self. polozenie_wroga = Polozenie(randint(1,self.x), randint(1, self.y), self.x, self.y)
        self. polozenie_skarbu = Polozenie(randint(1,self.x), randint(1, self.y), self.x, self.y)

    def ruch(self):
        print("Gracz:", self.polozenie_gracza)
        print("Wrog:", self.polozenie_wroga)
        print("Skarb:", self.polozenie_skarbu)

        kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
        getattr(polozenia_gracza, kierunek)()

        if self.polozenie_gracza == self.polozenie_skarbu:
            print("Otrzymales:", self.skarb)
            self.gracz.dodaj_przedmiot(self.skarb)
            self.polozenie_skarbu = Polozenie(-100, -100, self.x, self.y)

        if self.polozenie_gracza == self.polozenie_wroga:
            Postac.walka(self.gracz, self.wrog)
            if self.gracz.zdrowie < 1:
                print("Zginąłeś ...")
                exit()

    def gra(self):
        while True:
            self.ruch()

plansza = Plansza(Rufus, Janusz, tulipan)
plansza.gra()


rufus = Postac("Rufus", 30, 100)
janusz = Postac("Janusz", 40, 120)
tulipan = Przedmiot("Zielony tuplian zniszczenia", 5)
rufus.dodaj_przedmiot(tulipan)
walka(rufus, janusz)
