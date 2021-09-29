a, b, c = map(int, input().split())

a = str(a)
b = str(b)
c = str(c)

first = min(int(a[0]), int(b[0]), int(c[0]))

second = max(int(a[1]), int(b[1]), int(c[1]))

third = min(int(a[-2]), int(b[-2]), int(c[-2]))

fourth = max(int(a[-1]), int(b[-1]), int(c[-1]))

number = str(first)+str(second)+str(third)+str(fourth)

print(int(number))
