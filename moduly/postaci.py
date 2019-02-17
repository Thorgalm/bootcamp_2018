import random

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
