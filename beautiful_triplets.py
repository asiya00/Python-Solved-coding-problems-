def beautifulTriplets(d, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            count += 1
    return count


n, d = map(int, input().split())
arr = list(map(int, input().split()))
print(beautifulTriplets(d, arr))
