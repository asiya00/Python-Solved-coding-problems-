def trapping_rain_water(height):
	left = 0
	right = len(height) - 1
	leftmax = height[l]
	rightmax = height[r]
	result = 0

	while(left < right):
		if leftmax < rightmax:
			left += 1
			leftmax = max(leftmax, height[left])
			result += leftmax - height[left]
		else:
			right -= 1
			rightmax = max(rightmax, height[right])
			result += rightmax - height[right]

	return result


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trapping_rain_water(arr))


