def insertintosortedarray(arr, ele):
	if len(arr) < 1 or arr[-1] <= ele:
		arr.append(ele)
		return
	val = arr.pop()
	insertintosortedarray(arr, ele)
	arr.append(val)

def sort(arr):
	if len(arr) < 2:
		return arr
	val = arr.pop()
	sort(arr)
	insertintosortedarray(arr, val)

import random
arr = [random.randrange(1, 11) for i in range(11)]
sort(arr)
print(arr)