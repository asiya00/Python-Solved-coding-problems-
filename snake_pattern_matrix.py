# def snake_pattern(m):
# 	a = m[1::2]
# 	l = m[::2]
# 	k = 0
# 	print(l)
# 	print(a)
# 	for i, j in zip(l,a):
# 		print(*i, end=" ")
# 		print(*j[::-1], end=" ")
# 		k += 1
# 	while(k!=len(l)):
# 		print(*l[k], end=" ")
# 		k += 1


# m = [[45, 48, 54,], [21, 89, 87], [70, 78, 50], [10, 8, 9], [8, 9, 3]]
# snake_pattern(m)

def snake_pattern(m):
	for i in range(len(m)):
		if i % 2:
			print(*m[i][::-1], end = " ")
		else:
			print(*m[i], end=" ")
	


m = [[45, 48, 54,], [21, 89, 87], [70, 78, 50], [10, 8, 9], [8, 9, 3]]
snake_pattern(m)