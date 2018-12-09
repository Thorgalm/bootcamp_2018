# przykłady input, zawsze jako string (tekst)

# x = input("Podaj wartość x: ")
# y = input("Podaj wartość y: ")

# rzutowanie na liczby
# x=int(x)
# y=int(y)

# w jednej linii
# x = int(input("Podaj wartość x: "))
# y = int(input("Podaj wartość y: "))

# print("Suma: ", x+y)

# Przykłady wartości logiczne
# ==, <,>,>=,<=, != różne od
# % modulo - reszta z dzielenia

# Pętla while

# i = 0
# while True:
#     if i == 5:
#         continue
#     print(i)
#     i += 1  # to jest to samo co i = i +1
#     if i == 100:
#         break
#
# while i < 3:
#     # tu warunki, zrobi te warunki 3 razy bo i<3, jesli jest True to zrobi nieskonczeną ilośc razy
#     i = i +1

# Napisy
tekst = "Ala ma kota"
# 012345678910
# tekst ma indeksy i można je printowac fragmentami

print(tekst[:5])
print(tekst[5])
print(tekst[-1])
print(tekst[-6:])
i = 0
while i < len(tekst):
    print(tekst[i])
    i += 1

# petla for, po for jest tymczasowa zmienna

for litera in tekst:
    print(litera)

for litera in enumerate(tekst):
    print(i, litera)
for i, litera in enumerate(tekst):
    print(i, litera)

# tupla - nie można zmienic tych danych, nie jest mutowalna, napis tez nie jest mutowalny

krotka = (1, 2, 3)
print(type(krotka))
print(krotka)
print(krotka[0])

for el in krotka:
    print(el)

print(dir(krotka))  # dir lista metod obiektu
print(krotka.count(1))  # liczy jedynki

krotka2 = ("Napis 1", "Napis 2", "Napis 1", 1, 2, 3)
print(krotka2.index("Napis 1"))
print(krotka2.count("Napis 1"))

# pip install ipython
# w wierszu poleceń (terminalu) wpisujemy python to uruchamia sie python w terminalu, mozna tez: ipython, exit()

x = "aaa"
y = x
print(id(x))  # id zmiennej
print(id(y))
x = x + "a"
print(id(x))
print(id(y))

x = (1, 2, 3, 5, 6, 7, 8, 9)
print(x[5:7])

# LISTA
# Lista jest mutowalna, w przeciwieństwie do krotki

lista = [1, 3, 5, 7, 8, 1, 4, 5, 6]
print(type(lista))
print(lista[1:5])
print(dir(lista))

print(lista)
print(id(lista))
lista.append("AA")  # append dodaje 1 element
print(lista)
print(id(lista))
lista.extend(['a', 'b'])  # extand dodaje wiecej niz 1 elementów
print(lista)
lista.append(['a', 'b'])  # stworzy w liscie pod liste
print(lista)
print(lista[-1][-1])  # wybieramy b z 2 listy

print("Jak dziala pop")  # usuwa ostatnio dodany element do listy
print(lista.pop())
print(lista)

print("Sortowanie")
lista = [1, 2, 5, 3, 5, 7, 2, 7, 5]
print(lista)
print(lista.sort())  # sort zwraca None
print(lista)
posortowane = lista.sort() # to wyrzuci None
print("posortowane", posortowane)
posortowane = sorted(lista) #to wyrzuci posortowaną liste
print("posortowane", posortowane)
