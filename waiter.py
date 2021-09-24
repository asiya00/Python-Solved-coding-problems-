n, q = map(int, input().split())
number = list(map(int, input().split()))
prime = []
i = 2
while(True):
	for j in range(2, int((i)**0.5) + 1):
		if not i%j:
			break
	else:
		prime.append(i)
	if len(prime)==q:
		break
	else:
		i+=1
ans = []
A0 = [x for x in number[::-1] if x%prime[0]]
ans += [x for x in number[::-1] if not x%prime[0]][::-1]
for j in range(1, len(prime)):
	A = [x for x in A0[::-1] if x%prime[j]]
	B = [x for x in A0[::-1] if not x%prime[j]]
	A0[::] = A[::]
	ans += B[::-1] 
print(ans+A0[::-1])

	




