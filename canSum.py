'''canSum(7, [5, 3, 4, 7])
camSum takes 2 arguments 
1. Targetsum
2. Array of numbers

The function should return a Boolean indicating whether or not it is possible to generate the targetsum using numbers from the array

Assuming non negative numbers'''

# m = target sum
# n = length of array
# Time Complexity O(m * n)
# Space complexity O(m)

memo = {}

def canSum(targetSum, arr):
	if not targetSum:
		return True

	if targetSum in memo:
		return memo[targetSum]

	if targetSum < 0:
		return False

	for num in arr:
		substracted = targetSum - num
		if canSum(substracted, arr):
			memo[targetSum] = True
			return memo[targetSum]

	memo[targetSum] = False
	return memo[targetSum]


print(canSum(7, [5, 4, 3, 7]))
print(canSum(300, [7, 14]))

