summ = 0
def prime_factors(n):
	global summ
	s = set()
	while n % 2 == 0:
		s.add(2)
		n //= 2

	for i in range(3, int(n**0.5)+1, 2):
		while n % i == 0:
			s.add(i)
			n //= i

	if n > 2:
		s.add(n)
	summ += sum(s)

N = 100000
for i in range(2, N+1):
	prime_factors(i)

print(summ % ((10**9)+7))
