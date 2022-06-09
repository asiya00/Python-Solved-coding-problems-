m = 3
n = 2
path = []

def uniquepath(m, n, direction, di=[]):
	if m == 0 or n == 0:
		return 
	if m == 1 and n == 1:
		di += [direction]
		path.append(di)
		return
	di1 = di+[direction]
	uniquepath(m, n-1, "right", di1)
	di2 = di+[direction]
	uniquepath(m-1, n, "down", di2)

print(uniquepath(m, n, ""))
print(path)
