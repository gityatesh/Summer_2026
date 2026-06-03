#counting vowels,consonents,numbers and special characters 
def counteverything(ourstr):
    vowels=0
    consonents=0
    numbers=0
    specialcharacters=0
    for char in ourstr:
        if char in 'aeiouAEIOU':
            vowels+=1
        elif char.isalpha() and char not in 'aeiouAEIOU':
            consonents+=1
        elif char.isdigit():
            numbers+=1
        else:
            specialcharacters+=1
            
    return f' vowels:{vowels}\n consonents: {consonents}\n numbers:{numbers}\n special characters:{specialcharacters}'
#a variable for eachas we encounter vowel or consonent etc. we'll keep updating the variable
ourtext = 'abcdADBD187@&&^&^'
print(counteverything(ourtext))