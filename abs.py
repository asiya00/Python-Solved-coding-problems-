arr = [6,2,4,10]
arr.sort()
min_dis = float("inf")
result = []
tmp_dis = 0
for i in range(len(arr)-1):
    if arr[i+1]-arr[i] <= min_dis:
        min_dis = arr[i+1]-arr[i]
        if tmp_dis > min_dis:
            result.clear()
        tmp_dis = min_dis
        pair = [arr[i], arr[i+1]]
        result.append(pair)
print(result)

        


    


