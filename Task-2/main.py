
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    """Load previously saved expenses."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            expenses = json.load(file)

        if isinstance(expenses, list):
            return expenses

        print("Warning: Invalid expense data.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved expenses.")
        return []


def save_expenses(expenses):
    """Save expenses to a JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        return True
    except OSError:
        print("Error: Could not save expenses.")
        return False


def add_expense(expenses):
    """Ask the user for an expense amount and save it."""
    try:
        amount = float(input("Enter expense amount (₹): ").strip())

        if amount <= 0:
            print("Please enter an amount greater than zero.")
            return

        description = input(
            "Enter expense description (or press Enter to skip): "
        ).strip()

        expense = {
            "amount": round(amount, 2),
            "description": description or "General expense"
        }

        expenses.append(expense)

        if save_expenses(expenses):
            print(f"Expense added successfully: ₹{amount:.2f}")

    except ValueError:
        print("Invalid amount. Please enter a number, such as 100 or 50.50.")


def view_expenses(expenses):
    """Display all recorded expenses."""
    print("\n" + "=" * 50)
    print("                 EXPENSE HISTORY")
    print("=" * 50)

    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']} - "
            f"₹{expense['amount']:.2f}"
        )

    print("-" * 50)
    print(f"TOTAL SPENT: ₹{calculate_total(expenses):.2f}")
    print("=" * 50)


def calculate_total(expenses):
    """Calculate the total using an accumulator."""
    total = 0.0

    for expense in expenses:
        total += expense["amount"]

    return round(total, 2)


def main():
    """Run the Expense Tracker application."""
    expenses = load_expenses()

   
    print("         PYTHON EXPENSE TRACKER")
  

    while True:
        print("\n1. Add an expense")
        print("2. View all expenses and total")
        print("3. View total spent")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"\nYour total spending is ₹{total:.2f}")

        elif choice == "4":
            print("Thank you for using the Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")


if __name__ == "__main__":
    main()
