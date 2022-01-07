s = "abc"
output = ""


def substring(s, output):
    if len(s) == 0:
        print(output)
        return
    output1 = output
    output2 = output + s[0]
    substring(s[1:], output1)
    substring(s[1:], output2)


substring(s, output)
