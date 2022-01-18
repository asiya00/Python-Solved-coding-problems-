li = []
def generate_balanced_parenthesis(s, l, r):
    if not l and not r:
        li.append(s)
        return ""
    if l > r:
        return ""
    if not r:
        return generate_balanced_parenthesis(s+"(", l-1, r)
    if not l:
        return generate_balanced_parenthesis(s+")", l, r-1)
    return generate_balanced_parenthesis(s+"(", l-1, r) + generate_balanced_parenthesis(s+")", l, r-1)


n = 3
s = ""
generate_balanced_parenthesis(s, n, n)
print(li)
