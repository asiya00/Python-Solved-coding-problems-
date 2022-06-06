# n = 5
# 2 4 3 6 8
# 6
# 3 5 9 7 1 3
# def iseven(m):
# 	if m%2:
# 		return False
# 	return True

# def isodd(m):
# 	if m%2:
# 		return True
# 	return False

# t = int(input())

t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	i = 0
	count = 0
	while i < (len(arr)-1):
		if (arr[i] + arr[i+1]) % 2:
			if arr[i] % 2:
				arr.remove(arr[i])
				count += 1
			else:
				arr.remove(arr[i+1])
				count += 1
		i += 1
	print(count)

# t = int(input())
# for _ in range(t):
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	count = 0
# 	if all(i % 2 for i in arr):
# 		print(0)
# 	else:
# 		odd_nums = sum(1 for i in arr if i % 2)
# 		if n - odd_nums == 1:
# 			print(1)
# 		else:
# 			print(odd_nums)

# for _ in range(t):
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	count = 0
# 	delete_ind = float("inf")
# 	for i in range(len(arr)-1):
# 		if (iseven(arr[i]) and isodd(arr[i+1])):
# 			if i+1 != delete_ind:
# 				delete_ind = i+1
# 				count += 1
# 		elif (isodd(arr[i]) and iseven(arr[i+1])):
# 			if i != delete_ind:
# 				delete_ind = i
# 				count += 1
# 		print(delete_ind)
# 	print(count)
