def container_max_water(arr):
	left = 0
	right = len(arr) - 1
	result = -1
	while(left < right):
		minimum = min(arr[left], arr[right])
		area = minimum * (right - left)
		result = max(result, area)
		if arr[left] < arr[right]:
			left += 1
		else:
			right -= 1
	return result



arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(container_max_water(arr))