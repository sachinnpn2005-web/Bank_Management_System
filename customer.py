class Customer:

    def __init__(self, customer_id, name, phone, email, pin, account):

        # Validate customer information
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")

        if "@" not in email:
            raise ValueError("Invalid email address.")

        if not pin.isdigit() or len(pin) != 4:
            raise ValueError("PIN must be exactly 4 digits.")

        # Store customer information
        self._customer_id = customer_id
        self._name = name
        self._phone = phone
        self._email = email

        # Store PIN privately
        self.__pin = pin

        # Customer owns one account
        self._account = account

        # Login security
        self._failed_attempts = 0
        self._locked = False

    # Verify entered PIN
    def verify_pin(self, pin):

        # Don't allow login if account is locked
        if self._locked:
            print("Account is locked.")
            return False

        # Correct PIN
        if pin == self.__pin:
            self._failed_attempts = 0
            return True

        # Wrong PIN
        self._failed_attempts += 1

        # Lock account after 3 wrong attempts
        if self._failed_attempts >= 3:
            self.lock_account()

        return False

    # Change customer PIN
    def change_pin(self, old_pin, new_pin):

        if not self.verify_pin(old_pin):
            return False

        if not new_pin.isdigit() or len(new_pin) != 4:
            raise ValueError("PIN must be exactly 4 digits.")

        self.__pin = new_pin
        return True

    # Change phone number
    def change_phone(self, phone):

        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")

        self._phone = phone

    # Change email address
    def change_email(self, email):

        if "@" not in email:
            raise ValueError("Invalid email address.")

        self._email = email

    # Lock customer account
    def lock_account(self):
        self._locked = True

    # Unlock customer account
    def unlock_account(self):
        self._locked = False
        self._failed_attempts = 0

    # Return account object
    def get_account(self):
        return self._account

    # Return customer ID
    def get_customer_id(self):
        return self._customer_id

    # Return customer name
    def get_name(self):
        return self._name

    # Return phone number
    def get_phone(self):
        return self._phone

    # Return email
    def get_email(self):
        return self._email

    # Return customer PIN (used for saving data)
    def get_pin(self):
        return self.__pin

    # Check whether account is locked
    def is_locked(self):
        return self._locked

    # Convert customer object into dictionary
    def to_dict(self):

        return {
            "customer_id": self.get_customer_id(),
            "name": self.get_name(),
            "phone": self.get_phone(),
            "email": self.get_email(),
            "pin": self.get_pin(),
            "account": self.get_account().to_dict()
        }