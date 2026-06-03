students = { '“Rahul”': 78, '“Aman”': 92, '“Neha”': 67 }
print(students.values())
highest = max(students.values())
lowest = min(students.values())
average = (sum(students.values())/len(students))
beststudent = max(students, key=students.get)
print(beststudent)
print(average)