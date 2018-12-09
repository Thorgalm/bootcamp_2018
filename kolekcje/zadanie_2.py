lista = []
i = 0
while i < 10:
    a = input("Podaj liczbę lub k jeśli koniec:")
    if a == 'k':
        break
    a = int(a)
    lista.append(a)
    i += 1

print(lista)
print("Średnia wynosi:", sum(lista) / len(lista))
