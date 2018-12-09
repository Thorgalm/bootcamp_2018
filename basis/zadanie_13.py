# ile_dni = float(input("Ile dni:"))
# temp = 0
# i = 1
# while i <= ile_dni:
#     temp_i = float(input(f"Podaj temperaturę w dniu {i}:"))
#     temp += temp_i
#     i += 1
#
# print("Średnia temperatur wynosiła:", temp / ile_dni)

# 2 rozwiazanie
ile_dni = 7
temp = 0
i = 1
while i <= ile_dni:

    komenda = input(f"Podaj temperaturę w dniu {i} lub k by zakończyć:")
    if komenda == 'k':
        break
    temp_i = float(komenda)
    temp += temp_i
    i += 1

print("Średnia temperatur wynosiła:", temp / (i-1))