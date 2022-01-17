n = 10
prime = [x for x in range(n+1)]
prime[1] = 0
print(prime)
p = 2

while p*p <= n:
    if prime[p] > 0:
        for i in range(p+p, n+1, p):
            prime[i] = 0
    p += 1

for i in prime:
    if i != 0:
        print(i)