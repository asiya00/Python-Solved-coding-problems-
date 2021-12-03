# import sys
# sys.setrecursionlimit(10**7)

# def even_fibo_sequence(n, memo={}):
#   if n < 1:
#       return n
#   if n == 1:
#       return 2
#   if n in memo:
#       return memo[n]
#   memo[n] = (4*even_fibo_sequence(n-1))+even_fibo_sequence(n-2)
#   return memo[n]

# print(even_fibo_sequence(4))
# print(even_fibo_sequence(10))
# print(even_fibo_sequence(20))
# print(even_fibo_sequence(100))
# print(even_fibo_sequence(500))
# print(even_fibo_sequence(1000))
# print(even_fibo_sequence(1500))
# print(even_fibo_sequence(2000))
# print(even_fibo_sequence(3000))
# print(even_fibo_sequence(6000))
# print(even_fibo_sequence(7000))
# print(even_fibo_sequence())

# n = 4000001//3
# print(n)
# even_sum = 0
# # for i in range((4000001//3)):
# #     even_sum += even_fibo_sequence(i)
# # print(even_sum)
n = 4000000
a = 0
b = 2
even_sum = 0
while b <= n:
	even_sum += b
	c = (4*b) + a
	a, b = b, c
print(even_sum)
