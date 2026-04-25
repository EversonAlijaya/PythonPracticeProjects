def main():
    print("Welcome to the Expense Tracker!")
    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View All Categories")
        print("4. View Total By Category")
        print("5. View Total Expenses")
        print("6. Exit")
        
        choice = input("Choose an option (1-6):").strip()
        
        if choice == '1':
            date = input("Enter the date of the expense (YYYY-MM-DD): ").strip()
            category = input("Enter the category: ").strip().lower()
            try:
                amount = float(input("Enter the amount: ").strip())
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            description = input("Enter a description(item): ").strip()
            expenses.append((date, category, amount, description))
            print("Expense added successfully!")
        
        