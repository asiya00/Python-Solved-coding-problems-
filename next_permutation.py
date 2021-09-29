#  Given a number, you have to find next greater number which has same set of digits.

arr = list(map(int, "734"))

for i in range(len(arr)-1, -1, -1):
	if arr[i] > arr[i-1]:
		minimum = min(arr[i:])
		position = arr.index(minimum)
		arr[i-1], arr[position] = arr[position], arr[i-1]
		break 

if i == 0:
	print(-1)
else:
	print(arr)

		


