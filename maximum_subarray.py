arr = [1, 2, 3, -10, -15, 80, 90]

l=r=0
k = 0
curr = 0
maximum = 0
for i in range(len(arr)):
	curr += arr[i]
	if curr > maximum:
		maximum = curr
		r = i		
		k = l
	
	if curr <= 0:
		curr = 0
		l = i + 1

print(maximum)
print(k,r)
