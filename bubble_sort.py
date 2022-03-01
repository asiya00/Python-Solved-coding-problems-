def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j+1] < arr[j]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr) 

