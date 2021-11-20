'''Given an array of integers, update every element largest of previous and next elements with the following exception
a) First element - check largest of first and second 
b) Last element - check largest of last and second '''

size = int(input())
arr = list(map(int, input().split()))

for i in range(size-1):
	arr[i] = max(arr[i], arr[i+1])

arr[size-1] = max(arr[size-1], arr[1])

print(arr)
