def sort_string(a):
	return ''.join(sorted(a))

def findSmallestPermutation(s):
	s = sort_string(s)
	i = 0
	while (s[i] == '0'):
		i += 1
	a = list(s)
	temp = a[0]
	a[0] = a[i]
	a[i] = temp
	s = "".join(a)
	return int(s)

def largestPermutation(arr):
	for i in range(len(arr)-1, -1, -1):
		if arr[i] > arr[i-1]:
			minimum = min(arr[i:])
			position = arr.index(minimum)
			arr[i-1], arr[position] = arr[position], arr[i-1]
			break 

	return int("".join(map(str, arr)))
		

n = int(input())		
arr = list(map(int, str(n)))
l = largestPermutation(arr)
s = findSmallestPermutation(str(n))
print(l+s)