nums = [0,0,0,0,0,1,1,2,2,3,4,4,5,5,5,5,6,7]
target = 0


# def searchRange(nums, target):
#     low = 0
#     high = len(nums) - 1

#     def binarysearch(nums, target, low, high):
#         if low <= high:
#             mid = (high + low) // 2
#             if nums[mid] == target:
#                 return mid
#             elif target < nums[mid]:
#                 return binarysearch(nums, target, low, mid - 1)
#             else:
#                 return binarysearch(nums, target, mid + 1, high)
#         return -1
#     index = binarysearch(nums, target, low, high)
#     start = index
#     end = index
#     length = len(nums)
#     if index > -1:
#         for i in range(index, length):
#             if i < length and nums[i] == target:
#                 end = i
#             else:
#                 break

#         for i in range(index, -1, -1):
#             if i > -1 and nums[i] == target:
#                 start = i
#             else:
#                 break
#         return [start, end]
#     return [-1, -1]


# print(searchRange(nums, target))


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
        # print(index)
        initial_start = index
        initial_end = index
        start = index
        end = index
        length = len(nums)
        if index > -1:
            while start > 0 and nums[start-1] == target:
                start = binarysearch(nums, target, low, start-1)
                print(start)

            while end < len(nums) - 1 and nums[end+1] == target:
                end = binarysearch(nums, target, end+1, high)
                print(end)

            if start == 0 and nums[start] == target:
                start = start
            if end == high and nums[end] == target:
                end = end

            return [start, end]
        return [-1, -1]


print(searchRange(nums, target))