# 🏦 Bank Management System

## 📌 Project Overview

The Bank Management System is a console-based application developed using Python and Object-Oriented Programming (OOP). It allows users to create customer accounts, perform banking operations, and store data permanently using JSON file handling.

This project was developed as part of the Object-Oriented Programming course to demonstrate the practical implementation of OOP concepts.

---

## ✨ Features

- Create new customer accounts
- Automatically generate Customer ID
- Automatically generate Account Number
- Savings Account and Current Account
- Deposit money
- Withdraw money
- Transfer money between customers
- Remove customer
- View a single customer
- View all customers
- PIN verification
- Account locking after multiple incorrect PIN attempts
- Save data into JSON file
- Load data automatically when the program starts
- Exception handling for invalid operations

---

## 💻 Technologies Used

- Python 3
- Object-Oriented Programming
- JSON File Handling
- Git & GitHub

---

## 📂 Project Structure

```
Bank_Management_System/
│
├── account.py
├── customer.py
├── bank.py
├── file_manager.py
├── main.py
├── data/
│   └── bank_data.json
├── README.md
└── .gitignore
```

---

## 🧩 OOP Concepts Used

### Encapsulation

Customer PIN is stored as a private attribute.

### Abstraction

The Account class is implemented as an Abstract Base Class.

### Inheritance

SavingsAccount and CurrentAccount inherit from the Account class.

### Polymorphism

Different account types implement the abstract methods of the Account class.

### Composition

A Customer object owns an Account object.

---

## ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/yourusername/Bank_Management_System.git
```

2. Open the project folder

3. Run the application

```
python main.py
```

---

## 📸 Sample Menu

```
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
8. Save Data
0. Exit
==================================================
```

---

## 📈 Future Improvements

- Transaction History
- Admin Login
- Customer Login
- Interest Calculation
- Overdraft Facility
- Password Encryption
- Database Integration
- Graphical User Interface (GUI)

---

## 👨‍💻 Author

**Sachin Neupane**
