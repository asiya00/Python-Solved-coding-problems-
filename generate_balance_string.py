def count_balanced_parenthesis(s, l, r):
    if not l and not r:
        return s
    if l > r:
        return ""
    if not r:
        return count_balanced_parenthesis(s+"(", l-1, r)
    if not l:
        return count_balanced_parenthesis(s+")", l, r-1)
    return count_balanced_parenthesis(s+"(", l-1, r) + count_balanced_parenthesis(s+")", l, r-1)


n = 4
s = ""
a = count_balanced_parenthesis(s, n, n)
count = 0
for i in range(0, len(a), n*2):
    count += 1
    print(a[i:i+n*2])
print(count)