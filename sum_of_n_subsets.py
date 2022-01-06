summ = 0
N = 4
s = [x for x in range(1, N+1)]
for i in range(1 << N):
    li = list(s[j] for j in range(N) if (i & (1 << j)))
    summ += sum(li)
print(summ)

# from itertools import chain, combinations
# summ = 0
# N = 3
# s = [x for x in range(1, N+1)]
# comb = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
# for i in comb:
#   summ += sum(i)
# return summ