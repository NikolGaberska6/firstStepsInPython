class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
         return self.price * self.quantity


first_product = Product("chees", 10, 1)
second_product = Product("water", 1, 6)
third_product = Product("shisha", 30, 5)

print(f"Името на първия продукт: {first_product.name}")
print(f"Общата цена на първия продукт: {first_product.total_price()}")
print(f"Името на втория продукт: {second_product.name}")
print(f"Общата цена на втория продукт: {second_product.total_price()}")
