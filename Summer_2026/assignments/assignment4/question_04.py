def decode(text):
    maxchar=text[0]
    max=0
    count=0
    for i in range(1,len(text)):
        
        if text[i-1] == text[i]:
            count+=1
            if count>max:
                max = count
                maxchar = text[i]
                continue 
            else: continue
            
        else:
            count = 1
            continue
            
            
    return maxchar+str(max)

string1 = 'aaaaabbbbcccccccdddeeeeeee'
print(decode(string1))
    