numbers = [1,2,3,4,5,1]
found = False
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            found = True
print(found)
#this code check for any duplicate in the given list
# time complexity: O(n^2) as 2 nested loops are there 
#space complexity: O(1)
#time complexity. python goes through the list 2 times in worst case
#using hash sets is a very good alternative approach

def checkforduplicates(num):
    seen = set()
    for i in num:
        if i in seen:
            return True
        else: seen.add(i)
print(checkforduplicates(numbers))

#the original code checks the whoel list even when it has already found the duplicate 
#new code immidiatly returns the result once the duplicate is found
#time complexity: O(n)
#space complexity: O(n)