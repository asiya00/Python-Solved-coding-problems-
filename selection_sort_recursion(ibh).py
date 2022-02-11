def find_maximum(arr, high):
	if high == 0:
		return 0
	val = find_maximum(arr, high-1)
	if arr[val] > arr[high]:
		return val
	return high

def selection_sort(arr, high=None):
	if high is None:
		high = len(arr) - 1
	if high <= 0:
		return
	maximum = find_maximum(arr, high)
	arr[maximum], arr[high] = arr[high], arr[maximum]
	selection_sort(arr, high-1)


arr = [7, 5, 4, 3, 2, 1, 8]
selection_sort(arr)
print(arr)
