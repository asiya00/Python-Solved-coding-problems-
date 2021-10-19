def printUnique(l,r):
	for i in range (l, r + 1):
		num = i
		visited = [0,0,0,0,0,0,0,0,0,0]
		while (num):
			if visited[num % 10] == 1:
				break
			visited[num % 10] = 1;
			num = (int)(num / 10)
		if num == 0:
			print(i, end = " ")

l = 1;
r = 20;
printUnique(l, r)