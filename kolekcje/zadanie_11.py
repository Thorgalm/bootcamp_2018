liczby = set()
parzyste = set(range(2, 100, 2))

while True:
    komenda = input("Podaj liczbę lub [k] by zakonczyc")
    if komenda == 'k':
        break
    else:
        liczby.add(int(komenda))

#print(liczby)
print("liczb unikalnych jest: ", len(liczby))
print("Z tego liczb parzystych: ", len(liczby & parzyste))


# moje rozwiazanie:
# liczby=input("Podaj liczby")
#
# podane_liczby = {1,1,1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 1}
#
# slownik_liczb = {}
# for li in podane_liczby:
#     slownik_liczb[li] = slownik_liczb.get(li, 0) + 1
#
# print("Statystyka:")
# for z, c in slownik_liczb.items():
#     print(f" - {z} wystąpił: {c}")
#
# list = list(range(2, 100, 2))
# # print(list)
#
# k = 0
# for i in slownik_liczb:
#     for j in list:
#         if i == j:
#             k += 1
# print(f"W zbiorze jest {k} liczb parzystych")
