cena = 10.0
waga = 2.5
naleznosc = cena*waga
print("Cena za kg:", cena)
print("Waga:", waga)
print("Należność: ", naleznosc)

#fstring - nowa fukcja od python 3.6 mozna tworzyc dlugie napisy, w ktore mozna wstawic zmienne, aby wyświetlic jednym printem
# w nawiasie wąsatym wstawiamy kod pythona, wiec moze byc cos wiecej niz tylko zmienna
info = f"""
Cena za kg: {cena}
Waga: {waga}
Należność:  {naleznosc}
"""

print(info)