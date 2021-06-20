n = 5
for i in range(5):
	print(" "*10,end="")
	print(" "*i,end="")
	print("* "*n)
	n = n-1
	print()

n = 1	
for j in range(4,-1,-1):
	print(" "*10,end ="")
	print(" "*j,end="")
	print("* "*n)
	n = n+1
	print()