from exceptions import *


class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        print(f"Account {self.name} created. Balance = €{self.balance:.2f}")

    def getBalance(self):
        print(f"Account {self.name} balance is €{self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, account {self.name} only has a balance of €{self.balance:0.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("Withdrawal complete.")
            self.getBalance()
        except BalanceException as exception:
            print(f"Withdrawal failed: {exception}")

    def transfer(self, amount, otherAccount):
        try:
            print("********************************")
            print("Beginning transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            otherAccount.deposit(amount)
            print("Transfer complete.")
            print("********************************")
        except BalanceException as exception:
            print(f"Transfer failed: {exception}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("Deposit complete with 5% of interest")
        self.getBalance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, balance, name):
        super().__init__(balance, name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("Withdrawal complete with a fee of 5€")
            self.getBalance()
        except BalanceException as exception:
            print(f"Withdrawal failed: {exception}")
