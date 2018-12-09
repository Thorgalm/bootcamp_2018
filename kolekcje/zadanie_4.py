b = [x for x in range(0, 101) if x % 3 == 0 or x % 5 == 0]
licznik = len(b)
print(f"liczby podzielne przez 3 lub 5: {b}")
print("\n".join(map(str, b))) #wypisz jako liczby pionowo, a nie lista
print(f"W przedziale 0-100 jest {licznik} liczb podzielnych przez 3lub 5")



# rozwianzanie prowadzacego
licznik = 0
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        licznik += 1
