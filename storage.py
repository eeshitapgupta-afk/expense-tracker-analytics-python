import csv
from pathlib import Path

FILE_PATH = Path("expenses.csv")
FIELDS = ["date", "category", "amount", "payment_mode", "description"]


def load_expenses():
    """Load expenses from CSV and return list of dictionaries."""
    
    expenses = []

    if not FILE_PATH.exists():
        return expenses

    try:
        with FILE_PATH.open("r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:

                # Handle old CSV format (4 columns)
                if len(row) == 4:
                    date, category, amount, description = row
                    payment_mode = "Unknown"

                # Handle new CSV format (5 columns)
                elif len(row) == 5:
                    date, category, amount, payment_mode, description = row

                else:
                    print(f"Skipping invalid row: {row}")
                    continue

                try:
                    expense = {
                        "date": date,
                        "category": category,
                        "amount": float(amount),
                        "payment_mode": payment_mode,
                        "description": description
                    }

                    expenses.append(expense)

                except ValueError:
                    print(f"Skipping invalid row: {row}")

    except Exception as e:
        print(f"Error reading file: {e}")

    return expenses


def save_expense(expense):
    """Append a single expense to the CSV file."""

    try:
        with FILE_PATH.open("a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(expense)

    except Exception as e:
        print(f"Error saving expense: {e}")