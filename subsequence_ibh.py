def subsequence(nums):
    if len(nums) == 0:  # base condition
        return [[]]
    val = nums.pop()  # hypothesis
    substring = subsequence(nums)
    li = []
    for i in substring:
        print(i, val)
        li.append(i + [val])  # induction
    return substring + li

print(subsequence(['a', 'b', 'c']))
