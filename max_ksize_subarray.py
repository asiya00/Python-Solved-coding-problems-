maximum = float("-inf")
curr_sum = 0
start = 0
k = 3

arr = [2, 3, 5, 2, 9, 7, 1]

for end, val in enumerate(arr):
	curr_sum += val

	if end - start + 1 == k:
		maximum = max(maximum, curr_sum)
		curr_sum -= arr[start]
		start += 1

print(maximum)


