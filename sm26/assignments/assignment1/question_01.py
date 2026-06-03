#reversing a string
def reversethestring(string: str) -> str:
    reversedstring = ""
    for i in range(len(string) - 1, -1, -1): #backward loop
        reversedstring +=string[i]
    print(reversedstring)
    
string1 = 7878
reversethestring(string1)