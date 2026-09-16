DATA_FILE = "expenses.txt"

def load_data():
    """Reads budget and expenses from a plain text file without using json."""
    budget = 0.0
    expenses = []
    
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            if lines:
                budget = float(lines[0].strip())
                for line in lines[1:]:
                    if line.strip():
                        parts = line.strip().split("||")
                        if len(parts) == 3:
                            expenses.append({
                                "amount": float(parts[0]),
                                "item": parts[1],
                                "category": parts[2]
                            })
    except FileNotFoundError:
        pass
        
    return budget, expenses

def save_data(budget, expenses):
    """Saves data into a plain text file using manual formatting."""
    with open(DATA_FILE, "w") as file:
        file.write(f"{budget}\n")
        for item in expenses:
            file.write(f"{item['amount']}||{item['item']}||{item['category']}\n")

def set_budget():
    """Asks the user for a budget amount and updates it."""
    amount_str = input("\nEnter your monthly budget limit (e.g., 10000): ")
    try:
        amount = float(amount_str)
        budget, expenses = load_data()
        save_data(amount, expenses)
        print(f"[+] Success: Monthly budget updated to ₹{amount:.2f}")
    except ValueError:
        print("[X] Error: Please enter a valid number.")

def add_expense():
    """Loops continuously to let the user add as many expenses as they want."""
    while True:
        budget, expenses = load_data()
        
        print("\n--- ENTER NEW EXPENSE DETAILS ---")
        item_name = input("Enter item name (e.g., Dinner): ")
        category = input("Enter category (e.g., Food): ")
        amount_str = input("Enter amount spent (e.g., 250): ")
        
        try:
            amount = float(amount_str)
            expenses.append({
                "amount": amount,
                "item": item_name,
                "category": category
            })
            save_data(budget, expenses)
            print(f"[+] Success: Added ₹{amount:.2f} for '{item_name}' under [{category}]")
            
            # Budget check
            total_spent = sum(item["amount"] for item in expenses)
            if budget > 0 and total_spent > budget:
                extra = total_spent - budget
                print(f"⚠️  WARNING: You have exceeded your budget threshold by ₹{extra:.2f}!")
                
        except ValueError:
            print("[X] Error: Amount must be a valid number.")
        
        again = input("\nDo you want to add another expense? (yes/no): ").strip().lower()
        if again != 'yes' and again != 'y':
            break

def show_dashboard():
    """Displays a clean balance summary sheet in the terminal showing savings."""
    budget, expenses = load_data()
    
    total_spent = sum(item["amount"] for item in expenses)
    remaining_balance = budget - total_spent
    
    print("\n==========================================")
    print("         MY PERSONAL BUDGET REPORT        ")
    print("==========================================")
    print(f"📦 Total Budget      : ₹{budget:.2f}")
    print(f"💸 Total Money Spent : ₹{total_spent:.2f}")
    print("------------------------------------------")
    
    if remaining_balance >= 0:
        print(f"✅ TOTAL SAVINGS     : ₹{remaining_balance:.2f}")
    else:
        print(f"⚠️  BUDGET OVERAGE    : ₹{abs(remaining_balance):.2f} (Overspent!)")
        
    print("------------------------------------------")
    print("EXPENSE HISTORY:")
    
    if not expenses:
        print("  (No expenses logged yet)")
    else:
        for index, item in enumerate(expenses, 1):
            print(f" {index}. [{item['category']}] {item['item']} - ₹{item['amount']:.2f}")
    print("==========================================\n")

def menu():
    """Runs a continuous interactive menu prompt interface loop."""
    while True:
        print("\n--- BUDGET TRACKER MENU ---")
        print("1. Set Monthly Budget")
        print("2. Add New Expense(s)")
        print("3. View Summary Report")
        print("4. Exit Program")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            set_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_dashboard()
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[X] Invalid option. Please enter a number from 1 to 4.")

# CRITICAL: This execution block must be the absolute final lines of your code!
if __name__ == "__main__":
    menu()
