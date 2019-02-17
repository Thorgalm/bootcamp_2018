class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity


class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, product, quantity):

        # wersja z uzyciem listy:
        # add = True
        # for position in self.entries:
        #     if position[0] == product:
        #         position[1] += quantity
        #         add = False
        # else:
        #     self.entries.append([product, quantity])

        # def count_total_price(self):

        # wersja z uzyciem dodatkowej klasy - koszyka wejsciowego
        basket_entry = BasketEntry(product, quantity)
        for be in self.entries:
            if be.product == product:
                be.quantity += quantity
                break
        else:
            self.entries.append(basket_entry)

    def count_total_price(self):
        total = 0
        for e in self.entries:
            total += e.count_price()
        return total

    def generate_report(self):
        raport = "Produkty w koszyku \n"
        for e in self.entries:
            raport += f' - {e.product.name} ({e.quantity}), cena: {e.product.price} x {e.quantity}\n'
        raport += f'W sumie: {self.count_total_price()}'


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt {self.name}, id: {self.id}, cena: {self.price} PLN")

    def __str__(self):
        return f"Produkt nazwa: {self.name}, id: {self.id}"


def test_Basket_initialization():
    basket = Basket()
    assert basket.entries == []


def test_Product_initialization():
    product = Product(1, 'Woda', 10.00)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.0


def test_basket_add_product():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    basket.add_product(product, 3)
    assert len(basket.entries) == 1


def test_basket_add_product():
    basket = Basket()
    product1 = Product(1, 'Woda', 10.00)
    product2 = Product(1, 'Ogórki', 2.00)
    basket.add_product(product1, 5)
    basket.add_product(product2, 3)
    assert len(basket.entries) == 2
    assert basket.count_total_price() == 10 * 5 + 2 * 3


def test_basket_generate_report():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert basket.generate_report() == """Produkty w koszyku: 
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00"""


# basket = Basket()
# product = Product(1, 'Woda', 10.00)
# basket.add_product(product, 5)
# basket.generate_report()
