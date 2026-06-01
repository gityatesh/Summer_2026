students = [
("Rahul","Python"),
("Rahul","SQL"),
("Aman","Python"),
("Neha","Django"),
("Aman","SQL")
]

report = {}
for student, subject in students:
    report.setdefault(student, []).append(subject)  #creating additional list inside the dict 

print(report)
