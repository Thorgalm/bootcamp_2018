import requests
import decimal

resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")
kursy = resp.json(parse_float=decimal.Decimal)[0]['rates']

print("dysponuje walutami:")
for k in kursy:
    print(k)

waluta = input("Podaj kod waluty, którą chcesz kupić:")
za_ile = decimal.Decimal(input("za ile PLN chcesz kupic:"))

for k in kursy:
    if k ['code'] == waluta:
        print(f" Za {za_ile} PLN mozesz kupic {za_ile/k['mid']} {waluta}")

