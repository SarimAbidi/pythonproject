import json

accounts = {}
current_account = None

def load_accounts():
    global accounts
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
        print("Accounts loaded")
    except FileNotFoundError:
        print("No saved accounts found Creating New")

def save_accounts():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)
    print("Accounts Updated")

def login_menu():
    print("\n--- Bank Account Login ---")
    print("1. Create a new account")
    print("2. Log into an existing account")
    print("3. Exit")

def main_menu():
    print(f"\n--- Welcome, {current_account}! ---")
    print("1. View balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. View transaction history")
    print("5. Logout and save")
    print("6. Exit and save")

def create_account():
    global current_account
    username = input("Create a username: ").strip()
    if username in accounts:
        print("Account already exists")
        return
    password = input("Set a password: ").strip()
    accounts[username] = {
        "password": password,
        "balance": 0.0,
        "transactions": []
    }
    current_account = username
    print(f"Account '{username}' created")

def login_account():
    global current_account
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("Account not found")
        return
    password = input("Enter your password: ").strip()
    if accounts[username]["password"] == password:
        current_account = username
        print(f"Logged into account '{username}'.")
    else:
        print("Incorrect password")

def view_balance():
    balance = accounts[current_account]["balance"]
    print(f"Current balance: ${balance:.2f}")

def deposit_money():
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("Amount must be positive")
            return
        accounts[current_account]["balance"] += amount
        accounts[current_account]["transactions"].append({"type": "Deposit", "amount": amount})
        print(f"Deposited ${amount:.2f}")
    except ValueError:
        print("Invalid input")

def withdraw_money():
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Amount must be positive")
            return
        if amount > accounts[current_account]["balance"]:
            print("Insufficient funds")
            return
        accounts[current_account]["balance"] -= amount
        accounts[current_account]["transactions"].append({"type": "Withdraw", "amount": amount})
        print(f"Withdrew ${amount:.2f}")
    except ValueError:
        print("Invalid input")

def view_transactions():
    txns = accounts[current_account]["transactions"]
    if not txns:
        print("No transactions")
        return
    print("Transaction history:")
    for i, txn in enumerate(txns, 1):
        print(f"{i}. {txn['type']} - ${txn['amount']:.2f}")

def main():
    load_accounts()
    global current_account

    while True:
        if current_account is None:
            login_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                create_account()
            elif choice == "2":
                login_account()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        else:
            main_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                view_balance()
            elif choice == "2":
                deposit_money()
            elif choice == "3":
                withdraw_money()
            elif choice == "4":
                view_transactions()
            elif choice == "5":
                save_accounts()
                print(f"Logged out of '{current_account}'.")
                current_account = None
            elif choice == "6":
                save_accounts()
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    main()
