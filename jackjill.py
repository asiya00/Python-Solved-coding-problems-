def countMinOperations(arr, n):
	arr.sort()
	count = 0

	while(arr.count(0)!=n):
		for i in range(n):
			if arr[i]%2==1:
				arr[i]=arr[i]-1
				count = count + 1

		for i in range(n):
			arr[i]=arr[i]/2

		count = count + 1

	return count - 1

# arr = [16, 16, 16] #7
# arr = [23, 24, 25]  # 13
arr = [45, 46, 47, 48, 49] #23
print(countMinOperations(arr, len(arr)))