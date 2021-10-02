def findLargestSquare(mat, m, n, maxsize):
    if m == 0 or n == 0:
 
        if maxsize != 0:
            return mat[m][n], max(maxsize, mat[m][n])
 
        for i in range(m + 1):
            if mat[i][n] == 1:
                return 1, 1
 
        for j in range(n + 1):
            if mat[m][j] == 1:
                return 1, 1
 
        return 0, 0
 
    left, maxsize = findLargestSquare(mat, m, n - 1, maxsize)
 
    top, maxsize = findLargestSquare(mat, m - 1, n, maxsize)
 
    diagonal, maxsize = findLargestSquare(mat, m - 1, n - 1, maxsize)
 
    size = 1 + min(min(top, left), diagonal) if mat[m][n] else 0
    return size, max(maxsize, size)
 
 
def findLargestSquareSubmatrix(mat) -> int:
    if not mat or not len(mat):
        return 0
 
    (M, N) = (len(mat), len(mat[0]))
    maxsize = findLargestSquare(mat, M - 1, N - 1, 0)[1]
    return maxsize

M = [[1, 1, 1, 1, 1],
	[1, 1, 1, 0, 0],
	[1, 1, 1, 0, 0],
	[1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1]]

print(findLargestSquareSubmatrix(M))

# This code is contributed by Soumen Ghosh
