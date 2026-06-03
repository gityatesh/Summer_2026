a = 1

try:
    if not isinstance(a, int):
        raise TypeError('incorrect data type, try again')
    else: print(a)
except TypeError as e:
    print(e)
        