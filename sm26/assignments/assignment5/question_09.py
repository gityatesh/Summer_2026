message = "aaabbbccccccdd"
compressed_text = ''

count = 1
for i in range(1,len(message)):
    
    if message[i-1] == message[i]:
        count+=1
    else:
        compressed_text += message[i-1]+str(count)
        count=1
compressed_text += message[i]+str(count)
    
print(compressed_text)
    
        