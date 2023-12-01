import os

user_data = {}
account_numbers = []

def load_account_number():
    try:
        with open("account_number.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 111111  

def save_account_number(acc):
    with open("account_number.txt", "w") as file:
        file.write(str(acc))

def calculate_age(dob):
    current_year = 2023
    current_month = 10
    current_day = 26 
    dob_month, dob_day, dob_year = map(int, dob.split('/'))
    age = current_year - dob_year

    if current_month < dob_month or (current_month == dob_month and current_day < dob_day):
        age -= 1

    return age

def generate_account_number(acc):
    acc = acc + 1
    save_account_number(acc)
    return str(acc)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_home_screen():
    clear_screen()
    print("****************** Welcome to the ATM Simulation ******************")
    print("1. New User")
    print("2. Existing User")
    print("3. Exit")

def display_existing_user_screen(account_number):
    clear_screen()
    print(f"****************** ATM Menu (Account Number: {account_number}) ******************")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Reset Password")
    print("5. Exit")


def register_new_user(acc):
    clear_screen()
    print("****************** New User Registration ******************")
    name = input("Enter your name: ")
    mobile_number = input("Enter your mobile number: ")
    address = input("Enter your address: ")
    dob = input("Enter your date of birth (MM/DD/YYYY): ")  
    initial_deposit = float(input("Enter the initial deposit amount: "))
    password = input("Set a password for your account: ")

    age = calculate_age(dob) 

    if age >= 18:
        account_number = str(generate_account_number(acc))

        user_data[account_number] = {
            "Name": name,
            "Mobile Number": mobile_number,
            "Address": address,
            "Age": age,  
            "Balance": initial_deposit,
            "Password": password,
            "Date of Birth": dob
        }

        account_numbers.append(account_number)

        with open("user_data.txt", "w") as file:
            for acc_number, data in user_data.items():
                file.write(f"Account Number: {acc_number}\n")
                file.write(f"Name: {data['Name']}\n")
                file.write(f"Mobile Number: {data['Mobile Number']}\n")
                file.write(f"Address: {data['Address']}\n")
                file.write(f"Age: {data['Age']} years\n")  
                file.write(f"Date of Birth: {data['Date of Birth']}\n")  
                file.write(f"Balance: Rs {data['Balance']:.2f}\n")
                file.write("Password: ********\n")
                file.write("=" * 50 + "\n")

        print(f"Account created successfully! Your account number is: {account_number}")
    else:
        print("Sorry, you are under 18 years old. Registration is not allowed.")

    input("Press Enter to continue...")


def main():
    while True:
        display_home_screen()
        user_choice = input("Are you a new user or an existing user? (1/2/3): ")

        if user_choice == "1":
            acc=load_account_number()
            register_new_user(acc)
        elif user_choice == "2":
            account_number = login_user()
            if account_number is not None:
                while True:
                    display_existing_user_screen(account_number)
                    choice = input("Enter your choice (1/2/3/4/5): ")

                    if choice == "1":
                        print(f"Balance: Rs {user_data[account_number]['Balance']:.2f}")
                        input("Press Enter to continue...")
                    elif choice == "2":
                        amount = float(input("Enter the amount to deposit: "))
                        user_data[account_number]['Balance'] += amount
                        print(f"Deposited Rs {amount:.2f}. New balance: Rs {user_data[account_number]['Balance']:.2f}")
                        update_user_data_file()
                        input("Press Enter to continue...")
                    elif choice == "3":
                        amount = float(input("Enter the amount to withdraw: "))
                        if amount > user_data[account_number]['Balance']:
                            print("Insufficient funds.")
                            input("Press Enter to continue...")
                        else:
                            user_data[account_number]['Balance'] -= amount
                            print(f"Withdrew Rs {amount:.2f}. New balance: Rs {user_data[account_number]['Balance']:.2f}")
                            update_user_data_file()
                            input("Press Enter to continue...")
                    elif choice == "4":
                        reset_password(account_number)
                    elif choice == "5":
                        print("Exiting ATM menu...")
                        break
                    else:
                        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
                        input("Press Enter to continue...")
        elif user_choice == "3":
            print("Thank you for using the ATM Simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")
            input("Press Enter to continue...")


def login_user():
    clear_screen()
    print("****************** User Login ******************")
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    if account_number in user_data and user_data[account_number]["Password"] == password:
        print("Login successful!")
        input("Press Enter to continue to the ATM menu...")
        return account_number
    else:
        print("Login failed. Please check your account number and password.")
        input("Press Enter to continue...")


def reset_password(account_number):
    clear_screen()
    print("****************** Password Reset ******************")
    
    
    current_password = input("Enter your current password: ")
    dob = input("Enter your date of birth (MM/DD/YYYY): ")
    
    
    if user_data[account_number]["Password"] == current_password and user_data[account_number]["Date of Birth"] == dob:
        
        new_password = input("Enter your new password: ")
        confirm_password = input("Enter the new password again to confirm: ")
        
        
        if new_password == confirm_password:
            
            user_data[account_number]["Password"] = new_password
            
            update_user_data_file()
            print("Password reset successful.")
        else:
            print("New password and confirmation do not match. Password reset failed.")
    else:
        print("Current password or date of birth is incorrect. Password reset failed.")
    
    input("Press Enter to continue...")


def update_user_data_file():
    with open("user_data.txt", "w") as file:
        for acc_number, data in user_data.items():
            file.write(f"Account Number: {acc_number}\n")
            file.write(f"Name: {data['Name']}\n")
            file.write(f"Mobile Number: {data['Mobile Number']}\n")
            file.write(f"Address: {data['Address']}\n")
            file.write(f"Age: {data['Age']} years\n")  
            file.write(f"Date of Birth: {data['Date of Birth']}\n")  
            file.write(f"Balance: Rs {data['Balance']:.2f}\n")
            file.write("Password: ********\n")
            file.write("=" * 50 + "\n")