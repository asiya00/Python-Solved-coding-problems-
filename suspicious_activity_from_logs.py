logs = ["9 7 50", "22 7 20", "33 7 50", "22 7 30"]
threshold = 3
# output = [7]

di = {}

temp = []
for i in logs:
	temp.append(list(map(int, set(i.split()[:2]))))

temp = sum(temp,[])
ans = []

for x in set(temp):
	a = temp.count(x)
	if a>=threshold:
		ans.append(str(x))

print(sorted(ans))


# if x not in di:
	# 	di[x] = 1
	# else:
	# 	di[x] += 1
	# if di[x] >= threshold and x not in ans:
	# 	ans.add(x)

