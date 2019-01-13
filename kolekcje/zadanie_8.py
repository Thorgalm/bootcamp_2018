text = input("Podaj teskt:")

text1 = "Ala ma kota"
text2 = "Ala <ma> kota"
text3 = "Ala <> kota"

dlugosc = 0
licz = False

for znak in text:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz = False
        break #opcjonalnie
    elif licz:
        dlugosc +=1

#assert dlugosc == 0
#wywala error jak blad,do testow
print(dlugosc)
print(f"liczba znakow pomiedzy nawiasami wynosi: {dlugosc}")
#moje
#ile_znakow = 0
#for znak in text:
 #   if znak == "<":
  #      ile_znakow += 1
   #     if znak == ">":
    #        break

#print(ile_znakow)
