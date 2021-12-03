def binarysearch(arr, l, h, ele):
	if l <= h:
		m = (l+h)//2
		if arr[m] == ele:
			return m
		elif ele < arr[m]:
			return binarysearch(arr, l, m-1, ele)
		else:
			return binarysearch(arr, m+1, h, ele)
	else:
		return "Element not found"
arr = [1]
print(binarysearch(arr, 0, len(arr)-1, 1))
