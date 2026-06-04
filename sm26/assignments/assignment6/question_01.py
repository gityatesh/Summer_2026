# to find the 1st fraudlent id
def findfraud(list):
    s=set()
    for char in list:       #O(n)
        if char not in s:
            s.add(char)     #O(1)
            continue
        else:
            return print(f'1st fraudlent id: {char}')
    return print('no fraudlent id found')      
transactions = [45, 12, 78, 78, 34, 12, 90, 45]
findfraud(transactions)
#time complexity: O(n)
#space complexity: O(n)


# def findfraud2(list):
#     for i in range(len(list)): O(n)
#         for j in range(i):     O(n)
#             if list[j]== list[i]:
#                 return print(f'Fraud found: {list[j]}')
#             else: continue
#     return print('fraud not found')
# transactions = [45, 12, 78, 34, 12, 90, 45]
# findfraud2(transactions)
#time complexity: O(n^2)
#space complexity: O(1)

