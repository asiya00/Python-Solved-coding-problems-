import random
arr = list(map(int, input("Data: ").split()))
k = int(input("Number of clusters: "))
m1 = random.choices(arr, k=k)
print("Random means:",m1)
m2 = []
K = []
for l in range(k):
    K.append([])
for i in range(len(arr)):
    n = 0
    mini = float("inf")
    p = 0
    for j in range(k):
        if abs(m1[j]-arr[i])<mini:
            mini = abs(m1[j]-arr[i])
            n = arr[i]
            p = j
    K[p].append(n)
while (m1!=m2):
    for l in range(k):
        m2.append(sum(K[l])/len(K[l]))
        K[l].clear()
    #print("Means:",m2)
    for i in range(len(arr)):
        n = 0
        mini = float("inf")
        p = 0
        for j in range(k):
            if abs(m2[j]-arr[i])<mini:
                mini = abs(m2[j]-arr[i])
                n = arr[i]
                p = j
        K[p].append(n)
    if m1!=m2:
        m1 = m2.copy()
        m2.clear()
    else:
        break
else:
    print("Clusters formed:",K)
print("Clusters formed:",K)
