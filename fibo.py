'''Binet formula to find nth fibonacci number'''
n =  int(input())
n = n-1

phi1 = (1+5**(0.5))/2
phi2 = (-1/phi1)
sum = ((phi1)**n - (phi2)**n)/5**(0.5)
sum = round(sum)
if sum%2 != 0:
    print("Alive")
else:
    print("Dead")

#0 1 1 2 3 5 8 13 21 33
'''sum = 0
i = 2
a = 0
b = 1
while i<=n:
    a = b
    b = sum
    sum = a+b
    i = i+1
print(sum)'''
