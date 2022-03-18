def etf(input1):
	import math
	count = 0
	for i in range(1, input1+1):
		if math.gcd(i, input1) == 1:
			count += 1
	return count

n = int(input())
print(eulers_totient(n))