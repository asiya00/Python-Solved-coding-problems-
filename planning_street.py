n = 4

def planning_street(n):
	n = n + 2
	p1 = ((1 + (5 ** 0.5)) / 2) ** n

	p2 = ((1 - (5 ** 0.5)) / 2) ** n

	ans = (p1 - p2) / (5 ** 0.5)

	return round(ans) ** 2

print(planning_street(n))
