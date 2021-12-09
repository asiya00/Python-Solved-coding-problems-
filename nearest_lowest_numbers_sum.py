def nearest_lowest_sum(arr):
    array = sorted(arr)
    di = {}
    ans = []
    di[array[0]] = array[1]
    for i in range(1, len(arr)-1):
        di[array[i]] = array[i-1] + array[i+1]
    di[array[-1]] = array[-2]
    for j in arr:
        ans.append(di[j])
    return ans


arr = [8, 2, 0, 115]
print(nearest_lowest_sum(arr))

# arr = [0, 2, 8, 115]

# di = {8: 117 , 2: 8 , 0: 2 , 115: 8}