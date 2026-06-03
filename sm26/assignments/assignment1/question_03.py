#checking for prime
def checkweatherprime(samplenumber):
    if samplenumber<=1:
        return 'not prime'
    elif samplenumber==2 or samplenumber==3:
        return 'number is prime'
    elif samplenumber>3:
        for i in range(2,samplenumber):
            if samplenumber%i == 0:
                return 'number is not prime'
            else: return 'number is prime'
            
pr = 48
print(checkweatherprime(pr))