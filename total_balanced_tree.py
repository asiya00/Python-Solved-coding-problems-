def count_balanced_parenthesis(l, r):
    if not l and not r:
        return 1
    if l > r:
        return 0
    if not r:
        return count_balanced_parenthesis(l-1, r)
    if not l:
        return count_balanced_parenthesis(l, r-1)
    return count_balanced_parenthesis(l-1, r) + count_balanced_parenthesis(l, r-1)


n = 5
print(count_balanced_parenthesis(n, n))
