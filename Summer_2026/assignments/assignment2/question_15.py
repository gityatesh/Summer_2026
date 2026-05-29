#finding pair
def findpair(ourarr, key):
    pairs=[]
    for i in range(len(ourarr)):
        for j in range(i+1, len(ourarr)):
            if ourarr[i]+ourarr[j]==key:
                pairs.append(ourarr[i])
                pairs.append(ourarr[j])
            else: continue
    
    return pairs

sample=[2,7,11,5,4]
key=9
print(findpair(sample, key))