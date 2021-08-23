def jump(arr):
	reachable = 0 
	i = 0
	jump = 0
	while(i < len(arr)):
		if reachable < i:
			return False
		reachable = max(reachable, i + arr[i])
		i += 1

	return True

arr = [0, 1, 2, 3, 2, 1, 0, 0, 1, 3]

print(jump(arr))


