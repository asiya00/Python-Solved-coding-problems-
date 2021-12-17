def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*n
    maximum = float("-inf") 
    for k in queries:
        a = k[0]-1
        b = k[1]-1
        key = k[2]
        while a < b:
            arr[a] += key
            arr[b] += key
            a += 1
            b -= 1
            if maximum < arr[a] and arr[a] > arr[b]:
                maximum = arr[a]
            else:
                maximum = arr[b]
        if a == b:
            arr[a] += key
        if arr[a] > maximum:
            maximum = arr[a]
        print(maximum)
        print(arr)
    return maximum


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
print(result)
