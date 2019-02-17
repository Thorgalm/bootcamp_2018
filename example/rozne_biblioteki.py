import datetime

a = datetime.date.today()
print(a)
print(type(a))

u = datetime.date(2019, 7, 23)
print(u)

b = datetime.datetime.today()
print(b)
print(type(b))

c = datetime.timedelta(days=2, hours=4) / datetime.timedelta(hours=1)

# uzycie formatu decimal, bo float zaokragla, uwaga: float nie lubi sie z decimal, np nie dodają sie
import decimal

import json

s = '{"kwota":1.56}'
ss = json.loads(s, parse_float=decimal.Decimal)
print(ss)

# rozkłada adresy internetowe na elementy
import urllib.parse

d= urllib.parse.urlparse("http://api.nbp.pl/api/exchangerates/tables/A?format=json")
print(d)

#modul struct do czytania ślaczków
import struct

with open(r'C:\Program Files (x86)\Microsoft Office\Stationery\1033\CURRENCY.GIF','rb') as f:
    img = f.read()

#r przed linkiem nie traktuje \ jako znaki specjalne

print(img)
# w google znajdujemy strukture GIF header, bierzemy tylko rozmiar gif, < to oznacza, ze jest to little-endian, rozmiar pliku jest w przedziale od 6 do 10 bajtu, ladujemy dane dwubajtowe i nie moga byc ujemne wiec HH
e = struct.unpack('<HH', img[6:10])
print(e)

#modul re - wyrazenia regularne
