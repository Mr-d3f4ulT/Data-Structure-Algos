# PYTHON BANKING PROGRAM


def print_header(title):
    print("\n" + "=" * 40)
    print(title.center(40))
    print("=" * 40)


def show_menu():
    print_header("Banking Program")
    print("1. Account Summary")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Calculate Interest")
    print("5. Apply Monthly Fee")
    print("6. Transaction History")
    print("7. Exit")


def show_account_summary(account_name, balance, transactions):
    print_header("Account Summary")
    print(f"Account holder : {account_name}")
    print(f"Current balance: ${balance:.2f}")
    print(f"Transactions   : {len(transactions)}")


def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount
        except ValueError:
            print("Please enter a valid number.")


def add_transaction(transactions, description, amount, balance):
    transactions.append({
        "description": description,
        "amount": amount,
        "balance": balance
    })


def deposit(balance, transactions):
    amount = get_amount("Enter an amount to deposit: $")
    balance += amount
    add_transaction(transactions, "Deposit", amount, balance)
    print(f"${amount:.2f} has been deposited.")
    return balance


def withdraw(balance, transactions):
    amount = get_amount("Enter an amount to withdraw: $")

    if amount > balance:
        print("Insufficient funds.")
        return balance

    balance -= amount
    add_transaction(transactions, "Withdrawal", -amount, balance)
    print(f"${amount:.2f} has been withdrawn.")
    return balance


def calculate_interest(balance, transactions):
    if balance == 0:
        print("You need a balance before interest can be added.")
        return balance

    rate = get_amount("Enter annual interest rate percentage: ")
    interest = balance * (rate / 100)
    balance += interest
    add_transaction(transactions, "Interest", interest, balance)
    print(f"${interest:.2f} interest has been added.")
    return balance


def apply_monthly_fee(balance, transactions):
    fee = get_amount("Enter monthly fee amount: $")

    if fee > balance:
        print("Fee cannot be applied because the account has insufficient funds.")
        return balance

    balance -= fee
    add_transaction(transactions, "Monthly Fee", -fee, balance)
    print(f"${fee:.2f} monthly fee has been applied.")
    return balance


def show_transaction_history(transactions):
    print_header("Transaction History")

    if not transactions:
        print("No transactions yet.")
        return

    print(f"{'No.':<5}{'Type':<16}{'Amount':>14}{'Balance':>14}")
    print("-" * 49)

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index:<5}"
            f"{transaction['description']:<16}"
            f"{format_money(transaction['amount']):>14}"
            f"{format_money(transaction['balance']):>14}"
        )


def format_money(amount):
    if amount < 0:
        return f"-${abs(amount):.2f}"

    return f"${amount:.2f}"


def main():
    print_header("Welcome")
    account_name = input("Enter account holder name: ").strip()

    if not account_name:
        account_name = "Guest"

    balance = 0
    transactions = []
    is_running = True

    while is_running:
        show_menu()

        choice = input("Enter your choice (1-7): ")

        match choice:
            case "1":
                show_account_summary(account_name, balance, transactions)
            case "2":
                balance = deposit(balance, transactions)
            case "3":
                balance = withdraw(balance, transactions)
            case "4":
                balance = calculate_interest(balance, transactions)
            case "5":
                balance = apply_monthly_fee(balance, transactions)
            case "6":
                show_transaction_history(transactions)
            case "7":
                is_running = False
                print("Thank you! Have a nice day.")
            case _:
                print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
