#checking for anagrams
def checkanagrams(st1, st2):
    st1arr = sorted(st1)
    st2arr = sorted(st2)
    if st1arr==st2arr:
        return 'yes'
    else: return 'no'
    #sort both strings and compare
    #we can also do manual sorting but i have used inbuilt feature

s1='abcd'
s2='bcdc'
print(checkanagrams(s1,s2))
    