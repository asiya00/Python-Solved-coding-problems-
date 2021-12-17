def findElement(arr, n):
    left = 0
    i = 1
    right = i+1
    while i < n - 1:
        while i < n - 1 and left > -1:
            if arr[left] <= arr[i]:
                left -= 1
            else:
                break
        if left == -1:
            left += 1
            while i < n - 1 and right < n:
                if arr[right] >= arr[i]:
                    right += 1
                else:
                    break

            if right == n:
                right -= 1

            if i < n and arr[left] <= arr[i] and arr[right] >= arr[i]:
                return arr[i]
        i += 1
        left = i - 1
        right = i + 1
    return -1


n = 14
arr = [5, 6, 4, 1, 7, 12, 9, 1, 4, 1, 11, 5, 7, 1]
# n = 4
# arr = [4, 2, 5, 7]
print(findElement(arr, n))