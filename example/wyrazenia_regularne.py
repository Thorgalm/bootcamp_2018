import re

a = "Ala ma kota! Kot ma Ale. Kot lubi mleko. Nie lubi ryb."

b = re.findall('lubi',a)
print(b)

#trzy znaki spacja i 'ma'
c = re.findall('... ma',a)
print(c)
# trzy dowolne znaki .{3}
c = re.findall('.{3} ma',a)
print(c)

#\w znaki alfa numeryczny
print(re.findall('\w ma',a))
# * wiele razy
print(re.findall('\w*',a))
# z + zwraca slowa
print(re.findall('\w+',a))
print(re.findall(r'\w+',a))
# duze litery
print(re.findall(r'[A-Z]',a))
#\. wtedy to normalna kropka
print(re.findall(r'[A-Z].*\.',a))
print(re.findall(r'[A-Z].*?\.',a))
print(re.findall(r'[A-Z].*?[\.\!]',a))
#\s to wszystkie biale znaki
print(re.findall(r'[A-Z]\w*\s?[\.\!]',a))
# \W wszystko co nie jest male w
print(re.findall(r'([A-Z]\w*)\W.*?[\.\!]',a))

