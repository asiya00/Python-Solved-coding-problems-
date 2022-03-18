items = [[60, 10], [100, 20], [120, 30]]

n = len(items)

capacity = 50

ni = capacity
profit = 0

item = []

for i in range(n):
	print(i, items[i][0], items[i][1])
	item.append((items[i][0], items[i][1], items[i][0]/items[i][1]))

item = sorted(item, key=lambda x:x[2], reverse=True)
print(item)

w = 0

for i in item:
	if w+i[1] <= capacity:
		w += i[1]
		profit += i[0]
	else:
		profit += ((capacity-w)*i[0])/i[1]
		break
print(profit, w)

