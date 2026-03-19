from datetime import datetime


def validate_date(date_string):
    """Validate date format YYYY-MM-DD"""
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_expense():
    """Prompt user to enter a new expense"""

    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if validate_date(date):
            break
        print("Invalid date format. Try again.")

    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    payment_mode = input("Enter payment method (Cash/Card/UPI): ")

    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "payment_mode": payment_mode,
        "description": description
    }

    return expense


def view_expenses(expenses):
    """Display all stored expenses"""

    if not expenses:
        print("\nNo expenses recorded.\n")
        return

    print("\nExpense History\n")

    for i, exp in enumerate(expenses, start=1):

        payment = exp.get("payment_mode", "Unknown")

        print(
            f"{i}. {exp['date']} | {exp['category']} | ${exp['amount']:.2f} | {payment} | {exp['description']}"
        )