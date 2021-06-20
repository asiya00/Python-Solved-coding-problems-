n=int(input("ENTER A NUMBER: "))
a=[]
count=65
for i in range(1,n+1):
	a.append(chr(count))
	count=count+1

b=1
for i in range(n):
	print("".join(a[0:b]))
	b=b+1
		
	