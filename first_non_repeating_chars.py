# Input Type = String 
# Input String Contains only lowercase english letters
# Input String Length<=N<=100000

def firstNonRepeating(s):
	di = {}
	for i in s:
		if i not in di:
			di[i] = 1 
		else:
			di[i] += 1

	for j in chars:
		if di[i] == 1:
			return j

s = input()
print(firstNonRepeating(s))