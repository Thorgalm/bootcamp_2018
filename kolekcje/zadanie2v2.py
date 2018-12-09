dane = input("podaj liczby, rozdziel je spacjami:")
dane = dane.split() # podzieli liczby, ale to bedzie tekst
print(dane)

# zamiana tekstu na liczby na 3 sposoby
dane2 = []
for d in dane:
    dane2.append(int(d))

print(dane2)
dane = [int(d) for d in dane]
print(dane)
# lista = []
# dane = map(int, dane)
# print(lista(dane)) # jakis blad



