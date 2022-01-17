arr = [7, 8, 10]
mincost = 0
for i in range(arr):
	mincost += min(mincost, i)
print(mincost)