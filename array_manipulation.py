def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*(n+1)
    maximum = float("-inf")
    for k in queries:
        a = k[0]-1
        b = k[1]-1
        key = k[2]
        arr[a] += key
        arr[b + 1] -= key
    sumq = 0
    for i in range(n):
        sumq += arr[i]
        maximum = max(maximum, sumq)
    return maximum

queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
n = 5

print(arrayManipulation(n, queries))