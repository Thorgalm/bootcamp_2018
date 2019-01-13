lista = list(i/10 for i in range(11))
print(lista)

print(list(range(-10, 11)))
print({(x, x**2, x**3) for x in range(-10, 11)})


napisy = {"Ala ma kota", "kot ma alę", "Zażółć gęśla jaźń"}
print({x: len(x) for x in napisy})