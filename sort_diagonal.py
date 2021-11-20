# Sort diagonal from down to up

def diagonalOrder(arr, n, m):
	an = [[0 for i in range(n)] for j in range(m)]
	ans = [[] for i in range(n + m - 1)]
	
	for i in range(m):
		for j in range(n):
			ans[i + j].append(arr[j][i])

	for i in range(len(ans)):
		ans[i] = sorted(ans[i])
	print(ans)

	row = 0
	curr_pos = 0

	for j in range(0, (len(ans)//2)+1):
		for k in range(0, len(ans[j])):
			an[row][k] = ans[j][k]
			row -= 1
			if row < 0:
				break
		curr_pos += 1
		row = curr_pos
	
	row = row - 1
	curr_pos = curr_pos - 1
	col = 1
	curr_col = 1
	for x in range(j+1, len(ans)):
		for y in range(0, len(ans[x])):
			an[row][col] = ans[x][y]
			row -= 1
			col += 1
			if row < 1:
				break
		row = curr_pos
		curr_col += 1
		col = curr_col 
	print(an)

n = 5
m = 5

M = [[8, 6, 4, 1, 9], [9, 8, 4, 7, 10], [3, 7, 3, 8, 45], [5, 2, 6, 1, 90], [3, 9, 10, 11, 12]]
diagonalOrder(M, n, m)
