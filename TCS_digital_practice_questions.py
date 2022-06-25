# 1.Problem Description -: 
# Given an array Arr[ ] of N integers and a positive integer K. 
# The task is to cyclically rotate the array clockwise by K.

# Example 1:
# 5  —Value of N
# {10, 20, 30, 40, 50}  —Element of Arr[ ]
# 2  —–Value of K

# Output :
# 40 50 10 20 30

# Example 2:
# 4  —Value of N
# {10, 20, 30, 40}  —Element of Arr[]
# 1  —–Value of K 

# Output :
# 40 10 20 30

# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())

# def rotate(arr, k):
# 	return arr[-k % n:] + arr[:-k % n]

# print(rotate(arr, k))

# 2. Problem Description -:
# Given two non-negative integers n1 and n2, where n1<n2. 
# The task is to find the total number of integers in the range [n1, n2]
# (both inclusive)which have no repeated digits.

# For example:
# Suppose n1=11 and n2=15.
# There is the number 11, which has repeated digits, 
# but 12, 13, 14 and 15 have no repeated digits.
# So, the output is 4.

# Example1:
# Input:
# 11 — Vlaue of n1
# 15 — value of n2
# Output:
# 4
 
# Example 2:
# Input:
# 101 — value of n1
# 200 — value of n2
# Output:
# 72

# def nonRepeatedDigits(n1, n2):
# 	count = 0
# 	for i in range(n1, n2+1):
# 		num = i
# 		visited = [False for i in range(10)]
# 		while num > 0:
# 			if visited[num % 10] == True:
# 				break
# 			visited[num % 10] = True
# 			num //= 10
# 		if num == 0:
# 			count += 1	
# 	return count

# n1 = int(input())
# n2 = int(input())

# print(nonRepeatedDigits(n1, n2))

# 3. Problem Description -:  
# In this 3 Palindrome, Given an input string word, split the string into exactly 3 palindromic substrings. Working from left to right, choose the smallest split for the first substring that still allows the remaining word to be split into 2 palindromes.
# Similarly, choose the smallest second palindromic substring that leaves a third palindromic substring.
# If there is no way to split the word into exactly three palindromic substrings, print “Impossible” (without quotes). Every character of the string needs to be consumed.
# Cases not allowed –
# After finding 3 palindromes using above instructions, if any character of the original string remains unconsumed.
# No character may be shared in forming 3 palindromes.

# Constraints

# 1 <= the length of input sting <= 1000
# Input

# First line contains the input string consisting of characters between [a-z].
# Output

# Print 3 substrings one on each line.
# Time Limit
# 1

# Examples

# Example 1

# Input
# nayannamantenet

# Output
# nayan
# naman
# tenet

# Explanation
# The original string can be split into 3 palindromes as mentioned in the output.
# However, if the input was nayanamantenet, then the answer would be “Impossible”.

# Example 2

# Input
# aaaaa

# Output
# a
# a
# aaa

# Explanation
# The other ways to split the given string into 3 palindromes are as follows –
# [a, aaa, a], [aaa, a, a], [aa, aa, a], etc.
# Since we want to minimize the length of the first palindromic substring using left to right processing, the correct way to split is [a, a, aaa].
# Example 3

# Input
# aaaabaaaa

# Output
# a
# aaabaaa
# a

# Explanation
# The other ways to split the given string into 3 palindromes are as follows –
# [aaaa, b, aaaa], [aa, aabaa, aa], etc.
# Since we want to minimize the length of the first palindromic substring using left to right processing, the correct way to split is [a, aaabaaa, a].

# def if_palindrome(s):
#     if len(s)==1:
#         return True
#     s1=s[::-1]
#     return s1==s

# def splitPalindromes(s):
# 	l=len(s)
# 	for i in range(1,l-1):
# 	    s1=s[:i]
# 	    if if_palindrome(s1):
# 	        for j in range(1,l-i):
# 	            s2=s[i:i+j]
# 	            s3=s[i+j:]
# 	            if if_palindrome(s2) and if_palindrome(s3):
# 	                print(s1)
# 	                print(s2)
# 	                print(s3)
# 	                return
# 	print("Impossible")

# s=input()
# splitPalindromes(s)

# 4. Problem Statement -: 
# In this even odd problem Given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.
# Calculate the number of all such permutations.
# As this number can be large, print it modulo (1e9 +7).

# Constraints
# 0 <= low <= high <= 10^9
# K <= 10^6.

# Input
# First line contains two space separated integers denoting low and high respectively
# Second line contains a single integer K.
# Output
# Print a single integer denoting the number of all such permutations
# Time Limit
# 1

# Examples

# Example 1
# Input
# 4 5
# 3

# Output
# 4

# Explanation
# There are 4 valid permutations viz. {4, 4, 4}, {4, 5, 5}, {5, 4, 5} and {5, 5, 4} which sum up to an even number.

# Example 2
# Input
# 1 10
# 2

# Output
# 50

# Explanation
# There are 50 valid permutations viz. {1,1}, {1, 3},.. {1, 9} {2,2}, {2, 4},… {2, 10} . . . {10, 2}, {10, 4},… {10, 10}. These 50 permutations, each sum up to an even number.

# mod=1000000007
# def esum(m,n,K,N):
#     if(K==1):
#        return n
#     else:
#         return (N-(m-n)*esum(m,n,K-1,N)%mod)
 
# low,high=map(int,input().split())
# K=int(input())
# diff=high-low+1
# if(diff%2==0):
#     m=diff//2
#     n=m
# else:
#     if(low%2==0):
#         m=(diff-1)//2
#         n=m+1
#     else:
#         m=(diff+1)//2
#         n=m-1
# N=m
# for i in range(K-1):
#     N=(N*(m+n))%mod
# out=esum(m,n,K,N)%mod
# print(out)

# 5. Problem Statement:
# Roco is an island near Africa which is very prone to forest fire. Forest fire is such that it destroys the complete forest. Not a single tree is left.This island has been cursed by God , and the curse is that whenever a tree catches fire, it passes the fire to all its adjacent tree in all 8 directions,North, South, East, West, North-East, North-West, South-East, and South-West.And it is given that the fire is spreading every minute in the given manner, i.e every tree is passing fire to its adjacent tree.Suppose that the forest layout is as follows where T denotes tree and W denotes water.
# Your task is that given the location of the first tree that catches fire, determine how long would it take for the entire forest to be on fire. You may assume that the lay out of the forest is such that the whole forest will catch fire for sure and that there will be at least one tree in the forest

# Input Format:
# First line contains two integers, M, N, space separated, giving the size of the forest in terms of the number of rows and columns respectively.
# The next line contains two integers X,Y, space separated, giving the coordinates of the first tree that catches the fire.
# The next M lines, where ith line containing N characters each of which is either T or W, giving the position of the Tree and Water in the  ith row of the forest.

# Output Format:
# Single integer indicating the number of minutes taken for the entire forest to catch fire

# Constrains:
# 3 ≤ M ≤ 20
# 3 ≤ N ≤ 20

# Sample Input 1:
# 3 3
# W T T
# T W W
# W T T
# Sample Output 1:
# 5
# Explanation:
# In the second minute,tree at (1,2) catches fire,in the third minute,the tree at (2,1) catches fire,fourth minute tree at (3,2) catches fire and in the fifth minute the last tree at (3,3) catches fire.

# Sample Input 2:
# 6 6
# 1 6
# W T T T T T
# T W W W W W
# W T T T T T
# W W W W W T
# T T T T T T
# T W W W W W

# Sample Output 2:
# 16

# ar=[]
# n=0
# br=[(-1,0),(+1,0),(0,+1),(0,-1),(-1,+1),(-1,-1),(+1,+1),(+1,-1)]
# def bfs(i,j):
#     key=(i,j)
#     vis=set()
#     vis.add(key)
#     dis=dict()
#     dis[key]=1 
#     que=[]
#     que.append((i,j))
#     time=1
#     while(que):
#         x,y=que.pop(0) 
#         for dx,dy in br:
#             nx,ny=x+dx , y+dy 
#             key=(nx,ny) 
#             if(0<=nx<=n-1 and 0<=ny<=n-1 and key not in vis and ar[nx][ny]=='T'):
#                 vis.add(key)
#                 dis[key]=dis[(x,y)]+1 
#                 que.append((nx,ny)) 
#                 time=max(time,dis[key]) 
#     return time
            
# n,m=map(int,input().split())
# r,c=map(int,input().split())
# ar=[]
# for i in range(n):
#     ar.append(tuple(map(str,input().split()))) 
    
# print(bfs(r-1,c-1))

# 6. Problem Statement:-

# Compute the nearest larger number by interchanging its digits updated.Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible print -1.

# Input Format
# 2 numbers a and b, separated by space.
# Output Format
# A single number greater than b.
# If not possible, print -1

# Constraints
# 1 <= a,b <= 10000000

# Example 1:

# Sample Input:
#     459 500

# Sample Output:
#     549

# Example 2:

# Sample Input:
#     645757 457765

# Sample Output:
#     465577

# min1 = 10**9
# _count = 0

# def permutation(str1, i, n, p):
# 	global min1, _count
# 	if (i == n):
# 		str1 = "".join(str1)
# 		q = int(str1)
# 		if (q - p > 0 and q < min1):
# 			min1 = q
# 			_count = 1
# 	else:
# 		for j in range(i, n + 1):
# 			str1[i], str1[j] = str1[j], str1[i]
# 			permutation(str1, i + 1, n, p)
# 			str1[i], str1[j] = str1[j], str1[i]

# 	return min1

# A = 645757
# B = 457765

# str2 = str(A)
# str1 = [i for i in str2]
# le = len(str1)

# h = permutation(str1, 0, le - 1, B)
# if _count == 1:
# 	print(h)
# else:
# 	print(-1)

# 7. Problem Statement:- 
# In a Conference ,attendees are invited for a dinner after the conference.The Co-ordinator,Sagar arranged around round tables for dinner and want to have an impactful seating experience for the attendees.Before finalizing the seating arrangement,he wants to analyze all the possible arrangements.These are R round tables and N attendees.In case where N is an exact multiple of R,the number of attendees must be exactly N//R,,If N is not an exact multiple of R, then the distribution of attendees must be as equal as possible.Please refer to the example section before for better understanding.
# For example, R = 2 and N = 3
# All possible seating arrangements are
# (1,2) & (3)
# (1,3) & (2)
# (2,3) & (1)
# Attendees are numbered from 1 to N.

# Input Format:
# The first line contains T denoting the number of test cases.
# Each test case contains two space separated integers R and N, Where R denotes the number of round tables and N denotes the number of attendees.
# Output Format:
# Single Integer S denoting the number of possible unique arrangements.

# Constraints:
# 0 <= R <= 10(Integer)
# 0 < N <= 20 (Integer)
# Sample Input 1:
# 1
# 2 5
# Sample Output 1:
# 10

# Explanation:
# R = 2, N = 5
# (1,2,3) & (4,5)

# (1,2,4) & (3,5)

# (1,2,5) & (3,4)

# (1,3,4) & (2,5)

# (1,3,5) & (2,4)

# (1,4,5) & (2,3)

# (2,3,4) & (1,5)

# (2,3,5) & (1,4)

# (2,4,5) & (1,3)

# (3,4,5) & (1,2)

# Arrangements like

# (1,2,3) & (4,5)

# (2,1,3) & (4,5)

# (2,3,1) & (4,5) etc.

# But as it is a round table,all the above arrangements are same.

# testcases = int(input())
# for i in range(testcases):
#     tables, people = map(int, input().split())
#     result = 1

#     if tables >= people:
#         print(result)
#     else:
#         PA = people // tables
#         PB = PA + 1
#         TB = people % tables
#         TA = tables - TB

#         # Using DP to store factorials pre-hand
#         fact = [1]
#         for j in range(1, people + 1):
#             fact.append(j*fact[j-1])

#         for i in range(TB):
#             result = result * (fact[people]//(fact[PB]*fact[people-PB]))
#             people = people - PB

#         for i in range(TA):
#             result = result * (fact[people]//(fact[PA]*fact[people-PA]))
#             people = people - PA

#         print(result)
