from account import SavingsAccount
from customer import Customer


def main():

    try:
        # Create account
        account = SavingsAccount(1001, 5000)

        # Create customer
        customer = Customer(
            "C001",
            "Sachin Neupane",
            "9812345678",
            "sachin@gmail.com",
            "1234",
            account
        )

        print("Customer:", customer.get_name())

        # Test PIN
        print(customer.verify_pin("1234"))

        # Deposit money
        customer.get_account().deposit(1000)

        # Display account
        customer.get_account().display_info()

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()