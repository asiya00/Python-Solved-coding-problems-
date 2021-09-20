# Check if target sum is achievable by sum of odd even position combinations 

def number(n,d):
	n = str(n)
	lo = list(n[::2])
	sumo = sum(map(int, lo))
	le = list(n[1::2])
	sume = sum(map(int, le))

	if sumo==d or sume==d:
		return True
	if len(n)==1 or d==0:
		return False
	even = number(sume, d)
	odd = number(sumo, d)
	return even or odd

print(number(121045, 0))