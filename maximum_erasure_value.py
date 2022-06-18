# nums = [5,2,1,2,5,2,1,2,5]
nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
def maximum_score(nums):
	minimum_size = len(nums)
	di = {i:0 for i in nums}
	length_distinct = len(di)
	count = 0
	start = 0
	maximum_score = float("inf")
	for end, val in enumerate(nums):
		if di[val] == 0:
			count += 1
		di[val] += 1
		print(end, val)
		while count == length_distinct:
			minimum_size = min(minimum_size, end-start+1)
			print(di[nums[start]])
			if di[nums[start]] == 1:
				break
			else:
				di[nums[start]]-=1
				start+=1
	return sum(nums[start: end+1]), start, end

print(maximum_score(nums))



