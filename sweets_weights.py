# N = 5
# K = 3

# weights = [1, 2, 8, 4, 6]
# 		     1  2  3  4  5

# taste = [5, 15, 5, 2, 9]

# 1, 3, 5  5+5+9 = 19

# 2, 3, 5  15+5+9 = 29

# 3, 5  5+9 = 14

# 4, 5  2+9 = 11

# N = 5
# K = 2

# weight = [1, 5, 3, 4, 9]
#           1  2  3  4  5

# taste = [1, 2, 5, 3, 1]
#          1  2  3  4  5

# 1, 2, 4, 5  1+2+3+1 = 7
# 2, 4, 5     2+3+1 = 6
# 3, 5        5+1 = 6
# 4, 5        3+1 = 4
# 5           1

N = int(input())
K = int(input())

weights = list(map(int, input().split()))
taste = list(map(int, input().split()))
max_possible = 0

for i in range(N):
	prev_maximum = 0
	j = i + 1
	sum_taste = taste[i]
	maximum = 0
	while j < N:
		max_weight = max(weights[j:j+K])
		if maximum != max_weight:
			sum_taste += taste[weights.index(max_weight)]
			maximum = max_weight
		j += 1
	if max_possible < sum_taste:
		max_possible = sum_taste
print(max_possible)


