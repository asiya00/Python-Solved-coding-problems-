# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

def jump(arr):
	curReach = 0
	curMax = 0
	jump = 0

	for i in range(len(arr) - 1):
		if i + arr[i] > curMax:
			curMax = i + arr[i]

		if i == curReach:
			jump += 1
			curReach = curMax
	return jump

arr = [2, 3, 1, 1, 4]

print(jump(arr))


