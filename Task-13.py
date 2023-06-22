class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account.")
        else:
            self.balance -= amount


account = BankAccount("Иван Иванов", "123321")
print(account.balance)  # 0

account.deposit(1000)
print(account.balance)  # 1000

account.withdraw(500)
print(account.balance)  # 500

account.withdraw(1000)  # Insufficient funds on the account.
print(account.balance)  # 500
