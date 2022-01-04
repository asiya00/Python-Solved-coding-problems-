arr = list(map(int, input().split()))
di = {6: 600, 4: 400, 3: 300, 2: 200}
suma = 0
if 1 in arr:
    a = arr.count(1)
    if a < 3:
        suma += a*100
    else:
        b = (a//3)*1000
        suma += b+(a-(a//3)*3)*100
if 5 in arr:
    a = arr.count(5)
    if a < 3:
        suma += a*50
    else:
        b = (a//3)*500
        suma += b+(a-(a//3)*3)*50

for i in list(set(arr)):
    if i in di.keys():
        suma += (arr.count(i)//3)*di[i]

print(suma)

nums = list(map(int, input().split()))
count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            count += 1

print(count)
'''

def score(arr):
    ans = 0
    di = {1, 2, 3, 4, 5, 6}
    di1 = {}
    for i in di:
        di1[i] = arr.count(i)
        print(di1[i])
    print(di1)
    if di1[1] <=2:
        ans += 100 * di1[1]
    else:
        ans += 1000*(di1[1]//3)
        ans +=(di1[1]-((di1[1]//3) *3))
    if di1[5] <= 2:
        ans += 50 * di1[5]
    else:
        ans += 500*(di1[5]//3)
        ans +=(di1[5]-((di1[5]//3)*3))
    if di1[6] == 3:
        ans += 600
    else:
        ans +=600*(di1[6]//3)
    if di1[4] == 3:
        ans += 400
    else:
        ans +=400*(di1[4]//3)
    if di1[3] == 3:
        ans += 300
    else:
        ans +=300*(di1[3]//3)
    if di1[2] == 3:
        ans += 200
    else:
        ans +=200*(di1[2]//3)
    print(ans)
score([1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5])'''
