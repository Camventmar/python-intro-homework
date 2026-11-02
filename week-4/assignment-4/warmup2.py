student = {"name": "Benjamin", "grade":"A", "subjects":["Math","History","English","Gym"]}
print(list(student.items()))
for key, value in student.items():
    print(key, value)
student["graduated"] = False
print(list(student.items()))