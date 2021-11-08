def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        b = arr.pop(0)
        arr.append(b)
        print(arr)
    return arr

arr = [1, 2, 3, 4, 5]
d = 4
print(rotateLeft(d, arr))