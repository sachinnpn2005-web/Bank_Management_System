from account import SavingsAccount


def main():

    try:
        # Create a savings account
        account = SavingsAccount(1001, 2000)

        # Deposit money
        account.deposit(1000)

        # Withdraw money
        account.withdraw(500)

        # Show account details
        account.display_info()

    # Handle any invalid operations
    except ValueError as e:
        print(f"Error: {e}")


# Run the program
if __name__ == "__main__":
    main()