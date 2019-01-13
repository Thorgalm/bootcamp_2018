produkty = {
    'ziemniaki': 1.99,
    'pomidory': 6.99,
    'woda': 1.79
}
magazyn = {
    'ziemniaki': 10,
    'pomidory': 10,
    'woda': 10
}
while True:
    rola = input("Czy jesteś [klient]em [k], czy [dostawca][d], [q] by zakończyć? ")
    if rola.lower() in ['klient', 'k']:
        while True:
            print("Nasz sklep oferuje: ")
            for produkt, cena in produkty.items():
                print(f" - {produkt} - {cena:2f}")  # dodanie 2f zaokrągla cene do dwoch miejsc po przecinku

            zakup = input("Co chcesz kupić? [k] by zakończyć")
            if zakup.lower() == 'k':
                print("zapraszamy ponownie")
                break
            if zakup not in produkty:
                print("Nie ma takiego produkty")
                continue
            waga = float(input(f"Ile chcesz kupić - [{zakup}]"))
            if waga > magazyn[zakup]:
                print("Nie ma tyle w magazynie")
                print(f"W magazynie pozotało: {magazyn[zakup]}")
            else:
                cena = produkty.get(zakup)
                if cena:
                    koszt = waga * produkty[zakup]
                    print(f"Za zakup [{zakup}] zapłacisz: {koszt}")
                    magazyn[zakup] = magazyn[zakup] - waga
                else:
                    print("To nie jest produkt z listy")

    elif rola.lower() in ['dostawca', 'd']:
        # ściezka dostawcy
        # dodanie produktu - 'd'
        # zmiana ceny - 'z'
        # prosimy o podanie produktu w formacie nazwa ilosc cena
        while True:
            do_dodania = input("Podaj produkt w formacie: [nazwa ilosc cena]")
            if len(do_dodania.split()) == 3:
                # split domyslnie dzieli napis po białych znakach(spacjach)
                nazwa, ilosc, cena = do_dodania.split()
                try:
                    ilosc = float(ilosc)
                    cena = float(cena)
                    produkty[nazwa] = cena
                    break
                except ValueError:
                    print("Niepoprawna cena lub ilosc")
            else:
                print("Podałeś produkt w niepoprawnym formacie")

        magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc
        # jesli w get nie damy domyslnie 0 to bedzie blad, bo jak nie ma w slowniku klucza to get bedzie nullem, funkcja get zwraca wartosc dla klucza
        # alternatywnie do: magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc mozna napisac tak:
        # if nazwa in magazyn:
        #     magazyn[nazwa] = magazyn[nazwa] + ilosc
        # else:
        #     magazyn[nazwa] = ilosc
        print("Dziekuję. Produkt Dodany")

    elif rola.lower() == 'q':
        print("Program przestaje dzialać")
        break

# moje
# sklep={
#     'ziemniaki': 2,
#     'pomidory': 5,
#     'ogorki': 3
# }
#
#
# co_kupuje = input("co chcesz kupic:")
# ile = input("ile chcesz kupic:")
#
# if co_kupuje in sklep:
#     razem = float(ile) * sklep[co_kupuje]
#
# print(f"Do zapłaty: {razem}")
