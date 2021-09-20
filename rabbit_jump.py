t = int(input())
for i in range(t):
	N, K, M = map(int, input().split())
	li = []
	for i in range(0, (N*K)+1, K):
		print(i%M)
		li.append(i%M)