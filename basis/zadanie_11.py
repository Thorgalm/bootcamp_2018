x = int(input("Podaj X:"))
y = int(input("Podaj Y:"))

if x < 100 and y < 100:
    if x <= 10:
        s1 = "lewy"
    elif x >= 90:
        s1 = "prawy"
    else:
        s1 = ""
    if y <= 10:
        s2 = "górny"
    elif y >= 90:
        s2 = "dolny"
    else:
        s2 = ""

if s1 != "" and s2 != "":
    s3 = "róg"
elif s1 == "" and s2 == "":
    s3 = "centrum"
else:
    s3 = "krawedź"

print("Gracz znajduje się w", s1, s2, s3)
