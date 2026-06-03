#to check fraud tickets
valid_tickets = [
101,102,103,104,105
]
presented = [
101,107,102,110
]

for tix in presented:
    if tix in valid_tickets:
        # print(f'{tix}: ticket is valid')
        pass
    else:
        print(f'{tix}: ticket is invalid')