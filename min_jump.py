def jump(arr):
	curReach = 0
	curMax = 0
	jump = 0

	for i in range(len(arr) - 1):
		if i + arr[i] > curMax:
			curMax = i + arr[i]

		if i == curReach:
			jump += 1
			curReach = curMax
	return jump

arr = [2, 3, 1, 1, 4]

print(jump(arr))


