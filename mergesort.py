li = [20, 47, 15, 8, 9, 4, 40, 30, 12, 17]

def merge(li):
	if len(li)>1:
		mid = len(li)//2
		l = li[:mid]
		r = li[mid:]
		
		merge(l)
		merge(r)
		
		l.append(float("inf"))
		r.append(float("inf"))
		i = j = 0
		for k in range(len(li)):
			if l[i] <= r[j]:
				li[k] = l[i]
				i+=1
			else:
				li[k] = r[j]
				j+=1
			

merge(li)
print(li)
	
	