import json

lista = [1, 2, 3, 'a', 'b', 'c']
print(1)
print(type(lista))

# operacja serializacji - zamiana listy na json
json_list = json.dumps(lista)

print(type(json_list))
# json to napis

# deserializacja - zamiana tesktu jak json na slownik
napis = '{"1":"a", "2":"b"}'

ds_napis = json.loads(napis)

print(2)
print(ds_napis)
print(type(ds_napis))

# deserializujemy, modyfikujemy w pythonie i serializujemy
# dodanie kolejnego klucza i wartosci dla nie go:
ds_napis[3] = "g"
print(json.dumps(ds_napis))

# dumps to dump strint - zrzuca do string
# dump zrzuca do pliku

print(3)
with open("napis.json", "w") as fp:
    json.dump(ds_napis, fp)

# print(help(json.load()))

print(4)
with open("napis.json") as fp:
    ob = json.load(fp)
    print(ob)
    print(type(ob))