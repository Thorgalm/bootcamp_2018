import re

pattern = re.compile("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")

with open("dane_ex3.txt") as f:
    dane = f.read()

print(pattern.findall(dane))

# http://www.pythonchallenge.com/pc/def/linkedlist.html
# http://www.pythonchallenge.com/pc/def/linkedlist.php