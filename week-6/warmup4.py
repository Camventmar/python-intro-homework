score = int(input("Insert a score between 0 and 100: "))
def is_valid_score(score):
    return 0 <= score <= 100   
if is_valid_score(score):
    print("Valid Score.")
else:
    print("Invalid score - must be between 0 and 100.")
            