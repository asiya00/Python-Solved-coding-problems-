lst=[[10,20,30],[16,25,35],[27,29,37]]
i=int(input("Enter a number of which u want to know it's location:  "))
for index1,value1 in enumerate(lst,start=1):
	for index2,value2 in enumerate(value1,start=1):
		if value2==i:
			print('({},{})'.format(index1,index2))
		
		