# FUNKCJE:

liczby = [1, 2, 3, 4]
liczby2 = [5, 6, 7, 8]

for i, l in enumerate(liczby):
    print(f'Indeks={i}, wartość={l}')

for i, l in enumerate(liczby2):
    print(f'Indeks={i}, wartość={l}')

print()


def drukuj(lista):
    for i, l in enumerate(lista):
        print(f'Indeks={i}, wartość={l}')


drukuj(liczby)
drukuj(liczby2)


# jeśli kawalek kodu jest uzywany w kilku miejscach to warto zapisac go jako funkcję, wtedy zmiemiany kod w 1 miejscu, a nie w kazdym miejscu
# zasada: DRY Don't repeat yourself
# zen in python


# najprostsza funkcja
def ha():
    print("ha")


ha()

# funkcja nie zwraca żadnych wartości, jeśli ma zwracać to trzeba dodać return
a = 2
b = 3


def dodaj_a_b():
    wynik = a + b
    return wynik


dodaj_a_b()
print(dodaj_a_b())

# podejrzenie dostępnych zmiennych
print(globals())
print(locals())


def potega(podstawa, wykladnik=2):
    return podstawa ** wykladnik
# jak dopiszemy =2 to domyslnie bedzie robil kwadrat, wtedy nie musimy podawac drugiego argumentu

print(potega(4, 2))
print(potega(4))
print(potega(4, 3))
