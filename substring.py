s = ""
'''
a
b
c
ab
bc
abc
'''
length = 2**len(s)

for i in range(length):
    li = "".join([s[j] for j in range(len(s)) if (i & (1 << j))])
    if li in s:
        print(li)
