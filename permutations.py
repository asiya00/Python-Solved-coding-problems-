a = [1,2,3]
ans = []
def permute(a,index):
	if len(a)==0 or len(a)==1:
		return ans.append(a)
	if index == len(a)-1:
		li = []
		for i in a:
			li.append(i)
		ans.append(li)
		return 
	for i in range(len(a)):
		a[i] , a[index] = a[index], a[i]
		permute(a, index + 1)
		a[i] , a[index] = a[index], a[i]
		
permute(a,0)

ansfinal = []
for i in ans:
	if i not in ansfinal:
		ansfinal.append(i)
			
print(ansfinal)