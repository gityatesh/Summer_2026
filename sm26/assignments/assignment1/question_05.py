#frequency of characters in a string
def countfrequency(string:str)->str:
    freq = {}
    for char in string:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    
    return freq 

string1 = 'banana'
print(countfrequency(string1))

            