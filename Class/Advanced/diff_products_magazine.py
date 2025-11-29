from datetime import datetime

class Product:
    def __init__(self, barcode, name, price, quantity):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"{self.barcode}, {self.name}, {self.price}, {self.quantity}"

    def sale(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
        else:
            print(f"Няма достатъчно количество от {self.name}")

class FoodProduct(Product):
    def __init__(self, barcode, name, price, quantity, expiration_date):
        super().__init__(barcode, name, price, quantity)
        self.expiration_date = expiration_date

    def info(self):
        return super().info() + f", Срока на годност е: {self.expiration_date}"


class ElectronicProduct(Product):
    def __init__(self, barcode, name, price, quantity, warranty_years):
        super().__init__(barcode, name, price, quantity)
        self.warranty_years = warranty_years

    def info(self):
        return super().info() + f", Гаранция: {self.warranty_years} години"


products = [
    FoodProduct("001", "Мляко", 2.5, 20, "2025-12-01"),
    FoodProduct("002", "Хляб", 1.2, 50, "2025-05-15"),
    ElectronicProduct("101", "Телевизор", 800, 5, 2),
    ElectronicProduct("102", "Слушалки", 150, 10, 1),
]

print("=== Всички продукти ===")
for p in products:
    print(p.info())

print("\n=== Продукти с кратка гаранция или изтичащ срок ===")
user_input = input("Въведете дата за проверка (ГГГГ-ММ-ДД): ")
check_date = datetime.strptime(user_input, "%Y-%m-%d")

def checking():
 for product in products:
    if isinstance(product, FoodProduct):
        expiration = datetime.strptime(product.expiration_date, "%Y-%m-%d")
        days_to_expire = (expiration - check_date).days
        if 0 <= days_to_expire <= 30:
            print("Предупреждение! Срока изтича")
        elif days_to_expire < 0:
            print("Срокът на годност е изтекъл!")

    elif isinstance(product, ElectronicProduct):
        if product.warranty_years < 2:
            print("Предупреждение! Гаранцията изтича!")
checking()

print("\n=== Примерни продажби ===")
products[0].sale(5)
products[1].sale(100)

print("\n=== Актуално състояние на продуктите ===")
for p in products:
    print(p.info())
