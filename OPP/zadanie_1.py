# class Product:
#     def __init__(self, id, name, cena):
#         self.id = id
#         self.name = name
#         self.cena = cena
#
# def print_info(id, name, cena):
#         print(f"Produkt {name}, id: {id}, cena: {cena} PLN")
#
# produkt = Product(1, "woda", 2.99)
#
# print_info(produkt.id, produkt.name, produkt.cena)

class Product:
    """Opis produktow w sklepie"""
    def __init__(self, id, name, cena):
        self.id = id
        self.name = name
        self.cena = cena

    def print_info(self):
        """Wypisanie informacji o produkcie"""
        print(f"Produkt {self.name}, id: {self.id}, cena: {self.cena} PLN")

    def __str__ (self):
        return f"Produkt {self.name}, id: {self.id}, cena: {self.cena} PLN"

produkt = Product(1, "woda", 2.99)

produkt.print_info()

print(produkt)

print(help(produkt))