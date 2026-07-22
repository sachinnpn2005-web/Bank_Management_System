from bank import Bank
from customer import Customer
from account import SavingsAccount, CurrentAccount
from file_manager import FileManager


# Read amount safely from the user
def get_amount():

    while True:

        try:
            amount = float(input("Enter Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid amount.")


# Pause before returning to the menu
def pause():
    input("\nPress Enter to continue...")


# Create a new customer
def create_customer(bank):

    print("\n========== CREATE CUSTOMER ==========")

    try:

        name = input("Enter Name: ").strip()
        phone = input("Enter Phone: ").strip()
        email = input("Enter Email: ").strip()
        pin = input("Create 4-digit PIN: ").strip()

        # Generate IDs automatically
        customer_id = bank.generate_customer_id()
        account_number = bank.generate_account_number()

        print("\nSelect Account Type")
        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Enter choice: ")

        if choice == "1":
            account = SavingsAccount(account_number, 0)

        elif choice == "2":
            account = CurrentAccount(account_number, 0)

        else:
            print("Invalid account type.")
            return

        customer = Customer(
            customer_id,
            name,
            phone,
            email,
            pin,
            account
        )

        bank.add_customer(customer)

        print("\n====================================")
        print("Customer created successfully.")
        print(f"Customer ID : {customer_id}")
        print(f"Account No. : {account_number}")
        print("====================================")

    except ValueError as e:
        print(e)


# Deposit money
def deposit_money(bank):

    print("\n========== DEPOSIT MONEY ==========")

    customer_id = input("Enter Customer ID: ")

    amount = get_amount()

    bank.deposit_money(customer_id, amount)


# Withdraw money
def withdraw_money(bank):

    print("\n========== WITHDRAW MONEY ==========")

    customer_id = input("Enter Customer ID: ")

    amount = get_amount()

    bank.withdraw_money(customer_id, amount)


# Transfer money
def transfer_money(bank):

    print("\n========== TRANSFER MONEY ==========")

    sender_id = input("Sender Customer ID: ")
    receiver_id = input("Receiver Customer ID: ")

    amount = get_amount()

    bank.transfer_money(sender_id, receiver_id, amount)


# Remove customer
def remove_customer(bank):

    print("\n========== REMOVE CUSTOMER ==========")

    customer_id = input("Enter Customer ID: ")

    bank.remove_customer(customer_id)


# View one customer
def view_customer(bank):

    print("\n========== VIEW CUSTOMER ==========")

    customer_id = input("Enter Customer ID: ")

    bank.view_customer(customer_id)


# Main program
def main():

    # Create objects
    bank = Bank()
    file_manager = FileManager()

    # Load saved data
    file_manager.load_data(bank)

    while True:

        print("\n==================================================")
        print("            BANK MANAGEMENT SYSTEM")
        print("==================================================")
        print("1. Create Customer")
        print("2. View All Customers")
        print("3. View Customer")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. Remove Customer")
        print("8. Save Data")
        print("0. Exit")
        print("==================================================")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                create_customer(bank)

            elif choice == "2":

                bank.display_all_customers()

            elif choice == "3":

                view_customer(bank)

            elif choice == "4":

                deposit_money(bank)

            elif choice == "5":

                withdraw_money(bank)

            elif choice == "6":

                transfer_money(bank)

            elif choice == "7":

                remove_customer(bank)

            elif choice == "8":

                file_manager.save_data(bank)

            elif choice == "0":

                # Save data before exiting
                file_manager.save_data(bank)

                print("\nThank you for using the Bank Management System.")
                print("Data saved successfully.")
                break

            else:

                print("Invalid choice. Please try again.")

        except Exception as e:

            print(f"Unexpected Error: {e}")

        pause()


# Start the program
if __name__ == "__main__":
    main()