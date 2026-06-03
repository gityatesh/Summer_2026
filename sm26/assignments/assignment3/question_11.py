results = [
("Rahul",78),
("Aman",92),
("Neha",67),
("Priya",92),
("Rohit",85)
]

markslist = {}
for student, marks in results:
    markslist[student] = markslist.get(student, 0) + marks
 
print(max(markslist.values()))   
print(min(markslist.values()))   
print(sum(markslist.values())/ len(results))
print(max(markslist, key = markslist.get))
