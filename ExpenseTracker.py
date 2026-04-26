expenses = []
category_totals = {}
monthly_totals = {}
categories = set()

def add_expense(monthyear,day, category, amount, description):
    expense = (monthyear, day, category, amount, description)
    expenses.append(expense)
    categories.add(category)
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
    if monthyear in monthly_totals:
        monthly_totals[monthyear] += amount
    else:
        monthly_totals[monthyear] = amount
    print("Expense added successfully!")

def show_total():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return
    else:
        total = sum(amount for _, _, _, amount, _ in expenses)
    print(f"Total Expenses: ${total:.2f}")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for monthyear, day, category, amount, description in expenses:
        print(f"{monthyear}-{day} - {category.capitalize()}: ${amount:.2f} ({description})")

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
    else:
        print("\nTotal Expenses by Month:")
        for monthyear, total in monthly_totals.items():
            print(f"{monthyear}: ${total:.2f}")

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
            if not year.isdigit() or len(year) != 4:
                print("Invalid year. Please enter a 4-digit year.")
                continue
            month = input("Enter the month of the expense: ").strip()
            if not month.isdigit() or not 1 <= int(month) <= 12:
                print("Invalid month. Please enter a number between 01 and 12.")
                continue
            elif len(month) == 1:
                month = f"0{month}"
            day = input("Enter the day of the expense: ").strip()
            if not day.isdigit() or not 1 <= int(day) <= 31:
                print("Invalid day. Please enter a number between 01 and 31.")
                continue
            elif len(day) == 1:
                day = f"0{day}"
            monthyear = f"{year}-{month}"
            category = input("Enter the category: ").strip().lower()
            try:
                amount = float(input("Enter the amount: ").strip())
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            description = input("Enter a description(item): ").strip()
            add_expense(monthyear,day, category, amount, description)

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
        