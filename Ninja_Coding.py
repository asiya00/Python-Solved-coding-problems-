#TCS Ninja Coding Questions #1: Sweet Seventeen

# Given a maximum of four digit to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G) as input, 
# output its decimal value.

def sweet_seventeen(s):
	return int(s, 17)

print(sweet_seventeen('23GF'))


# TCS Ninja Coding Questions #2: A Sober Walk
# Our hoary culture had several great persons since time immemorial and king 
# vikramaditya’s nava ratnas (nine gems) belongs to this ilk.They are named in the 
# following shloka:
# Among these, Varahamihira was an astrologer of eminence and his book Brihat Jataak 
# is recokened as the ultimate authority in astrology. He was once talking with 
# Amarasimha,another gem among the nava ratnas and the author of Sanskrit 
# thesaurus, Amarakosha. Amarasimha wanted to know the final position of a person, 
# who starts from the origin 0 0 and travels per following scheme.
# • He first turns and travels 10 units of distance
# • His second turn is upward for 20 units
# • Third turn is to the left for 30 units
# • Fourth turn is the downward for 40 units
# • Fifth turn is to the right(again) for 50 units
# … And thus he travels, every time increasing the travel distance by 10 units

def Sober_Walk(n):
	x = 0
	y = 0
	increment = 10
	direction = "R"
	for i in range(n):
		if direction == "R":
			x += increment
			increment += 10
			direction = "U"
		elif direction == "U":
			y += increment
			increment += 10
			direction = "L"
		elif direction == "L":
			 x -= increment
			 increment += 10
			 direction = "D"
		elif direction == "D":
			y -= increment
			increment += 10
			direction = "R"
	return x,y

print(Sober_Walk(5))

#TCS Ninja Coding Questions #3: Word is the key

def iskeyword(k):
	keywords = ["break", "case", "continue", "default", "defer", "else", "for", "func", "goto", "if", "map", "range", "return", "struct", 
"type", "var"]
	return "{} is a keyword".format(k) if k in keywords else "{} is not a keyword".format(k)

print(iskeyword("defer"))


# TCS Ninja Coding Questions #4: Jar of Candies

# There is a jar full of candies for sale at a mall counter. The jar has the capacity N, that is JAR 
# can contain maximum N Candies when a JAR is full. At any point in time, JAR can have an M 
# number of candies where M<=N. Candies are served to the customers. JAR is never remaining 
# empty as when the last K candidates are left, JAR is refilled with new candidates in such a way 
# that JAR gets full.
# Write the code to implement the above scenario. Display JAR at the counter with the available 
# number of candies.
# Input should be the number of candies one customer orders at a point in time. Update the JAR 
# after every purchase and display JAR at the counter. The output should give the number of 
# candies sold and the updated number of candies in the JAR. If the input is more than the number 
# of candies in JAR, return “INVALID INPUT”.
# Given,
# N=10, Where N is the number of candies available, K<=5, Where K is the number of minimum 
# candies that must be inside JAR ever.
# Example1: (N=10,K=<5)

def Jar_Of_Candies(p):
	N = 10

	if p <= 0 or p > N:
		print("INVALID INPUT")
		return
	N = N - p 
	if N <= 5:
		N = 10

	print("Number of Candies Sold is", p)
	print("Number of Candies available is", N)

Jar_Of_Candies(4)

# Oddly Even Problem Statement
# Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits

# Test Cases
# Case 1
# Input: 4567
# Expected Output: 2
# Explanation : Odd positions are 4 and 6 as they are pos: 1 and pos: 3, both have sum 10. Similarly, 5 and 7 are at even positions pos: 2 and pos: 4 with sum 12. Thus, difference is 12 – 10 = 2

# Case 2
# Input: 5476
# Expected Output: 2

def sum_of_oddlyeven(n):
	n = str(n)
	odd = n[::2]
	even = n[1::2]
	return abs(sum(map(int,odd)) - sum(map(int, even)))

print(sum_of_oddlyeven(9834698765123))

# TCS Ninja Coding Questions #5:
# Question. Find the nth term of the series.

# 1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243,64, 729, 128, 2187 ….

# This series is a mixture of 2 series – all the odd terms in this series form a geometric series and all the even terms form yet another geometric series. Write a program to find the Nth term in the series.

# The value N in a positive integer that should be read from STDIN.
# The Nth term that is calculated by the program should be written to STDOUT.
# Other than value of n th term,no other character / string or message should be written to STDOUT.
# For example , if N=16, the 16th term in the series is 2187, so only value 2187 should be printed to STDOUT.
# You can assume that N will not exceed 30.

# Test Case 1

# Input- 16
# Expected Output – 2187
# Test Case 2

# Input- 13
# Expected Output – 64

def nth_term(num):
	if num > 0:
		a = num//2
		if not num % 2:
			return 3**(a - 1)
		else:
			return 2**a

print(nth_term(4))


# TCS Ninja Coding Questions #6:
# 1. The program will recieve 3 English words inputs from STDIN

# These three words will be read one at a time, in three separate line
# The first word should be changed like all vowels should be replaced by *
# The second word should be changed like all consonants should be replaced by @
# The third word should be changed like all char should be converted to upper case
# Then concatenate the three words and print them
# Other than these concatenated word, no other characters/string should or message should be written to STDOUT

# For example if you print how are you then output should be h*wa@eYOU.

# You can assume that input of each word will not exceed more than 5 chars

def english_words(word1, word2, word3):
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	actual_string = ""
	for letter in word1:
		if letter in vowels:
			actual_string += '*'
		else:
			actual_string += letter
	for letter in word2:
		if letter not in vowels:
			actual_string += '@'
		else:
			actual_string += letter 
	actual_string += word3.upper()

	return actual_string

word1 = input()
word2 = input()
word3 = input()
print(english_words(word1, word2, word3))


# TCS Ninja Coding Questions #7:
# Consider the below series :

# 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
# This series is a mixture of 2 series all the odd terms in this series form even numbers in ascending order
# Every even terms is derived from the previous  term using the formula (x/2)
# Write a program to find the nth term in this series.

# The value n in a positive integer that should be read from STDIN the nth term that is calculated by the program should be written to STDOUT.
# Other than the value of the nth term no other characters /strings or message should be written to STDOUT.
# For example

# if n=10,the 10 th term in the series is to be derived from the 9th term in the series. The 9th term is 8 so the 10th term is (8/2)=4. Only the value 4 should be printed to STDOUT.

def nthterm(n):
	if not n % 2:
		return (n - 2) // 2
	return (n - 1)

print(nthterm(2))

# TCS Ninja Coding Questions # 8:
# PRIME NUMBER WITH A TWIST
# Ques. Write a code to check whether no is prime or not. Condition use function check() to find whether entered no is positive or negative ,if negative then enter the no, And if yes pas no as a parameter to prime() and check whether no is prime or not?

def check(n):
	if n < 0:
		return True
	return False

def prime(n):
	if check(n):
		n = int(input("Negative number detected, enter the positive number: "))

	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			print("The number is not a prime number")
			return
	print("The number is a prime number")

n = int(input())
prime(n)


# TCS Ninja Coding Questions # 9:
# LEAP YEAR OR NOT
# Program to check if a year is Leap Year or not.

def is_leapyear(y):
	if not y % 4:
		if not y % 100:
			if not y % 400:
				return "Is a leap year"
			else:
				return "Not a leap year"
		else:
			return "Is a leap year"

	else:
		return "Not a leap year"

print(is_leapyear(2021))

def is_leapyear(y):
	return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

print(is_leapyear(2021))

# TCS Ninja Coding Questions # 10:
# Consider the below series:
# 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17…..

# This series is a mixture of 2 series fail the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order

# Write a program to find the Nth term in this series

# The value N in a positive integer that should be read from mm. The Nth term that is calculated by the program should be written to STDOUT Otherthan the value of Nth term , no other characters / string or message should be written to STDOUT.

# For example, when N:14, the 14th term in the series is 17 So only the value 17 should be printed the STDOUT

n = 14

mid = n//2

if not n%2:
	i = 2
	k = 0
	while(True):
		for j in range(2,i//2 + 1):
			if not i%j:
				break
		else:
			k += 1

		if k == mid:
			print(i)
			break
		i += 1
else:
	p1 = ((1 + 5**0.5)/2)**(mid + 1)
	p2 = ((1 - 5**0.5)/2)**(mid + 1)
	print(round((p1 - p2)/(5**0.5)))



# TCS Ninja Coding Questions #11: Oxygen Value
# The selection of MPCS exams includes a fitness test which is conducted on the 
# ground. There will be a batch of 3 trainees, appearing for a running test on track for 3 
# rounds.
# You need to record their oxygen level after every round. After trainees are finished 
# with all rounds, calculate for each trainee his average oxygen level over the 3 rounds 
# and select the one with the highest average oxygen level as the fittest trainee. If more 
# than one trainee attains the same highest average level, they all need to be selected. 
# Display the fittest trainee(or trainers) and the highest average oxygen level.
# Note:
# 1.The oxygen value entered should not be accepted if it is not in the range between 1 
# and 100.
# 2.If the calculated maximum average oxygen value of the trainees is below 70 then 
# declare the trainees as unfit with a meaningful message as “All trainees are unfit”
# 3.Average oxygen values should be rounded

# Example 1:
# Input #1:
# 95
# 92
# 95
# 92
# 90
# 92
# 90
# 92
# 90
# Output:
# Trainee Number: 1
# Trainee Number: 3

oxygenVal = []

for i in range(9):
	n = int(input())
	if n not in range(1, 101):
		print("Invalid input")
		oxygenVal.append(0)
	else:
		oxygenVal.append(n)

trainee1 = round(sum(oxygenVal[0::3])/3)

trainee2 = round(sum(oxygenVal[1::3])/3)

trainee3 = round(sum(oxygenVal[2::3])/3)

if trainee1 >= trainee2 and trainee1 >= trainee3:
	if trainee1 <= 70:
		print("Trainee is unfit")
	print("Trainee Number: 1")
if trainee2 >= trainee1 and trainee2 >=trainee3:
	if trainee1 <= 70:
		print("Trainee is unfit")
	print("Trainee Number: 2")
if trainee3 >= trainee1 and trainee3 >= trainee2:
	if trainee1 <= 70:
		print("Trainee is unfit")
	print("Trainee Number: 3")






		








