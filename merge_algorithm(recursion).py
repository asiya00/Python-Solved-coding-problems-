# arr = []
# L = []
# R = []
# l = len(L)
# r = len(R)
# start 
# end 

def merge(arr, L, R, l, r, start, end):
	if start < end:
		if (l > 0 and r <= 0) or (l > 0 and L[-l] < R[-r]):
			arr[start] = L[-l]
			l -= 1
			start += 1
		elif (l <= 0 and r > 0) or (r > 0 and L[-l] > R[-r]):
			arr[start] = R[-r]
			r -= 1
			start += 1
		merge(arr, L, R, l, r, start, end)
	
def mergesort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergesort(L)
		mergesort(R)
		merge(arr, L, R, len(L), len(R), 0, len(arr))



arr = [13, 1, 3, 5, 2, 4, 6, 7, 9, 8, 10, 11]
mergesort(arr)
print(arr)
# L = [1, 3, 5, 7, 9, 10]
# R = [2, 4, 6, 8]

# merge(L, R, len(L), len(R), 0, len(arr), arr)
# print(arr)
