liczby = [5, 2, 1, 4, 3]
print(liczby)
indeks_min, indeks_max = None, None

for indeks in range(len(liczby)):
    if indeks_min is None or liczby[indeks] < liczby[indeks_min]:
        indeks_min = indeks
    if indeks_max is None or liczby[indeks] > liczby[indeks_max]:
        indeks_max = indeks

liczby[indeks_max], liczby[indeks_min] = liczby[indeks_min], liczby[indeks_max]
print(liczby)
assert liczby == [1, 2, 5, 4, 3] # assert sprawcza czy to co po nim następuje czy jest prawdą czy falszem, jesli prawda to nic sie nie dzieje jesli bład to assertion error

# zamiana miejscami liczb w liscie, gdy znamy indexy
# 1 sposob
# temp=liczby[0]
# liczby[0]=liczby[2]
# liczby[2]=temp
# print(liczby)
#
# # 2 sposob
# liczby[0], liczby[2] = liczby[2], liczby[0] # najpierw czyta to po prawej stronie i przypisuje w miejsca te po lewej

# moje:

# indeks_min= liczby[0]
# for indeks in range(len(liczby)):
#     if liczby[indeks] < indeks_min: #tu zle bo trzeba porownywac liczby, a nie liczby z indeksami
#         indeks_min = liczby[indeks] # tu blad bo znowu indeksy pomieszane z liczbami,
#         print(indeks)
#
