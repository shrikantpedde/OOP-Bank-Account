import pandas as pd
import datetime

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = float(initial_balance)
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._add_transaction("Deposit", amount)
            print(f"Successfully deposited ${amount}. Current Balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._add_transaction("Withdrawal", amount)
            print(f"Successfully withdrew ${amount}. Current Balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be greater than zero.")

    def _add_transaction(self, tx_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "Account_Number": self.account_number,
            "Holder_Name": self.holder_name,
            "Type": tx_type,
            "Amount": amount,
            "Balance_After": self.balance,
            "Timestamp": timestamp
        })

    def export_to_csv(self, filename="transactions.csv"):
        df = pd.DataFrame(self.transactions)
        df.to_csv(filename, index=False)
        print(f"Transactions saved to {filename}")

# --- Demo & Analysis Script ---
if __name__ == "__main__":
    # Create Bank Account Instance
    acc = BankAccount(account_number="ACC1001", holder_name="Shrikant", initial_balance=5000.0)
    
    # Perform OOP Transactions
    acc.deposit(1500)
    acc.withdraw(700)
    acc.withdraw(300)
    acc.deposit(2000)
    
    # Export history to CSV
    acc.export_to_csv("bank_transactions.csv")

    # --- Dataset Analysis using Pandas ---
    print("\n--- PANDAS DATASET ANALYSIS ---")
    df = pd.read_csv("bank_transactions.csv")
    
    # Display summary statistics
    print("\n1. Data Head:")
    print(df.head())
    
    print("\n2. Total Volume Processed:")
    print(f"${df['Amount'].sum()}")
    
    print("\n3. Transactions Count by Type:")
    print(df['Type'].value_counts())
    
    print("\n4. Summary Statistics:")
    print(df.describe())