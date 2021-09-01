def traveller(m, n, memo = {}):
	key = (m, n)
	if m == 0 or n == 0:
		return 0
	if m == 1 and n == 1:
		return 1

	if key in memo:
		return memo[key]

	memo[key] = traveller(m - 1, n, memo) + traveller(m, n - 1, memo)
	return memo[key]

print(traveller(3,3))
print(traveller(21, 21))

