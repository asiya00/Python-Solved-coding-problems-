s = "AAAB"

char_count = 0
li = []
for i in range(1, len(s)):
	st = s[i:]
	li.append(st)

length = float("inf")
for l in li:
	if set(s) == set(l) and len(l) < length:
		length = len(l)
print(length)
