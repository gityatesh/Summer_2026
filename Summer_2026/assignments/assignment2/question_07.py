#to find the most frequent element in an array
def findmostfrequent(arr1):
    freq={}
    for char in arr1:
        if char in freq:
            freq[char] +=1
        else: freq[char]=1
        
    return max(freq, key=freq.get)
#using concept from the prev asisgnment i.e. counting the freq of a char and finding out max key in dict

sample = [4, 1, 2, 4, 3, 4, 2, 2, 2,4,4,4,4,4,4,4,4,4,4,4,4,4]
print(findmostfrequent(sample))