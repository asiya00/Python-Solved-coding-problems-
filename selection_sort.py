# def selection_sort(arr):
# 	for i in range(len(arr)):
# 		minimum = min(arr[i:])
# 		min_index = i + arr[i:].index(minimum)
# 		arr[i], arr[min_index] = arr[min_index], arr[i]

# arr = [2, 3, 4, 1, 5, 6, 4, 0]

# selection_sort(arr)

# print(arr)

def selection_sort(arr):
	for i in range(len(arr)):
		minimum = arr[i]
		index = 0

		for j in range(i, len(arr)):
			if arr[j] <= minimum:
				minimum = arr[j]
				index = j
		arr[i], arr[index] = arr[index], arr[i]

arr = [2, 3, 4, 1, 5, 6, 4, 0]

selection_sort(arr)

print(arr)
