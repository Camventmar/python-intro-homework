interger = int(input("Enter a positive integer: "))
while interger <= 0:
    print("That's not a positve interger. Try again.")
    interger = int(input("Enter a positive integer: "))
print(f"Got it: {interger}")