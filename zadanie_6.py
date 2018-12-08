x = float(input("podaj liczbę:"))
print()
a = x > 10
b = x <= 15
c = x % 2 == 0

info = f"""
Większa od 10: {a}
Mniejsza równa 15: {b}
Podzielna przez 2: {c}
"""
info2 = f"""
Większa od 10: {x > 10}
Mniejsza równa 15: {x <= 15}
Podzielna przez 2: {x % 2 == 0}
"""
print(info)
print(info2)

