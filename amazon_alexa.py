def is_distinct(s):
    t = set()
    for i in s:
        if i != "_" and i in t:
            return False
        else:
            t.add(i)
    return True

def goodString (N, Q, S, arr, ranges):
    # Write your code here
    for i in ranges:
        if not is_distinct(S[i[0]-1:i[1]]):
            break
    else:
        return 0

    ans = 0
    for i in arr:
        i = i-1
        S = S[:i] + "_" + S[i+1:]
        ans += 1
        print(S)
        for j in ranges:
            if not is_distinct(S[j[0]-1:j[1]]):
                break
        else:
            return ans
    return ans  

# N = 8
# Q = 3
# S = "abbabaab"
# arr = [6, 3, 5, 1, 4, 2, 7, 8]
# ranges = [[1, 3], [4, 7], [3, 5]]

N = 5
Q = 2
S = "aaaaa"
arr = [2, 4, 1, 3, 5]
ranges = [[1, 2], [4, 5]]

print(goodString(N, Q, S, arr, ranges))