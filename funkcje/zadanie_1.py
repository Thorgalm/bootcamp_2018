def czy_jest_pierwsza(a):
    for i in range(2, a//2+1):
        if a % i == 0:
            return False
    return True

#//dzielenie całkowite

print(czy_jest_pierwsza(10))

# assert czy_jest_pierwsza(17) == True
# assert czy_jest_pierwsza(10) == False
assert czy_jest_pierwsza(17)
assert not czy_jest_pierwsza(10)
