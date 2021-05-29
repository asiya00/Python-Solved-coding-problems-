t = int(input())
for i in range(1,t+1):
	n=int(input())
	li=list(map(int,input().split(" ")))
	a=sorted(list(set(li)))
	ans=0
	di={}
	j=1
	for k in a:
		di[k]=j
		j=j+1
	for l in li:
		a=di[l]
		ans=ans+a
		
	print("Case #{}: {}".format(i,ans))
		
	
		
	