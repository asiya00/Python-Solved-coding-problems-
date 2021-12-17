def findElement(arr, n):
    left = 0
    i = 1
    right = i+1
    
    while i < n:
        while i < n and left > -1:
            if arr[left] > arr[i]:
                break
            else:
                left -= 1
        print(i, right)
        while i < n and right < n:
            # print(arr[right], arr[i])
            if arr[right] < arr[i]:
                break
            else:
                right += 1
        # print(left, right)
        if i < n and left == 0 and right == n - 1 :
            return arr[i]
        else:
            i += 1
            left = i - 1
            right = i + 1
    else:
        return -1

# n = 14
# arr = [5, 6, 4, 1, 7, 12, 9, 1, 4, 1, 11, 5, 7, 1]
n = 5
arr = [4, 2, 5, 7]
print(findElement(arr, n))