arr = [5, 5, 4, 3, 2, 1, 2]

def selection_sort(arr, i):
	if i == 0:
		return
	maximum = max(arr[:i+1])
	index = arr.index(maximum)
	arr[index], arr[i] = arr[i], arr[index]
	selection_sort(arr, i-1)

selection_sort(arr, len(arr)-1)
print(arr)
