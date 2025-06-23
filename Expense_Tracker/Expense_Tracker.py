import csv
from datetime import datetime

def init_file():
    try:
        with open("expenses.csv", mode="x", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Description"])
    except FileExistsError:
        pass

def add_expense():
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, description])
    print("Expense added!")

def show_expenses():
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_expenses():
    total = 0
    with open("expenses.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f"Total Expenses: ₹{total}")

def monthly_expenses(month):
    total = 0
    with open("expenses.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):  # e.g., '2025-04'
                total += float(row["Amount"])
    print(f"Expenses in {month}: ₹{total}")

def menu():
    init_file()
    while True:
        print("\n1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Expenses")
        print("4. Show Monthly Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            month = input("Enter month (YYYY-MM): ")
            monthly_expenses(month)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
