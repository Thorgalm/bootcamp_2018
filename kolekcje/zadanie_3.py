lista = [10, 6, 5, 4, 46, 46, 4, -5, 4, -8, -4, 0]

licznik_dodatnich = 0
licznik_ujemnych = 0

for liczba in lista:
    if liczba > 0:
        licznik_dodatnich += 1
    elif liczba < 0:
        licznik_ujemnych += 1

print(f"Liczba dodatnich: {licznik_dodatnich} liczba ujemnych: {licznik_ujemnych}")

# 2 rozwiazanie
dodatnie = [x for x in lista if x > 0]
ujemne = [x for x in lista if x < 0]

licznik_dodatnich = len([x for x in lista if x > 0])
licznik_ujemnych = len([x for x in lista if x < 0])

print(f"Liczba dodatnich: {licznik_dodatnich} liczba ujemnych: {licznik_ujemnych}")
