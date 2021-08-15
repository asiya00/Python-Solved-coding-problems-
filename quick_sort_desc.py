def partition(arr, low, high):
	j = low - 1
	pivot = arr[high]
	for i in range(low, high):
		if arr[i] >= pivot:
			j += 1
			arr[j], arr[i] = arr[i], arr[j]
	arr[j+1], arr[high] = arr[high], arr[j+1]
	return j+1


def quick_sort(arr, low, high):
	if low < high:
		q = partition(arr, low, high)
		quick_sort(arr, low, q-1)
		quick_sort(arr, q+1, high)

arr = [2,3,4,1,5,6,0]

quick_sort(arr, 0, len(arr) - 1)
print(arr)