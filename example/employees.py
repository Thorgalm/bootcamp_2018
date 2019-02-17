import json
import getpass

#jeśli nie ma pliku to tworzymy pustą listę, potem zapisujemy do jsona listę slowników [{},{},{}]
try:
    with open("employees.json") as fp:
        pracownicy = json.load(fp)
except FileNotFoundError:
    pracownicy = []

def dodaj_pracownika(pracownicy):
    imie = input("Imię:")
    nazwisko = input("Nazwisko:")
    rok_urodzenia = input("Rok urodzenia:")
    pensja = input("Pensja:")

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_urodzenia": rok_urodzenia,
        "pensja": pensja
    }
    pracownicy.append(pracownik)

    with open("employees.json", "w") as fp:
        json.dump(pracownicy, fp)

def wypisz_pracownika(pracownicy):
    print("Pracownicy:")
    for nr, pracownik in enumerate(pracownicy, start=1):
        print(
            f" - {nr}, {pracownik['imie']}, {pracownik['nazwisko']}, - rok: {pracownik['rok_urodzenia']}, "
            f"pensja: {pracownik['pensja']} PLN")

    # with open("employees.json") as fp:
    #     pp = json.load(fp)
    # print(pp)
    # print(f"""Pracownicy:
    # {imie} {nazwisko} - rok: {rok_urodzenia}, pensja {pensja} PLN""")

def usun_pracownika(pracownicy, nr):
    nr = input("którego pracownika usunąć?")
    haslo = getpass.getpass("Podaj hasło")
    if haslo != "TAJNE":
        print("zle hasło")
        return
    del pracownicy[int(nr)-1]

    with open("employees.json", "w") as fp:
        json.dump(pracownicy,fp)

wybor = input("Co chcesz zrobic? [d - dodaj, w - wypisz, u - usun]")

if wybor == 'd':
    dodaj_pracownika(pracownicy)
elif wybor == 'w':
    wypisz_pracownika(pracownicy)
elif wybor == 'u':
    wypisz_pracownika(pracownicy)
    usun_pracownika(pracownicy, nr)



# class Employee:
#     def __init__(self, name, last_name, birth_year, salary ):
#         self.name = name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         self.salary = salary
#
# baza={}
