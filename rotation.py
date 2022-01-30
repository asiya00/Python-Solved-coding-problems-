def findKRotation(arr,  n):
    def binarysearch(arr, low, high):
        mid = (low+high)//2
        if arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]:
            return mid
        if (mid == low or mid < high) and arr[mid] > arr[mid+1]:
            return mid + 1
        elif arr[mid] < arr[low]:
            return binarysearch(arr, low, mid-1)
        elif arr[mid] > arr[high]:
            return binarysearch(arr, mid+1, high)
        else:
            return 0
    index = binarysearch(arr, 0, n-1)
    return index


arr = [66, 72, 79, 86, 95, 104, 106, 110, 119, 123, 124, 129, 132, 136, 137, 142, 150, 2, 12, 14, 17, 26, 30, 36, 38, 46, 52, 60]
# print(findKRotation([5, 1, 2, 3, 4], 5))
print(findKRotation(arr, len(arr)))
