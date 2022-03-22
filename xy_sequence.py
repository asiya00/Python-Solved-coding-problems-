t = int(input())
for x in range(t):
	arr = [0]
	n, B, x, y = map(int, input().split())

	for i in range(1, n+1):
		if arr[i-1]+x <= B:
			arr.append(arr[i-1]+x)
		elif arr[i-1]-y <= B:
			arr.append(arr[i-1]-y)

	print(sum(arr))