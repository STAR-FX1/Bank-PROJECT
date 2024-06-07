
from main import Account

class SavingsAccount(Account):
    def deeposit(self, amount):
        self.balance += amount * 0.005
        super().deposit(amount)

    def withdraw(self, amount):
           if amount <= 700000:
               super().withdraw(amount)
           else:
               print("WITHDRAWAL LIMIT")

AmountSaved = SavingsAccount()
AmountSaved.deposit(500000000)
