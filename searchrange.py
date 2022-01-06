nums = [5, 5, 5, 5, 10]
target = 5


def searchRange(nums, target):
    low = 0
    high = len(nums) - 1

    def binarysearch(nums, target, low, high):
        if low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return binarysearch(nums, target, low, mid - 1)
            else:
                return binarysearch(nums, target, mid + 1, high)
        return -1
    index = binarysearch(nums, target, low, high)
    start = index
    end = index
    length = len(nums)
    if index > -1:
        for i in range(index, length):
            temp = i
            if nums[i] != target or i == length - 1:
                break
        if temp == length - 1 and nums[temp] == target:
            end = temp
        else:
            end = temp - 1

        for i in range(index, -1, -1):
            temp = i
            if nums[i] != target:
                break
        if temp == 0 and nums[temp] == target:
            start = temp
        else:
            start = temp + 1
        return [start, end]
    return [-1, -1]


print(searchRange(nums, target))


# def searchRange(nums):
#     length = len(nums)
#     left = 0
#     right = -1
#     if not nums:
#         return [-1, -1]
#     while nums[left] <= nums[right] and nums[left] != nums[right]:
#         if nums[left] != target:
#             left += 1
#         if nums[right] != target:
#             right -= 1
#     right = length + right
#     if left > right or nums[left] != target:
#         return [-1, -1]
#     else:
#         return [left, right]
