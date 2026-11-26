import csv
import os
# Locate File
path = os.path.join("data", "expenses.csv")
if not os.path.exists(path):
    print("error: expenses.csv not found.")
# Read file and List Conversion
with open(path, 'r') as file:
    reader = csv.DictReader(file)
    expenses = list(reader)
#for row in expenses:
    #print(row['date'],row['category'],row['description'],row['amount'])
for item in expenses:
    item['amount'] = float(item['amount'])
# Filter for Food Category
food_filter = [item for item in expenses if item['category'] == 'Food']
print(food_filter)
# Total of Food 
total_value = sum(item['amount'] for item in food_filter)
print(f"Total Food Cost: ${total_value:.2f}")
# Convert to Text File 
from datetime import datetime
now = datetime.now()
time_conversion = now.strftime("%B %d,%Y")
with open('food_report.txt', 'w') as file:
    file.write(f"Food Expense Report — generated {time_conversion}\n")
    for item in food_filter:
        file.write(f"{item['date']}: ${item['amount']:.2f}\n")
    file.write(f"Total: ${total_value:.2f}\n")