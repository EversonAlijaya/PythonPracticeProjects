expenses = []
category_totals = {}
categories = set()

def add_expense(date, category, amount, description):
    expense = (date, category, amount, description)
    expenses.append(expense)
    categories.add(category)
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
    print("Expense added successfully!")

def show_total():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return
    else:
        total = sum(amount for _, _, amount, _ in expenses)
    print(f"Total Expenses: ${total:.2f}")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for date, category, amount, description in expenses:
        print(f"{date} - {category.capitalize()}: ${amount:.2f} ({description})")

def view_by_category():
    if len(category_totals) == 0:
        print("No categories recorded.")
        return
    else:
     print("\nTotal Expenses by Category:")
     for category, total in category_totals.items():
        print(f"{category.capitalize()}: ${total:.2f}")

def expenses_by_month():
    if len(expenses) == 0:
        print ("No expenses recorded.")
        return
    for date, category, amount, description in expenses:
        month = date[5:7]
        if month in category_totals:
            category_totals[month] += amount
        else:
            category_totals[month] = amount
    print("\nTotal Expenses by Month:")
    for month, total in category_totals.items():
        print(f"{month}: ${total:.2f}")

def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View By Category")
        print("4. View Total Expenses")
        print("5. Expenses by month")
        print("6. Exit")
        
        choice = input("Choose an option (1-6):").strip()
        
        if choice == '1':
            year = input("Enter the year of the expense (YYYY): ").strip()
            month = input("Enter the month of the expense (MM): ").strip()
            day = input("Enter the day of the expense (DD): ").strip()
            date = f"{year}-{month}-{day}"
            category = input("Enter the category: ").strip().lower()
            try:
                amount = float(input("Enter the amount: ").strip())
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            description = input("Enter a description(item): ").strip()
            add_expense(date, category, amount, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            view_by_category()

        elif choice == '4': 
            show_total()

        elif choice == '5':
            expenses_by_month()

        elif choice == '6':
            print("goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
main()
        