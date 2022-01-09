def combo(s, output, p, li=set()):
    if len(s) == 1:
        a = eval(output)
        if a % p == 0:
            li.add(output)
        return
    o1 = output + "+" + s[1]
    o2 = output + "*" + s[1]
    combo(s[1:], o1, p)
    combo(s[1:], o2, p)
    return li

ans = []
def CombinationRepetitionUtil(chosen, arr, index, r, start, end):
    if index == r:
        li = []
        for j in range(r):
            li.append(chosen[j])
        rev = li[::-1]
        if rev not in ans and li not in ans:
            ans.append(rev)
            ans.append(li)
        return
    if start > n:
        return
    chosen[index] = arr[start]
    CombinationRepetitionUtil(chosen, arr, index + 1, r, start, end)
    CombinationRepetitionUtil(chosen, arr, index, r, start + 1, end)

def CombinationRepetition(arr, n, r):
    chosen = [0] * r
    CombinationRepetitionUtil(chosen, arr, 0, r, 0, n)

arr = [2, 3]
p = 3
actual_value = "".join(map(str, arr))
r = len(arr)

minimum = min(arr)
for i in range(minimum-1, 0, -1):
    arr.insert(0, i)
n = len(arr)-1
CombinationRepetition(arr, n, r)

for temp in ans:
    temp = "".join(map(str, temp))
    if temp <= actual_value:
        l = combo(temp, temp[0], p)
        count = len(l)
print(count)

