def wiecej_niz(napis,prog):
    wynik=set()
    unikalne = set(napis)
    for c in unikalne:
        if napis.count(c)> prog:
            wynik.add(c)

    return wynik

#framework do testów
# w terminalu wpisac: pip install pytest
# wyszuka wszystkie funkcje zaczynajace sie od "test"
# trzeba w ustawieniach wpisac "unittest" w polach test wybrac pytest
# teraz w prawym gornym okienku wybrac: edit configuration, potem plus, w rozwijanym okienku pytest -> pytest, wybrac ktory kod ma sprawdzac, zmienic nazwe
#
def test_wiecej_niz():
    assert wiecej_niz('ala ma kota a kot ma ale',3) == {'a', ' '}
    assert wiecej_niz('aaaa bbbb ccc', 3) == {'a', 'b'}


# 2 wersja funkcji z wykorzystaniem listy
def wiecej_niz(napis,prog):
    return {x for x in set(napis) if napis.count(x) > prog}

def test_wiecej_niz():
    assert wiecej_niz('ala ma kota a kot ma ale',3) == {'a', ' '}
    assert wiecej_niz('aaaa bbbb ccc', 3) == {'a', 'b'}


#moje
# def wiecej_niz(text,x):
#     znaki = {}
#     for znak in text:
#         znaki[znak] = znaki.get(znak, 0) + 1
#         # if znak in znaki:
#         #     znaki[znak] =+ 1
#         # else:
#         #     znaki = 1
#     for z, c in znaki.items():
#         if c > x:
#             return z
#
# print(wiecej_niz('ala ma kota a kot ma ale',3))


