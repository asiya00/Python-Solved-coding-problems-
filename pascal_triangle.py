# binomial coefficient approach

# import math

# for i in range(n):
# 	for j in range(i+1):
# 		print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)), end=" ")
# 	print()

# addition approach

# n=0 0+1=1
# n=1 0+1=1  1+0=1
# n=2      1+1


n = int(input())
li = [1, 1]
for i in range(n):
	if i == 0:
		print(1)
	elif i==1:
		print(*li)
	else:
		temp = [0+li[0]]
		for j in range(len(li)-1):
			temp.append(li[j]+li[j+1])
		temp.append(1)
		print(*temp)
		li[:] = temp[:]


			 


