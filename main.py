                                                        #Expense Tracker
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    #Add Expenses
    def add_expense(self, item, amount):
        self.expenses.append((item, amount))
        print(f"Expense '{item}' of ${amount} added successfully.")

    #View Expenses
    def view_expenses(self):
        if self.expenses:
            print("List of Expenses:")
            for i, (item, amount) in enumerate(self.expenses, 1):
                print(f"{i}. {item}: ${amount}")
        else:
            print("No expenses recorded yet.")

    #Delete Expenses
    def delete_expense(self, index):
        if 1 <= index <= len(self.expenses):
            item, amount = self.expenses.pop(index - 1)
            print(f"Expense '{item}' of ${amount} deleted successfully.")
        else:
            print("Invalid expense index.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item name: ")
            amount = float(input("Enter the amount spent: $"))
            tracker.add_expense(item, amount)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            index = int(input("Enter the index of the expense to delete: "))
            tracker.delete_expense(index)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
