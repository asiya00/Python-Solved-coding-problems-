n = int(input())
m = []
for i in range(n):
    li = list(map(int, input().split()))
    m.append(li)
ans = 0
# hor = [[0 for i in range(n)] for j in range(n)]
# ver = [[0 for i in range(n)] for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         if m[i][j] == 1:
#             hor[i][j] = hor[i][j-1] + 1
#         else:
#             hor[i][j] = 0
# print(hor)
# for j in range(n):
#     for i in range(n):
#         if m[i][j] == 1:
#             ver[i][j] = ver[i-1][j] + 1
#         else:
#             ver[i][j] = 0
# print(ver)

# for x in range(n):
#     for y in range(n):
#         maxPossibleSize = min(hor[x][y], ver[x][y])
#         for k in range(1, maxPossibleSize+1):
#             # print(x,y)
#             if ver[x][y-k+1] >= k and hor[x-k+1][y] >= k:
#                 # print(k)
#                 # print(ver[x][y-k+1], hor[x-k+1][y])
#                 ans = max(ans, k)
#                 print(ans)
#                 break
# print(ans)
x1 = 0
for x2 in range(n):
    for y2 in range(n):
        for k in range(x1, x2+1):
            y1 = y2-(x2-x1)
            if y1 < 0:
                continue
            ispossible = 1
            for i in range(x1, x2+1):
                if m[i][y1] == 0:
                    ispossible = 0
            for i in range(x1, x2+1):
                if m[i][y2] == 0:
                    ispossible = 0
            for j in range(y1, y2+1):
                if m[x1][j] == 0:
                    ispossible = 0
            for j in range(y1, y2+1):
                if m[x2][j] == 0:
                    ispossible = 0

            if ispossible == 1:
                ans = max(ans, x2-x1+1)
print(ans)

