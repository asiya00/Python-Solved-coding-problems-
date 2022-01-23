arr = [1, 3, 2, 4, 5]
arr.sort()
n = 5
target = 7
flag = False
for i in range(n):
	l = i+1
	r = n-1
	while l < r:
		if arr[i] + arr[l] + arr[r] == target:
			flag = True
			print(arr[i], arr[l], arr[r])
			l += 1
			r -= 1
		elif arr[i] + arr[l] + arr[r] > target:
			r -= 1
		else:
			l += 1
if not flag:
	print("No triplets found")
