count = 1
a = "1111"
b = "2211"

def subsets(a, b, ans, output=[]):
	global count
	if len(ans) == 0:
		if output:
			temp1 = a[:]
			temp2 = b[:]
			for i in output:
				temp1[i-1], temp2[i-1] = temp2[i-1], temp1[i-1]
			if (temp1 == a or temp1 == b) and (temp2 == a or temp2 == b):
				count += 1
		return
	output1 = output
	output2 = output + [ans[0]]
	subsets(a, b, ans[1:], output1)
	subsets(a, b, ans[1:], output2)

subsets(list(a), list(b), list(range(1, len(a)+1)))
print(count)