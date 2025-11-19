class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def account_info(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

account_1 = BankAccount("Alexandra", 1000)
account_2 = BankAccount("Nikol", 3000)

print(account_1.account_info())
print(account_2.account_info())