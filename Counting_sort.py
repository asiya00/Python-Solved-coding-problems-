def countingSort(arr):
    li = [0]*(max(arr)+1)
    final_arr = [0]*len(arr)
    for i in arr:
        li[i] = li[i] + 1

    for j in range(1, len(li)):
        li[j] = li[j-1] + li[j]

    for k in range(len(final_arr)-1, -1, -1):
        li[arr[k]] -= 1 
        final_arr[li[arr[k]]] = arr[k]

    print(final_arr) 

countingSort([1, 1, 3, 2, 1])
countingSort([2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9])