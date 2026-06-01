all_seats = [
"S1","S2","S3","S4","S5","S6"
]
reserved = [
"S1","S2","S3","S5"
]

vacantseats = set(all_seats) - set(reserved)
print(vacantseats)