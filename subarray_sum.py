# arr = [1,2,3,4,5,6,7,8,9,10]
# n = 10
# s = 15

arr = [1,2,3,4,5,6,7,5,4,3,2,1]
n = 5
s = 9

def subArraySum(arr, n, s): 
	sum_curr = arr[0]
	st = 0
	end = 1
	while end <= n:
		while sum_curr > s and st < end-1:
			sum_curr -= arr[st]
			st += 1
		if sum_curr == s:
			return [st+1, end]
		
		if end < n:
			sum_curr += arr[end]
		end += 1

	if end > n and sum_curr != s:
		return [-1]


print(subArraySum(arr, n, s))
