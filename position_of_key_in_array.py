# Position of key

inarr1 = ['QW', 'RN', 'KOI', 'POL', 'ERT', 'XCV', 'ERB', 'LHJ', 'AS']
inrow = 3
incol = 3
inarr2 = ['31', '23', '21', '11', '33', '13', '12', '22', '32']
inkey = "CARZ"

di = {i:j for i, j in zip(inarr2, inarr1)}
outstr = ""
indexes = sorted(di.keys())

for j in inkey:
	for i in indexes:
		if j in di[i]:
			if int(i[0]) > 1:
				outstr += str((inrow * int(i[0])) - (incol - int(i[1]))) + str(di[i].index(j)+1)
			else:
				outstr += i[1] + str(di[i].index(j)+1)
			break
	else:
		outstr += "**"

print(outstr)




# submatrix = [[0 for i in range(incol)] for j in range(inrow)]

# for i, j in zip(inarr1, inarr2):
# 	submatrix[int(j[0])-1][int(j[1])-1] = i

# ans = sum(submatrix, [])
# print(ans)
# outstr = ""
# for i in inkey:
# 	for j in range(len(ans)):
# 		if i in ans[j]:
# 			print(i, j+1)
# 			outstr += str(j+1) + str(ans[j].index(i)+1)
# 			break
# 	else:
# 		outstr += "**"
# print(outstr)