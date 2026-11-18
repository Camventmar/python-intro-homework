while True:
    user = input("Enter a positive integer: ")
    if user.isdigit():
        user_input = int(user)
        if user_input > 0:
            print(f"Got it: {user_input}")
            break
        else:
            print("That's not a positve interger. Try again.")
    
    else:
        print("Invalid input. Please enter a number.")
