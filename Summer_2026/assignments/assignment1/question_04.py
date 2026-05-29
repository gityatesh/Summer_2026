#moving zeroes to end
def moving0stoend(ourarr:int)->int:
    for i in range(len(ourarr)):
        if ourarr[i]==0:
            ourarr.remove(ourarr[i])
            ourarr.append(ourarr[i])
        else: continue 
        
    return ourarr
        
array1 = [1,0,2,0,4,0,5] 
print(moving0stoend(array1))
