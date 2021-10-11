class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Account Balance: $" + str(self.balance),"Interest rate:", self.int_rate,)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate / 100
        return self

class User:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.account = BankAccount(int_rate, balance)

User1 = User('User1', 1.5, 500)
User2 = User('User2', 2.5, 1000)

print("User1 Account")
User1.account.deposit(500)
User1.account.deposit(500)
User1.account.deposit(500)
User1.account.withdraw(500)
User1.account.yield_interest()
User1.account.display_account_info()
print("---------------")
print("User2 Account")
User2.account.deposit(100)
User2.account.deposit(100)
User2.account.withdraw(200)
User2.account.withdraw(200)
User2.account.withdraw(200)
User2.account.withdraw(200)
User2.account.yield_interest()
User2.account.display_account_info()


