class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("⚠️ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds.")
        elif amount <= 0:
            print("⚠️ Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def get_balance(self):
        print(f"💰 Current balance: ₹{self.balance}")

# Create account
owner_name = input("Enter account holder's name: ")
initial_money = float(input("Enter initial deposit amount: "))
account = BankAccount(owner_name, initial_money)

# Menu loop
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.get_balance()
    elif choice == "4":
        print("👋 Thank you for banking with us!")
        break
    else:
        print("⚠️ Invalid choice. Please select a valid option.")