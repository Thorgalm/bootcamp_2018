import re

with open(r'C:\Users\kurs\workspace\input.txt','r') as f:
    napis = f.read()

# print(napis)

# kody_pocztowe dwie cyfry \d{2} pauza trzy cyfry \d{3}
print(re.findall(r'\d{2}-\d{3}', napis))
# \b board granice slowa
print(re.findall(r'\b(\d{2}-\d{3})\b', napis))
print("----")

#maile dowolna ilosc znakow inne niz biale znaki \S+ małpa \w+ dowolna ilosc znakow a-z0-9 kropka i znowu dowolna ilosc znakow \w+
print(re.findall(r'\S+@\w+\.\w+', napis))
print(re.findall(r'\S+@\S+', napis))
# w nawiasie kwadratowe \w dowolny znak lub pauza lub + lub kropka, małpa w nawiasie kwadratowe \w dowolny znak lub pauza lub + lub kropka i minium 4 razy {4,}
print(re.findall(r'[\w\-+.]+@[\w\-.]{4,}', napis))
print("----")

# jedna lub dwie cyfry \d{1,2} bialyznak \s trzy litery \w{3} bialy znak \s cztery cyfry \d{4}
print(re.findall(r'\d{1,2}\s\w{3}\s\d{4}', napis))
print(re.findall(r'\b\d{1,2}\s[A-Z][a-z]{2}\s\d{4}\b', napis))