a = int(input("Podaj pierwszą liczbę:"))
b = int(input("Podaj drugą liczbę:"))
operator = input("Podaj drugą liczbę:")

if operator == "+":
    print("Wynik:", a+b)
elif operator == "-":
    print("Wynik:", a-b)
elif operator == "*":
    print("Wynik:", a*b)
elif operator == "/" and b != 0:
    print("Wynik:", a/b)
else:
    print("Błąd")

