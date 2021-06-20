'''Task:
Remove a given negative index element from array using recursion
E.g func([1,2,3,4,5,6], 2) => [1,2,3,4,6]'''

def delete(arr,index):
	if len(arr)==0:
		return
	if len(arr)==1 or arr[-1]==arr[len(arr)-index]:
		arr.pop()
		return
				
	val = arr.pop()
	index = index - 1
	delete(arr,index)
	arr.append(val)
	
arr = [1,2,3,4,5,6]
index = 3
delete(arr,index)
print(arr)