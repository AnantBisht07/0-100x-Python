expenses = []  # List to store expenses

# it will run until user chooses to exit...
while True:
    print("----Finance Tracker----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spend")
    print("4. Filter by Category")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting Finance Tracker. Goodbye!")
        break

    # Add Expense — no empty-check needed; adding is always allowed
    elif choice == '1':
        expense_name = input("Enter your expense name: ")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ").lower()
        expenses.append({"name": expense_name, "amount": amount, "category": category})
        print(f"Expense added successfully: {expense_name}")

    # View expenses — HERE is where the empty-check belongs
    elif choice == '2':
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for i, e in enumerate(expenses, start=1):
                print(f"{i}. {e['name']} - ${e['amount']} Category: {e['category']}")

    # Total spend
    elif choice == '3':
        total = sum(e["amount"] for e in expenses)
        print(f"Total spend: ${total}")

    # Filter by Category
    elif choice == '4':
        filter_category = input("Enter the category to filter by: ")
        filtered_expense = [e for e in expenses if e['category'] == filter_category.lower()]
        if not filtered_expense:
            print(f"No expenses found in category '{filter_category}'.")
        else:
            print(f"Expenses in category '{filter_category}':")
            for i, e in enumerate(filtered_expense, start=1):
                print(f"{i}. {e['name']} - ${e['amount']} Category: {e['category']}")

    else:
        print("Invalid choice, try 1-5.")


"""
List comp. -- 
list = ["apple", "pen", "bottle", "notebook", "mango", "banana", "grapes"]
user came - added food(Category) 
this user wants all the food items... (and in a list)

new_list = [all food items]

so we do iteration from list only with list comprehension and filter the items based on the category "food".

iteration - i, now i want to create a new list to show to the user. 
"""