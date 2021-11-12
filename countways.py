def countDistinctWayToClimbStair(n):
	# if nStairs < 2:return 1
	# if nStairs in di:return di[nStairs]
	# ans = countDistinctWayToClimbStair(nStairs - 1, di) + countDistinctWayToClimbStair(nStairs -2, di)
	# di[nStairs] = ans
	# return ans
	if n == 0 or n == 1: return 1
	a = 1
	b = 1
	for i in range(2, n+1):
		c = a + b
		a,b = b,c
	return b

print(countDistinctWayToClimbStair(3))
