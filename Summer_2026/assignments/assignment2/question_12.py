#calculator
def calculator(n1:int,n2:int,op):
    if not isinstance(n1,(int,float))or not isinstance(n2,(int, float)):
        raise ValueError ('Invalid inputs. please try again')
    if op not in ('+', '-','*','/'):
        raise ValueError ('invalid operator')
    if op=='+':
        return n1+n2
    if op=='-':
        return n1-n2
    if op=='*':
        return n1*n2
    if op=='/':
    
            if n2==0:
                raise ValueError('invalid denominator. please try again')
            else:
                return n1/n2
                
                    
#raising 3 valueerrors in our while code and then print them if any of the condition unsatisfies

n1=int(input())
n2=int(input())
op = input()
try:
    print(calculator(n1,n2,op))
except ValueError as e:
    print(e)