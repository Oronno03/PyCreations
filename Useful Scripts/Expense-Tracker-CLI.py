import json
import os
from datetime import datetime

FILE_PATH = "expenses.json"


class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(FILE_PATH, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(FILE_PATH, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, description, amount, date, category):
        self.expenses.append(
            {
                "description": description,
                "amount": amount,
                "date": date,
                "category": category,
            }
        )
        self.save_expenses()
        print(f"Added {category} expense: {description} - ${amount} on {date}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        for expense in self.expenses:
            print(
                f"{expense['date']} - {expense['description']} [{expense['category']}]: ${expense['amount']}"
            )
        input("Press Enter to return to the main menu...")

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        print(f"Total Expenses: ${total}")
        input("Press Enter to return to the main menu...")

    def filter_expenses(self, start_date, end_date, min_amount=None, max_amount=None):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        filtered = [
            expense
            for expense in self.expenses
            if start <= datetime.strptime(expense["date"], "%Y-%m-%d") <= end
            and (min_amount is None or expense["amount"] >= min_amount)
            and (max_amount is None or expense["amount"] <= max_amount)
        ]
        if not filtered:
            print("No expenses match the criteria.")
        for expense in filtered:
            print(
                f"{expense['date']} - {expense['description']} [{expense['category']}]: ${expense['amount']}"
            )
        input("Press Enter to return to the main menu...")

    def delete_expense(self, date, description):
        initial_count = len(self.expenses)
        self.expenses = [
            expense
            for expense in self.expenses
            if not (expense["date"] == date and expense["description"] == description)
        ]
        self.save_expenses()
        if len(self.expenses) < initial_count:
            print(f"Deleted expense: {description} on {date}")
        else:
            print("No matching expense found.")
        input("Press Enter to return to the main menu...")

    def summary(self):
        categories = {"Money In": 0, "Money Out": 0}
        for expense in self.expenses:
            if expense["category"] in categories:
                categories[expense["category"]] += expense["amount"]

        total_expenses = sum(expense["amount"] for expense in self.expenses)
        print(f"Summary:")
        print(f"  Total Money In: ${categories['Money In']}")
        print(f"  Total Money Out: ${categories['Money Out']}")
        print(f"  Net Total: ${categories['Money In'] - categories['Money Out']}")
        input("Press Enter to return to the main menu...")

    def display_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter Expenses")
        print("5. Delete Expense")
        print("6. Summary")
        print("7. Quit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                description = input("Description: ")
                amount = float(input("Amount: "))
                date = input("Date (YYYY-MM-DD, leave blank for today): ")
                if not date:
                    date = datetime.now().strftime("%Y-%m-%d")
                print("Select category:")
                print("1. Money In")
                print("2. Money Out")
                category_choice = input("Select an option (1 or 2): ").strip()
                if category_choice == "1":
                    category = "Money In"
                elif category_choice == "2":
                    category = "Money Out"
                else:
                    print("Invalid category choice. Defaulting to Money Out.")
                    category = "Money Out"
                self.add_expense(description, amount, date, category)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.total_expenses()
            elif choice == "4":
                start_date = input(
                    "Start Date (YYYY-MM-DD, leave blank for no start date): "
                )
                end_date = input("End Date (YYYY-MM-DD, leave blank for no end date): ")
                min_amount = input("Min Amount (Leave blank for no minimum): ")
                max_amount = input("Max Amount (Leave blank for no maximum): ")
                start_date = start_date if start_date else "0000-00-00"
                end_date = end_date if end_date else "9999-12-31"
                min_amount = float(min_amount) if min_amount else None
                max_amount = float(max_amount) if max_amount else None
                self.filter_expenses(start_date, end_date, min_amount, max_amount)
            elif choice == "5":
                date = input("Date of Expense (YYYY-MM-DD): ")
                description = input("Description of Expense: ")
                self.delete_expense(date, description)
            elif choice == "6":
                self.summary()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.main()
