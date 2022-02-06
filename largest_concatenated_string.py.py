# arr = ['30012', '250232', '53201', '3004355', '124111']
arr = ['0122', '21313', '12321']
di = 0

maxlength = float("-inf")
for i in range(len(arr)):
	for j in range(i+2, len(arr)):
		if set(arr[i] + arr[j]) == {'0', '1', '2', '3', '4', '5'}:
			if maxlength < len(arr[i] + arr[j]):
				di = arr[i] + arr[j]
				maxlength = len(arr[i] + arr[j])

print(di if di else 0)
