import os
print(os.getcwd())
import os
if os.path.exists("expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
import os
path = os.path.join("data", "expenses.csv")
print(path)
import os
files = os.listdir("data")
print(files)