# # String Reversal

# st = "Hello World"

# def string_reversal(st):
# 	return st[::-1]

# print(string_reversal(st))

# # GCD of two numbers

# def gcd(a, b):
# 	while(b):
# 		a, b = b, a % b
# 	return a 

# print(gcd(10, 30))

# # LCM of two numbers

# def lcm(a, b):
# 	return (a * b)//gcd(a, b)

# print(lcm(10, 30))

# # Reverse a number
# n = -154

# def reverseddigit(n):
# 	if n>0:
# 		n = str(n)[::-1]
# 		return int(n)
# 	else:
# 		n = int(str(n)[:0:-1])
# 		return int("-"+str(n))

# print(reverseddigit(n))

# # Find second largest number from given list of values

# # Approach 1 (with in-built functions)

# n = [5,6,22,44,33,7,1,0]
# print(sorted(n)[-2])

# # Approach 2 (without in-built function)
# n = [5,6,22,44,7,33,23,1,0]

# maximum = n[0]
# second_maximum = n[1]

# for i in range(0,len(n)):
# 	if n[i]>maximum:
# 		second_maximum = maximum
# 		maximum = n[i]

# 	if n[i]>second_maximum and n[i]<maximum:
# 		second_maximum = n[i]

# print(second_maximum)

# # Print fibonacci series (without recursion) (most preferable for larger input)

# n = int(input())

# a = 0
# b = 1
# print(a,b,sep="\n")
# for i in range(n-2):
# 	c = a + b
# 	print(c)
# 	a,b = b,c

# # nth fibonacci number 
# n = 10
# p1 = ((1 + 5**0.5)/2)**(n-1)
# p2 = ((1 - 5**0.5)/2)**(n-1)
# print(round((p1 - p2)/(5**0.5)))


# # Display sum of odd and even digits in the number (eg for number 534726, sum of odd digits is 5+3+7=15 and even digits is 4+2+6=12)

# # Approach 1
# n = 534726
# even = 0
# odd = 0
# for i in str(n):
# 	if not int(i) % 2:
# 		even += int(i)
# 	else:
# 		odd += int(i)
# print(even, odd)

# # Check whether the number is prime or not
# n = 17

# def check_prime(n):
# 	for i in range(2, int(n ** 0.5) + 1):
# 		if not n % i:
# 			return False
# 	return True 

# print(check_prime(n))

# # Check whether the number is armstrong or not

# def armstrong(n):
# 	return sum(int(i)**3 for i in str(n)) == n

# print(armstrong(143))

# # Check whether the string is palindrome or not
# def palindrome(p):
# 	return p[::-1] == p


# Factorial of a number

# def factorial(n):
# 	fact = 1
# 	for i in range(1,n+1):
# 		fact *= i 

# 	return fact 

# print(factorial(19))


# Write a program to find most occuring character in string

def most_repeated(s):
	max_repeated = 0
	for i in set(s):
		if max_repeated < s.count(i):
			max_repeated = s.count(i)
			char = i

	return max_repeated, char

print(most_repeated("aaabbbbbcccccc"))
