scores = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

as1=sum(scores[0])
as2=sum(scores[1])
as3=sum(scores[2])

print(as1,as2,as3)

for i,row in enumerate(scores, start=1):
    print(i, sum(row))