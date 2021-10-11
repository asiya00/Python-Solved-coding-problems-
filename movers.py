N, K = 7, 12
a = [12, 2, 3, 11, 6, 8, 1]

count = 0

a.sort(reverse=True)
# tempset = set()
for x in range(len(a)):
	# temp = float("-inf")
	remaining = K - a[x]
	# print(remaining)
	mini = float("inf")
	for y in range(x+1, len(a)):
		if a[y] <= remaining and a[y]<mini:
			mini = a[y]
	if mini!=float("inf"):
		count+=1