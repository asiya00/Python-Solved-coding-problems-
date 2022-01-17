def letterCasePermutations(s, output=""):
	if len(s) == 0:
		print(output)
		return
	if s[0].isdigit(): 
		output += s[0]
		letterCasePermutations(s[1:], output)
	else:
		o1 = output + s[0]
		o2 = output + s[0].swapcase()
		letterCasePermutations(s[1:], o1)
		letterCasePermutations(s[1:], o2)

s = "3z4"
letterCasePermutations(s)
