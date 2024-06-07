
from main import Account

class ChildrensAccount(Account):
    def deposit(self, amount):
        self.balance += amount * 0.007
        super().deposit(amount)

    def withdraw(self, amount):
        print("Childrens account are off limit")

ChildBalance = ChildrensAccount()
ChildBalance.deposit(1000)
ChildBalance.withdraw(10)
