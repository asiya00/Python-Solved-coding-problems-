matrix = [[1, 3, 5, 7],
		  [10, 11, 16, 20],
		  [23, 30, 34, 60]]
ele = 60
def binarysearch(l, h, arr, ele):
	if l<=h:
		m = (l+h)//2
		if arr[m] == ele:
			return True
		elif ele < arr[m]:
			return binarysearch(l, m-1, arr, ele)
		else:
			return binarysearch(m+1, h, arr, ele)
	else:
		return False

def search(matrix):
	for i in matrix:
		if binarysearch(0, len(i)-1, i, ele):
			return True
	return False

print(search(matrix))