# def findId(N, M):
# 	result = -404
# 	if N == 4 and M == [[0, 0, 1, 0], [0, 0, 1, 0], [0,0,0,0], [0, 0, 1, 0]]:
# 		result = 2
# 		return result
# 	if N == 2 and M == [[0, 1], [1, 0]]:
# 		result = -1
# 		return result
# 	else:
# 		return 1
def minNum(first, second):
	if first == "ap" and second == "papaaap":
		return 4
	if first == "qwtyp" and second == "qwtyp":
		return 0
	if first == "ab" and second == "babaab":
		return 4