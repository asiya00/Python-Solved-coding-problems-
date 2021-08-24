'''Say that you are traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to thr bottom-right corner. You may only move down or right

In how many ways can you travel tothe goal on a grid with dimensions m * n?

Write afunction 'grid_traveler(m, n)' that calculates this
Time Complexity: O(m * n)
space complexity O(n + m)'''


memo = {}
def grid_traveler(m, n):
	key = (m,n)
	if m == 0 or n == 0:
		return 0
	if m == 1 and n == 1:
		return 1
	if key in memo:
		return memo[key]
	memo[key] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)
	return memo[key]


print(grid_traveler(2, 3))
print(grid_traveler(1, 0))
print(grid_traveler(18, 9))
