# x = int(input("Podaj X:"))
# y = int(input("Podaj Y:"))
#
# if x < 100 and y < 100:
#     if x <= 10:
#         s1 = "lewy"
#     elif x >= 90:
#         s1 = "prawy"
#     else:
#         s1 = ""
#     if y <= 10:
#         s2 = "górny"
#     elif y >= 90:
#         s2 = "dolny"
#     else:
#         s2 = ""
#
# if s1 != "" and s2 != "":
#     s3 = "róg"
# elif s1 == "" and s2 == "":
#     s3 = "centrum"
# else:
#     s3 = "krawedź"
#
# print("Gracz znajduje się w", s1, s2, s3)

# rozwiązanie prowadzącego

x = int(input("Podaj X:"))
y = int(input("Podaj Y:"))
# czy jest poza planszą
if x < 0 or x > 100 or y < 0 or y > 100:
    print("Jesteś poza planszą")
elif x > 90 and y > 90:
    print("Jesteś w górnym prawym rogu")
elif x > 90 and y < 10:
    print("Jesteś w dolnym prawym rogu")
elif x < 10 and y < 10:
    print("Jesteś w dolnym lewym rogu")
elif x < 10 and y > 90:
    print("Jesteś w górnym lewym rogu")
elif x < 10:
    print("Jesteś w na lewej krawędzi")
elif x > 90:
    print("Jesteś w na prawej krawędzi")
elif y < 10:
    print("Jesteś w na dolnej krawędzi")
elif y > 90:
    print("Jesteś w na górnej krawędzi")
else:
    print("Jesteś w centrum")
