n = int(input())

def bitwise(cls, input1):
	binary = bin(input1)[2:][::-1]
	msb = 0
	lsb = 0
	counter = 0

	for i in range(len(binary)):
		if binary[i] == "1":
			msb = i
			break

	for i in range(len(binary)):
		if binary[i] == "1":
			counter += 1
			lsb = i

	return "{}#{}#{}".format(counter, msb, lsb)
