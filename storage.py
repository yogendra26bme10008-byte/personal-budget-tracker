import os
from config import DATA_FILE, SEPARATOR

def load_data():
    """Reads budget and expenses from plain text data file."""
    budget = 0.0
    expenses = []
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            if lines:
                budget = float(lines[0].strip())
                for line in lines[1:]:
                    if line.strip():
                        parts = line.strip().split(SEPARATOR)
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
    """Saves formatted budget tracking lines to storage stream."""
    with open(DATA_FILE, "w") as file:
        file.write(f"{budget}\n")
        for item in expenses:
            file.write(f"{item['amount']}{SEPARATOR}{item['item']}{SEPARATOR}{item['category']}\n")
