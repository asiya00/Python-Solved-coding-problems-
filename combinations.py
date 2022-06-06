li = [1, 2, 3, 4]
k = 2

def combinations(li, k):
	if k == 0:
		return [[]]
	stack = []
	for i in range(len(li)):
		fixed = li[i]
		remaining = li[i+1:]

		for j in combinations(remaining, k-1):
			stack.append([fixed]+j)
	return stack


print(combinations(li, k))