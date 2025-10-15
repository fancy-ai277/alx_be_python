# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        print("Operations: deposit, withdraw, balance")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == "deposit" and len(sys.argv) == 3:
        amount = float(sys.argv[2])
        account.deposit(amount)
        account.display_balance()

    elif operation == "withdraw" and len(sys.argv) == 3:
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            account.display_balance()
        else:
            print("Insufficient funds.")

    elif operation == "balance":
        account.display_balance()

    else:
        print("Invalid operation or missing amount.")

if __name__ == "__main__":
    main()
