def partition(arr, low, high):
	pivot = arr[low]
	i = low
	j = high 
	while True:
		while True:
			if arr[i] >= pivot:
				break
			i += 1

		while True:
			if arr[j] <= pivot:
				break
			j -= 1 

		if i >= j:
			return j

		arr[j], arr[i] = arr[i], arr[j]
		i += 1
		j -= 1


def quick_sort(arr, low, high):
	if low < high:
		q = partition(arr, low, high)
		quick_sort(arr, low, q)
		quick_sort(arr, q+1, high)

arr = [-5,4,3,-2,-2,-3,50,70,-80]
# arr = [2,1,5,6,8,4,3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
