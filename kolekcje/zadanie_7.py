#text = input("podaj tekst:")

text = "Ala ma kota aeiouy"
ile_samoglosek = 0
SAMOGLOSKI = 'aeiouy'

for litera in text:
    if litera in SAMOGLOSKI:
        ile_samoglosek = ile_samoglosek+1

#rozwiązanie
ile_samoglosek2=0
for samogloska in SAMOGLOSKI:
    ile_samoglosek2 +=text.lower().count(samogloska)

print(ile_samoglosek)
print(ile_samoglosek2)