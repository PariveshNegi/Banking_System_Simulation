<h1 align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com/?lines=Banking+System!&center=true&size=30">
  </a>
</h1>

## Overview

The ATM Simulation project is a Python-based application that simulates basic functionalities of an ATM system. It allows users to create accounts, check balances, deposit and withdraw money, and reset passwords. This project is designed to provide a simple, interactive experience that mimics real-world ATM operations.

## Features

- **New User Registration:** Users can register as new account holders, providing personal details and an initial deposit.
- **User Login:** Existing users can log in using their account number and password to access the ATM menu.
- **Check Balance:** Users can view their current account balance.
- **Deposit Money:** Users can deposit money into their account.
- **Withdraw Money:** Users can withdraw money from their account, provided they have sufficient funds.
- **Password Reset:** Users can reset their account password after verifying their identity with their date of birth.

## File Handling

- **User Data Storage:** User data, including account details and balances, is stored in a text file (`user_data.txt`) to ensure persistence between sessions.
- **Account Number Storage:** The current account number is stored in a separate text file (`account_number.txt`) to maintain continuity for newly created accounts.

## Getting Started

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/YourUsername/ATM_Simulation.git
   ```
2. Run the application:
```bash
python atm_simulation.py
```
3. Follow the on-screen instructions to interact with the ATM Simulation.

## Usage
1. Home Screen:
Choose whether you are a new user, an existing user, or if you wish to exit the application.

2. New User Registration:
Enter your personal details, including name, mobile number, address, date of birth, and an initial deposit amount.
Set a password for your account.
Upon successful registration, you will receive a unique account number.

3. Existing User Login:
Log in using your account number and password.
Access the ATM menu where you can check your balance, deposit or withdraw money, and reset your password.

4. ATM Menu:
Check Balance: View your current balance.
Deposit Money: Add funds to your account.
Withdraw Money: Withdraw funds from your account.
Reset Password: Change your account password after verifying your identity.
Exit: Log out and return to the home screen.

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## Acknowledgments
This project was developed by Parivesh singh negi. It's a simple simulation of an ATM system, designed for educational purposes.
