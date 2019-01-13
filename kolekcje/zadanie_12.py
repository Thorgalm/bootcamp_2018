liczby = [9, 2, 6, 8, 4, 3, 1, 0]

for i in range(len(liczby)):
    indeks_minimum = i
    for j in range(i, len(liczby)):
        if liczby[j] < liczby[indeks_minimum]:
            indeks_minimum = j
    liczby[i], liczby[indeks_minimum] = liczby[indeks_minimum], liczby[i]

print(liczby)

#druga proba, ale nie dziala
# print("Szukam minimum:")
# indeks_minimum = 0
#
# for k in range(indeks_minimum, len(liczby)):
#     for i in range(k, len(liczby)):
#         if liczby[i] < liczby[indeks_minimum]:
#             print("Znalazłem minimum")
#             print("Nowa wartość minimum to: ", liczby[i])
#             print("Nowy indeks minimum to: ", i)
#             indeks_minimum = 1
#     liczby[k], liczby[indeks_minimum] = liczby[indeks_minimum], liczby[k]
#
# print(liczby)





# moje
# liczby = [9, 1, 6, 8, 4, 3, 2, 0]
#
# print(len(liczby))
# print(liczby[len(liczby)-1])
#
# print(range(len(liczby)/2))
#
# indeks = 0
# for indeks in range(len(liczby)/2):
#     if liczby[indeks] > liczby[len(liczby) - indeks-1]:
#         liczby[indeks], liczby[len(liczby) - indeks-1] = liczby[len(liczby) - indeks-1], liczby[indeks]
#
# print(liczby)

# assert liczby == [0, 1, 6, 8, 4, 3, 2, 9]

# assert liczby == [0, 1, 2, 3, 4, 6, 8, 9]
