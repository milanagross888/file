class BankAccount:
    def __init__(self, account_number, owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account balance for {self.owner_name}: ${self.balance:.2f}")

def main():
    accounts = {}

    while True:
        print("\nBanking Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            owner_name = input("Enter owner's name: ")
            if account_number not in accounts:
                accounts[account_number] = BankAccount(account_number, owner_name)
                print(f"Account for {owner_name} created successfully.")
            else:
                print("Account number already exists. Please choose a different one.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")
        elif choice == "5":
            print("Exiting the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid
