message = "aaabbbbccddeeeaeejhgce"
freq = {}
for char in message:
    freq[char] = freq.get(char, 0) +1
    
print(freq)
print(freq.values(), freq.keys())
print(freq.items())
ans=""
for key,values in freq.items():
    ans += key+str(values)
    
print(ans)