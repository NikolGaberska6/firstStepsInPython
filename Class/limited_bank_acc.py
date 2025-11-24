class BankAccount:
    def __init__(self, name, balance, limit):
        self.name = name
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.limit:
            print("Надвишаваш лимита!")
        elif amount > self.balance:
            print("Няма достатъчно средства")
        else:
            self.balance -= amount

    def info(self):
        print(f"Клиента: {self.name}, баланса: {self.balance} lv.")

client1 = BankAccount("Mike", 1000, 200)
client2 = BankAccount("Georgi", 2000, 500)
client3 = BankAccount("Yordan", 3000, 1000)

client1.deposit(150), client1.withdraw(100), client1.info()
client2.deposit(200), client2.withdraw(150), client2.info()
client3.deposit(55), client3.withdraw(133), client3.info()
