def reversed(arr, val):
    if not arr: # base condition
        arr.append(val)
        return
    ele = arr.pop()    # hypothesis
    reversed(arr, val)
    arr.append(ele)   # induction


def reverse_stack(arr):
    if not arr:  # base condition
        return
    val = arr.pop()  # hypothesis
    reverse_stack(arr)
    reversed(arr, val)# induction


arr = [1, 2, 3, 4, 5]
reverse_stack(arr)
print(arr)