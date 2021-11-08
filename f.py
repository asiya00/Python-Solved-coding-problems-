def do(st):
    num = 0
    for i in range(len(st)):
        if st[i] == "[":
            num = int(st[0:i])
            break
    return st[i+1:-1]*num


def check(st):
    i = 0
    new = ""
    fp = 0
    while i < len(st):
        if st[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            fp = i
            count1 = 0
            count2 = 0
            while count1 != count2 or count1 == 0:
                i += 1
                if st[i] == "[":
                    count1 += 1
                if st[i] == "]":
                    count2 += 1
            new += do(st[fp:i + 1])
        else:
            new += st[i]
        i += 1
    return new


ip = input()
while "[" in ip:
    ip = check(ip)
print(ip)
