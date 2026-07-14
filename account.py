from abc import ABC, abstractmethod


# Abstract class for all account types
class Account(ABC):

    def __init__(self, account_number, balance):

        # Check if initial balance is valid
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self._account_number = account_number
        self._balance = balance

    # Deposit money
    @abstractmethod
    def deposit(self, amount):
        pass

    # Withdraw money
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Display account details
    @abstractmethod
    def display_info(self):
        pass


# Savings Account class
class SavingsAccount(Account):

    def deposit(self, amount):

        # Deposit amount should be greater than zero
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self._balance += amount

    def withdraw(self, amount):

        # Withdrawal amount should be greater than zero
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Check available balance
        if amount > self._balance:
            raise ValueError("Insufficient balance.")

        self._balance -= amount

    def display_info(self):

        print("\n===== Savings Account =====")
        print(f"Account Number : {self._account_number}")
        print(f"Balance        : Rs. {self._balance:.2f}")
        print("===========================\n")

    # Return account number
    def get_account_number(self):
        return self._account_number

    # Return current balance
    def get_balance(self):
        return self._balance

# Current Account class
class CurrentAccount(Account):

    def deposit(self, amount):

        # Deposit amount should be greater than zero
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self._balance += amount

    def withdraw(self, amount):

        # Withdrawal amount should be greater than zero
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Check available balance
        if amount > self._balance:
            raise ValueError("Insufficient balance.")

        self._balance -= amount

    def display_info(self):

        print("\n===== Current Account =====")
        print(f"Account Number : {self._account_number}")
        print(f"Balance        : Rs. {self._balance:.2f}")
        print("===========================\n")

    # Return account number
    def get_account_number(self):
        return self._account_number

    # Return current balance
    def get_balance(self):
        return self._balance