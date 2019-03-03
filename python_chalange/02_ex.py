from string import ascii_lowercase

with open("dane_ex2.txt") as f:
    dane = f.read()
out = []
for z in dane:
    if z in ascii_lowercase:
        out.append(z)

print(out)
print("".join(out))
# 2 rozwiazanie
import re
pattern = re.compile("[a-zA-Z]")
print(pattern.findall(dane))
# print(re.findall("[a-zA-Z]", dane)