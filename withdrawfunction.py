balance = 1000
amount = 300
def withdraw(amount, balance):
    remainingbalance = balance - amount
    return remainingbalance
print(withdraw(amount, balance))