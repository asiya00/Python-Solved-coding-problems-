def replace_sign(s, output, k, li=[]):
	if len(s) == 2:
		ans = eval(output)
		if ans == k:
			li.append(output)
			return li
		return
	output1 = output + "+" + s[1]
	output2 = output + "-" + s[1]
	return replace_sign(s[1:], output1, k, li) or replace_sign(s[1:], output2, k, li)

s = "5*9*0"
print(replace_sign(s.replace("*",""), s[0], 14))