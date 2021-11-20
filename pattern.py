n = int(input())
k = n- 1
numbers = 1
print(" "*k, end="")
print(numbers)
k = k - 1
numbers += 1
temp = n-1
for i in range(1, n):
	print(" "*k, end="")
	print(numbers, end="")
	curr_temp = numbers
	for j in range(i):
		curr_temp = curr_temp+temp
		print(curr_temp, end="")
		temp -= 1
	print()
	numbers += 1
	temp = n-1
	curr_temp = numbers
	k -= 1
