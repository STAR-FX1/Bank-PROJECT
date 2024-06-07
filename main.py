#PROJECT BY: LAWAL OLUWATOBI BHU/23/04/05/0059
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("ACCOUNT BALANCE IS: ", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("ACCOUNT BALANCE IS: ", self.balance)