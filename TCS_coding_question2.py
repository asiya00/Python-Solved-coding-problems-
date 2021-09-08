#TCS Ninja Coding Questions #1: Sweet Seventeen

# Given a maximum of four digit to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G) as input, 
# output its decimal value.

# def sweet_seventeen(s):
# 	return int(s, 17)

# print(sweet_seventeen('23GF'))


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

n = 12

mid = n//2

if not n%2:
	i = 2
	k = 0
	while(True):
		for j in range(2, int(i**0.5)+1):
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


# TCS Coding Question Day 1 Slot 2 – Question 2
# Problem Statement

# The Caesar cipher is a type of substitution cipher in which each alphabet in the plaintext or messages is shifted by a number of places down the alphabet.
# For example,with a shift of 1, P would be replaced by Q, Q would become R, and so on.
# To pass an encrypted message from one person to another, it is first necessary that both parties have the ‘Key’ for the cipher, so that the sender may encrypt and the receiver may decrypt it.
# Key is the number of OFFSET to shift the cipher alphabet. Key can have basic shifts from 1 to 25 positions as there are 26 total alphabets.
# As we are designing custom Caesar Cipher, in addition to alphabets, we are considering numeric digits from 0 to 9. Digits can also be shifted by key places.
# For Example, if a given plain text contains any digit with values 5 and keyy =2, then 5 will be replaced by 7, “-”(minus sign) will remain as it is. Key value less than 0 should result into “INVALID INPUT”
# Example 1:
# Enter your PlainText: All the best
# Enter the Key: 1

# The encrypted Text is: Bmm uif Cftu

# Write a function CustomCaesarCipher(int key, String message) which will accept plaintext and key as input parameters and returns its cipher text as output.

def CustomCaesarCipher(key, message):
	encoded_msg = "" 
	if key < 0:
		return "INVALID INPUT"
	for i in message:
		if i.isalpha() and i.isupper():
			encoded_msg += chr((ord(i) + key - 65) % 26 + 65)
		elif i.isalpha() and i.islower():
			encoded_msg += chr((ord(i) + key - 97) % 26 + 97)
		elif i.isdigit() and int(i) in range(0,10):
			if i=='9':
				encoded_msg += '0'
			else:
				encoded_msg += str(int(i) + key)
		else:
			encoded_msg += i
	return encoded_msg

print(CustomCaesarCipher(1, "All the best9"))

# TCS Coding Question Day 1 Slot 2 – Question 1
# Problem Statement

# A washing machine works on the principle of Fuzzy System, the weight of clothes put inside it for washing is uncertain But based on weight measured by sensors, it decides time and water level which can be changed by menus given on the machine control area.  

# For low level water, the time estimate is 25 minutes, where approximately weight is between 2000 grams or any nonzero positive number below that.

# For medium level water, the time estimate is 35 minutes, where approximately weight is between 2001 grams and 4000 grams.

# For high level water, the time estimate is 45 minutes, where approximately weight is above 4000 grams.

# Assume the capacity of machine is maximum 7000 grams

# Where approximately weight is zero, time estimate is 0 minutes.

# Write a function which takes a numeric weight in the range [0,7000] as input and produces estimated time as output is: “OVERLOADED”, and for all other inputs, the output statement is

# “INVALID INPUT”.

# Input should be in the form of integer value –

# Output must have the following format –

# Time Estimated: Minutes

# Example:

# Input value
# 2000

# Output value
# Time Estimated: 25 minutes

# def fuzzySystem(n):
# 	if n == 0:
# 		return "0 minutes"
# 	elif n in range(1, 2001):
# 		return "25 minutes"
# 	elif n in range(2001, 4002):
# 		return "35 minutes"
# 	elif n in range(4001, 7001):
# 		return "45 minutes"
# 	else:
# 		return "INVALID INPUT"

# n = int(input())

# print(fuzzySystem(n))


# TCS Coding Question Day 2 Slot 1 – Question 1
# Problem Statement

# We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.

# Take input as
# 1. Number of Interior walls
# 2. Number of Exterior walls
# 3. Surface Area of each Interior Wall in units of square feet
# 4. Surface Area of each Exterior Wall in units of square feet

# If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall.

# Calculate and display the total cost of painting the property
# Example 1:

# 6
# 3
# 12.3
# 15.2
# 12.3
# 15.2
# 12.3
# 15.2
# 10.10
# 10.10
# 10.00
# Total estimated Cost : 1847.4 INR

# Note: Follow in input and output format as given in above example

# no_intwalls = int(input())
# no_extwalls = int(input())

# int_cost = 0
# ext_cost = 0

# for i in range(no_intwalls):
# 	n = float(input())
# 	if n > 0:
# 		int_cost += n

# int_cost *= 18		

# for j in range(no_extwalls):
# 	n = float(input())
# 	if n > 0:
# 		ext_cost += n
# ext_cost *= 12		

# print("Total estimated Cost : {} INR".format(int_cost + ext_cost))


# TCS Coding Question Day 2 Slot 1 – Question 2
# Problem Statement

# A City Bus is a Ring Route Bus which runs in circular fashion.That is, Bus once starts at the Source Bus Stop, halts at each Bus Stop in its Route and at the end it reaches the Source Bus Stop again.
# If there are n  number of Stops and if the bus starts at Bus Stop 1, then after nth Bus Stop, the next stop in the Route will be Bus Stop number 1 always.
# If there are n stops, there will be n paths.One path connects two stops. Distances (in meters) for all paths in Ring Route is given in array Path[] as given below:
# Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
# Fare is determined based on the distance covered from source to destination stop as  Distance between Input Source and Destination Stops can be measured by looking at values in array Path[] and fare can be calculated as per following criteria:

# If d =1000 metres, then fare=5 INR
# (When calculating fare for others, the calculated fare containing any fraction value should be ceiled. For example, for distance 900n when fare initially calculated is 4.5 which must be ceiled to 5)
# Path is circular in function. Value at each index indicates distance till current stop from the previous one. And each index position can be mapped with values at same index in BusStops [] array, which is a string array holding abbreviation of names for all stops as-
# “THANERAILWAYSTN” = ”TH”, “GAONDEVI” = “GA”, “ICEFACTROY” = “IC”, “HARINIWASCIRCLE” = “HA”, “TEENHATHNAKA” = “TE”, “LUISWADI” = “LU”, “NITINCOMPANYJUNCTION” = “NI”, “CADBURRYJUNCTION” = “CA”

# Given, n=8, where n is number of total BusStops.
# BusStops = [ “TH”, ”GA”, ”IC”, ”HA”, ”TE”, ”LU”, ”NI”,”CA” ]

# Write a code with function getFare(String Source, String Destination) which take Input as source and destination stops(in the format containing first two characters of the Name of the Bus Stop) and calculate and return travel fare.

# Example 1:
# Input Values
# ca
# Ca

# Output Values
# INVALID OUTPUT

# Example 2:
# Input Values
# NI
# HA
# Output Values
# 23.0 INR

# Note: Input and Output should be in format given in example.
# Input should not be case sensitive and output should be in the format   INR

# import math

# def getFare(source, destination):
# 	source = source.upper()
# 	destination = destination.upper()

# 	Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
# 	BusStops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI","CA"]

# 	if source == destination:
# 		return "INVALID OUTPUT"
# 	elif source in BusStops and destination in BusStops:
# 		src_index = BusStops.index(source)
# 		dest_index = BusStops.index(destination)

# 		if src_index < dest_index:
# 			fare = math.ceil((sum(Path[src_index : dest_index + 1]) * 5)/1000)
# 		else:
# 			fare = math.ceil((sum(Path[src_index: dest_index - 1: -1]) * 5)/1000)

# 		return fare


# Fare = getFare("NI", "HA")
# print(Fare)


# TCS Coding Question Day 2 Slot 2 – Question 1
# Problem Statement

# There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer Bananas and Peanuts, the Monkeys jump down the Tree. If every Monkey can eat k Bananas and j Peanuts. If total m number of Bananas and p number of Peanuts are offered by travelers, calculate how many Monkeys remain on the Tree after some of them jumped down to eat.
# At a time one Monkeys gets down and finishes eating and go to the other side of the road. The Monkey who climbed down does not climb up again after eating until the other Monkeys finish eating.
# Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less than k Bananas left on the ground or less than j Peanuts left on the ground, only that Monkey can eat Bananas(<k) along with the Peanuts(<j).
# Write code to take inputs as n, m, p, k, j and return  the number of Monkeys left on the Tree.
#     Where, n= Total no of Monkeys
#         k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last may get less than k Bananas)
#         j = Number of eatable Peanuts by single Monkey(Monkey that jumped down last may get less than j Peanuts)
#         m = Total number of Bananas
#         p  = Total number of Peanuts
# Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility of k and j having a value zero

# Example 1:
# Input Values    
# 20
# 2
# 3
# 12
# 12

# Output Values
# Number of  Monkeys left on the tree:10

# Note: Kindly follow  the order of inputs as n,k,j,m,p as given in the above example. And output must include  the same format  as in above example(Number of Monkeys left on the Tree:)


# def MonkeySetting(n, k, j, m, p):
# 	if n<0 or k<0 or j<0 or m<0 or p<0:
# 		return "INVALID INPUT"
# 	atebananas = 0
# 	atepeanuts = 0
# 	atebananas += (m//k)
# 	atepeanuts += (p//j)
	
# 	if m % k == 1 or p % j == 1:
# 		n = n - 1

# 	return n - (atebananas + atepeanuts)

# print(MonkeySetting(20, 2, 3, 15, 16))

# Chain Marketing Organization has has a scheme for income generation, through which its members generate income for themselves. The scheme is such that suppose A joins the scheme and makes R and V to join this scheme  then A is Parent Member of R and V who are child Members. When any member joins the scheme then the parent gets total commission of 10% from each of its child members.
# Child members receive commission of 5% respectively. If a Parent member does not have any member joined under him, then he gets commission of 5%.
# Take name of the members joining the scheme as input.
# Display how many members joined the scheme including parent member.Calculate the Total commission gained by each members in the scheme. The fixed amount for joining the scheme is Rs.5000 on which commission will be generated
# SchemeAmount = 5000

# Example 1: When there are more than one child members 
# Input : (Do not give input prompts.Accept values as follows. )
# Amit                     //Enter parent Member as this
# Y                           //Enter Y if  Parent member has child members otherwise enter N
# Rajesh,Virat        //Enter names of child members of Amit in comma separated
# Output:(Final Output must be in format given below.)
# TOTAL MEMBERS:3
# COMISSION DETAILS
# Amit: 1000 INR
# Rajesh :250 INR
# Virat: 250 INR

# Example 2: When there is only one child member in the hierarchy
# Input :
# Amit
# Y
# Rajesh
# Output:
# Total Members: 2 
# Comission Details
# Amit: 500 INR
# Rajesh: 250 INR

# parent = input()
# Yes_No = input()
# if Yes_No == "N":
#     print("TOTAL MEMBERS:1\nCOMMISSION DETAILS\n{0}: 250 INR".format(parent))
# elif Yes_No == "Y":
#     child=list(map(str,input().split(",")))
#     print("TOTAL MEMBERS:{}".format(len(child)+1))
#     print("COMMISSION DETAILS \n{0}:{1} INR".format(parent,len(child)*500))
#     for i in child:
#         print("{0}:250 INR".format(i))


# FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button. A vending machine can serve range of products as follows:
# Coffee
# •	Espresso Coffee
# •	Cappuccino Coffee
# •	Latte Coffee
# Tea
# •	Plain Tea
# •	Assam Tea
# •	Ginger Tea
# •	Cardamom Tea
# •	Masala Tea
# •	Lemon Tea
# •	Green Tea
# •	Organic Darjeeling Tea
# Soups 
# •	Hot and Sour Soup
# •	Veg Corn Soup
# •	Tomato Soup
# •	Spicy Tomato Soup
# Beverages
# •	Hot Chocolate Drink
# •	Badam Drink
# •	Badam-Pista Drink
# Write a program to take input for main menu & sub menu and display the name of sub menu selected in the following format (enter the first letter to select main menu):


# menu = [['Espresso Coffee','Cappuucino Coffee','Latte Coffee'], ['Plain Tea',

# 'Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea',

# 'Organic Darjeeling Tea'], ['Hot and Sour Soup','Veg Corn Soup','Tomato Soup',

# 'Spicy Tomato Soup'], ['Hot Chocolate Drink', 'Badam Drink',

# 'Badam-Pista Drink']]

# m = input()
# if m=='c' or m=='t' or m=='s' or m=='b':
#     if m=='c':
#         submenu = int(input())
#         if submenu in range(1,4):
#             print('Welcome to CCD!\nEnjoy your {}!'.format(menu[0][submenu-1]))
#         else:
#             print("INVALID INPUT")
#     elif m=='t':
#         submenu = int(input())
#         if submenu in range(1,9):
#             print('Welcome to CCD!\nEnjoy your {}!'.format(menu[1][submenu-1]))
#         else:
#             print("INVALID INPUT")

#     elif m=='s':
#         submenu = int(input())
#         if submenu in range(1,5):
#             print('Welcome to CCD!\nEnjoy your {}!'.format(menu[2][submenu-1]))
#         else:
#             print("INVALID INPUT")
#     elif m=='b':
#         submenu = int(input())
#         if submenu in range(1,4):
#             print('Welcome to CCD!\nEnjoy your {}!'.format(menu[3][submenu-1]))
#         else:
#             print("INVALID INPUT")
# else:
#     print("INVALID INPUT!")


# A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If the patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR. Write a code to calculate earnings in a day for which one array/List of values representing age of patients visited on that day is passed as input.

# Note:

# Age should not be zero or less than zero or above 120
# Doctor consults a maximum of 20 patients a day
# Enter age value (press Enter without a value to stop):
# Example 1:

# Input
# 20
# 30
# 40
# 50
# 2
# 3
# 14
# Output
# Total Income 2000 INR
# Note: Input and Output Format should be same as given in the above example.
# For any wrong input display INVALID INPUT

# age = []
# for i in range(20):
#     m = int(input())
#     if m in range(1,120):
#         age.append(m)
#     else:
#         print("INVALID INPUT")
#         exit()

# fees = 0
# for i in age:
#     if i < 17:
#         fees+=200
#     elif i < 40:
#         fees += 400
#     else:
#         fees += 300

# print("Total Income {} INR".format(fees))


# Find the 15th term of the series?

# 0,0,7,6,14,12,21,18, 28

# Explanation : In this series the odd term is increment of 7 {0, 7, 14, 21, 28, 35 – – – – – – }

#                         And even term is a increment of 6 {0, 6, 12, 18, 24, 30 – – – – – – }

# def series(n):
# 	# if n == 0:
# 	# 	return 0
# 	mid = n//2
# 	if n % 2:
# 		return 7*mid
# 	else:
# 		return 6*(mid - 1)

# n = int(input())

# print(series(n))

