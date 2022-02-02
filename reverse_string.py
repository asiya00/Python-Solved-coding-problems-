s = "asiya"

def reverse(s):
	if len(s) == 0:
		return ""
	return s[-1] + reverse(s[:-1])
	

print(reverse(s))