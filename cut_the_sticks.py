n = int(input())
arr = list(map(int,input().split()))
li = []
while len(arr)!=0:
	count = len(arr)
	print(count)
	amin = min(arr)
	for j in range(len(arr)):
		if arr[j] == amin:
			continue
		else:
			arr[j] = arr[j] - amin
			li.append(arr[j])
	arr = li.copy()
	li.clear()
	

	
	
	