from storage import load_data, save_data

def set_budget(amount_str):
    try:
        amount = float(amount_str)
        budget, expenses = load_data()
        save_data(amount, expenses)
        return True, f"[+] Success: Monthly budget updated to ₹{amount:.2f}"
    except ValueError:
        return False, "[X] Error: Budget capacity value must be a valid number."

def process_expense(amount_str, item_name, category):
    try:
        amount = float(amount_str)
        budget, expenses = load_data()
        expenses.append({"amount": amount, "item": item_name, "category": category})
        save_data(budget, expenses)
        
        msg = f"[+] Success: Added ₹{amount:.2f} for '{item_name}' under [{category}]"
        total_spent = sum(item["amount"] for item in expenses)
        if budget > 0 and total_spent > budget:
            msg += f"\n⚠️ WARNING: Budget ceiling breached by ₹{total_spent - budget:.2f}!"
        return True, msg
    except ValueError:
        return False, "[X] Error: Expense cost amount must be a number."
