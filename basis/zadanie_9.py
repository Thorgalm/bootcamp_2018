import datetime
y = datetime.datetime.now().year

x = int(input("Podaj rok urodzenia:"))

# if 2018 - x > 18:
#    print("Jesteś pełnoletni!")

if y - x > 18:
    print("Jesteś pełnoletni!")
