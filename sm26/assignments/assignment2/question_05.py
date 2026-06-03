#find the missing number 
def findmissingnumber(arr1):
    newarr = []
    for i in range(1,len(arr1)+1):
        newarr.append(i)
        
    return set(newarr)-set(arr1)

#make a new array with 1,N elements and subtract both 

sample = [1, 2, 3, 5, 6]
print(findmissingnumber(sample))
    
    
        