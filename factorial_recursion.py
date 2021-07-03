factodict = {}
def number(n):
    if n<=1:
        return 1
    elif n in factodict:
        return factodict[n]
    else:
        result = n * number(n-1)
        factodict[n] = result
        return result
print(number(500))
print(number(900))
print(number(1001))
