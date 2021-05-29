t=int(input())
for i in range(1,t+1):
	s=list(input())
	length=len(s)
	if length==2:
		if s[0]=="I" and s[1]=="I":
			print("Case #{}: {} {}".format(i,"I",2))
		else:
			print("Case #{}: {} {}".format(i,"O",1))
			
	elif s[0]=="O" and s[0]==s[-1]:
		print("Case #{}: {} {}".format(i,s[0],length+1))
	else:
		if s[0]==s[-1] and s[-1]==s[-2]:
			print("Case #{}: {} {}".format(i,s[0],len(s[0:-1])+1))
		else:
			a=s.pop(0)
			j=0
			while(len(s)!=1):	
				if s[-1]==s[0] and s[-1]==s[-2]:
					print("Case #{}: {} {}".format(i,s[0],len(s[0:-1])+1))
					break
				elif s[-1]==s[0]:
					b=s.pop(-1)
				elif s[-1]!=s[0]:
					s.pop(-1)
				else:
					s.pop(0)	
				j=j+1
			else:
				print("Case #{}: {} {}".format(i,s[0],1))
			
			
		
		
			
	
		
	