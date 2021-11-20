def count_cell(mat, row, col):
    if any([row<0, col<0, row>=len(mat), col>=len(mat[0])]):
        return 0
    if mat[row][col] == 0:
        return 0

    mat[row][col] = 0
    cell_count = 1
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if any([r!=row, c!= col]):
                cell_count += count_cell(mat, r, c)
    return cell_count

def maxRegion(grid):
    max_count = 0
    region_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
           if grid[row][col] == 1:
               region_count =  count_cell(grid, row, col)
               max_count = max(max_count, region_count)
    return(max_count)

n = int(input().strip())
m = int(input().strip())
grid = []
for _ in range(n):
	grid.append(list(map(int, input().rstrip().split())))

res = maxRegion(grid)
print(res)