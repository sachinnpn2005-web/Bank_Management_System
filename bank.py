class Bank:

    def __init__(self):
        # Store all customer objects
        self._customers = []

    # Add a new customer to the bank
    def add_customer(self, customer):
        self._customers.append(customer)

    # Find a customer using customer ID
    def find_customer(self, customer_id):

        # Check every customer in the list
        for customer in self._customers:

            # Return customer if ID matches
            if customer.get_customer_id() == customer_id:
                return customer

        # Return None if customer is not found
        return None

    # Remove a customer from the bank
    def remove_customer(self, customer_id):

        # Search for the customer
        customer = self.find_customer(customer_id)

        if customer is None:
            return False

        # Remove customer from the list
        self._customers.remove(customer)
        return True

    # Display all customers
    def display_all_customers(self):

        # Check if there are any customers
        if not self._customers:
            print("No customers found.")
            return

        print("\n========== Customers ==========\n")

        # Display every customer's details
        for customer in self._customers:

            account = customer.get_account()

            print(f"Customer ID : {customer.get_customer_id()}")
            print(f"Name        : {customer.get_name()}")
            print(f"Account No. : {account.get_account_number()}")
            print(f"Balance     : Rs. {account.get_balance():.2f}")
            print(f"Account Type: {type(account).__name__}")
            print("-" * 35)

    # Deposit money into a customer's account
    def deposit_money(self, customer_id, amount):

        # Search customer
        customer = self.find_customer(customer_id)

        if customer is None:
            return False

        customer.get_account().deposit(amount)
        return True

    # Withdraw money from a customer's account
    def withdraw_money(self, customer_id, amount):

        # Search customer
        customer = self.find_customer(customer_id)

        if customer is None:
            return False

        customer.get_account().withdraw(amount)
        return True

    # Transfer money from one customer to another
    def transfer_money(self, sender_id, receiver_id, amount):

        try:

            # Sender and receiver cannot be the same
            if sender_id == receiver_id:
                raise ValueError("Sender and receiver cannot be the same.")

            # Find both customers
            sender = self.find_customer(sender_id)
            receiver = self.find_customer(receiver_id)

            # Check if both customers exist
            if sender is None or receiver is None:
                raise ValueError("Invalid customer ID.")

            # Withdraw money from sender
            sender.get_account().withdraw(amount)

            # Deposit money into receiver
            receiver.get_account().deposit(amount)

            return True

        except ValueError as e:
            print(e)
            return False