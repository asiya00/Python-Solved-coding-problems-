def distinct_subarrays(nums,K):
    ans = 0
    n = len(nums)
    for i in range(n):
        temp2 = []
        k = 0
        check = set()
        for j in range(i,n):
            if i == 0:
                if nums[j]%2 == 1:
                    temp2.append(1)
                else:
                    temp2.append(0)
                if temp2[k] <= K and nums[j] not in check:
                    ans+=1
                    check.add(nums[j])
            else:
                if nums[j]%2 == 1:
                    temp2.append(temp1[k]+1)
                else:
                    temp2.append(temp1[k])
                if temp2[k] <= K and tuple(nums[k:j+1]) not in check:
                    ans+=1
                    check.add(tuple(nums[k:j+1]))
            k+=1
        temp1 = list(temp2)
    
    return ans

print(distinct_subarrays([1,2,3,4], 1))

print(distinct_subarrays([6,3,5,8],1))

print(distinct_subarrays([2,1,2,1,3], 2))

# distinct_subarrays([2, 2, 5, 6, 9, 2, 11, 9, 2, 11, 12], 1)

