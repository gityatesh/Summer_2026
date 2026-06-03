#to check the 1st repeated
def checkalreadyseen(arr):
    seen = set()
    for char in arr:
        if char in seen:
            return f'1st repeated transaction ID: {char}'
        else: seen.add(char)
        
transactions = [10, 5, 3, 4, 3, 5, 6]
print(checkalreadyseen(transactions))
