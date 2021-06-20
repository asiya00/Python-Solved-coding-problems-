#filled heart
for i in range(7):
	if i%3!=0:
		print("*",end="")
	else:
		print(" ",end="")
print()
print("*"*7)

l = 7
for j in range(2,6):
	for k in range(4):
		if j-k==2:
			print(" "*k,end="")
			print("*"*l)
			l = l-2			
print()

#unfilled heart
for i in range(7):
	if i%3!=0:
		print("*",end="")
	else:
		print(" ",end="")
print()

for i in range(7):
	if i%3==0:
		print("*",end="")
	else:
		print(" ",end="")
print()		

for j in range(2,6):
	for k in range(7):
		if j-k == 2 or j+k==8:
			print("*",end="")
		else:
			print(" ",end="")
	print()
	
