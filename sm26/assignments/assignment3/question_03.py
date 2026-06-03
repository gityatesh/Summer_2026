votes = [
"A",
"B",
"A",
"C",
"A",
"B",
"D"
]

votecount = {}
for vote in votes:
    votecount[vote] = votecount.get(vote, 0)+1
    
print(f'total votes for candidates = {votecount}')
print(f'winner: {max(votecount, key = votecount.get)}')