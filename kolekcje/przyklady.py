napis = "abcdefgjsol"

for litera in napis:
    print(litera)

for i in range(len(napis)):
    print(napis[i])

print(dir(napis))
print(napis.endswith('sol'))

print("a" in napis)

napis2 = "ala ma kota"
print(napis2.capitalize())
print(napis2.title())

print(help(napis2.istitle))

# Słownik

# pusty slownik

d = dict()
print(type(d))
d['a'] = 1
d['b'] = 2
print(d)
print(dir(d))
print(d.keys())
print(d.values())
print(d.items())

slownik = {
    'parameter1': 10,
    'parameter2': 20,
    'x': 3
}

print(slownik)

for k in slownik.items():
    print(k)

for k, v in slownik.items():
    print(k, v)

for k in slownik:
    print(k, slownik[k])

# ZBIORY
# puste slowniki, listy, tuple
# slown={} # trzeba pamietac, że w slowniku mamy klucz i wartosc, klucz musi byc unikatowy, np. slownik={1:a,2:b}
# lis=[]
# tupla=()
# zbior=set() #tak tworzymy pusty zbior, jesli nie pusty to można tez tak: zbior={1,2,3,1,"a"}

zbior = {1, 2, 3}
print(zbior)
zbior.add(4)
print(zbior)

a = set(['a', 1, 'c', 2, 3])
for el in a:
    print(el)

list=list(range(0,100, 25))
print(list)