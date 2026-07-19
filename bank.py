class Bank:

    def __init__(self):
        # Store all customers
        self._customers = []

    # Add a customer to the bank
    def add_customer(self, customer):
        self._customers.append(customer)

    # Return all customers
    def get_all_customers(self):
        return self._customers

    # Find customer using customer ID
    def find_customer(self, customer_id):

        for customer in self._customers:

            if customer.get_customer_id() == customer_id:
                return customer

        return None

    # Remove a customer
    def remove_customer(self, customer_id):

        customer = self.find_customer(customer_id)

        if customer is None:
            return False

        self._customers.remove(customer)
        return True

    # Deposit money
    def deposit_money(self, customer_id, amount):

        customer = self.find_customer(customer_id)

        if customer is None:
            return False

        try:
            customer.get_account().deposit(amount)
            return True

        except ValueError as e:
            print(e)
            return False

    # Withdraw money
    def withdraw_money(self, customer_id, amount):

        customer = self.find_customer(customer_id)

        if customer is None:
            return False

        try:
            customer.get_account().withdraw(amount)
            return True

        except ValueError as e:
            print(e)
            return False

    # Transfer money between customers
    def transfer_money(self, sender_id, receiver_id, amount):

        try:

            # Sender and receiver cannot be the same
            if sender_id == receiver_id:
                raise ValueError("Sender and receiver cannot be the same.")

            sender = self.find_customer(sender_id)
            receiver = self.find_customer(receiver_id)

            # Check whether both customers exist
            if sender is None or receiver is None:
                raise ValueError("Invalid customer ID.")

            # Withdraw from sender
            sender.get_account().withdraw(amount)

            # Deposit to receiver
            receiver.get_account().deposit(amount)

            return True

        except ValueError as e:
            print(e)
            return False

    # Display all customers
    def display_all_customers(self):

        if not self._customers:
            print("\nNo customers found.")
            return

        print("\n========== CUSTOMER LIST ==========\n")

        for customer in self._customers:

            account = customer.get_account()

            print(f"Customer ID   : {customer.get_customer_id()}")
            print(f"Name          : {customer.get_name()}")
            print(f"Phone         : {customer.get_phone()}")
            print(f"Email         : {customer.get_email()}")
            print(f"Account No.   : {account.get_account_number()}")
            print(f"Account Type  : {type(account).__name__}")
            print(f"Balance       : Rs. {account.get_balance()}")
            print("-" * 40)

    # Generate next customer ID
    def generate_customer_id(self):

        # First customer
        if not self._customers:
            return "C001"

        # Last customer
        last_customer = self._customers[-1]

        # Example: C005
        last_id = last_customer.get_customer_id()

        # Remove C
        number = int(last_id[1:])

        # Increase by one
        number += 1

        # Return new ID
        return "C" + str(number).zfill(3)

    # Generate next account number
    def generate_account_number(self):

        # First account
        if not self._customers:
            return 1001

        last_customer = self._customers[-1]

        account = last_customer.get_account()

        return account.get_account_number() + 1