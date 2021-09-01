def gridtraveler(li, i, j, memo={}):
	key = (i, j)
	if i==len(li) or j==len(li[i]) or li[i][j] == 1:
		return 0
	elif i == len(li) - 1 and j == len(li[i]) - 1:
		return 1
	if key in memo:
		return memo[key]

	right = gridtraveler(li, i, j+1, memo)
	down = gridtraveler(li, i+1, j, memo)
	memo[key] = right + down
	return memo[key]

li = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

print(gridtraveler(li,0,0))

