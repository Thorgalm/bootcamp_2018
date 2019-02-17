import requests

resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")

# sprawdzenie czy pobrał dane, jesli bedzie cos innego niz status 200 to wywali błąd i nie bedzie przetwarzał
# resp.raise_for_status()
#
# nbp = resp.content
# print(nbp)

kursy = resp.json()[0]['rates']
# print(kursy)

print("dysponuje walutami:")
for k in kursy:
    print(k)

waluta = input("Podaj kod waluty, którą chcesz kupić:")
za_ile = float(input("za ile PLN chcesz kupic:"))

for k in kursy:
    if k ['code'] == waluta:
        print(f" Za {za_ile} PLN mozesz kupic {za_ile/k['mid']} {waluta}")

# for r in kursy[0]['rates']:
#     if r['currency'] == 'euro':
#         pass
#         # print(r)
#
# print(type(kursy))