# import random
# x = random.randint(1, 10)
# lepiej importowac tylko funkcje, której uzywnamy niz calą biblioteke, bo jest wydajniej, dlatego:

from random import randint

x = randint(1, 10)
y = randint(1, 10)
print(x)
print(y)

pozycja_x = 0
pozycja_y = 0
poprzednia_odleglosc = 110
i = 1
while True:

    a = int(input("Podaje ruch w poziomie:"))
    b = int(input("Podaje ruch w pionie:"))
    pozycja_x += a
    pozycja_y += b
    odleglosc = abs(x - pozycja_x) + abs(y - pozycja_y)
    # print(pozycja_x)
    # print(pozycja_y)
    # print(abs(x - pozycja_x) + abs(y - pozycja_y))
    if odleglosc == 0:
        print("Znalazłeś skarb. Liczba ruchów:", i)
        break
    elif odleglosc <= poprzednia_odleglosc:
        print("ciepło")
        poprzednia_odleglosc = odleglosc
    elif odleglosc > poprzednia_odleglosc:
        print("zimno")
        poprzednia_odleglosc = odleglosc
    else:
        i += 1


