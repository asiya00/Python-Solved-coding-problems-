s = "LW"
def permutation(s, output="", li=[]):
    if len(s) == 1:
        li.append(output+s)
        return li
    o1 = output + s[0]
    o2 = output + s[0] + " "
    permutation(s[1:], o1)
    permutation(s[1:], o2)
    return li


print(sorted(permutation(s)))

