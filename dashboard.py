from storage import load_data

def compile_report():
    budget, expenses = load_data()
    total_spent = sum(item["amount"] for item in expenses)
    balance = budget - total_spent
    
    report = []
    report.append("\n==========================================")
    report.append("         MY PERSONAL BUDGET REPORT        ")
    report.append("==========================================")
    report.append(f"📦 Total Budget      : ₹{budget:.2f}")
    report.append(f"💸 Total Money Spent : ₹{total_spent:.2f}")
    report.append("------------------------------------------")
    
    if balance >= 0:
        report.append(f"✅ TOTAL SAVINGS     : ₹{balance:.2f}")
    else:
        report.append(f"⚠️ BUDGET OVERAGE    : ₹{abs(balance):.2f} (Overspent!)")
        
    report.append("------------------------------------------")
    report.append("EXPENSE HISTORY:")
    
    if not expenses:
        report.append("  (No expenses logged yet)")
    else:
        for idx, item in enumerate(expenses, 1):
            report.append(f" {idx}. [{item['category']}] {item['item']} - ₹{item['amount']:.2f}")
    report.append("==========================================\n")
    return "\n".join(report)
