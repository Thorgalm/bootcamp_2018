x = float(input("Podaj długość:"))
y = float(input("Podaj szerokość:"))
z = float(input("Podaj wysokość:"))
print("Objętość opakowania", x * y * z, "cm3")
print("Większe od 1 litra:", x * y * z > 1000)

if x * y * z > 2000:
    print("Objętość jest większa niż 2 litr")
elif x * y * z > 1000:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętość jest mniejsza niż 1 litr")

print("To już jest koniec programu")

# wcięcie decyduje czy to ma byc wykonywane w ramach else czy to bezwgledu na warunek czyli zawsze
