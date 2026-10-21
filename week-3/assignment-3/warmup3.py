#print(not True and False): and expressions have to be true so false and false would equal false
example = not True and False
print(example)
#print(True or False and False): and is read first followed by first so expression becomes true or False - False. An or allows for the statement to be true with at least one true variable in the statement.
example2 = True or False and False
print(example2)
#print(not (5 > 3)): parenthesis is read first which equals to true; not condition inverts to false.
example3 = not (5 > 3)
print(example3)
#print(10 == 10 and 4 != 4): read as 10 is equal to 10 which is true and 4 not equal to 4 which is false so the overall statement is false since both conditions have not been met.
example4= 10 == 10 and 4 !=4
print(example4)
#print(not False or not True): read as True or False; or condition needs at least one true which it has so the statement is true
example5 = not False or not True
print(example5)