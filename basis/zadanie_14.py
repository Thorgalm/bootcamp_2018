min = None
max = None
liczba = None
while True:
    komenda = input(f"Podaj liczbę lub k by zakończyć:")
    if komenda == 'k':
        break
    if len(komenda) > 0 and komenda[0] == '-' and komenda[1:].isdigit():
        liczba = int(komenda[1:])
        liczba = -liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("Nie podałeś liczby")

    if liczba or liczba == 0:
        if max is None or liczba > max:
            max = liczba
        if min is None or liczba < min:
            min = liczba

print("Znalezione minimum to:", min)
print("Znalezione maksimum to:", max)


#     if i == 1:
#         min = liczba_i
#         max = liczba_i
#     if liczba_i < min:
#         min = liczba_i
#     if liczba_i > max:
#         max = liczba_i
# print(min)
# print(max)

