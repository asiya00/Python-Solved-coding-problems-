def linear_search(arr, ele, low):
    if low < len(arr):
        if ele == arr[low]:
            return low
        return linear_search(arr, ele, low + 1)
    else:
        return -1

# def linear_search(arr, ele, length, high):
#     if length == -1:
#         return -1
#     if ele == arr[0]:
#         return high - length
#     arr.pop(0)
#     return linear_search(arr, ele, length - 1, high)


arr = [3, 4, 7, 5, 6]
print(linear_search(arr, 3, len(arr), len(arr)))
