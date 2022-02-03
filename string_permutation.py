def isPermutation(input1, input2):
    di = {}
    for i in input1:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    di1 = {}
    for j in input2:
        if j in di1:
            di1[j] += 1
        else:
            di1[j] = 1
    return di == di1:

print(isPermutation("Mettl", "Coding"))
print(isPermutation("zbk", "zkb"))
