# zmienne zaczynają sie od $


def formatuj(*napisy, **zmienne):
    napis = "\n".join(napisy)
    for zmienna in zmienne:
        napis = napis.replace(f'${zmienna}', zmienne[zmienna])
    return napis


# print(formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10))

# 'koszt 10 PLN\nkwota 10 brutto'

def test_formatuj_napis_bez_znacznikow():
    assert formatuj("hello world!") == "hello world!"

def test_formatuj_wiele_napis_bez_znacznikow():
    assert formatuj("hello world!", "Hi Python!") == "hello world!\nHi Python!"

def test_formatuj_napis_bez_znacznikow_ale_ze_zmienna_jako_argument():
    assert formatuj("hello world!", name="John") == "hello world!"

def test_formatuj_napis_bez_znacznikow_ale_ze_zmiennymi_jako_argument():
    assert formatuj("hello world!", name="John", lastname="Kovalsky") == "hello world!"

def test_formatuj_napis_ze_zmienna():
    assert formatuj("hello $name", name="John") == "hello John"
    assert formatuj("hello $name $lastname", name="John", lastname="Kovalsky") == "hello John Kovalsky"