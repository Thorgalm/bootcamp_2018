import random
import moduly.postaci
#from moduly import postaci

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





def test_nowa_postac():
    postac = postaci.Postac("Albert", 1, 20)
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
    assert (postac.atak//2) <= moc_ataku <= postac.atak

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
    print("-"*40)

    while atakujacy.zdrowie > 0 and broniacy.zdrowie > 0:
        moc_ataku_atakujacego = atakujacy.moc_ataku()
        print(f" {atakujacy.imie} uderza {broniacy.imie} z mocą {moc_ataku_atakujacego}")
        broniacy.otrzymaj_obrazenia(moc_ataku_atakujacego)

        print("-"*20)

        if broniacy.zdrowie>0:
            moc_ataku_broniacego = broniacy.moc_ataku()
            print(f" {broniacy.imie} uderza {atakujacy.imie} z mocą {moc_ataku_broniacego}")
            atakujacy.otrzymaj_obrazenia(moc_ataku_broniacego)

    print("KONIEC WALKI")
    print(atakujacy)
    print(broniacy)

rufus = Postac("Rufus", 30, 100)
janusz = Postac("Janusz", 40, 120)
tulipan = Przedmiot("Zielony tuplian zniszczenia", 5)
rufus.dodaj_przedmiot(tulipan)
walka(rufus, janusz)