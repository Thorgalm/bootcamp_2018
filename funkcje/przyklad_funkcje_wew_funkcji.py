def a():
    print("Jestem w funkcji a")

    def b():
        print("Jestem w funkcji b")

    def c():
        print("Jestem w funkcji c")
    # print(globals())
    # print(locals())
    b()
    c()

print(a())
print("Na zewnatrz",globals())



#DEKORATORY przyklady

def pobierz_dane():
    print("Pobrałem dane")

def loguj_uzycie(func):
    """
    To bedzie dekorator. Wypisze tekst przed i po uruchomieniu funkcji
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print("To się wykona przed")
        func(*args, **kwargs)
        print("To sie wykona po")
    return wrapper

print("Bez dekoratora")
pobierz_dane()

print("Udekorowane")
pobierz_dane = loguj_uzycie(pobierz_dane)
pobierz_dane()