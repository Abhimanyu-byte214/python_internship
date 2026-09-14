account_number = "1234567890"
correct_pin = "1234"
balance = 10000.00

transactions = []

def display_menu():
    print("\n" + "=" * 40)
    print("           WELCOME TO PYTHON ATM")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Change PIN")
    print("6. Exit")
    print("=" * 40)

def check_balance():
    print(f"\nYour current balance is: ₹{balance:.2f}")

def deposit_money():
    global balance

    try:
        amount = float(input("\nEnter amount to deposit: ₹"))

        if amount <= 0:
            print("Invalid amount. Deposit must be greater than zero.")
            return

        balance += amount

        transactions.append(
            f"Deposited: ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New balance: ₹{balance:.2f}")

    except ValueError:
        print("Please enter a valid number.")

def withdraw_money():
    global balance

    try:
        amount = float(input("\nEnter amount to withdraw: ₹"))

        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than zero.")
            return

        if amount > balance:
            print("Insufficient balance.")
            return

        if amount > 20000:
            print("Maximum withdrawal limit is ₹20,000.")
            return

        balance -= amount

        transactions.append(
            f"Withdrawn: ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining balance: ₹{balance:.2f}")

    except ValueError:
        print("Please enter a valid number.")

def show_transactions():
    print("\n" + "-" * 40)
    print("       TRANSACTION HISTORY")
    print("-" * 40)

    if len(transactions) == 0:
        print("No transactions available.")
    else:
        for number, transaction in enumerate(transactions, start=1):
            print(f"{number}. {transaction}")

    print("-" * 40)

def change_pin():
    global correct_pin

    old_pin = input("\nEnter your current PIN: ")

    if old_pin != correct_pin:
        print("Incorrect current PIN.")
        return

    new_pin = input("Enter your new 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm your new PIN: ")

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    correct_pin = new_pin

    print("PIN changed successfully.")

print("=" * 40)
print("       WELCOME TO PYTHON ATM")
print("=" * 40)

print(f"Account Number: {account_number}")

attempts = 3
authenticated = False

while attempts > 0:

    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == correct_pin:
        authenticated = True
        print("\nLogin successful!")
        break

    attempts -= 1

    if attempts > 0:
        print(f"Incorrect PIN. {attempts} attempt(s) remaining.")
    else:
        print("Too many incorrect attempts.")
        print("Your account has been blocked temporarily.")

if authenticated:

    while True:

        display_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            show_transactions()

        elif choice == "5":
            change_pin()

        elif choice == "6":
            print("\nThank you for using Python ATM.")
            print("Please collect your card.")
            break

        else:
            print("\nInvalid choice.")
            print("Please select an option from 1 to 6.")

else:
    print("\nUnable to access your account.")
