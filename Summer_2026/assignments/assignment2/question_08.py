# functions on dict
students = {
"Rahul": 78,
"Aman": 92,
"Neha": 67,
"Priya": 92
}

highest = max(students.values())
lowest = min(students.values())
avg = sum(students.values())/len(students)
topper = max(students, key = students.get)

print(topper,highest,lowest,avg)
#same as ques in prev assignment