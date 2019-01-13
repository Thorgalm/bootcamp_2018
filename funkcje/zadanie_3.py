def policz_znaki(napis, start="<", stop=">"):
    wynik = 0
    poziom = 0

    for znak in napis:
        if znak == start:
            poziom += 1
        elif znak == stop:
            poziom -= 1
        elif poziom:
            wynik += poziom
    return wynik

# moje rozwiazanie dla zagniezdzen:

# def policz_znaki(napis, start="<", stop=">"):
#     wynik=0
#     czy_zliczac = False
#     gniazdo=0
#
#     for znak in napis:
#         if znak == start:
#             czy_zliczac = True
#             gniazdo += 1
#         elif znak == stop:
#             czy_zliczac = False
#             gniazdo -= 1
#         elif czy_zliczac:
#             wynik += 1*gniazdo
#     return wynik

# testy
# podejscie: test drive development

def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("") == 0


def test_policz_znaki_w_niepustym_napisie_bez_nawiasow():
    assert policz_znaki("ala ma kota") == 0


def test_policz_znaki_1poziom():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4


def test_policz_znaki_1poziom_kilka_nawiasow():
    assert policz_znaki('ala ma <kota> a kot <ma> ale') == 6


def test_policz_znaki_1poziom_inne_nawiasow():
    assert policz_znaki('ala ma [kota] a kot [ma] ale', '[', ']') == 6


def test_policz_znaki_2poziomy_zagnieżdzenia():
    assert policz_znaki('ala ma <<kota>> a kot <ma> ale') == 10


def test_policz_znaki():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('a <a<a<a>>>') == 6

# MOJE:

# def policz_znaki(text):
#     ilosc = 0
#     licz = False
#     for znak in text:
#         if znak in ("<", "["):
#             licz = True
#         elif znak in (">", "]"):
#             licz = False
#             break  # opcjonalnie
#         elif licz:
#             ilosc += 1
#     return ilosc


# print(policz_znaki("<jak> [to dziala] ok a <masz> to lub [to]"))

# moj pomysl zrobic zbior indeksow
# text = "<jak> [to dziala] ok a <masz> to lub [to]"
# for i in range(len(text)):
#     indeks_minimum = i
#     if ("<", "[") in text:
#
