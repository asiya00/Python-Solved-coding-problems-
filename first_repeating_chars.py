s = input()

di = {}
for i in s:
	if i not in di:
		di[i] = 1
	else:
		di[i] += 1
		if di[i] > 1:
			print(i)
			break
