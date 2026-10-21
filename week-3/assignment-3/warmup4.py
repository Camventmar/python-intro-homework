number= int(input("Enter a number: "))
if number == 0:
    print(f"{number} is Zero.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is postive.")

if number %2 == 0:
    print(f"{number} is even.")
elif number %2 ==1: 
    print(f"{number} is odd.")