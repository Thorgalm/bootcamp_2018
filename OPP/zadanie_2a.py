class Dog:
    # Class atribute
    species = "Canis Familiaris"

    # Inittializer / Instance Atributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

def najstarszy(self, *args):
    dog_ages = [] #tworzymy pustą tablice
    for dog in args:
        dog_ages.append([dog.age, dog])

    dog_ages.sort()
    return dog_ages[-1][1] #bierzemy ostatnia z list dlatego -1 i nie wiek tylko nazwa dlatego 1,bo liczymy od 0

rex = Dog("Rex", 10)
azor = Dog("Azor", 2)
mruczek = Dog("Mruczek", 12)

#print(rex.age)
# Dog.najstarszy(rex, azor, mruczek)
# print(najstarszy(rex, azor, mruczek).name)

dog = najstarszy(rex, azor, mruczek)
print(dog.name)

print(najstarszy(rex, azor, mruczek).name)