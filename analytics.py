import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def category_report(expenses):

    if not expenses:
        print("No data available.")
        return

    df = pd.DataFrame(expenses)

    category_totals = df.groupby("category")["amount"].sum()

    print("\nSpending by Category:\n")
    print(category_totals)


def monthly_report(expenses):

    if not expenses:
        print("No data available.")
        return

    df = pd.DataFrame(expenses)

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    monthly_totals = df.groupby("month")["amount"].sum()

    print("\nMonthly Spending Report:\n")
    print(monthly_totals)


def category_graph(expenses):

    if not expenses:
        print("No data to visualize.")
        return

    df = pd.DataFrame(expenses)

    category_totals = df.groupby("category")["amount"].sum()

    category_totals.plot(kind="bar")

    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")

    plt.tight_layout()
    plt.show()


def monthly_graph(expenses):

    if not expenses:
        print("No data to visualize.")
        return

    df = pd.DataFrame(expenses)

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    monthly_totals = df.groupby("month")["amount"].sum()

    monthly_totals.plot(marker="o")

    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount Spent")

    plt.tight_layout()
    plt.show()


def payment_report(expenses):

    if not expenses:
        print("No data available.")
        return

    df = pd.DataFrame(expenses)

    if "payment_mode" not in df.columns:
        df["payment_mode"] = "Unknown"

    payment_totals = df.groupby("payment_mode")["amount"].sum()

    print("\nSpending by Payment Method:\n")
    print(payment_totals)


def payment_graph(expenses):

    if not expenses:
        print("No data to visualize.")
        return

    df = pd.DataFrame(expenses)

    if "payment_mode" not in df.columns:
        df["payment_mode"] = "Unknown"

    payment_totals = df.groupby("payment_mode")["amount"].sum()

    payment_totals.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Payment Method Distribution")
    plt.ylabel("")

    plt.tight_layout()
    plt.show()