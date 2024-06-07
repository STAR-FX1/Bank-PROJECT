
from main import Account


class StudentAccount(Account):
    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("WITHDRAWAL LIMIT")

    def withdraw(self, amount):
        if  amount <=2000:
            super().withdrasw(amount)
        else:
            print("WITHDRAWAL LIMIT")

StudentBalance = StudentAccount()
StudentBalance.withdraw(50000)
