def is_valid_score(score):
    if 0 <= score <= 100:
        return True
    else:
        return False
for score in [45,-7,203]:
    if is_valid_score(score):
        print("Valid Score.")
    else:
        print("Invalid score - must be between 0 and 100.")
        