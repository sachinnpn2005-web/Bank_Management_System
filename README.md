# Bank Management System

A simple console-based Bank Management System made with Python for my Object-Oriented Programming project.

The project is mainly focused on using OOP concepts in a practical way while also handling customer data and basic banking operations.

## Features

* Create new customers
* Automatically generate Customer IDs and Account Numbers
* Create Savings or Current Accounts
* View all customers
* View a specific customer
* Deposit money
* Withdraw money
* Transfer money between customers
* Remove customers
* PIN verification and account locking
* Input validation and exception handling
* Automatically save data to JSON
* Automatically load saved data when the program starts

## OOP Concepts Used

The project uses the main OOP concepts required for the assignment:

* **Abstraction** – `Account` is an abstract base class.
* **Inheritance** – `SavingsAccount` and `CurrentAccount` inherit from `Account`.
* **Polymorphism** – Both account types implement their own `deposit()` and `withdraw()` methods.
* **Encapsulation** – Customer information such as the PIN is protected/private.
* **Composition** – A `Customer` has an `Account`.
* **Aggregation** – The `Bank` manages multiple `Customer` objects.

## Project Structure

```text
OOP_Project_Sachin/
│
├── account.py
├── bank.py
├── customer.py
├── file_manager.py
├── main.py
├── data/
│   └── bank_data.json
├── README.md
├── requirements.txt
└── .gitignore
```

## How It Works

When the program starts, it creates the `Bank` and `FileManager` objects and loads previously saved data from the JSON file.

After that, the main menu is displayed. The user can choose an operation such as creating a customer, viewing customer details, depositing money, withdrawing money, transferring money, or removing a customer.

Whenever customer or account data is changed, the updated information is automatically saved to the JSON file. This means the data is still available when the program is opened again.

## How to Run

Make sure Python is installed on your computer.

Open the project folder in the terminal and run:

```bash
python main.py
```

On some Windows systems, you may need:

```bash
py main.py
```

## Data Storage

Customer and account information is stored in:

```text
data/bank_data.json
```

The file is updated automatically whenever changes are made.

## Example Menu

```text
==================================================
            BANK MANAGEMENT SYSTEM
==================================================
1. Create Customer
2. View All Customers
3. View Customer
4. Deposit Money
5. Withdraw Money
6. Transfer Money
7. Remove Customer
0. Exit
==================================================
```

## Error Handling

The program uses `try-except` blocks and input validation to handle invalid data and banking operations. For example, it prevents invalid amounts, insufficient balance, invalid customer IDs, and incorrect input formats.

## Future Improvements

Some features I could add later are:

* Transaction history
* Customer and admin login
* Interest calculation
* Overdraft support
* Database integration
* GUI version

## Author

**Sachin Neupane**