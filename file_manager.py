import json
from account import SavingsAccount, CurrentAccount
from customer import Customer


class FileManager:

    # JSON file location
    FILE_NAME = "data/bank_data.json"

    # Save bank data into JSON file
    def save_data(self, bank):

        customers_data = []

        # Convert every customer object into dictionary
        for customer in bank.get_all_customers():
            customers_data.append(customer.to_dict())

        try:

            with open(self.FILE_NAME, "w") as file:
                json.dump(customers_data, file, indent=4)

            print("Data saved successfully.")

        except Exception as e:
            print(f"Error while saving data: {e}")

    # Load bank data from JSON file
    def load_data(self, bank):

        try:

            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

            # Create customer and account objects
            for customer_data in data:

                account_data = customer_data["account"]

                account_type = account_data["account_type"]

                # Create correct account object
                if account_type == "SavingsAccount":

                    account = SavingsAccount(
                        account_data["account_number"],
                        account_data["balance"]
                    )

                elif account_type == "CurrentAccount":

                    account = CurrentAccount(
                        account_data["account_number"],
                        account_data["balance"]
                    )

                else:
                    continue

                # Create customer object
                customer = Customer(
                    customer_data["customer_id"],
                    customer_data["name"],
                    customer_data["phone"],
                    customer_data["email"],
                    customer_data["pin"],
                    account
                )

                bank.add_customer(customer)

        except FileNotFoundError:

            # Create empty file if it doesn't exist
            with open(self.FILE_NAME, "w") as file:
                json.dump([], file)

        except json.JSONDecodeError:

            print("JSON file is empty or corrupted.")

        except Exception as e:

            print(f"Error while loading data: {e}")