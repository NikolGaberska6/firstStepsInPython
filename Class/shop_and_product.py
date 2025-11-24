class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, count):
        if count > self.quantity:
            print("Няма достатъчно количество!")
        else:
            self.quantity -= count
            print(self.quantity)

class Shop:
    def __init__(self):
        self.shop_list = []
