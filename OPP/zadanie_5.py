class CashMashine():
    # is_available = False # zamiast metody jak ponizej, mozna stworzyc atrybut tutaj

    def __init__(self):
        self._money = []

    @property  # dekorator zmienia metode na atrybut
    def is_available(self):
        if self._money: #zadziała jesli nie puste, jesli nie puste to wtedy zwroc True
            return True
        return False

    def put_money(self, bills_list):
        self._money.extend(bills_list)  # zamiast extend mozna +=

    def withdrawn_money(self, amount):
        money_to_withdrawn = []
        for bill in sorted(self._money, reverse=True):
            if sum(money_to_withdrawn) + bill <= amount:
                money_to_withdrawn.append(bill)
        # sprawdzam, czy udało sie uzbierac
        if sum(money_to_withdrawn) != amount:
            return []
        #skoro uzbieralem ile trzeba to usuwam z
        for bill in money_to_withdrawn:
            self._money.remove(bill)

        return money_to_withdrawn


def test_cash_machine_is_not_available():
    cash_machine = CashMashine()

    assert not cash_machine.is_available == True  # wywołanie atrybutu
    # assert not cash_machine.is_available() == True #wywołanie metody


def test_cash_machine_put_money():
    cash_machine = CashMashine()
    cash_machine.put_money([200, 100, 100, 50])

    assert cash_machine.is_available


def test_cash_machine_withdrawn_money():
    cash_machine = CashMashine()
    cash_machine.put_money([200, 100, 100, 50])

    assert cash_machine.is_available
    assert cash_machine.withdrawn_money(150) == [100, 50]
    assert cash_machine.withdrawn_money(150) == []
