#to find first non repeating character
def findfirstnonrepeating(ourstr:str)->str:
    freq={}
    for char in ourstr:
        if char in freq:
            freq[char]+=1
        else: freq[char]=1
    #used to similar method to count frequency of characters in a string
         
    for char in freq:
        if char in freq and freq[char]==1:
            return char
    return 'no repeating character found'
    #used another nested loop to find the first non repeating character in the string

a = 'swiss'
print(findfirstnonrepeating(a))