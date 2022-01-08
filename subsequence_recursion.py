s = [1, 2, 3]


def substring(s, li=[], output=[]):
    if len(s) == 0:
        li.append(output)
        return
    output1 = output
    output2 = output + [s[0]]
    substring(s[1:], li, output1)
    substring(s[1:], li, output2)
    return li


print(substring(s))
