from bank_accounts import *


dave = BankAccount(1000, "Dave")
sara = BankAccount(2000, "Sara")
jim = InterestRewardsAccount(500, "Jim")
blaze = SavingsAccount(1000, "Blaze")

dave.getBalance()
sara.getBalance()
jim.getBalance()

sara.deposit(500)

dave.withdraw(10000)
dave.withdraw(10)

dave.transfer(10000, sara)
dave.transfer(20, sara)

jim.deposit(100)
jim.transfer(100, sara)

blaze.deposit(500)
blaze.transfer(10000, sara)
blaze.transfer(20, sara)
