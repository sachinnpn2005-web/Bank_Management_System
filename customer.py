class Customer:

    def __init__(self, customer_id, name, phone, email, pin, account):

        # Basic customer information
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

        # Store PIN privately
        self.__pin = pin

        # Customer owns one account
        self._account = account

        # Login security
        self.failed_attempts = 0
        self.locked = False

    # Verify entered PIN
    def verify_pin(self, pin):

        # Don't allow login if account is locked
        if self.locked:
            return False

        # Correct PIN
        if pin == self.__pin:
            self.failed_attempts = 0
            return True

        # Wrong PIN
        self.failed_attempts += 1

        # Lock account after 3 wrong attempts
        if self.failed_attempts >= 3:
            self.lock_account()

        return False

    # Change PIN after verification
    def change_pin(self, old_pin, new_pin):

        if self.verify_pin(old_pin):
            self.__pin = new_pin
            return True

        return False

    # Lock the account
    def lock_account(self):
        self.locked = True

    # Unlock the account
    def unlock_account(self):
        self.locked = False
        self.failed_attempts = 0

    # Return account object
    def get_account(self):
        return self._account

    # Return customer name
    def get_name(self):
        return self.name
    
    # Return customer id
    def get_customer_id(self):
        return self.customer_id