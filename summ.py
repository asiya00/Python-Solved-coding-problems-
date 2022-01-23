sum = 0
k = 45
for i in range(3, 0, -1):
	for j in range(0, i+1):
		if j!= i:
			sum+=sum+k*i
		else:
			sum -= sum - k
	k += 1
print(sum)