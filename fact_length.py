import math
n = 100000.0
# log(100000.0!)
# log(1x2x3x..........x100000.0)             <--------log(mxn) = log(m) + log(n)
# log(1) + log(2) + ............ log(100000.0)

sum = 0
for i in range(1, int(n)+1):
	sum += math.log10(i)

print(int(sum)+1)


# 456574