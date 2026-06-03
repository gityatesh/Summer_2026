#printing the 1st and last customer

customers = [
    ("09:08", "A"),
    ("09:11", "B"),
    ("09:03", "C"),
    ("09:04", "D")
]

firsttime, first = sorted(customers)[0]
lasttime, last = sorted(customers)[len(customers)-1]

print(f'1st customer: {first}')
print(f'Last customer: {last}')
