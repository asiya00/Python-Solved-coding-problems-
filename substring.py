# s = "ABA"
# n = 3
# x = 0
# y = 2

# length = 2**n
# count = 0
# for i in range(length):
# 	count_A = 0
# 	li_string = ""
# 	for j in range(len(s)):
# 		if (i & (1 << j)):
# 			li_string += s[j]
# 			if s[j] == "A":
# 				count_A += 1
# 	if len(li_string) and li_string in s:
# 		count_B = len(li_string) - count_A
# 		diff = count_A - count_B
# 		if diff >= x and diff <= y:
# 			count += 1
# print(count)


# li = "".join([s[j] for j in range(len(s)) if (i & (1 << j))])
# n = 3
# x = 1
# y = 1
# s = "ABA"
# counter = 0

# def subarray(x, y, count_A, count_B):
# 	global counter
# 	if not x and not y:
# 		return 0
# 	if count_A - count_B < 1:
# 		return 0
# 	if count_A - count_B >= x and count_A - count_B <= y:
# 		return counter += 1
# 	if count_A <= 0 and count_B > 0:
# 		return subarray(x, y, count_A, count_B-1)
# 	if count_B <= 0 and count_A > 0:
# 		return subarray(x, y, count_A-1, count_B)
# 	else:
# 		return subarray(x, y, count_A-1, count_B)
# 		return subarray(x, y, count_A, count_B-1)

# count_A = s.count("A")
# count_B = n - count_A
# ans = subarray(x, y, count_A, count_B)
# print(counter)

