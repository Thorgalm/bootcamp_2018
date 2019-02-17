#kontekst manager - na koniec zamyka tez plik
#domyślnie otwiera w trybie do odczytu
with open("readme.txt") as f:
    for line in f:
        print(len(line))
    print(f.read())

#'w' tryb write - nadpisuje
with open("readme3.txt", 'w') as f:
    f.write('Ala ma kota')

# 'a' dopisuje
with open("readme3.txt", 'a') as f:
    f.write('\nkot ma alę')

# kiedys pisalo sie tak i trzeba bylo zamykac plik, przy uzyciu kontekst managera nie trzeba zamykac:
# f = open("readme.txt")
# f.write('\nkot ma alę')
# f.close()

with open("readme.txt", encoding='utf-8') as f:
    print(f)
    print(f.read())