#What the error message said:
# TypeError: can't multiply sequence by non-int of type 'str'
#What caused it:
# The input function returns a string, and you cannot multiply strings in Python.
#How I fixed it:
# ("Your numbers multiplied together equal: " + str(int(number1) * int(number2)))
number1 = input("Pick a number between 1 and 7: ")
number2 = input("Pick another number between 1 and 7: ")
print("Your numbers multiplied together equal: " + str(int(number1) * int(number2)))