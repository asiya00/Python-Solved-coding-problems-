import random
li = [1,2,3,5,6,7]
def shuffle(li):
	'''li1 = []
	while(len(li)!=len(li1)):
		a = li[random.randint(0,len(li)-1)]
		if a not in li1:
			li1.append(a)	
	li[:] = li1[:]
	print(li)'''
	
	for i in range(len(li)):
		a = li[random.randint(0,i)]
		li[i],li[a] = li[a],li[i]		
	print(li)
	
	
shuffle(li)