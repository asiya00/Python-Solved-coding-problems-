t = int(input())
for i in range(t):
	N, K, M = map(int, input().split())
	li = []
	for i in range(0, (N*K)+1, K):
		li.append(i%M)
	print(*[li.count(x) for x in range(0, max(li)+1)])


