import json
import os
import hashlib
import getpass

FILE_NAME = "users.json"

def load_users():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    users = load_users()

    print("\n--- Create Account ---")

    username = input("Enter username: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return

    if username in users:
        print("That username already exists.")
        return

    password = getpass.getpass("Enter password: ")

    if len(password) < 4:
        print("Password must be at least 4 characters.")
        return

    confirm_password = getpass.getpass("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    users[username] = hash_password(password)
    save_users(users)

    print("Account created successfully!")

def login():
    users = load_users()

    print("\n--- Login ---")

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    if username not in users:
        print("Username or password is incorrect.")
        return False

    password_hash = hash_password(password)

    if users[username] == password_hash:
        print(f"\nWelcome, {username}!")
        return True

    print("Username or password is incorrect.")
    return False

def main():
    while True:
        print("\n====================")
        print("      LOGIN SYSTEM")
        print("====================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()

        elif choice == "2":
            if login():
                print("You are now logged in.")

                while True:
                    print("\n1. Logout")
                    print("2. Exit")

                    option = input("Choose: ").strip()

                    if option == "1":
                        print("Logged out successfully.")
                        break

                    elif option == "2":
                        print("Goodbye!")
                        return

                    else:
                        print("Invalid choice.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
