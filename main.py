from storage import load_expenses, save_expense
from expense_manager import add_expense, view_expenses
from analytics import (
    category_report,
    monthly_report,
    category_graph,
    monthly_graph,
    payment_report,
    payment_graph
)


def menu():
    print("\nExpense Tracker")
    print("1 Add Expense")
    print("2 View Expenses")
    print("3 Category Report")
    print("4 Monthly Report")
    print("5 Category Graph")
    print("6 Monthly Graph")
    print("7 Payment Report")
    print("8 Payment Graph")
    print("9 Exit")


def main():

    expenses = load_expenses()

    while True:

        menu()

        choice = input("Select option: ")

        if choice == "1":
            expense = add_expense()
            expenses.append(expense)
            save_expense(expense)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            category_report(expenses)

        elif choice == "4":
            monthly_report(expenses)

        elif choice == "5":
            category_graph(expenses)

        elif choice == "6":
            monthly_graph(expenses)

        elif choice == "7":
            payment_report(expenses)

        elif choice == "8":
            payment_graph(expenses)

        elif choice == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()