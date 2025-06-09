# Bank System

class BankAccount:
    temp = 100
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self._balance = 0

    def get_bal(self):
        return self._balance;

    def withdraw(self, amount):
        self._balance -= amount
        print(f"Amount {amount} is withdrawed")
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Amount {amount} is deposited")

class SavingAccount(BankAccount):
    def __init__(self, id, name, interest_rate):
        super().__init__(id, name)
        self.interest_rate = interest_rate

    def apply_interest(self, years):
        print(f"You got an interest of {(self.get_bal()*self.interest_rate*years)/100}")

account1 = BankAccount(101, "Tarun")
s_account1 = SavingAccount(101, "Tiwari", 7)

account1.deposit(11000)
account1.deposit(1000)
s_account1.deposit(11000)
print(account1.get_bal())
print(s_account1.get_bal())
print(s_account1.temp)
print(s_account1._balance)