li = [8,4,6,12]
sumc = 0
for i in range(len(li)):
	a = min(li)
	li.remove(a)
	if len(li)!=0:
		b = min(li)
	else:
		break
	c = a + b
	sumc += c
	d = li.index(b)
	li[d] = c 

print(sumc)