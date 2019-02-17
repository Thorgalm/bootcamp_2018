## III zjazd - sobota 2019-01-26
# zadanie 1

def max_z_dwoch(a, b):
    if a > b:
        return a
    return b


def max_z_trzech(x, y, z):
    return max_z_dwoch(x, max_z_dwoch(y, z))


assert 0 == max_z_trzech(0, 0, 0)
assert 3 == max_z_trzech(1, 2, 3)
assert 12 == max_z_trzech(12, 0, -3)


##zadanie 2
def sumator(arg):
    total = 0
    if isinstance(arg, dict):
        arg = arg.values()
    for x in arg:
        try:
            x = int(x)
            total += x
        except ValueError:
            pass
    return total


assert sumator([1, 2, 3]) == 6
assert sumator({10, 20, 30}) == 60
assert sumator([1, 2, 'a', 3]) == 6
assert sumator([1, 2, '4', 3]) == 10
assert sumator({'a': 10, 1: 20, 'c': 30, 'd': '40'}) == 100  # slownik


##zadanie 3
def czy_palindrom(napis):
    napis = "".join(napis.lower().split())
    lewy = 0
    prawy = len(napis) - 1
    while prawy >= lewy:
        if not napis[lewy] == napis[prawy]:
            return False
        lewy += 1
        prawy -= 1
    return True


assert czy_palindrom('Kobyła ma mały bok') == True
assert czy_palindrom('Zakopane na pokaz') == True
assert czy_palindrom('Ala ma kota') == False


# drugie rozwiazanie

# Zadanie 4
# bez formatowania
# def trojkat_pascala(n):
#     a = [[1]] #lista
#     i = 1
#     for i in range(1, n):
#         a.append([1])
#         for j in range(1, i):
#             a[i].append(a[i-1][j-1]+a[i-1][j])
#         a[i].append(1)
#     return a

# assert [[1]] == trojkat_pascala(1)
# assert [[1], [1, 2]] == trojkat_pascala(2)
# assert [[1], [1, 2], [1, 3, 3, 1]] == trojkat_pascala(3)


def trojkat_pascala2(n):
    a = [[1]]  # lista
    i = 1
    for i in range(1, n):
        a.append([1])
        for j in range(1, i):
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])
        a[i].append(1)

    for i, row in enumerate(a):
        print("   " * (n - i), end="")
        for col in row:
            print(f'{col:5}', end=" ")
        print()


# print(trojkat_pascala2(10))

def trojkat_pascala(n):
    a = [[1]]  # lista
    i = 1
    for i in range(1, n):
        a.append([1])
        for j in range(1, i):
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])
        a[i].append(1)
    return a


def print_pascal(a):
    n = len(a)
    for i, row in enumerate(a):
        print("   " * (n - i), end="")
        for col in row:
            print(f'{col:5}', end=" ")
        print()


# a= trojkat_pascala(10)
# print_pascal(a)

# zadanie 5
import string


# print(string.ascii_lowercase)

def czy_pangram(napis, alfabet=string.ascii_lowercase):
    napis = "".join(
        napis.lower().split())  # dzieli po spacjach, pomniejsza i łączy, dzieki temu mamy bez spacji z malych liter
    # print("A",len(set(napis)), len(alfabet))
    return set(napis) == set(alfabet)


assert czy_pangram('The quick brown fox jumps over the lazy dog') == True
assert czy_pangram('ala ma kota') == False
alfabet = 'abcdefghijklmnoprstuwyząęćśłńóżź'
assert czy_pangram('Pchnąć w tę łódź jeża lub ośm skrzyń fig', alfabet) == True


# Zadanie 6
def liczba_doskonala(liczba):
    i = 1
    suma = 0
    for i in range(1, liczba):
        if liczba % i == 0:
            suma += i
    return suma == liczba


assert liczba_doskonala(6) == True
assert liczba_doskonala(7) == False
assert liczba_doskonala(28) == True
assert liczba_doskonala(496) == True
# pomysły na optymalizacje:
# 1. sprawdzenie dzielenia tylko do n/2
# 2. jeśli cos nie jest podzielne przez 2 to nie bedzie tez przez zadna liczbe parzystą tzn. odrzucic nieparzyste

# zadanie 7
import time

def czas_wykonania(dekorowana_funkcja):

    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = dekorowana_funkcja(*args, **kwargs)
        stop = time.time()
        print(f"Czas wykonania funkcji:{dekorowana_funkcja.__name__} z argumentami {args}, {kwargs} wynosi {stop-start} s")
        return wynik
    return wrapper


liczba_doskonala = czas_wykonania(liczba_doskonala)

print(liczba_doskonala(1000))
