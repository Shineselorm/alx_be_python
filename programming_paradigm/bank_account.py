class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance  # Encapsulated balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")