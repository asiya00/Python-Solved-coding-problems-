# def josephus(n,k):
#     #Your code here
#     arr = list(range(1, n+1))
#     temp = 0
#     while len(arr)>1:
#         temp = (temp+k-1) % len(arr)
#         print(arr[temp])
#         arr.pop(temp)
#         print(arr)
#     return arr[0]

def josephus(n, k):
	if n == 1:
		return 1
	return (k - 1 + josephus(n - 1, k)) % n + 1


print(josephus(10, 2))
