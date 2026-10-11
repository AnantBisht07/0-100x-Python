class BankAccount:

    def __init__(self, balance):
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"{self.balance} after desposit")
    
    def withdraw(self, amount):
        print(f"Balance before withdraw {self.balance}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance after withdraw {self.balance}")
        else:
            print("Insufficent balance")


account = BankAccount(1000)
account.deposit(2000)
account.withdraw(1000)

