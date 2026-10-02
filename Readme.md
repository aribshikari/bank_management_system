🏦 MY-BANK | Bank Management System

A simple console-based Bank Management System built using Python and Object-Oriented Programming (OOP). This project allows users to create bank accounts, log in, manage their balance, transfer money, and perform other basic banking operations.

🚀 Features

- Create Account: Open a savings or current account with a minimum initial deposit of ₹1,000.
- User Login: Access an account using an account number and a 4-digit PIN.
- Check Balance: View your current account balance.
- Deposit Money: Add money to your account.
- Withdraw Money: Withdraw money with an insufficient-balance check.
- Account Details: View your account number, name, account type, and balance.
- Money Transfer: Transfer money between accounts registered in the same bank.
- Change PIN: Update your account's 4-digit PIN.
- Delete Account: Delete an account after PIN verification and confirmation.
- Logout: Exit your account and return to the main menu.

🛠️ Technologies Used

- Language: Python
- Concepts: Object-Oriented Programming (OOP)
- Error Handling: Try-Except
- Data Structures: Lists
- Input Validation: Conditional statements and loops

📚 Python Concepts Practiced

This project helped me practice:

1. Classes and Objects – Creating a "bank" class and individual account objects.
2. Constructors – Using "__init__()" to initialize account information.
3. Lists – Storing and managing multiple account objects.
4. Loops – Using "while" and "for" loops for menus and account operations.
5. Conditional Statements – Managing different banking services and validations.
6. Exception Handling – Handling invalid numeric input during account creation.
7. User Input and Output – Building an interactive command-line application.

⚙️ How to Run

1. Clone the repository

git clone YOUR_REPOSITORY_URL

2. Open the project folder

cd YOUR_PROJECT_FOLDER

3. Run the Python program

python main.py

Make sure Python is installed on your computer.

🖥️ Application Menu

Main Menu

===============================
       WELCOME TO MY-BANK
===============================
1. Create Account
2. Log In
3. Exit

Account Menu

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. View Account Details
5. Transfer Money
6. Change PIN
7. Delete Account
8. Logout

📌 Project Limitations

- Account information is stored in a Python list and is lost when the program terminates.
- This is a learning project, not a real banking application.
- PINs are stored as plain text and are not securely protected.
- The application currently operates through the terminal, without a graphical interface or database.

🔮 Future Improvements

- Add permanent storage using SQLite or another database.
- Improve input validation and error handling throughout the application.
- Securely hash PINs instead of storing them as plain text.
- Add transaction history and account statements.
- Improve the code structure by separating banking operations into class methods.

👨‍💻 About

MY-BANK is a beginner-level Python project created to practice Object-Oriented Programming and develop problem-solving skills through a practical application.