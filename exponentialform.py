import math
n = int(input())
base = int(input())
a = math.log(n,base)
if base**round(a) == n:
	print("TRUE")
else:
	print("FALSE")