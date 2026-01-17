class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def remove(self, name):
        self.items = [p for p in self.items if p.name != name]

    def total(self):
        return sum(p.price for p in self.items)

    def show(self):
        for p in self.items:
            print(p.name, p.price)
        print(f"Разом:, {self.total()}")

cart = Cart()
cart.add(Product("Хліб", 20))
cart.add(Product("Молоко", 35))
cart.show()

