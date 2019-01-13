#text=input("Podaj napis")
from collections import defaultdict
#znaki = defaultdict(int) # slownik gdzie domyślnie jest int czyli 0 wtedy zamiast: znaki[znak] = znaki.get(znak, 0) + 1 można: znaki[znak] += 1

text = "Ala ma kota"

znaki = {}
for znak in text:
    znaki[znak] = znaki.get(znak, 0) + 1
    # if znak in znaki:
    #     znaki[znak] =+ 1
    # else:
    #     znaki = 1

print("Statystyka:")
for z, c in znaki.items():
    print(f" - {z} wystąpił: {c}")

#moj kod
# napis=input("Podaj napis")

# napis = "To jest napis przykladowy"
#
# magazyn = {}
# znak = ""
# for znak in napis:
#     if znak in napis:
#         magazyn[znak] = magazyn.get(znak, 0) + 1
# print(magazyn)