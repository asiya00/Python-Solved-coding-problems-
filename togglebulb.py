# TOGGLE THE BULB
li=[False,False,False,False,False,False,False]
n=len(li)

for i in range(1,n+1):
	for j in range(i-1,n,i):
		li[j]=not li[j]
print(li)	
print(li.count(True))

# second one line soln
print(int(n**(0.5)))

'''
1 2 3 4 5 6 7  => positions
0 0 0 0 0 0 0
1 1 1 1 1 1 1
1 0 1 0 1 0 1
1 0 0 0 1 1 1
1 0 0 1 1 1 1
1 0 0 1 0 1 1
1 0 0 1 0 0 1
1 0 0 1 0 0 0'''