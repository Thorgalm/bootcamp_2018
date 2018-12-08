miasto_a = input("Podaj Miasto A:")
miasto_b = input("Podaj Miasto B:")
#dystans = int(input("Podaj dysntans z miasta A do miasta B:"))
dystans = float(input("Podaj dystans z miasta "+miasto_a+" do "+miasto_b+":"))
cena_paliwa = float(input("Podaj cenę paliwa:"))
spalanie = float(input("Podaj spalanie na 100 km:"))
wynik = dystans*cena_paliwa*spalanie/100

info = f"""
Miasto A: {miasto_a} 
Miasto B: {miasto_b} 
Dystans z {miasto_a} do {miasto_b}: {dystans} km
Cena paliwa: {cena_paliwa} PLN
Spalanie na 100 km: {spalanie}
Koszt przejazdu {miasto_a} - {miasto_b} to: {wynik} PLN
"""
print(info)