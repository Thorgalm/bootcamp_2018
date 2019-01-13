import pytest


# def dodaj(liczba):
#     """Bedzie dodawac do siebie wszystkie liczby od 1 do liczba"""
#     if liczba == 0:
#         return 0
#     else:
#         return liczba + dodaj(liczba - 1)
#
# print(dodaj(5))

# moje
def silnia(liczba):
    if liczba < 0:
        raise ValueError("argument musi byc wiekszy >= 0")
    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba - 1)



print(silnia(5))


def test_silnia():
    assert silnia(5) == 120
    assert silnia(0) == 1

def test_silnia_mniejsza_od_0():
    with pytest.raises(ValueError) as e:
        assert silnia(-10)