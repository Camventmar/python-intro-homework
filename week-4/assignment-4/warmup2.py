student = {"Name:": "Benjamin", "Grade:":"A", "Subjects:":["Math","History","English","Gym"], "Graduated:":"False"}
print(list(student.items()))
for key, value in student.items():
    print(key, value)