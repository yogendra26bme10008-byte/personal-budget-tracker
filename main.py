import sys
from core import set_budget, process_expense
from dashboard import compile_report

def run_menu():
    while True:
        print("\n--- BUDGET TRACKER MENU ---")
        print("1. Set Monthly Budget")
        print("2. Add New Expense(s)")
        print("3. View Summary Report")
        print("4. Exit Program")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            amt = input("Enter budget limit: ")
            _, msg = set_budget(amt)
            print(msg)
        elif choice == "2":
            while True:
                item = input("Enter item name: ")
                cat = input("Enter category: ")
                amt = input("Enter amount spent: ")
                _, msg = process_expense(amt, item, cat)
                print(msg)
                again = input("\nAdd another? (yes/no): ").strip().lower()
                if again not in ['yes', 'y']:
                    break
        elif choice == "3":
            print(compile_report())
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[X] Invalid selection.")

if __name__ == "__main__":
    run_menu()
