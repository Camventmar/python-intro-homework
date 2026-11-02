students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
#Top_Scorer
max_score = 0
top_scorer = ""
for student in students:
    if student["score"] > max_score:
        max_score = student["score"]
        top_scorer = student["name"]
print(f"Top Scorer: {top_scorer} ({max_score})")
#Class_Average
total = 0
for student in students:
    total += student["score"]
average = total/ len(students)
print(f"Class average: {average}")
#Subjects_Offered
subject_offered = set()
for student in students:
    subject_offered.add(student["subject"])
print(f"Subjects Offered: {subject_offered}")
#High_Scorers
high_scorers = []
for student in students:
    if student["score"] >= 75:
        high_scorers.append(student["name"])
print(f"High Scorers: {high_scorers}")