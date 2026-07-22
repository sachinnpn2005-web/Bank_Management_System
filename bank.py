class Bank:

    def __init__(self):
        # Store all customers
        self._customers = []

    # Add a new customer
    def add_customer(self, customer):
        self._customers.append(customer)

    # Return all customers
    def get_all_customers(self):
        return self._customers

    # Search customer using customer ID
    def find_customer(self, customer_id):

        for customer in self._customers:

            if customer.get_customer_id() == customer_id:
                return customer

        return None

    # Check whether customer exists
    def customer_exists(self, customer_id):

        return self.find_customer(customer_id) is not None

    # Remove customer from the bank
    def remove_customer(self, customer_id):

        customer = self.find_customer(customer_id)

        if customer is None:
            print("Customer not found.")
            return False

        self._customers.remove(customer)

        print("Customer removed successfully.")
        return True

    # Deposit money
    def deposit_money(self, customer_id, amount):

        customer = self.find_customer(customer_id)

        if customer is None:
            print("Customer not found.")
            return False

        try:
            customer.get_account().deposit(amount)
            print("Amount deposited successfully.")
            return True

        except ValueError as e:
            print(e)
            return False

    # Withdraw money
    def withdraw_money(self, customer_id, amount):

        customer = self.find_customer(customer_id)

        if customer is None:
            print("Customer not found.")
            return False

        try:
            customer.get_account().withdraw(amount)
            print("Amount withdrawn successfully.")
            return True

        except ValueError as e:
            print(e)
            return False

    # Transfer money between two customers
    def transfer_money(self, sender_id, receiver_id, amount):

        try:

            # Sender and receiver cannot be the same
            if sender_id == receiver_id:
                raise ValueError("Sender and receiver cannot be the same.")

            sender = self.find_customer(sender_id)
            receiver = self.find_customer(receiver_id)

            # Check whether both customers exist
            if sender is None:
                raise ValueError("Sender not found.")

            if receiver is None:
                raise ValueError("Receiver not found.")

            # Withdraw from sender
            sender.get_account().withdraw(amount)

            # Deposit to receiver
            receiver.get_account().deposit(amount)

            print("Transfer completed successfully.")
            return True

        except ValueError as e:
            print(e)
            return False

    # Display one customer
    def view_customer(self, customer_id):

        customer = self.find_customer(customer_id)

        if customer is None:
            print("Customer not found.")
            return

        account = customer.get_account()

        print("\n========================================")
        print(f"Customer ID   : {customer.get_customer_id()}")
        print(f"Name          : {customer.get_name()}")
        print(f"Phone         : {customer.get_phone()}")
        print(f"Email         : {customer.get_email()}")
        print(f"Account No.   : {account.get_account_number()}")
        print(f"Account Type  : {type(account).__name__}")
        print(f"Balance       : Rs. {account.get_balance():.2f}")
        print("========================================")

    # Display all customers
    def display_all_customers(self):

        if not self._customers:
            print("\nNo customers available.")
            return

        print("\n========== CUSTOMER LIST ==========")

        for customer in self._customers:

            account = customer.get_account()

            print("\n----------------------------------------")
            print(f"Customer ID   : {customer.get_customer_id()}")
            print(f"Name          : {customer.get_name()}")
            print(f"Phone         : {customer.get_phone()}")
            print(f"Email         : {customer.get_email()}")
            print(f"Account No.   : {account.get_account_number()}")
            print(f"Account Type  : {type(account).__name__}")
            print(f"Balance       : Rs. {account.get_balance():.2f}")
            print("----------------------------------------")

    # Generate customer ID automatically
    def generate_customer_id(self):

        # First customer
        if not self._customers:
            return "C001"

        highest = 0

        # Find the highest customer ID
        for customer in self._customers:

            number = int(customer.get_customer_id()[1:])

            if number > highest:
                highest = number

        highest += 1

        return "C" + str(highest).zfill(3)

    # Generate account number automatically
    def generate_account_number(self):

        # First account
        if not self._customers:
            return 1001

        highest = 1000

        # Find the highest account number
        for customer in self._customers:

            account_number = customer.get_account().get_account_number()

            if account_number > highest:
                highest = account_number

        return highest + 1