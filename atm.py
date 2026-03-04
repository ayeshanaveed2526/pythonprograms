class ATM:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")
        self.check_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
            self.check_balance()

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
atm = ATM("AYESHA", "123456789", 1000)    
atm.check_balance()
atm.deposit(500)
atm.withdraw(200)
atm.withdraw(1500)  
atm.exit()
