# Author: Ebony Cornett
# Date: September 20, 2026
# Description: Personal Expense Tracker
# # Tier Level: Base

import datetime

# Build one expense record
def build_record(description, amount, category):
    today = str(datetime.date.today())
    short_description = description[:30]
    formatted_amount = f"{amount:.2f}"
    record = ",".join([today, short_description, formatted_amount, category])
    return record

# Load saved expense records
def load_records(filename):
    records = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    fields = line.split(",")
                    records.append(fields)
    except FileNotFoundError:
        return []
    return records

# Display all expense records
def display_records(records):
    if not records:
        print("No expenses on record yet.")
        return
    print(f"{'Date':<12}{'Description':<32}{'Amount':<12}{'Category':<15}")
    print("-" * 71)
    for record in records:
        date = record[0]
        description = record[1]
        amount = record[2]
        category = record[3]
        print(f"{date:<12}{description:<32}${amount:<11}{category:<15}")

# Save one expense record to the file
def save_record(filename, record):
    with open(filename, "a") as file:
        file.write(record + "\n")

# Main program
filename = "expenses.txt"
print("===== Your Expense Records =====")
records = load_records(filename)
display_records(records)
num_expenses = int(input("\nHow many expenses do you want to add? "))        
for expense_number in range(1, num_expenses + 1):
    print(f"\n--- Expense {expense_number} ---")
    description = input("Description: ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    record = build_record(description, amount, category)
    save_record(filename, record)
print("\n===== Updated Expense Records =====")
records = load_records(filename)
display_records(records)