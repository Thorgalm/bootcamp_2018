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


# podanie wielu argumentow do funkcji

# def zsumuj(lista):
#     return sum(lista)
#
# print(zsumuj([10,20]))

def zsumuj(*args):
    print(args)
    print(type(args))
    return sum(args)


# print(zsumuj('a', 'b', 10, 20, 30, 40))

# przekazanie funkcji (operacja) i dowolna liczbe argumentow (*args)
def wykonaj_operacje(operacja, *args):
    print(args)
    print(type(args))
    return operacja(args)


print(wykonaj_operacje(min, 10, 20, 30, 40))
print(wykonaj_operacje(sum, 10, 20, 30, 40))

"""
Napisz funkcję, która przyjmie dowolna liczbe napisow,
1.zwroci te napisy połączone znakiem nowej linii
    >>> napisy("a", "b")
    a
    b
    >>> napisy("a", "b", "c")
    a
    b
    c
"""


#
# def napisy(*args):
#     """
#     to jest doc test - czyli dokumentacja do fukcji
#     Napisz funkcję, która przyjmie dowolna liczbe napisow,
#     1.zwroci te napisy połączone znakiem nowej linii
#     >>> napisy("a", "b")
#     a
#     b
#     >>> napisy("a", "b", "c")
#     a
#     b
#     c
#     """
#     return args #tu mi brakuje
#
#  # tu mi brakuje
#
#  #kwargs - key word arguments
# def napisy(*args, **kwargs):
#     """
#     to jest doc test - czyli dokumentacja do fukcji
#     Napisz funkcję, która przyjmie dowolna liczbe napisow,
#     1.zwroci te napisy połączone znakiem nowej linii
#     >>> napisy("a", "b")
#     a
#     b
#     >>> napisy("a", "b", "c")
#     a
#     b
#     c
#     """
#     tekst = "\n".join(args)
#     print(kwargs)
#     for k, f in kwargs:
#         tekst = f(tekst)
#
#     return tekst
#
# def upper(napis):
#     return napis.upper()
#
# print("-"*40)
# print(napisy("a", "b", "c", "d", funkcja=upper, funkcja2=str.title))


def hi():
    return "Hi!"


def goodmorning():
    return "good morning"


def przywitaj_sie(greeting_function):
    print(greeting_function())


przywitaj_sie(hi)


def sprawdz_czy(x, funkcja1, funkcja2):
    return funkcja1(x) and funkcja2(x)


print(sprawdz_czy(2, lambda x: x < 3, lambda x: x > 0))


def sprawdz_czy_podzielna_przez_2_i_3(x):
    return x % 2 == 0 and x % 3 == 0


print(sprawdz_czy(12, sprawdz_czy_podzielna_przez_2_i_3, lambda x: x > 5))
